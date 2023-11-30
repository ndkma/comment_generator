import together
from tkinter import *

together.api_key = "YOUR API KEY HERE"

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
    model = "togethercomputer/llama-2-13b-chat",
    max_tokens = 70,
    temperature = 0.6,
    top_k = 90,
    top_p = 0.8,
    repetition_penalty = 1.1,
    stop = ['</s>']
)

complete_output = output['output']['choices'][0]['text']

print(complete_output)

short_output = complete_output.split(":")[1]

# Needs to be output somewhere copy-able ===================================================
print(short_output)

# Create base GUI
master = Tk()
master.title("Report Card Comment Generator")
master.geometry("1200x600")

# Create student name input field
student_name_field = Entry(master, font = 40).place(x = 200, y = 25)

# Create static labels
Label(master, text = "Student Name:", font=40).place(x = 25, y = 25)
Label(master, text = "Writing Score:", font=40).place(x = 25, y = 125)
Label(master, text = "Speaking Score:", font=40).place(x = 25, y = 225)
Label(master, text = "Listening Score:", font=40).place(x = 25, y = 325)
Label(master, text = "Reading Score:", font=40).place(x = 25, y = 425)

# Create scales for scoring
writing_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218).place(x = 200, y = 112)
speaking_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218).place(x = 200, y = 212)
listening_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218).place(x = 200, y = 312)
reading_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218).place(x = 200, y = 412)

# Create set score buttons



master.mainloop()