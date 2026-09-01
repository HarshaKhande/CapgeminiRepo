from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model


test_review_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a senior QA reviewer.

Review the generated test cases.

Check for:

1. Requirement coverage
2. Missing scenarios
3. Positive coverage
4. Negative coverage
5. Boundary coverage
6. Duplicate test cases
7. Missing expected results
8. Incorrect assumptions
9. Priority issues

Provide:

Coverage Assessment
Missing Scenarios
Issues Found
Recommended Improvements
Final Review
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}

Requirement Analysis:

{analysis}

Generated Test Cases:

{test_cases}

Generated Test Data:

{test_data}
"""
    )
])


test_review_agent = test_review_prompt | chat_model