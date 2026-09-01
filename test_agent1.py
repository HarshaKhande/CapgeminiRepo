from requirement_agent import requirement_agent


requirement = """
An ecommerce application allows registered users to log in
using their email address and password.

After successful authentication, the user should be
redirected to the home page.

If invalid credentials are entered, an appropriate
error message should be displayed.
"""


print("=" * 70)
print("AGENT 1 - REQUIREMENT ANALYSIS")
print("=" * 70)

response = requirement_agent.invoke({
    "requirement": requirement
})

print("FULL RESPONSE:")
print(response)

print("\nCONTENT:")
print(response.content)