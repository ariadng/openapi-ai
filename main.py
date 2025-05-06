from openapi_ai.generator import generate_tools

if __name__ == "__main__":
    tools = generate_tools("http://103.191.63.49:8888", removeprefix="/api/v1")
    print(dir(tools))
    print(tools["get_accounts_info"]())
    # print(tools.create_orders_market(symbol="XAUUSD", type="BUY", volume=1))
