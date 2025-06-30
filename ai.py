import requests
import Template_prompt
from flask import Flask, render_template, request

master_instruction = (
    "Primary Instruction:\n"
    "You are a skilled storywriter who writes compelling stories in exactly 3 acts:\n"
    "- Act 1: Setup - Introduce the main character(s), the world or setting, and the initial conflict or situation.\n"
    "- Act 2: Confrontation - Deepen the conflict, raise the stakes, introduce complications, and show character evolution.\n"
    "- Act 3: Resolution - Resolve the main conflict, bring closure, and reflect on character transformation or consequences.\n\n"

    "You must always write the **entire story from Act 1 through Act 3 in each output**. "
    "Never continue from a previous act or generate incomplete stories. Do not exceed or skip acts.\n\n"

    "**User input and change requests must take the highest priority.** All user instructions must be followed exactly, "
    "even if it requires altering the structure, characters, or events.\n\n"

    "Write the story using vivid, immersive language. Do not include summaries, comments, or explanations.\n"
    "always write act numbers following the story text, like this:\n"
    "Act 1: story\n"
    "Act 2: story\n"
    "Act 3: story\n\n"
)

sub_instruction = (
    "Secondary Instruction:\n"
    "If the user provides changes, edits, or corrections, you must revise the story accordingly. "
    "You must fully rewrite the story from the beginning (Act 1 to Act 3), incorporating the changes precisely and naturally.\n\n"
    "Ensure that the revised story still follows the 3-act format and maintains logical flow, coherence, and character integrity."
)

logic_instruction = (
    "Logic Evaluation Role:\n"
    "evaluate it for logical consistency and internal coherence.\n"
    "If something is unrealistic or breaks the narrative logic, specify **what to add or fix**, **in which act**, and **how**, in a short and direct format.\n"
    "Example: Act 2 - Conflict is resolved too quickly; add a second obstacle to increase tension."
)

creativity_instruction = (
    "Creativity Evaluation Role:\n"
    "Evaluate the story for uniqueness and creative depth. If any part is bland, cliché, or lacking imagination, suggest what to change.\n"
    "Be specific: **what to improve**, **in which act**, and **how**. Keep it brief.\n"
    "Example: Act 1 - The setting is too ordinary; add an unusual tradition or surreal element to the environment."
)



previous_changes_logic = ""
previous_changes_creativity = ""
previous_changes_master = ""
current_changes = "none"
message_sub = ""
user_changes = "none"



accept_status = 0
count = 0




def get_story(input1, master_instruction, sub_instruction, logic_instruction, creativity_instruction, previous_changes_master, previous_changes_logic, previous_changes_creativity, current_changes,user_changes):
    #master agent
    temp = Template_prompt.Master_prompt.format(
    master_primary_instruction=master_instruction,
    message=input1,
    master_secondary_instruction=sub_instruction,
    changes=current_changes,
    previous_changes_master=previous_changes_master,
    )
    response_master = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral:instruct",
        "prompt": temp,
        "stream": False,
    })
    data_master = response_master.json()
    story = data_master.get("response")
    #logic agent
    sub_temp_logic = Template_prompt.Sub_agent_prompt.format(
        sub_primary_instruction=logic_instruction,
        sub_secondary_instruction="none",
        history_story=message_sub,
        message_sub=story,
        previous_changes_sub=previous_changes_logic
    )
    response_sub_uniqueness = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral:instruct",
        "prompt": sub_temp_logic,
        "stream": False,
    })
    data_logic = response_sub_uniqueness.json()
    logic = data_logic.get("response")
    previous_changes_master += logic + "\n"
    previous_changes_logic += logic + "\n"
    #uniqueness agent
    sub_temp_creativity = Template_prompt.Sub_agent_prompt.format(
        sub_primary_instruction=creativity_instruction,
        sub_secondary_instruction="none",
        history_story=message_sub,
        message_sub=story,
        previous_changes_sub=previous_changes_creativity
    )
    response_sub_creativity = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral:instruct",
        "prompt": sub_temp_creativity,
        "stream": False,
    })
    data_creativity = response_sub_creativity.json()
    creativity = data_creativity.get("response")
    previous_changes_creativity += creativity + "\n"
    previous_changes_master += creativity + "\n"

    print("Intermediate Story: \n", story)
    current_changes = Template_prompt.changes.format(
        logical_agent=logic,
        creativity_agent=creativity,
        user_changes=user_changes
    )
    return story