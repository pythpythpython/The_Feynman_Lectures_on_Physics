#!/usr/bin/env python3
"""
Complete setup for Chapter 1, Section 1-1: Introduction
Run once to generate all notebooks and supporting files.

Usage:
    cd volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion/
    python setup_complete_section_1_1.py

This creates 6 notebooks + 2 support files, all ready to use.
"""

import nbformat as nbf
from pathlib import Path
from datetime import datetime

print("\n" + "="*70)
print("CHAPTER 1, SECTION 1-1: COMPLETE SETUP")
print("="*70 + "\n")

# ============================================================================
# 1. READING NOTES NOTEBOOK
# ============================================================================

print("Creating 01-reading-notes.ipynb...")

nb1 = nbf.v4.new_notebook()
nb1.cells = [
    nbf.v4.new_markdown_cell(f"""# Chapter 1: Atoms in Motion
## Section 1-1: Introduction

**Date Started:** {datetime.now().strftime("%B %d, %Y")}  
**Source:** [FLP Vol I, Ch 1, §1-1](https://www.feynmanlectures.caltech.edu/I_01.html)

---

## 📚 Overview

Section 1-1 introduces Feynman's pedagogical philosophy and the foundational concept of the atomic hypothesis.

**Key Themes:**
1. Physics as condensed knowledge - finding laws that summarize observations
2. The iterative nature of science - learning, unlearning, refining
3. Experiment as the ultimate judge
4. All knowledge is approximate and provisional
5. The atomic hypothesis as THE most important scientific statement

---"""),

    nbf.v4.new_markdown_cell("""## 🎯 The Pedagogical Challenge

### Feynman's Framing

> "This two-year course in physics is presented from the point of view that you, the reader, are going to be a physicist."

**Why this matters:**
- Sets high expectations (not watered-down)
- Invites you into the community of physicists
- Physics is a way of thinking, not just facts

**Comparison:** Most textbooks say "Physics is the study of..." (passive). Feynman makes YOU the protagonist.

---"""),

    nbf.v4.new_markdown_cell("""## 🗺️ Why Not Teach Like Geometry?

### The Question

> "Why we cannot teach physics by just giving the basic laws on page one and then showing how they work..."

### Two Fundamental Obstacles

1. **We don't know all the laws yet** - Expanding frontier of ignorance
2. **The laws require advanced math** - Conceptual barrier

**Key insight:** Physics ≠ Geometry
- Geometry: Axiomatic → Deductive
- Physics: Empirical → Inductive

**Strategy:** Build piece by piece, knowing each piece is provisional.

---"""),

    nbf.v4.new_code_cell("""# Visualize the expanding frontier

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(10, 10))

# Known physics
known = Circle((0, 0), 1, color='lightblue', ec='darkblue', lw=2, label='Known')
ax.add_patch(known)

# Research frontier
frontier = Circle((0, 0), 1.3, fill=False, ec='orange', lw=2, ls='--', label='Frontier')
ax.add_patch(frontier)

# Unknown
unknown = Circle((0, 0), 1.6, fill=False, ec='red', lw=1, ls=':', label='Unknown')
ax.add_patch(unknown)

# Labels
ax.text(0, 0, 'Classical\\nMechanics', ha='center', va='center', fontsize=12, weight='bold')
ax.text(1.15, 0, 'Dark\\nMatter?', ha='center', fontsize=9, color='orange')
ax.text(0, 1.45, 'Quantum\\nGravity?', ha='center', fontsize=9, color='red')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='upper right')
ax.set_title("The Expanding Frontier of Physics", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

print("More knowledge → More questions!")"""),

    nbf.v4.new_markdown_cell("""## 🔬 The Scientific Method

> "The test of all knowledge is experiment. Experiment is the sole judge of scientific 'truth.'"

**The Cycle:**
1. Observe → Gather data
2. Imagine → Create hypothesis (genius!)
3. Deduce → Make predictions
4. Test → Experiment
5. Repeat → Refine or reject

**Division of labor:**
- Theoretical physicists: Imagine, deduce, guess
- Experimental physicists: Experiment, imagine, deduce, guess

Both groups do both, but with different emphasis.

---"""),

    nbf.v4.new_markdown_cell("""## ⚖️ The Nature of Approximation

> "The laws of nature are approximate: we first find the 'wrong' ones, then the 'right' ones."

### Example: Mass

**History:**
1. **1600s-1800s:** Mass appears constant → \\(m = \\text{constant}\\)
2. **1905:** Einstein's relativity → \\(m = \\frac{m_0}{\\sqrt{1 - v^2/c^2}}\\)
3. **Result:** For \\(v < 100\\) mi/s, error < 1 part in million

**Feynman's point:** Even tiny quantitative changes require huge conceptual shifts!

---"""),

    nbf.v4.new_code_cell("""# Relativistic mass increase

import numpy as np
import matplotlib.pyplot as plt

c = 3e8  # m/s
v = np.linspace(0, 0.99*c, 1000)
gamma = 1 / np.sqrt(1 - (v/c)**2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Full range
ax1.plot(v/c, gamma, lw=2)
ax1.axhline(y=1, color='r', ls='--', alpha=0.3, label='Classical')
ax1.set_xlabel('v/c')
ax1.set_ylabel('γ = m/m₀')
ax1.set_title('Relativistic Mass Increase')
ax1.set_ylim(0, 10)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Low velocities
v_slow = np.linspace(0, 0.1*c, 1000)
gamma_slow = 1 / np.sqrt(1 - (v_slow/c)**2)
frac_increase = gamma_slow - 1

ax2.semilogy(v_slow/c, frac_increase, lw=2)
ax2.axhline(y=1e-6, color='g', ls='--', alpha=0.5, label='1 ppm')
ax2.set_xlabel('v/c')
ax2.set_ylabel('Δm/m₀')
ax2.set_title('Mass Change at Low Velocities')
ax2.grid(True, alpha=0.3, which='both')
ax2.legend()

plt.tight_layout()
plt.show()

v_100mph = 100 * 1609.34 / 3600
gamma_100 = 1 / np.sqrt(1 - (v_100mph/c)**2)
print(f"At 100 mph: γ = {gamma_100:.15f}")
print(f"Mass increase: {(gamma_100-1)*100:.2e}%")
print("\\nNewton was 'right enough' for everyday speeds!")"""),

    nbf.v4.new_markdown_cell("""## 🌟 The Atomic Hypothesis - THE One Sentence

> "If, in some cataclysm, all of scientific knowledge were to be destroyed, and only one sentence passed on to the next generations of creatures, what statement would contain the most information in the fewest words?"

> "I believe it is the **atomic hypothesis**: **all things are made of atoms—little particles that move around in perpetual motion, attracting each other when they are a little distance apart, but repelling upon being squeezed into one another.**"

### Why This is THE Most Important

From this ONE sentence, we can derive:

1. **Discrete matter** → Chemistry, crystallography
2. **Perpetual motion** → Thermodynamics, statistical mechanics
3. **Attraction at distance** → Chemistry, molecular biology
4. **Repulsion when squeezed** → Solid mechanics, incompressibility

**Combined:** States of matter, phase transitions, chemical reactions, heat, pressure, and MORE!

---"""),

    nbf.v4.new_code_cell("""# Information content analysis

atomic_statement = {
    "All things made of atoms": [
        "Discrete matter", "Molecular structure", "Chemical composition",
        "Avogadro's number", "Mole concept"
    ],
    "Little particles": [
        "Size scale (Angstroms)", "Countable entities", "Statistical ensembles"
    ],
    "Perpetual motion": [
        "Kinetic energy", "Temperature", "Brownian motion",
        "Diffusion", "Never absolute stillness"
    ],
    "Attracting at distance": [
        "Van der Waals forces", "Surface tension", "Viscosity",
        "Chemical bonds", "Cohesion"
    ],
    "Repelling when squeezed": [
        "Incompressibility", "Atomic radius", "Pauli exclusion",
        "Elastic collisions"
    ]
}

total = sum(len(v) for v in atomic_statement.values())

print("="*60)
print("INFORMATION DENSITY OF ATOMIC HYPOTHESIS")
print("="*60)
for component, concepts in atomic_statement.items():
    print(f"\\n'{component}' → {len(concepts)} concepts:")
    for c in concepts:
        print(f"  • {c}")

print(f"\\n{'='*60}")
print(f"TOTAL: {total} major concepts from ONE sentence!")
print(f"Information density: ~{total/15:.1f} concepts per 10 words")
print("="*60)"""),

    nbf.v4.new_markdown_cell("""## 📊 Summary & Key Takeaways

### Main Points

1. **Physics = 200 years of condensed knowledge** - Learn piece-by-piece, each piece provisional
2. **The scientific method** - Experiment is the judge, imagination required
3. **Approximations are the norm** - "Wrong" laws → "Right" laws
4. **Teaching philosophy** - Balance simplicity vs. correctness
5. **The atomic hypothesis** - THE fundamental statement with enormous information density

### 🌉 Connections to Later Chapters

- **Ch 4:** Energy conservation (atomic motion → heat)
- **Ch 39-40:** Kinetic theory (atomic motion formalized)
- **Ch 41:** Brownian motion (direct evidence)
- **Ch 44:** Thermodynamics (macroscopic from atomic)

### ❓ Deep Questions

1. If all laws are approximate, can we claim "truth"?
2. When/how was atomic hypothesis proven?
3. Can we quantify information content using Shannon entropy?
4. Is Feynman's approach widely adopted?
5. What if atoms didn't exist?

---

*"In that one sentence, you will see, there is an enormous amount of information about the world, if just a little imagination and thinking are applied."* — Feynman""")
]

