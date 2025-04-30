from agent_tools.generator import generate_tools

if __name__ == "__main__":
    tools = generate_tools("http://103.191.63.49:8888")
    response = tools.get_accounts_info()
    print(response)