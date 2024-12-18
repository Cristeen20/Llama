from model_conf import model_return,config_data
#from prompt_script import prompt

model_name = config_data["model_name"]
text_generator = model_return(model_name)


prompt = "generate a 200 word story on monkey"
# Generate text based on the prompt
generated_text = text_generator(prompt)

# Print the output
print(generated_text)
