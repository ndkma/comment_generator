import together
import tkinter as tk
from tkinter import *

together.api_key = "YOUR TOGETHER.AI API KEY HERE AS STRING"

def generate_comment() -> None:
    """
    Grabs the following variables from the widgets on the GUI, and adds them to specific_prompt list:

    - Score between 0 - 10 from the Scales widgets (sliders); Writing, Speaking, Listening and Reading
    - Student name from the Entry widget

    The specific_prompt and context_prompt are then used in conjunction with the LLM to generate a comment.
    The comment is then displayed on the output_area.

    Called by Button btn_gen
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    output_area.delete('1.0', tk.END)       # Clear the text box

    # Create variables from objects on GUI
    student_name = student_name_field.get()
    writing = "Writing"
    writing_score = str(writing_scale.get())
    speaking = "Speaking"
    speaking_score = str(speaking_scale.get())
    listening = "Listening"
    listening_score = str(listening_scale.get())
    reading = "Reading"
    reading_score = str(reading_scale.get())

    # Provide background context for the LLM for generating responses
    context_prompt = (
        "You are a teacher, writing report cards for first grade ESL students. "
        "You will be assigned 4 subjects and for each a score out of 10. "
        "Comment on each subject individually, no more than 30 words each. "
    )

    # Provide specific information for the LLM to base the comment off of
    specific_prompt = [
        f"Student name is {student_name}. {writing}, {writing_score}/10"
        f"{speaking}, {speaking_score}/10"
        f"{listening}, {listening_score}/10"
        f"{reading}, {reading_score}/10"
    ]

    # Construct the final prompt for the LLM based off of the context_prompt and specific_prompt
    prompt = f"<s>[INST] <<SYS>>{context_prompt}<</SYS>>\\n\\n"

    for specifics in specific_prompt:
        prompt += f"[INST]{specifics}[/INST]"

    # Generates the comment with the following parameters
    output = together.Complete.create(
        prompt,
        model = "togethercomputer/llama-2-13b-chat",        # Chat model to be used
        max_tokens = 250,                                   # Hard limit on length of comment
        temperature = 0.5,                                  # Measure of comment creativity
        top_k = 90,                                         # Measure of comment diversity
        top_p = 0.8,
        repetition_penalty = 1.1,                           # Slightly discourage repetition between comments
        stop = ['</s>']
    )

    # Save final generated comment to variable
    complete_output = output['output']['choices'][0]['text']
    print(complete_output)

    # Display generated comment on text-box on GUI.
    output_area.insert(tk.END, complete_output.strip())

# Create base GUI
master = Tk()
master.title("Report Card Comment Generator")
master.geometry("1170x590")

# Create student name input field
student_name_field = Entry(master, font = 40, width = 25)
student_name_field.place(x = 200, y = 25)

# Create static labels
Label(master, text = "Student Name:", font = 40).place(x = 25, y = 25)
Label(master, text = "Writing Score:", font = 40).place(x = 25, y = 125)
Label(master, text = "Speaking Score:", font = 40).place(x = 25, y = 225)
Label(master, text = "Listening Score:", font = 40).place(x = 25, y = 325)
Label(master, text = "Reading Score:", font = 40).place(x = 25, y = 425)

# Create scales for scoring
writing_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218)
writing_scale.place(x = 200, y = 112)
speaking_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218)
speaking_scale.place(x = 200, y = 212)
listening_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218)
listening_scale.place(x = 200, y = 312)
reading_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, length = 218)
reading_scale.place(x = 200, y = 412)

# Create button for generating comment, it calls generate_comment() function on click
btn_gen = Button(master, text = "Generate Comment", width = 25, font = 80, command = generate_comment).place(x = 470, y = 225)

# Create text output area for the generated comment
output_area = Text(master, height = 28, width = 40, wrap = WORD)
output_area.place(x = 800, y = 25)

master.mainloop()