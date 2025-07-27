from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the Ollama model and prompt template
OLLAMA_MODEL = "llama3.2"  # Replace with your desired Ollama model
prompt_template = """
Write an email to my boss for resignation.
"""

# Initialize the model and prompt
model = OllamaLLM(model=OLLAMA_MODEL)
prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | model

def test_ollama_api():
    """
    Tests the Ollama LLM API by invoking the chain with a prompt.
    """
    try:
        # Use the defined chain to process the prompt
        response = chain.invoke({"context": "", "question": "Write an email to my boss for resignation."})
        print("Response from Ollama API:")
        print(response)
    except Exception as e:
        print(f"Error during Ollama LLM invocation: {e}")

if __name__ == "__main__":
    test_ollama_api()
