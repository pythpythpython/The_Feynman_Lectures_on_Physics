#!/usr/bin/env python3
"""
GENERATE COMPREHENSIVE PROJECT LOG
Creates 'Log_AI_QA_Journal.ipynb' containing the full history of the AI work
and the migrated physics deep dives.
"""

import nbformat as nbf
import os

# Set Target Directory
try:
    target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
    os.chdir(target_dir)
except FileNotFoundError:
    pass 

print(f"\n📓 Generating Comprehensive Project Log in: {os.getcwd()}")

# 1. Try to read the existing deep dive file to preserve it
deep_dive_content = ""
deep_dive_file = "section_1_1_deep_dive.md"
if os.path.exists(deep_dive_file):
    with open(deep_dive_file, 'r') as f:
        deep_dive_content = f.read()

# 2. Create the Notebook
nb = nbf.v4.new_notebook()
cells = []

# --- SECTION 1: HEADER ---
cells.append(nbf.v4.new_markdown_cell(
    "# 📓 AI Project Log & QA Journal: Chapter 1\n"
    "## A History of the Build & The Physics\n\n"
    "This notebook serves two purposes:\n"
    "1.  **Project Log:** Documenting how we built this computational learning environment using AI.\n"
    "2.  **Learning Journal:** Deep dives into the physics concepts encountered along the way."
))

# --- SECTION 2: THE AI WORK LOG (Project History) ---
cells.append(nbf.v4.new_markdown_cell(
    "## 🛠️ Project Build History\n"
    "A summary of the structural changes and AI generation tasks performed to create this chapter environment.\n\n"
    "### 🔹 Phase 1: Foundation (Section 1-1)\n"
    "- **Goal:** Establish the core concept (\"The Atomic Hypothesis\").\n"
    "- **Actions:**\n"
    "  - Created `Section_1-1_Introduction.ipynb`: Detailed breakdown of Feynman's \"One Sentence.\"\n"
    "  - Generated `section_1_1_deep_dive.md`: An external analysis of the hypothesis (now migrated below).\n\n"
    "### 🔹 Phase 2: Expansion (Sections 1-2 to 1-4)\n"
    "- **Goal:** Cover the full breadth of the chapter content.\n"
    "- **Actions:**\n"
    "  - Generated `Section_1-2_Matter_is_Made_of_Atoms.ipynb`: Notes on solids, liquids, gases, and lattice structures.\n"
    "  - Generated `Section_1-3_Atomic_Processes.ipynb`: Notes on evaporation, cooling, and pressure.\n"
    "  - Generated `Section_1-4_Chemical_Reactions.ipynb`: Notes on burning, biology, and molecular partners.\n\n"
    "### 🔹 Phase 3: The \"Laboratory\" (Activities)\n"
    "- **Goal:** Make the physics interactive.\n"
    "- **Actions:**\n"
    "  - Created `Activity_Interactive_Playground.ipynb` (formerly `02-examples-and-code`): Python simulations for Brownian motion and temperature kinetics.\n"
    "  - Created `Activity_Flashcards.ipynb` (formerly `06-flashcards`): An `ipywidgets`-based active recall deck.\n\n"
    "### 🔹 Phase 4: Restructuring & Optimization\n"
    "- **Goal:** Clean up the file system for clarity and ease of use.\n"
    "- **Actions:**\n"
    "  - **Renaming:** Converted numbered files (e.g., `04-reading-notes`) to descriptive names (e.g., `Section_1-4_Chemical_Reactions`).\n"
    "  - **Consolidation:** Deleted scattered exercise files (`03-exercises-in-progress`, `04-solutions`) and merged them into a single `Activity_Exercise_Bank.ipynb` with toggleable solutions.\n"
    "  - **Dashboarding:** Created `Overview_Master_Dashboard.ipynb` as the central navigation hub."
))

# --- SECTION 3: PHYSICS DEEP DIVES (Subject Matter) ---
cells.append(nbf.v4.new_markdown_cell("## 🧠 Physics Deep Dives\n"
                                      "Detailed explorations of specific topics generated during our sessions."))

# Insert the Deep Dive Content from Section 1-1
if deep_dive_content:
    cells.append(nbf.v4.new_markdown_cell(
        "### 🔍 Deep Dive: The Atomic Hypothesis (Section 1-1)\n"
        "*(Original content migrated from `section_1_1_deep_dive.md`)*\n\n"
        f"{deep_dive_content}"
    ))
else:
    # Fallback if file wasn't found (or already deleted)
    cells.append(nbf.v4.new_markdown_cell(
        "### 🔍 Deep Dive: The Atomic Hypothesis (Section 1-1)\n"
        "**The Feynman Sentence:**\n"
        "> *\"All things are made of atoms—little particles that move around in perpetual motion, attracting each other when they are a little distance apart, but repelling upon being squeezed into one another.\"*\n\n"
        "**Why this matters:**\n"
        "Feynman argues this single statement contains the most information in the fewest words. It implies:\n"
        "1.  **Structure:** Matter is granular, not continuous.\n"
        "2.  **Dynamics:** Nothing is static; heat is motion.\n"
        "3.  **Interaction:** The force law (Attract far, Repel close) explains everything from elasticity to chemical bonding."
    ))

# Standard Q&A Examples
cells.append(nbf.v4.new_markdown_cell(
    "### 🌡️ Concept: The Mechanics of Evaporation (Section 1-3)\n"
    "**Question:** Why does blowing on hot soup cool it down?\n\n"
    "**AI Explanation:**\n"
    "1.  **Temperature = Average Energy:** In the soup, molecules have a distribution of speeds. Some are fast, some are slow.\n"
    "2.  **Escape:** Only the very fastest molecules have enough energy to break the surface tension and escape into the air.\n"
    "3.  **Selection Bias:** When the fastest ones leave, the average energy of the *remaining* molecules drops. Thus, the liquid cools.\n"
    "4.  **The Role of Blowing:** Normally, the escaping vapor hangs around the surface and some bounce back in. Blowing removes this vapor layer, preventing re-entry and maximizing the net loss of \"hot\" molecules."
))

cells.append(nbf.v4.new_markdown_cell(
    "### 🧊 Concept: Solid vs. Liquid Structure (Section 1-2)\n"
    "**Question:** If atoms in a solid are moving, why doesn't the solid fall apart?\n\n"
    "**AI Explanation:**\n"
    "They *are* moving (vibrating), but they are trapped in a \"potential well.\" Imagine a dog on a short leash. It can run around (vibrate), but it can't leave the yard (lattice site). In a liquid, the leash is broken, but the yard is still crowded—the atoms slide past each other but stay close."
))

# --- SECTION 4: TEMPLATE ---
cells.append(nbf.v4.new_markdown_cell("---"))
cells.append(nbf.v4.new_markdown_cell("## 📝 New Entry Template\nUse this for future questions."))
cells.append(nbf.v4.new_code_cell(
    "# Date: 2025-MM-DD\n"
    "# Topic: [Topic Name]\n"
    "# Question: [Your Question]\n"
    "# Insight: [Summary of the answer]"
))

nb.cells = cells

# 3. Write the Notebook
with open("Log_AI_QA_Journal.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("✅ Created: Log_AI_QA_Journal.ipynb (Includes Full Project History)")

# 4. Cleanup
if os.path.exists(deep_dive_file):
    os.remove(deep_dive_file)
    print(f"🗑️  Cleanup: Deleted {deep_dive_file} (Migrated to Journal)")
