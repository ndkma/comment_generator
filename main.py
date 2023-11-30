import together

together.api_key = "<<YOUR API KEY HERE>>"

# Provide context for generating responses
context_prompt = (
    "You are a teacher, writing report cards for first grade ESL students. "
    "You will be assigned a subject and a score out of 10. Write a 30-word comment on their ability."
)

# Needs to change on input and with buttons ==============================
student_name = "Bob"
subject_name = "Speaking"
subject_score = "6"

# Clicking generate should run the code below ================================
# Provide specific information for the LLM to base the comment off of
specific_prompt = [
    f"Student name is {student_name}. {subject_name}, {subject_score}/10"
]

# Construct the final prompt for the LLM based off of the context_prompt and specific_prompt
prompt = f"<s>[INST] <<SYS>>{context_prompt}<</SYS>>\\n\\n"

for user_msg in specific_prompt:
    prompt += f"[INST]{user_msg}[/INST]"

output = together.Complete.create(
    prompt,
    model="togethercomputer/llama-2-13b-chat",
    max_tokens=70,
    temperature=0.6,
    top_k=90,
    top_p=0.8,
    repetition_penalty=1.1,
    stop=['</s>']
)

complete_output = output['output']['choices'][0]['text']

print(complete_output)

short_output = complete_output.split(":")[1]

# Needs to be output somewhere copy-able ===================================================
print(short_output)
