#!/usr/bin/env python3
"""
Fixes the Chapter 3 Quiz to include proper grading, visual feedback, and a final score.
"""

import nbformat as nbf
import os

# Set directory
chapter_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch03-relation-of-physics-to-other-sciences"
os.chdir(chapter_dir)

def create_notebook(filename, cells):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    with open(filename, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"✅ Fixed Quiz: {filename}")

# ---------------------------------------------------------
# Improved Quiz Code
# ---------------------------------------------------------
quiz_code = r"""
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

# Quiz Data
questions = [
    {
        "q": "Why is Mathematics NOT considered a natural science by Feynman?",
        "options": ["It is too difficult", "It is not based on experiment", "It is not useful", "It is older than physics"],
        "correct": "It is not based on experiment"
    },
    {
        "q": "Which scientific principle was first discovered in Biology (by Mayer) before Physics?",
        "options": ["Gravity", "Evolution", "Conservation of Energy", "Relativity"],
        "correct": "Conservation of Energy"
    },
    {
        "q": "What is the source of a star's energy?",
        "options": ["Chemical Burning", "Nuclear Fusion", "Gravitational Collapse", "Friction"],
        "correct": "Nuclear Fusion"
    },
    {
        "q": "Why is the weather harder to predict than the motion of planets?",
        "options": ["We don't know the equations", "The air is invisible", "Turbulent flow is unstable", "Planets move slower"],
        "correct": "Turbulent flow is unstable"
    },
    {
        "q": "According to Feynman, what is the most powerful assumption in biology?",
        "options": ["Life requires a vital force", "Evolution is random", "Everything animals do, atoms do", "The brain is a computer"],
        "correct": "Everything animals do, atoms do"
    },
    {
        "q": "Why does Feynman call Psychoanalysis 'witch-doctoring'?",
        "options": ["It is fake", "It lacks experimental verification", "It uses magic", "It is too expensive"],
        "correct": "It lacks experimental verification"
    },
    {
        "q": "Which element was discovered on the Sun before the Earth?",
        "options": ["Hydrogen", "Helium", "Carbon", "Oxygen"],
        "correct": "Helium"
    },
    {
        "q": "What is the 'Glass of Wine' metaphor about?",
        "options": ["Alcoholism", "The unity of all sciences", "Fluid dynamics", "Chemistry of fermentation"],
        "correct": "The unity of all sciences"
    }
]

# State
score = 0
answered_count = 0
total_questions = len(questions)

# Output widget for final score
result_out = widgets.Output()

def run_quiz():
    print("🧠 Chapter 3 Mastery Quiz")
    print("Select the best answer for each question.\n")
    
    display(result_out)
    
    for i, q in enumerate(questions):
        # Question Label
        display(HTML(f"<b>Q{i+1}: {q['q']}</b>"))
        
        # Button handler
        def create_handler(btn, correct_answer, other_btns):
            def handler(b):
                global score, answered_count
                
                # Disable all buttons for this question
                for ob in other_btns:
                    ob.disabled = True
                
                # Check answer
                if b.description == correct_answer:
                    b.style.button_color = '#90EE90'  # Light Green
                    b.icon = 'check'
                    score += 1
                else:
                    b.style.button_color = '#FFB6C1'  # Light Pink
                    b.icon = 'times'
                    # Highlight correct one
                    for ob in other_btns:
                        if ob.description == correct_answer:
                            ob.style.button_color = '#90EE90'
                            ob.icon = 'check'
                
                answered_count += 1
                
                # Check if finished
                if answered_count == total_questions:
                    with result_out:
                        clear_output()
                        percentage = (score / total_questions) * 100
                        display(HTML(f"<h3>🎉 Quiz Complete!</h3>"))
                        display(HTML(f"<b>Final Score: {score}/{total_questions} ({percentage:.0f}%)</b>"))
                        if percentage >= 80:
                            print("🌟 Excellent job! You have mastered this chapter.")
                        else:
                            print("📚 Good effort! Review the sections you missed.")

            return handler

        # Create Buttons
        btns = []
        for opt in q["options"]:
            btn = widgets.Button(description=opt, layout=widgets.Layout(width='300px'))
            btns.append(btn)
        
        # Attach handlers
        for btn in btns:
            btn.on_click(create_handler(btn, q["correct"], btns))
            
        display(widgets.VBox(btns))
        display(HTML("<hr>"))

run_quiz()
"""

create_notebook("Activity_Interdisciplinary_Quiz.ipynb", [nbf.v4.new_code_cell(quiz_code)])
