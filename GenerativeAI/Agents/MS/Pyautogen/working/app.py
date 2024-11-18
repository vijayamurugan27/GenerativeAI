from autogen import AssistantAgent, UserProxyAgent

# Define the configuration for the code LLama model
config_list = [
    {
        "model":"qwen2.5-coder:3b",
        "base_url":"http://localhost:11434/v1",
        "api_key":"ollama",
    }
]

# create an AssistantAgent with the Code llama model
assistant = AssistantAgent("assistant", llm_config = {"config_list": config_list})

#Create an UserProxyAgent that can execute code.
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir":"coding", "use_docker":False})

user_proxy.initiate_chat(assistant, message="whats is today? find the stock price of TATAMOTORS change YTD.Get information using yfinance.")