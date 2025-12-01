#!/usr/bin/env python3
"""
Create the COMPLETE Flashcard Deck for Chapter 1 (06-flashcards.ipynb)
Restores the full set of 10 Feynman cards.
"""

import nbformat as nbf
import os

target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
os.chdir(target_dir)

print(f"\n🧠 Restoring Flashcard Deck in: {os.getcwd()}")

nb = nbf.v4.new_notebook()

nb.cells = [
    # Title and Intro
    nbf.v4.new_markdown_cell("""# 🧠 Chapter 1 Flashcards: Atoms in Motion
## Master the Concepts through Active Recall

**Instructions:**
1.  Run the cell below to load the flashcard engine.
2.  Read the **Question**.
3.  Try to answer it in your head or out loud.
4.  Click **"Flip Card"** to check your answer.
5.  Rate your confidence or just move to **"Next"**.

*"You cannot fool yourself, and you are the easiest person to fool."* — R.P. Feynman
"""),

    # Flashcard Data & Engine
    nbf.v4.new_code_cell("""import ipywidgets as widgets
from IPython.display import display, Markdown, clear_output
import random

# ---------------------------------------------------------
# 📚 THE FLASHCARD DECK (Chapter 1)
# ---------------------------------------------------------
flashcards = [
    {
        "q": "### The Atomic Hypothesis\\n\\nWhat is the one sentence Feynman would save if all scientific knowledge were destroyed?",
        "a": "**\"All things are made of atoms—little particles that move around in perpetual motion, attracting each other when they are a little distance apart, but repelling upon being squeezed into one another.\"**"
    },
    {
        "q": "### Heat\\n\\nWhat is 'heat' energy at the atomic level?",
        "a": "**Molecular Motion.**\\n\\nIn a gas, it's the kinetic energy of the particles. In a solid, it's the vibration of atoms in their lattice spots."
    },
    {
        "q": "### Forces Between Atoms\\n\\nDescribe the force between two atoms as a function of distance.",
        "a": "1. **Far apart:** Weak attraction (gravity, negligible).\\n2. **Little distance:** Strong **Attraction**.\\n3. **Very close (squeezed):** Very strong **Repulsion**."
    },
    {
        "q": "### States of Matter\\n\\nWhat distinguishes a **Solid** from a **Liquid** atomically?",
        "a": "**Structure vs. Mobility**\\n\\n*   **Solid:** Atoms occupy fixed positions in a lattice pattern (though they vibrate).\\n*   **Liquid:** Atoms are packed close together but have no fixed structure and slide past one another."
    },
    {
        "q": "### Temperature & Evaporation\\n\\nWhy does evaporation cause the remaining liquid to cool down?",
        "a": "**Selection of the Fastest**\\n\\nOnly the fastest molecules have enough energy to escape the attraction of their neighbors. When they leave, the *average* energy (temperature) of the remaining molecules drops."
    },
    {
        "q": "### Pressure\\n\\nWhat causes pressure in a gas confined in a piston?",
        "a": "**Bombardment**\\n\\nPressure is the result of billions of atoms hitting the walls of the container and bouncing off, transferring momentum."
    },
    {
        "q": "### Evidence for Atoms\\n\\nWhat is **Brownian Motion** and why is it significant?",
        "a": "It is the random jiggling of microscopic particles (like pollen or dust) in a fluid.\\n\\n**Significance:** It provides direct visible evidence of the existence of atoms, as the jiggling is caused by the random bombardment of invisible molecules."
    },
    {
        "q": "### Crystal Structure\\n\\nWhat does the shape of a crystal (like salt) tell us about atoms?",
        "a": "It reveals the **geometric arrangement** of the atoms.\\n\\nThe macroscopic faces and angles of a crystal directly reflect the microscopic lattice structure of its atoms."
    },
    {
        "q": "### Chemical Reactions\\n\\nWhat is a 'Chemical Reaction' in terms of atoms?",
        "a": "**Atoms changing partners.**\\n\\nBurning carbon, for example, is just carbon atoms snapping into a new combination with oxygen atoms (C + O₂ → CO₂), releasing energy in the process."
    },
    {
        "q": "### Biology\\n\\nWhat is the most important hypothesis in biology regarding physics?",
        "a": "**\"Everything that animals do, atoms do.\"**\\n\\nThere is no \"vital force.\" Life can be understood as atoms acting according to the laws of physics."
    }
]

# ---------------------------------------------------------
# ⚙️ INTERACTIVE ENGINE
# ---------------------------------------------------------
class FlashcardViewer:
    def __init__(self, deck):
        self.deck = deck
        self.index = 0
        self.showing_answer = False
        self.shuffled_indices = list(range(len(deck)))
        
        # Widgets
        self.out = widgets.Output(layout={'border': '1px solid #444', 'padding': '20px', 'min_height': '200px'})
        self.btn_flip = widgets.Button(description="🔄 Flip Card", button_style='info', icon='exchange')
        self.btn_next = widgets.Button(description="Next ➡️", button_style='')
        self.btn_prev = widgets.Button(description="⬅️ Prev", button_style='')
        self.btn_shuffle = widgets.Button(description="🔀 Shuffle", icon='random')
        self.lbl_count = widgets.Label(value=f"Card 1 of {len(deck)}")
        
        # Layout
        self.controls = widgets.HBox([self.btn_prev, self.btn_flip, self.btn_next, self.btn_shuffle])
        self.layout = widgets.VBox([self.lbl_count, self.out, self.controls])
        
        # Events
        self.btn_flip.on_click(self.flip)
        self.btn_next.on_click(self.next_card)
        self.btn_prev.on_click(self.prev_card)
        self.btn_shuffle.on_click(self.shuffle)
        
        self.display_card()

    def display_card(self):
        self.out.clear_output()
        card_idx = self.shuffled_indices[self.index]
        card = self.deck[card_idx]
        
        with self.out:
            if not self.showing_answer:
                display(Markdown(f"# ❓ Question\\n\\n{card['q']}"))
            else:
                display(Markdown(f"# 💡 Answer\\n\\n{card['a']}"))
        
        self.lbl_count.value = f"Card {self.index + 1} of {len(self.deck)}"

    def flip(self, b):
        self.showing_answer = not self.showing_answer
        self.display_card()

    def next_card(self, b):
        self.index = (self.index + 1) % len(self.deck)
        self.showing_answer = False
        self.display_card()

    def prev_card(self, b):
        self.index = (self.index - 1) % len(self.deck)
        self.showing_answer = False
        self.display_card()

    def shuffle(self, b):
        random.shuffle(self.shuffled_indices)
        self.index = 0
        self.showing_answer = False
        self.display_card()

# Run the viewer
viewer = FlashcardViewer(flashcards)
display(viewer.layout)""")
]

with open("06-flashcards.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("✅ Flashcards RESTORED: 06-flashcards.ipynb")
