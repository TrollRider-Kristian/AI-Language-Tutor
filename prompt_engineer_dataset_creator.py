import ollama

# KRISTIAN_TODO - When I try running this, I get a segmentation fault.  Why?
# Not in the scope of this project right now, use existing Ollama models for project first.
# from huggingface_attempt import run_huggingface_model

def create_topic_list_from_prompt(ollama_client, llm_model):
    prompt = "You are a helpful Swedish textbook author.  Please assemble a list of "\
        "topics an English native speaker could learn in an introductory course to "\
        "acquire the ability to converse in Swedish."
    response = ollama_client.generate (model = llm_model, prompt = prompt)
    return response

def main():
    response = create_topic_list_from_prompt (ollama.Client(), "llama3.1")
    print (response.response)

if __name__ == "__main__":
    main()
    