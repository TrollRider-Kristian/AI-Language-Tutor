import os
import transformers
import torch

# KRISTIAN_TODO - Now that my account has been approved for this model,
# How do I download / run it locally via Ollama?
# When I try ollama run, I get this error: pull model manifest: 400:
# {"error":"Repository is not GGUF or is not compatible with llama.cpp"}
# So here's my attempt to run it straight from online HuggingFace.
def run_huggingface_model ():
    # Pass in a token to get access to an approved model:
    # https://stackoverflow.com/questions/79211723/cannot-load-a-gated-model-from-hugginface-despite-having-access-and-logging-in
    hf_token = os.environ["HUGGINGFACE_API_KEY"]
    model_id ="meta-llama/Meta-Llama-3.1-8B-Instruct"
    # tokenizer = transformers.AutoTokenizer.from_pretrained (model_id, token = hf_token)
    hf_model = transformers.AutoModelForCausalLM.from_pretrained (model_id, token = hf_token)
    pipeline = transformers.pipeline (
        "text-generation",
        model = hf_model,
        model_kwargs = {"torch_dtype": torch.bfloat16}, # KRISTIAN_TODO - What is this? Why Torch?
        device_map = "auto", # KRISTIAN_TODO - What even is this??
    )
    messages = [
        {"role": "system", "content": "You are a helpful Swedish language tutor."},
        {"role": "user", "content": "Ask a question for a beginner in Swedish and rate the grammatical correctness of my answer."},
    ]
    outputs = pipeline (messages, max_new_tokens = 10000)
    return outputs
