from langchain_core.prompts import ChatPromptTemplate
from llm_config import chat_model


test_data_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a test data generation specialist.

Generate realistic but synthetic test data for the given
software testing requirement.

Do NOT use real personal information.

Include:

- Valid data
- Invalid data
- Boundary data
- Empty/null data
- Special characters where appropriate

Present the data in a clear table-like format.
"""
    ),
    (
        "human",
        """
Requirement:

{requirement}

Test Cases:

{test_cases}
"""
    )
])


test_data_agent = test_data_prompt | chat_model