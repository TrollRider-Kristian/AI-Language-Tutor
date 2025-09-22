from prompt_engineer_dataset_creator import create_topic_list_from_prompt #, test_prompts_on_console
from flask import Flask
import ollama
# from huggingface_attempt import run_huggingface_model # KRISTIAN_TODO - Why does it segfault?
app = Flask(__name__)

@app.route('/')
def index():
    return create_topic_list_from_prompt (ollama.Client(), "llama3.1").response

def main():
    # test_prompts_on_console()
    app.run (debug = True)  # KRISTIAN_TODO - Make a nice favicon for my new app.

if __name__ == "__main__":
    main()
