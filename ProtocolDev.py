# to take prompts and get replies

import openai

openai.api_key = "####" 

messages=[{"role": "system", "content": "You are an expert in biological science, wetlab experimentation and protocol creation. You will get requests to write protocol for biology experiments and you should give a detailed, in-depth list of steps to be followed in the lab."}]
# Write a protocol for Capture HiC on neural stem cells.

def generate_response(prompt):
    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        n = 1, 
        messages = messages
        )
    message = completion.choices[0].message.content #completion['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": message})
    return message 

m = input("Enter prompt")
generate_response(m)
