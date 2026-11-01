from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-5-sonnet-latest", 
    anthropic_api_key="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"  # Note the parameter name
)

question = input("Enter the question: ")
response = llm.invoke(question)
print(response.content)