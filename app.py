from prompt_engineer_dataset_creator import create_topic_list_from_prompt #, test_prompts_on_console
from flask import Flask, render_template
import logging
from logging import FileHandler
import ollama

# from huggingface_attempt import run_huggingface_model # KRISTIAN_TODO - Why does it segfault?

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'placeholder'

def initialize_logger():
    logger = FileHandler ('debug.log')
    logger.setLevel (logging.DEBUG)
    app.logger.setLevel (logging.DEBUG)
    app.logger.addHandler (logger)

def write_response_to_log(response):
    app.logger.debug (response)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

def main():
    # test_prompts_on_console()
    initialize_logger()
    response = create_topic_list_from_prompt (ollama.Client(), "llama3.1")
    write_response_to_log (response.response)
    app.run (debug = True)  # KRISTIAN_TODO - Make a nice favicon for my new app.

if __name__ == "__main__":
    main()
