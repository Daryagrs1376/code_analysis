from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LocalLLM:
    def __init__(self, model_name="llama-7b"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def analyze(self, function_code: str):
        inputs = self.tokenizer(function_code, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(inputs["input_ids"], max_length=100)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result

local_llm = LocalLLM()

def analyze_code(function_code: str):
    return local_llm.analyze(function_code)
