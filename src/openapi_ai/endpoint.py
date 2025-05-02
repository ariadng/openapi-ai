from .loader import load_spec
from .schema import process_schema


def list_endpoints(url: str, removeprefix: str = ""):
    spec = load_spec(url)
    base_url = str(url).removesuffix("/openapi.json")
    paths = spec['paths']

    print("\n---\n")

    for path, methods in paths.items():
        for method in methods.keys():
            _process_method(method, path, methods[method])

            print("\n---\n")
        

def _process_method(method: str, path: str, method_spec: dict):
    method_name = method.lower()
    method_desc = method_spec["description"] if "description" in method_spec else ""
    method_params = method_spec["parameters"] if "parameters" in method_spec else []
    request_body = method_spec["requestBody"] if "requestBody" in method_spec else None

    print(method_name, path)
    print("  • Parameters:")
    params = _process_params(method_params, request_body)
    # print(params)
    print("\n")


def _process_params(params: list, request_body: dict | None = None):

    # Params fields: name, type, required, description

    query_params = {}
    path_params = {}
    body_params = {}
    all_params = {}

    body_type = None
    body_schema = None
    if request_body:
        # Only supports application/json for v1.0
        body_type = "application/json"
        body_schema = request_body['content'][body_type]['schema'] if body_type in request_body['content'] else None
        print(body_schema)

    for param in params:
        name = param['name'] if 'name' in param else None
        in_ = param['in'] if 'in' in param else None
        required = param['required'] if 'required' in param else False
        schema = param['schema'] if 'schema' in param else None
        description = param['description'] if 'description' in param else ""

        type_ = process_schema(schema)

        param = {
            "name": name,
            "type": type_,
            "required": required,
            "description": description,
        }

        all_params[name] = param

        if in_ == "query":
            query_params[name] = param
        elif in_ == "path":
            path_params[name] = param

    return {
        "query_params": query_params,
        "path_params": path_params,
        "body_params": body_params,
        "all_params": all_params,
    }



