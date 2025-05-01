from openapi_ai.generator import generate_tools

if __name__ == "__main__":
    tools = generate_tools("http://103.191.63.49:8888", removeprefix="/api/v1")
    positions = tools.get_positions_symbol(symbol="XAUUSD")
    print("\n >> Response:")
    print(positions)

