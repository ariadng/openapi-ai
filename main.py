from openapi_ai.endpoint import list_endpoints

if __name__ == "__main__":
    # tools = generate_tools("http://103.191.63.49:8888", removeprefix="/api/v1")
    # positions = tools.get_accounts_info()
    # print("\n >> Response:")
    # print(positions)

    list_endpoints("http://103.191.63.49:8888", removeprefix="/api/v1")
