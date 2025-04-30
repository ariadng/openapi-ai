from llmtools.generator import generate_tools, load_spec, generate_components

if __name__ == "__main__":
    # tools = generate_tools("http://103.191.63.49:8888")

    # positions = tools.get_positions_symbol(symbol="XAUUSD")
    # print(positions)

    # Create order
    # order = tools.create_orders_market(body={
    #     "symbol": "XAUUSD",
    #     "volume": 1,
    #     "type": "BUY",
    # })
    
    # print(order)
    
    # func_list = [fn for fn in vars(tools).values() if callable(fn)]

    # for fn in func_list:
    #     print(fn.__name__ + "()")
    #     print(fn.__doc__)
    #     print("\n")

    spec = load_spec("http://103.191.63.49:8888")
    generate_components(spec)
    


