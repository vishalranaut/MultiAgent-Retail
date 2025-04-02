import ollama

def llm_predict(prompt):
    model_name = "mistral"
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]