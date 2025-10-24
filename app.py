from prompt_engineer_dataset_creator import create_topic_list_from_prompt, create_follow_up_question_from_prompt #, test_prompts_on_console
from flask import Flask, render_template, request
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
    app.logger.setLevel (logging.DEBUG)
    app.logger.addHandler (logger)

def write_response_to_log(response):
    app.logger.debug (response)

@app.route('/', methods = ['GET', 'POST'])
def index():
    initialize_logger()
    # KRISTIAN_TODO - Start a question here.
    response = create_topic_list_from_prompt (ollama.Client(), "llama3.1")
    write_response_to_log ('PROMPT --------')
    write_response_to_log (response.response)
    write_response_to_log ('REQUEST --------')
    write_response_to_log (request)
    if (request.method == 'GET'):
        # KRISTIAN_TODO - Every time I respond, fetch the response
        write_response_to_log ('RESPONSE FROM USER --------')
        write_response_to_log (request.form.to_dict())
        # KRISTIAN_TODO - Use that response to give a follow up question here.
        write_response_to_log ('FOLLOW_UP_PROMPT ------------------')
        response = create_follow_up_question_from_prompt (ollama.Client(), "llama3.1", request.form.to_dict())
    # KRISTIAN_TODO - Return that question under the prompt_response variable that displys as HTML here.
    return render_template('index.html', prompt_response = response)

def main():
    # test_prompts_on_console()
    # KRISTIAN_TODO - Make a nice favicon for my new app.
    app.run (debug = True)

if __name__ == "__main__":
    main()
