from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-5-sonnet-latest", 
    anthropic_api_key="dsfsdfdsfsfsd"  # Note the parameter name
)

question = input("Enter the question: ")
response = llm.invoke(question)
print(response.content)
