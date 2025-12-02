#!/usr/bin/env python3
"""
Creates the deep-dive notebook for Ch 4, Section 4-4: Other forms of energy.
"""

import nbformat as nbf
import os

chapter_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch04-conservation-of-energy"
os.chdir(chapter_dir)

def create_notebook(filename, cells):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    with open(filename, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"✅ Created: {filename}")

cells = [
    # Header
    nbf.v4.new_markdown_cell(
        "# 4-4: Other forms of energy\n"
        "## The Full Catalog\n"
        "Feynman expands the energy inventory beyond gravitational and kinetic to include elastic, heat, electrical, chemical, nuclear, and mass energy."
    ),
    
    # Elastic Energy
    nbf.v4.new_markdown_cell(
        "## Elastic Energy\n"
        "When you stretch a spring, you do work. The spring can then lift a weight, so it has stored energy.\n"
        "- **Formula:** \\(E_{elastic} = \\frac{1}{2}kx^2\\) (where \\(k\\) is the spring constant and \\(x\\) is displacement).\n"
        "- **Behavior:** The spring oscillates, converting elastic energy ↔ kinetic energy.\n"
        "- **But eventually it stops.** Where does the energy go?"
    ),
    
    # Heat Energy
    nbf.v4.new_markdown_cell(
        "## Heat Energy: The Hidden Motion\n"
        "> \"We lose track of that energy; we find the atoms are wiggling inside in a random and confused manner.\"\n\n"
        "- When things rub, slide, or compress, atoms jiggle randomly.\n"
        "- This **internal kinetic energy** is what we call **heat**.\n"
        "- It is not a new form of energy—it is just kinetic energy we cannot see or control.\n"
        "- We measure it with thermometers."
    ),
    
    # The Energy Catalog
    nbf.v4.new_markdown_cell(
        "## The Full Energy Catalog\n"
        "| Form | What it is | Example |\n"
        "| :--- | :--- | :--- |\n"
        "| **Gravitational** | Position in a gravitational field | \\(mgh\\) |\n"
        "| **Kinetic** | Motion | \\(\\frac{1}{2}mv^2\\) |\n"
        "| **Elastic** | Stretching/compressing | Spring, rubber band |\n"
        "| **Heat** | Random atomic motion | Friction, temperature |\n"
        "| **Electrical** | Pushing/pulling by charges | Batteries, capacitors |\n"
        "| **Radiant** | Electromagnetic waves | Light, radio waves |\n"
        "| **Chemical** | Attraction between atoms | Burning fuel, digestion |\n"
        "| **Nuclear** | Arrangement inside nuclei | Fission, fusion |\n"
        "| **Mass** | Sheer existence | \\(E = mc^2\\) |"
    ),
    
    # E=mc^2
    nbf.v4.new_markdown_cell(
        "## Mass Energy: \\(E = mc^2\\)\n"
        "Feynman introduces Einstein's most famous equation:\n"
        "> \"An object has energy from its sheer existence.\"\n\n"
        "- If a positron and electron meet and annihilate, they release energy as light.\n"
        "- The amount is \\(E = mc^2\\), where \\(m\\) is the mass that disappeared.\n"
        "- This is the ultimate form of energy: **mass itself is energy**."
    ),
    
    # Other Conservation Laws
    nbf.v4.new_markdown_cell(
        "## Other Conservation Laws\n"
        "Energy is not the only conserved quantity. Feynman lists six conservation laws:\n\n"
        "### Subtle (Related to Space-Time Symmetry)\n"
        "1. **Energy** → Conservation comes from time-translation symmetry.\n"
        "2. **Linear Momentum** → Conservation comes from space-translation symmetry.\n"
        "3. **Angular Momentum** → Conservation comes from rotational symmetry.\n\n"
        "### Simple (Counting Blocks)\n"
        "4. **Charge** → Total positive minus negative charges never changes.\n"
        "5. **Baryon Number** → Protons, neutrons (and their antiparticles) are conserved.\n"
        "6. **Lepton Number** → Electrons, muons, neutrinos (and their antiparticles) are conserved."
    ),
    
    # Available Energy
    nbf.v4.new_markdown_cell(
        "## Available Energy vs. Total Energy\n"
        "> \"Although we know for a fact that energy is conserved, the energy available for human utility is not conserved so easily.\"\n\n"
        "- The ocean has enormous heat energy (random atomic motion).\n"
        "- But we cannot *extract* it without putting in more energy elsewhere.\n"
        "- This leads to the concept of **entropy** and the Second Law of Thermodynamics."
    ),
    
    # Energy Sources
    nbf.v4.new_markdown_cell(
        "## Where Do We Get Energy?\n"
        "- **Sun:** Powers rain, wind, plants (which become coal/oil).\n"
        "- **Uranium:** Nuclear fission.\n"
        "- **Hydrogen:** Nuclear fusion (controlled fusion is the dream).\n\n"
        "Feynman's challenge:\n"
        "> \"With 150 gallons of running water a minute, you have enough fuel to supply all the energy used in the United States today! Therefore it is up to the physicist to figure out how to liberate us from the need for having energy. It can be done.\""
    ),
    
    # Reflection
    nbf.v4.new_markdown_cell(
        "### 🧠 Reflection\n"
        "Feynman admits:\n"
        "> \"In the last analysis, we do not understand the conservation laws deeply. We do not understand the conservation of energy.\"\n\n"
        "Energy is not little blobs. It is a mathematical abstraction that always adds up to the same number.\n\n"
        "**Question:** If energy is just a number, not a 'thing,' why is it so powerful? What does conservation of energy allow us to predict that we otherwise could not?\n\n"
        "> [Your answer here...]"
    )
]

create_notebook("Section_4-4_Other_forms_of_energy.ipynb", cells)
