from llm_config import chat_model

response = chat_model.invoke(
    "Generate 5 test cases for an ecommerce login page."
)

print("RESPONSE:")
print(response)
print("\nCONTENT:")
print(response.content)