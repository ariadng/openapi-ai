from __future__ import annotations

import json
import re
import types

from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urljoin, urlparse

import requests

from .loader import load_spec, to_snake


def _build_function(
    base_url: str,
    path: str,
    method: str,
    query_params: List[str],
    path_params: List[str],
    func_name: str,
    doc: str,
    has_body: bool,
):

    def _endpoint_function(*, base_url: str = base_url, **kwargs):

        base = base_url
        if not base.endswith("/"):
            base += "/"

        url = urljoin(base, path.format(**{k: kwargs.pop(k) for k in path_params}))
        
        
        params = {k: kwargs.pop(k) for k in query_params if kwargs.get(k) is not None} or None
        body = kwargs.pop('body', None) if has_body else None

        response = requests.request(method, url, params=params, json=body, timeout=30)
        response.raise_for_status()
        return response.json()

    _endpoint_function.__name__ = func_name
    _endpoint_function.__doc__ = doc or ""
    return _endpoint_function


def generate_tools(
    spec_src: str | Path,
) -> types.SimpleNamespace:
    
    namespace = types.SimpleNamespace()
    spec = load_spec(spec_src)
    base_url = str(spec_src).removesuffix("/openapi.json")
    
    # Iterate through paths
    for path, methods in spec['paths'].items():
        func_path = to_snake(path, "/api/v1")
        
        # Iterate through methods in each path
        for method, method_spec in methods.items():
            method_name = method.lower()
            method_signature = method.lower()
            if method_name == 'post':
                method_signature = 'create'
            elif method_name == 'put':
                method_signature = 'update'
            
            func_name = f"{method_signature}_{func_path}"

            path_params: List[str] = []
            query_params: List[str] = []
            py_args: List[str] = []

            # Define path and query params
            for param in method_spec.get('parameters', []):
                name, location, required = param['name'], param['in'], param['required']

                if location == 'path':
                    path_params.append(name)
                elif location == 'query':
                    query_params.append(name)

                py_args.append(name if required else f"{name}=None")

            has_body = (method_name in ['post', 'put']) and ('requestBody' in method_spec)
            
            # Request body
            if has_body:
                py_args.append('body')
            
            func = _build_function(
                base_url=base_url,
                path=path,
                method=method,
                query_params=query_params,
                path_params=path_params,
                func_name=func_name,
                doc=method_spec.get("description"),
                has_body=has_body,
            )

            setattr(namespace, func_name, func)

    return namespace