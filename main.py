from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

# Fixed the spelling of {reviews} here
template = """
You are an expert in answering questions about a pizza restaurant.

here are some relevant reviews: {reviews}

here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

#asking question as we are using while loop so that we can repeat the process 
while True:
    print("\n\n --------------------------------------------------------------")
    question = input("Ask your Question (q to quit): ")
    print("Pizza bot response: ")
    if question == "q":
        break
    # Sending the corrected dictionary
    result = chain.invoke({
    "reviews": [], 
    "question": "What is the best pizza place in town?"
    })

    print(result)
