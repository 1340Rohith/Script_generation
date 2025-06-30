from flask import render_template, request
from flask import Flask
import Template_prompt
import requests
from ai import get_story
import ai


previous_changes_logic = ""
previous_changes_creativity = ""
previous_changes_master = ""
current_changes = "none"
message_sub = ""
user_changes = "none"


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.static_folder = 'static'
@app.route('/', methods=['GET', 'POST'])
def hello():
    global previous_changes_master, previous_changes_logic, previous_changes_creativity
    global current_changes, message_sub, accept_status,user_changes

    if request.method == 'POST':
        film_title = request.form.get('filmTitle', '')
        genre = request.form.get('genre', '')
        input_text = film_title  # Optional: Combine with genre

        if request.form.get('acceptButton') == 'true':
            # User accepted the story
            print("Accept button clicked")  # Debug
            previous_changes_master = ""
            previous_changes_logic = ""
            previous_changes_creativity = ""
            current_changes = "none"
            message_sub = ""
            return render_template('index.html', plot="✅ Story accepted!")

        elif request.form.get('rejectButton') == 'true':
            print("Reject button clicked")  # Debug
            # User rejected the story — generate new version
            user_changes = request.form.get('filmTitle', 'none')
            new_story = get_story(
                input1=input_text,
                master_instruction=ai.master_instruction,
                sub_instruction=ai.sub_instruction,
                logic_instruction=ai.logic_instruction,
                creativity_instruction=ai.creativity_instruction,
                previous_changes_master=previous_changes_master,
                previous_changes_logic=previous_changes_logic,
                previous_changes_creativity=previous_changes_creativity,
                current_changes=current_changes,
                user_changes=user_changes
            )
            message_sub = new_story
            return render_template('index.html', plot=new_story, Filmtitle="Enter your changes or accept the story")

        else:
            # Initial generation
            new_story = get_story(
                input1=input_text,
                master_instruction=ai.master_instruction,
                sub_instruction=ai.sub_instruction,
                logic_instruction=ai.logic_instruction,
                creativity_instruction=ai.creativity_instruction,
                previous_changes_master=previous_changes_master,
                previous_changes_logic=previous_changes_logic,
                previous_changes_creativity=previous_changes_creativity,
                current_changes=current_changes,
                user_changes=user_changes
            )
            message_sub = new_story
            return render_template('index.html', plot=new_story, Filmtitle="Enter your changes or accept the story")

    return render_template('index.html', plot=None, Filmtitle='film title')
