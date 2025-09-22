import ollama

def create_topic_list_from_prompt(ollama_client, llm_model):
    prompt = "You are a helpful Swedish textbook author.  Please assemble a list of "\
        "topics an English native speaker could learn in an introductory course to "\
        "acquire the ability to converse in Swedish."
    response = ollama_client.generate (model = llm_model, prompt = prompt)
    return response

def test_prompts_on_console():
    response = create_topic_list_from_prompt (ollama.Client(), "llama3.1")
    print (response.response)
    