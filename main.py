import test_case_agent
from requirement_agent import requirement_agent
from test_case_agent import test_case_chain
from test_data_agent import test_data_agent
from test_review_agent import test_review_agent


requirement = """
An ecommerce application allows registered users to log in
using their email address and password.

After successful authentication, the user should be
redirected to the home page.

If invalid credentials are entered, an appropriate
error message should be displayed.
"""


# ==========================================
# AGENT 1 - REQUIREMENT ANALYSIS
# ==========================================

print("\n" + "=" * 70)
print("AGENT 1 - REQUIREMENT ANALYSIS")
print("=" * 70)

analysis_response = requirement_agent.invoke({
    "requirement": requirement
})

analysis = analysis_response.content

print(analysis)


# ==========================================
# AGENT 2 - TEST CASE GENERATION
# ==========================================

print("\n" + "=" * 70)
print("AGENT 2 - TEST CASE GENERATION")
print("=" * 70)

test_case_response = test_case_chain.invoke({
    "requirement": requirement,
    "analysis": analysis
})

test_cases = test_case_response.content

print(test_cases)

print("\nFULL RESPONSE:")
print(test_case_response)

print("\nCONTENT:")
print(test_case_response.content)


# ==========================================
# AGENT 3 - TEST DATA GENERATION
# ==========================================

print("\n" + "=" * 70)
print("AGENT 3 - TEST DATA GENERATION")
print("=" * 70)

test_data_response = test_data_agent.invoke({
    "requirement": requirement,
    "test_cases": test_cases
})

test_data = test_data_response.content

print(test_data)

print("\nFULL RESPONSE:")
print(test_data_response)

print("\nCONTENT:")
print(test_data_response.content)


# ==========================================
# AGENT 4 - TEST REVIEW
# ==========================================

print("\n" + "=" * 70)
print("AGENT 4 - TEST REVIEW")
print("=" * 70)

review_response = test_review_agent.invoke({
    "requirement": requirement,
    "analysis": analysis,
    "test_cases": test_cases,
    "test_data": test_data
})

review = review_response.content

print(review)

print("\nFULL RESPONSE:")
print(review_response)

print("\nCONTENT:")
print(review_response.content)