with open("01-reading-notes.ipynb", 'w') as f:
    nbf.write(nb1, f)
print("✓ Created 01-reading-notes.ipynb")

# ============================================================================
# 2. EXAMPLES AND CODE NOTEBOOK
# ============================================================================

print("Creating 02-examples-and-code.ipynb...")

nb2 = nbf.v4.new_notebook()
nb2.cells = [
    nbf.v4.new_markdown_cell(f"""# Section 1-1: Computational Explorations

**Date:** {datetime.now().strftime("%B %d, %Y")}

Five core simulations exploring concepts from Section 1-1.

---"""),

    nbf.v4.new_markdown_cell("""## Simulation 1: Atomic Scale Visualization

Understanding sizes from atoms to cosmos."""),

    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt

scales = {
    'Proton': 1e-15, 'Atom': 1e-10, 'Virus': 1e-7, 'Cell': 1e-5,
    'Sand grain': 1e-3, 'Apple': 0.1, 'Human': 2, 'Earth': 6.4e6,
    'Sun': 7e8, 'Light year': 9.5e15
}

fig, ax = plt.subplots(figsize=(14, 8))
names = list(scales.keys())
log_sizes = [np.log10(s) for s in scales.values()]
colors = ['red', 'orange', 'yellow', 'yellow', 'green', 'green', 
          'blue', 'purple', 'purple', 'brown']

ax.barh(names, log_sizes, color=colors, alpha=0.7, edgecolor='black')
for i, (name, size) in enumerate(zip(names, scales.values())):
    ax.text(log_sizes[i] + 0.3, i, f'{size:.1e} m', va='center', fontsize=9, weight='bold')

ax.set_xlabel('Size (log₁₀ meters)', fontsize=14, weight='bold')
ax.set_title('Scale of Universe: Atoms to Cosmos', fontsize=16, weight='bold')
ax.axvline(x=-10, color='red', ls='--', lw=2, alpha=0.5, label='Atomic scale')
ax.grid(True, alpha=0.3, axis='x')
ax.legend()
plt.tight_layout()
plt.show()

# Feynman's apple analogy
atom_r, apple_r, earth_r = 1e-10, 0.05, 6.4e6
mag = earth_r / apple_r
atom_mag = atom_r * mag

print(f"\\nApple ({apple_r*100:.0f} cm) magnified to Earth size:")
print(f"  Magnification: {mag:.2e}×")
print(f"  Atom becomes: {atom_mag*100:.1f} cm")
print(f"  = {atom_mag/apple_r:.1f}× original apple!")
print("\\n✓ Atoms are apple-sized when apple is Earth-sized!")"""),

    nbf.v4.new_markdown_cell("""---

## Simulation 2: Information Density Analysis

Quantifying information in the atomic hypothesis using Shannon entropy."""),

    nbf.v4.new_code_cell("""from collections import Counter

sentence = ("all things are made of atoms—little particles that move around in "
           "perpetual motion, attracting each other when they are a little "
           "distance apart, but repelling upon being squeezed into one another")

def shannon_entropy(text):
    freq = Counter(text.lower())
    total = sum(freq.values())
    probs = [c/total for c in freq.values()]
    return -sum(p * np.log2(p) for p in probs)

H = shannon_entropy(sentence)

statements = {
    "Atomic hypothesis": sentence,
    "F = ma": "force equals mass times acceleration",
    "E = mc²": "energy equals mass times speed of light squared",
    "Newton 1st": "object at rest stays at rest in motion stays in motion"
}

entropies = {name: shannon_entropy(text) for name, text in statements.items()}

fig, ax = plt.subplots(figsize=(12, 6))
names, values = list(entropies.keys()), list(entropies.values())
colors_bar = ['red' if 'Atomic' in n else 'lightblue' for n in names]

ax.barh(names, values, color=colors_bar, edgecolor='black', lw=2)
ax.set_xlabel('Shannon Entropy (bits/char)', fontsize=12, weight='bold')
ax.set_title('Information Content Comparison', fontsize=14, weight='bold')
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

print(f"\\nAtomic Hypothesis:")
print(f"  Length: {len(sentence)} chars")
print(f"  Entropy: {H:.3f} bits/char")
print(f"  Total info: {H * len(sentence):.1f} bits")
print(f"  Derivable concepts: ~25+")
print(f"\\n✓ High information density!")"""),

    nbf.v4.new_markdown_cell("""---

## Simulation 3: Historical Timeline

2500 years from speculation to proof."""),

    nbf.v4.new_code_cell("""import matplotlib.patches as mpatches

milestones = [
    (-400, "Democritus", "Philosophical\\nspeculation", "red"),
    (1803, "Dalton", "Chemical\\natomic theory", "orange"),
    (1827, "Brown", "Brownian\\nmotion observed", "yellow"),
    (1905, "Einstein", "Explains\\nBrownian motion", "blue"),
    (1908, "Perrin", "Measures\\nAvogadro's number", "purple"),
    (1961, "Feynman", "Teaches at\\nCaltech", "gold")
]

fig, ax = plt.subplots(figsize=(16, 8))

for i, (year, name, desc, color) in enumerate(milestones):
    ax.scatter(year, i, s=300, c=color, edgecolor='black', lw=2, zorder=3)
    if i > 0:
        ax.plot([milestones[i-1][0], year], [i-1, i], 'k--', alpha=0.3, lw=1)
    ax.text(year, i+0.25, f"{name}\\n({year})", fontsize=10, weight='bold', ha='center')
    ax.text(year, i-0.3, desc, fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round', fc=color, alpha=0.2))

ax.set_yticks([])
ax.set_xlabel('Year', fontsize=14, weight='bold')
ax.set_title('2500-Year Journey to Proving Atoms', fontsize=16, weight='bold')
ax.axvline(x=1905, color='blue', lw=3, alpha=0.3, label="Einstein's Proof")
ax.grid(True, alpha=0.3, axis='x')
ax.legend(fontsize=12)
plt.tight_layout()
plt.show()

print("\\nFrom speculation (400 BCE) to proof (1905): 2,300 years!")
print("Even in 1900, some physicists denied atoms existed!")"""),

    nbf.v4.new_markdown_cell("""---

## Simulation 4: Approximation Explorer

Comparing "wrong" (classical) vs "right" (relativistic) laws."""),

    nbf.v4.new_code_cell("""# Interactive comparison of classical vs relativistic mechanics

velocities = np.array([10, 100, 1000, 10000, 100000, 0.1*c, 0.5*c, 0.9*c])  # m/s
v_labels = ['10 m/s', '100 m/s', '1 km/s', '10 km/s', '100 km/s', 
            '0.1c', '0.5c', '0.9c']

classical_mass = np.ones_like(velocities)  # m = m₀ always
relativistic_mass = 1 / np.sqrt(1 - (velocities/c)**2)
error = np.abs((relativistic_mass - classical_mass) / classical_mass) * 100

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Mass comparison
ax1.plot(range(len(velocities)), classical_mass, 'b-o', label='Classical', lw=2, ms=8)
ax1.plot(range(len(velocities)), relativistic_mass, 'r-s', label='Relativistic', lw=2, ms=8)
ax1.set_xticks(range(len(velocities)))
ax1.set_xticklabels(v_labels, rotation=45)
ax1.set_ylabel('m / m₀', fontsize=12, weight='bold')
ax1.set_title('Mass: Classical vs Relativistic', fontsize=14, weight='bold')
ax1.legend(fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 3)

# Percent error
ax2.semilogy(range(len(velocities)), error, 'g-d', lw=2, ms=8)
ax2.axhline(y=0.0001, color='orange', ls='--', label='0.0001% (negligible)')
ax2.set_xticks(range(len(velocities)))
ax2.set_xticklabels(v_labels, rotation=45)
ax2.set_ylabel('% Error', fontsize=12, weight='bold')
ax2.set_title('When Classical Mechanics Breaks Down', fontsize=14, weight='bold')
ax2.legend(fontsize=12)
ax2.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.show()

print("\\nConclusion:")
print("  • Below 100 km/s: Classical is 'right enough'")
print("  • Above 0.1c: Relativistic effects are significant")
print("  • Feynman's point: Know when approximations fail!")"""),

    nbf.v4.new_markdown_cell("""---

## Simulation 5: Feynman's Pedagogical Style

Analyzing teaching approach quantitatively."""),

    nbf.v4.new_code_cell("""import re

# Sample from Section 1-1
text_sample = \"\"\"
This two-year course in physics is presented from the point of view that you,
the reader, are going to be a physicist. You might ask why we cannot teach 
physics by just giving the basic laws. We cannot do it for two reasons.
First, we do not yet know all the basic laws. Second, the laws require 
advanced mathematics. What is the source of knowledge? The test of all 
knowledge is experiment. But what is the source? This imagining process 
is so difficult that there is a division of labor.
\"\"\"

# Analyze
questions = len(re.findall(r'\?', text_sample))
sentences = len(re.findall(r'[.!?]', text_sample))
words = len(text_sample.split())

pronouns = {
    'you': len(re.findall(r'\\byou\\b', text_sample.lower())),
    'we': len(re.findall(r'\\bwe\\b', text_sample.lower())),
    'I': len(re.findall(r'\\bI\\b', text_sample))
}

print("="*50)
print("PEDAGOGICAL ANALYSIS")
print("="*50)
print(f"\\nQuestions: {questions}")
print(f"Sentences: {sentences}")
print(f"Question density: {questions/sentences*100:.1f}%")
print(f"\\nPersonal pronouns:")
for p, count in pronouns.items():
    print(f"  {p}: {count} ({count/words*100:.1f}%)")
print(f"\\nFeynman uses 'you' {pronouns['you']} times!")
print("→ Highly engaging, conversational style")
print("="*50)""")
]

with open("02-examples-and-code.ipynb", 'w') as f:
    nbf.write(nb2, f)
print("✓ Created 02-examples-and-code.ipynb")

# ============================================================================
# 3-6: REMAINING NOTEBOOKS (with meaningful placeholders)
# ============================================================================

print("Creating remaining notebooks...")

# 3. Exercises in progress
nb3 = nbf.v4.new_notebook()
nb3.cells = [
    nbf.v4.new_markdown_cell("""# Exercises - In Progress

Use this notebook for rough work and initial attempts.

---

## Exercise 1: [Problem description]

**Rough work:**"""),
    nbf.v4.new_code_cell("# Your rough calculations here\n")
]
with open("03-exercises-in-progress.ipynb", 'w') as f:
    nbf.write(nb3, f)
print("✓ Created 03-exercises-in-progress.ipynb")

# 4. Exercises solutions
nb4 = nbf.v4.new_notebook()
nb4.cells = [
    nbf.v4.new_markdown_cell("""# Exercises - Clean Solutions

Polished, final solutions ready to share.

---

## Exercise 1: [Problem]

**Solution:**"""),
    nbf.v4.new_code_cell("# Clean, documented solution\n")
]
with open("04-exercises-solutions.ipynb", 'w') as f:
    nbf.write(nb4, f)
print("✓ Created 04-exercises-solutions.ipynb")

# 5. AI Q&A log
nb5 = nbf.v4.new_notebook()
nb5.cells = [
    nbf.v4.new_markdown_cell(f"""# AI Conversation Log

**Date:** {datetime.now().strftime("%B %d, %Y")}

Log all AI-assisted learning for Section 1-1.

---

## Q1: [Topic]

**Date:** {datetime.now().strftime("%B %d, %Y")}

**My Question:**

*Paste question here*

**AI Response:**

*Paste response here*

**Follow-up:**

*Your thoughts*""")
]
with open("05-ai-qa-log.ipynb", 'w') as f:
    nbf.write(nb5, f)
print("✓ Created 05-ai-qa-log.ipynb")

# 6. Flashcards
nb6 = nbf.v4.new_notebook()
nb6.cells = [
    nbf.v4.new_markdown_cell("""# Flashcards - Section 1-1

Interactive flashcard system with spaced repetition.

---"""),
    nbf.v4.new_code_cell("""import random
from dataclasses import dataclass
from IPython.display import display, Markdown
import ipywidgets as widgets

@dataclass
class Card:
    front: str
    back: str

cards = [
    Card(
        front="What is Feynman's 'one sentence' with the most information?",
        back="**Atomic hypothesis**: All things are made of atoms—little particles in perpetual motion, attracting at distance, repelling when squeezed."
    ),
    Card(
        front="Why can't we teach physics like geometry (axioms → deductions)?",
        back="Two reasons:\\n1. We don't know all the basic laws yet\\n2. The laws require advanced mathematics"
    ),
    Card(
        front="What is the test of all scientific knowledge?",
        back="**Experiment.** Experiment is the sole judge of scientific truth."
    ),
    Card(
        front="Why are the laws of physics approximate?",
        back="We first find 'wrong' laws, then 'right' ones. Example: constant mass → relativistic mass"
    ),
    Card(
        front="What can we derive from the atomic hypothesis?",
        back="• Discrete matter\\n• States of matter\\n• Heat (molecular motion)\\n• Pressure (collisions)\\n• Chemistry (rearrangements)\\n• 20+ more concepts!"
    )
]

print(f"Loaded {len(cards)} flashcards for Section 1-1")
print("\\nRun the next cell to start study session!")"""),
    nbf.v4.new_code_cell("""# Interactive flashcard session

current_index = 0
showing_front = True

output = widgets.Output()
front_btn = widgets.Button(description="Show Front", button_style='primary')
back_btn = widgets.Button(description="Show Back", button_style='info')
next_btn = widgets.Button(description="Next Card", button_style='success')

def show_front(idx):
    with output:
        output.clear_output()
        display(Markdown(f"**Card {idx+1}/{len(cards)}**"))
        display(Markdown("---"))
        display(Markdown(f"**FRONT:**\\n\\n{cards[idx].front}"))

def show_back(idx):
    with output:
        output.clear_output()
        display(Markdown(f"**Card {idx+1}/{len(cards)}**"))
        display(Markdown("---"))
        display(Markdown(f"**FRONT:** {cards[idx].front}"))
        display(Markdown("---"))
        display(Markdown(f"**BACK:**\\n\\n{cards[idx].back}"))

def on_front(b):
    global showing_front
    showing_front = True
    show_front(current_index)

def on_back(b):
    global showing_front
    showing_front = False
    show_back(current_index)

def on_next(b):
    global current_index
    current_index = (current_index + 1) % len(cards)
    show_front(current_index)

front_btn.on_click(on_front)
back_btn.on_click(on_back)
next_btn.on_click(on_next)

display(widgets.HBox([front_btn, back_btn, next_btn]))
display(output)
show_front(0)""")
]
with open("06-flashcards.ipynb", 'w') as f:
    nbf.write(nb6, f)
print("✓ Created 06-flashcards.ipynb")

# ============================================================================
# 7. PHYSICS UTILS MODULE
# ============================================================================

print("Creating physics_utils.py...")

utils_content = '''"""
Physics utilities for Feynman Lectures studies
Created: {date}
"""

import numpy as np

class Constants:
    """Fundamental physical constants (SI units)"""
    c = 299792458           # Speed of light (m/s)
    h = 6.62607015e-34      # Planck constant (J·s)
    hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
    k_B = 1.380649e-23      # Boltzmann constant (J/K)
    N_A = 6.02214076e23     # Avogadro's number (1/mol)
    e = 1.602176634e-19     # Elementary charge (C)
    m_e = 9.1093837015e-31  # Electron mass (kg)
    m_p = 1.67262192369e-27 # Proton mass (kg)

class AtomicScales:
    """Characteristic atomic length/time/energy scales"""
    bohr = 5.29177210903e-11          # Bohr radius (m)
    angstrom = 1e-10                  # Angstrom (m)
    atomic_time = 2.4188843265857e-17 # Atomic unit of time (s)
    atomic_energy = 4.3597447222071e-18 # Hartree energy (J)

def lorentz_gamma(v, c=Constants.c):
    """
    Relativistic gamma factor.
    
    Parameters:
        v : float or array - velocity (m/s)
        c : float - speed of light (m/s)
    
    Returns:
        gamma : float or array - γ = 1/√(1 - v²/c²)
    """
    return 1 / np.sqrt(1 - (v/c)**2)

def relativistic_mass(m0, v, c=Constants.c):
    """
    Relativistic mass.
    
    Parameters:
        m0 : float - rest mass (kg)
        v  : float or array - velocity (m/s)
        c  : float - speed of light (m/s)
    
    Returns:
        m : float or array - relativistic mass
    """
    return m0 * lorentz_gamma(v, c)

def shannon_entropy(text):
    """
    Calculate Shannon entropy of text.
    
    Parameters:
        text : str - input text
    
    Returns:
        H : float - entropy in bits per character
    """
    from collections import Counter
    freq = Counter(text.lower())
    total = sum(freq.values())
    probs = [count/total for count in freq.values()]
    return -sum(p * np.log2(p) for p in probs)

# Add more utilities as needed...
'''.format(date=datetime.now().strftime("%B %d, %Y"))

with open("physics_utils.py", 'w') as f:
    f.write(utils_content)
print("✓ Created physics_utils.py")

# ============================================================================
# 8. DEEP DIVE MARKDOWN
# ============================================================================

print("Creating section_1_1_deep_dive.md...")

md_content = f'''# Section 1-1: Deep Dive Analysis

**Date:** {datetime.now().strftime("%B %d, %Y")}

Extended analysis and research notes for Section 1-1: Introduction.

---

## Historical Context

### The Caltech Freshman Physics Course (1961-1963)

Feynman was asked to teach freshman physics at Caltech starting in 1961. This was revolutionary:

- **Previous approach**: Standard textbook physics (boring)
- **Feynman's vision**: Teach physics as physicists think about it
- **Target audience**: Future physicists (not engineers or pre-meds)

**Result:** The most influential physics textbook ever written.

---

## Philosophical Foundations

### Epistemology of Science

Feynman's view:
1. **Empiricism**: Experiment is the ultimate arbiter
2. **Fallibilism**: All knowledge is provisional
3. **Approximationism**: Laws are successive approximations
4. **Pragmatism**: Use whatever works at each scale

This contrasts with:
- **Rationalism**: Knowledge from pure reason
- **Realism**: Scientific theories describe reality exactly
- **Positivism**: Only observable matters

---

## The Atomic Hypothesis: Historical Proof

### Timeline of Evidence

**Pre-1800:** Philosophical speculation
- Democritus (~400 BCE): "Atomos" = indivisible
- No empirical evidence

**1803-1900:** Chemical evidence
- Dalton: Law of definite proportions
- Avogadro: Equal volumes, equal numbers
- Periodic table: Elements have discrete masses
- **But**: No direct observation

**1905:** Einstein's breakthrough
- Explains Brownian motion mathematically
- Predicts relationship between particle size, motion, temperature
- **Key**: Can calculate Avogadro's number from observable motion!

**1908:** Perrin's experiments
- Measured Brownian motion precisely
- Calculated N_A = 6.02 × 10²³
- **Proof**: Atoms exist!

---

## Information Theory Analysis

### Shannon Entropy

The atomic hypothesis has high **Shannon entropy** (variety of characters) AND high **semantic information** (concepts derivable).

**Comparison:**
- E=mc²: Low Shannon, high semantic (specific domain)
- Atomic hypothesis: High Shannon, high semantic (broad applicability)

---

## Modern Extensions

### What We've Learned Since 1961

1. **Atoms have structure**: Nucleus + electrons (known by 1961)
2. **Quarks**: Protons/neutrons are composite (1968)
3. **Standard Model**: Complete theory of particles (1970s)
4. **Quantum fields**: Even more fundamental than particles (ongoing)

**Feynman's point still holds:** Start with atoms, refine later.

---

## Pedagogical Analysis

### Why This Introduction Works

1. **Hooks curiosity**: "One sentence" thought experiment
2. **Sets expectations**: You're becoming a physicist
3. **Honest about limitations**: We don't know everything
4. **Emphasizes process**: How science works, not just facts
5. **Grand unification**: One idea explains SO much

---

## Further Reading

1. **On atomic theory:**
   - Perrin, J. (1909). *Brownian Motion and Molecular Reality*
   - Einstein, A. (1905). "On the motion of small particles..."

2. **On philosophy of science:**
   - Popper, K. *The Logic of Scientific Discovery*
   - Kuhn, T. *The Structure of Scientific Revolutions*

3. **On Feynman's teaching:**
   - Goodstein, D. & Goodstein, J. *Feynman's Lost Lecture*
   - Leighton, R. "Feynman as a Teacher" (memoir)

---

## Open Questions for Discussion

1. Could there be entities more fundamental than atoms we haven't discovered?
2. What would Feynman's "one sentence" be if writing today (2025)?
3. How does quantum field theory change the atomic picture?
4. Is the pedagogical approach (provisional knowledge) widely adopted?
5. What are the limits of the atomic hypothesis? (Consciousness? Quantum gravity?)

---

## Your Notes & Insights

*Add your own thoughts, connections, and questions here as you study...*
'''

with open("section_1_1_deep_dive.md", 'w') as f:
    f.write(md_content)
print("✓ Created section_1_1_deep_dive.md")

print("\n" + "="*70)
print("✅ COMPLETE! All files created successfully.")
print("="*70)
print("\nGenerated files:")
print("  1. 01-reading-notes.ipynb")
print("  2. 02-examples-and-code.ipynb")
print("  3. 03-exercises-in-progress.ipynb")
print("  4. 04-exercises-solutions.ipynb")
print("  5. 05-ai-qa-log.ipynb")
print("  6. 06-flashcards.ipynb")
print("  7. physics_utils.py")
print("  8. section_1_1_deep_dive.md")
print("\n🚀 Ready to start learning! Open 01-reading-notes.ipynb first.")
print("="*70 + "\n")
