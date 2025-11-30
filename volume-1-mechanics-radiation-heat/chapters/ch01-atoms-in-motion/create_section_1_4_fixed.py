#!/usr/bin/env python3
"""
FIXED: Create COMPLETE reading notes for Section 1-4: Chemical Reactions and Evidence for Atoms
Fixes syntax error in Carbon Burning visualization code
"""

import nbformat as nbf
from datetime import datetime
import os

target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
os.chdir(target_dir)

print("\n🔨 Creating FIXED Section 1-4 Reading Notes...")
print(f"📁 Working directory: {os.getcwd()}\n")

nb = nbf.v4.new_notebook()

nb.cells = [
    nbf.v4.new_markdown_cell(f"""# Volume 1, Chapter 1 – Atoms in Motion
## Section 1-4: Chemical Reactions and Evidence for Atoms

**Date Started:** {datetime.now().strftime("%B %d, %Y")}  
**Source:** [FLP Vol I, Ch 1, §1-4](https://www.feynmanlectures.caltech.edu/I_01.html#Ch1-S4)

---

## 🌟 Overview

This final section of Chapter 1:

1. Introduces **chemical reactions** as atoms changing partners  
2. Shows how **molecular structure** explains smells (violets!)  
3. Presents **evidence for atoms** (Brownian motion, crystal shapes)  
4. States the boldest claim: **“Everything that animals do, atoms do.”**

This is the *culmination* of the atomic hypothesis: from burning carbon to human thought.

---"""),

    # CHEMICAL REACTIONS INTRO
    nbf.v4.new_markdown_cell("""## 🔥 Chemical Reactions: Atoms Changing Partners

### 📖 Feynman's Text

> "In all of the processes which have been described so far, the atoms and the ions have not changed partners, but of course there are circumstances in which the atoms do change combinations, forming new molecules."

> "A process in which the rearrangement of the atomic partners occurs is what we call a **chemical reaction**."

### 🔍 Physical vs Chemical Processes

- **Physical processes:**  
  - Evaporation, melting, dissolving  
  - Atoms keep same partners (same molecules/ions)
  - Only positions/energies change

- **Chemical reactions:**  
  - Atoms **change partners**  
  - New molecules form  
  - Example: C + O₂ → CO, CO₂

There is **no sharp line** between physical and chemical processes. Nature just keeps going; our labels are for our convenience.

---"""),

    # FIGURE 1-8: CARBON BURNING IN OXYGEN
    nbf.v4.new_markdown_cell("""## 🔥 Figure 1-8: Carbon Burning in Oxygen

### 📖 Feynman's Text

> "This figure is supposed to represent carbon burning in oxygen. In the case of oxygen, **two oxygen atoms stick together very strongly**."

> "At any rate, two oxygen atoms form, saturated and happy, a molecule."

> "The carbon atoms are supposed to be in a solid crystal (which could be graphite or diamond)."

### 🔍 Reaction Steps

1. **Reactants:**
   - Carbon in solid form (C, as graphite or diamond)
   - Molecular oxygen in gas form (O₂)

2. **Reaction 1: Formation of CO**
   - O₂ + C → 2 CO
   - Each O atom takes a C as a partner → CO (carbon monoxide)

3. **Reaction 2: Formation of CO₂**
   - CO + ½ O₂ → CO₂
   - Or overall: C + O₂ → CO₂

4. **Energy:**
   - Carbon–oxygen attraction stronger than:
     - Oxygen–oxygen
     - Carbon–carbon
   - New bonds → energy released as heat and light
   - This is **burning** (combustion)

**Key idea:** Burning = atoms rearranging into more stable combinations, releasing energy.

---"""),

    # CODE: REACTION DIAGRAM (FIXED STRING ESCAPING)
    nbf.v4.new_code_cell(r"""# Visualize carbon burning in oxygen: C + O2 -> CO, CO2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Helper to draw atom
def draw_atom(ax, x, y, radius, color, label):
    c = Circle((x, y), radius, color=color, ec='black', linewidth=1.5)
    ax.add_patch(c)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, weight='bold')

# Panel 1: Reactants (C + O2)
ax = axes[0]
ax.set_title('Reactants: C + O₂', fontsize=14, weight='bold')
# Carbon solid (3 C atoms)
for i, x in enumerate([1, 2, 1.5]):
    draw_atom(ax, x, 1+i*0.6, 0.25, 'gray', 'C')

# Oxygen molecule O2
draw_atom(ax, 4, 2.5, 0.25, 'red', 'O')
draw_atom(ax, 5, 2.5, 0.25, 'red', 'O')
ax.plot([4.25, 4.75], [2.5, 2.5], 'k-', linewidth=2)

# FIXED: Use raw string or explicit newline character
ax.text(3, 0.5, 'C (solid)\n+ O₂ (gas)', ha='center', fontsize=11)
ax.set_xlim(0, 6)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

# Arrow to products
axes[0].arrow(6.2, 2, 1.2, 0, head_width=0.2, head_length=0.3, 
              fc='black', ec='black', linewidth=2)

# Panel 2: Intermediate CO
ax = axes[1]
ax.set_title('Intermediate: CO', fontsize=14, weight='bold')
# CO molecules (2 or 3)
for i, y in enumerate([1.5, 2.5, 3.5]):
    # C
    draw_atom(ax, 2, y, 0.25, 'gray', 'C')
    # O
    draw_atom(ax, 3, y, 0.25, 'red', 'O')
    ax.plot([2.25, 2.75], [y, y], 'k-', linewidth=2)
ax.text(2.5, 0.5, 'CO (carbon monoxide)', ha='center', fontsize=11)
ax.set_xlim(0, 5)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

# Arrow to CO2
axes[1].arrow(5.2, 2, 1.2, 0, head_width=0.2, head_length=0.3, 
              fc='black', ec='black', linewidth=2)

# Panel 3: Final CO2
ax = axes[2]
ax.set_title('Final: CO₂', fontsize=14, weight='bold')
for i, y in enumerate([1.5, 2.7, 3.9]):
    # O
    draw_atom(ax, 1.5, y, 0.25, 'red', 'O')
    # C
    draw_atom(ax, 2.5, y, 0.25, 'gray', 'C')
    # O
    draw_atom(ax, 3.5, y, 0.25, 'red', 'O')
    ax.plot([1.75, 2.25], [y, y], 'k-', linewidth=2)
    ax.plot([2.75, 3.25], [y, y], 'k-', linewidth=2)
ax.text(2.5, 0.5, 'CO₂ (carbon dioxide)', ha='center', fontsize=11)
ax.set_xlim(0, 5)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

plt.suptitle('Figure 1-8: Carbon Burning in Oxygen', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\n" + "="*70)
print("CARBON BURNING SUMMARY")
print("="*70)
print("\nSteps:")
print("  1. C (solid) + O₂ (gas) -> CO (gas)   [partial oxidation]")
print("  2. CO + 1/2 O₂ -> CO₂ (gas)          [complete oxidation]")
print("\nEnergy:")
print("  - C-O bonds stronger than O-O or C-C")
print("  - Energy released as heat (molecular motion)")
print("  - Can be enough to produce light -> flames")
print("="*70)"""),

    # VIOLET SMELL MOLECULE
    nbf.v4.new_markdown_cell("""## 🌸 The Smell of Violets: Complex Molecules

### 📖 Feynman's Text

> "If we go into a field of small violets, we know what 'that smell' is. It is some kind of **molecule**, or arrangement of atoms, that has worked its way into our noses."

> "Now chemists can take special molecules like the odor of violets, and analyze them and tell us the **exact arrangement of the atoms in space**."

> "Figure 1–9 is a picture of the air in the neighborhood of a violet; again we find nitrogen and oxygen in the air, and water vapor. However, we also see a 'monster' composed of carbon atoms, hydrogen atoms, and oxygen atoms..."

### 🔍 Key Ideas

- The smell is a specific **molecule** (α‑irone).
- It diffuses randomly in the air (Brownian-like motion).
- It occasionally enters our nose by chance.
- Chemists have determined its:
  - Full 3D arrangement
  - Exact bond lengths and angles
- Chemical formulas are **2D pictures** of 3D realities.

**Example:**  
CO₂: O—C—O (linear, symmetric)  
α‑irone: large, ring + chain, many atoms

---"""),

    # CODE: SIMPLIFIED α-IRONE-LIKE DIAGRAM
    nbf.v4.new_code_cell("""# Sketch a simplified 'violet smell' molecule and surrounding air

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 8))

# Background: air molecules
np.random.seed(0)
for _ in range(40):
    x, y = np.random.rand(2)*10
    mol_type = np.random.choice(['N2', 'O2', 'H2O'])
    color = {'N2':'gray', 'O2':'red', 'H2O':'blue'}[mol_type]
    ax.add_patch(Circle((x, y), 0.12, color=color, alpha=0.4))

ax.text(1, 9.5, 'Air:\nN₂, O₂, H₂O', fontsize=11, weight='bold',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 'Monster' molecule (α-irone-like): ring + chain
# Ring (6 carbons)
ring_center = (6.5, 5)
R = 1.0
ring_coords = []
for k in range(6):
    angle = 2*np.pi*k/6
    ring_coords.append((ring_center[0] + R*np.cos(angle),
                        ring_center[1] + R*np.sin(angle)))

# Draw ring carbons
for (x, y) in ring_coords:
    ax.add_patch(Circle((x, y), 0.18, color='black', zorder=3))
    ax.text(x, y, 'C', ha='center', va='center', fontsize=9, color='white')

# Connect ring
for i in range(6):
    x1, y1 = ring_coords[i]
    x2, y2 = ring_coords[(i+1) % 6]
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

# Attach chain
chain_atoms = [
    (ring_center[0] + 1.8, ring_center[1]),        # C
    (ring_center[0] + 2.8, ring_center[1]),        # C
    (ring_center[0] + 3.6, ring_center[1]+0.5),    # O
]

labels = ['C', 'C', 'O']
colors = ['black', 'black', 'red']

for (x, y), lab, col in zip(chain_atoms, labels, colors):
    ax.add_patch(Circle((x, y), 0.18, color=col, zorder=3))
    ax.text(x, y, lab, ha='center', va='center', fontsize=9,
            color='white' if col=='black' else 'white')

# Bonds in chain
ax.plot([ring_center[0]+R, chain_atoms[0][0]-0.18], 
        [ring_center[1], chain_atoms[0][1]], 'k-', linewidth=2)
for i in range(len(chain_atoms)-1):
    x1, y1 = chain_atoms[i]
    x2, y2 = chain_atoms[i+1]
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

# Annotate
ax.text(6.5, 2.2, 'Odor molecule\n(α-irone-like)', ha='center', fontsize=11,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Arrow to nose (right edge)
ax.add_patch(FancyArrowPatch((8.5, 5), (10.5, 5),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='purple'))
ax.text(10.7, 5, 'NOSE', fontsize=11, va='center', color='purple')

ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Figure 1-9: Violet Odor Molecule in Air', fontsize=14, weight='bold')

plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("VIOLET SMELL MOLECULE")
print("="*70)
print("\\nKey points:")
print("  - Specific large organic molecule (α-irone)")
print("  - Moves randomly in air with N₂, O₂, H₂O")
print("  - Occasionally enters nose by chance (no 'desire')")
print("  - Chemists can determine full 3D arrangement")
print("="*70)"""),

    # NAMING MOLECULES
    nbf.v4.new_markdown_cell("""## 🔤 Naming Molecules: Why So Complicated?

### 📖 Feynman's Text

> "One problem of chemistry is to name a substance, so that we will know what it is."

> "Not only must the name tell the shape, but it must also tell that here is an oxygen atom, there a hydrogen—exactly what and where each atom is."

> "So we can appreciate that the chemical names must be complex in order to be complete."

> "It is not that they wish to be obscure, but they have an extremely difficult problem in trying to describe the molecules in words!"

### 🔍 Example: α‑irone

Full name Feynman quotes:

> 4‑(2,2,3,6‑tetramethyl‑5‑cyclohexenyl)‑3‑buten‑2‑one

This name encodes:

- A 6‑carbon ring (cyclohexene)
- Specific positions of double bonds
- Exact locations of methyl (CH₃) groups
- Side chain details (buten‑2‑one fragment)

**Key idea:** Names encode STRUCTURE. Long names = lots of structural information.

---"""),

    # EVIDENCE FOR ATOMS: BROWNIAN MOTION
    nbf.v4.new_markdown_cell("""## 🔍 Evidence for Atoms: Brownian Motion

### 📖 Feynman's Text

> "How do we *know* that there are atoms? ... There is also somewhat more direct evidence, a good example of which is the following:"

> "If the atoms are always in motion, say in water, and we put a big ball of something in the water, a ball much bigger than the atoms, the ball will jiggle around—much as in a push ball game..."

> "Therefore, if we look at very tiny particles (colloids) in water through an excellent microscope, we see a **perpetual jiggling of the particles**, which is the result of the bombardment of the atoms. This is called **Brownian motion**."

### 🔍 Why This Matters

- Atoms too small to see directly, even with electron microscopes.
- But their effects on larger particles (colloids) are visible.
- Einstein (1905) predicted:
  - Mean squared displacement of particles vs time
  - Dependence on temperature, viscosity, particle size
- Perrin (1908) measured this and extracted Avogadro's number.

This was decisive evidence that **atoms are real** and not just a convenient model.

---"""),

    # CODE: BROWNIAN MOTION SIMULATION
    nbf.v4.new_code_cell("""# Simulate Brownian motion of a large particle in water

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Parameters
n_steps = 2000
dt = 0.01
D = 0.1  # Diffusion coefficient (arbitrary units)

# Brownian motion: x(t+dt) = x(t) + sqrt(2Ddt)*N(0,1)
x = np.zeros(n_steps)
y = np.zeros(n_steps)

for i in range(1, n_steps):
    dx = np.sqrt(2*D*dt) * np.random.randn()
    dy = np.sqrt(2*D*dt) * np.random.randn()
    x[i] = x[i-1] + dx
    y[i] = y[i-1] + dy

# Compute mean squared displacement
times = np.arange(n_steps) * dt
msd = x**2 + y**2  # For a single particle (ensemble = time here)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Trajectory
ax1.plot(x, y, 'b-', alpha=0.7)
ax1.plot(x[0], y[0], 'go', label='Start')
ax1.plot(x[-1], y[-1], 'ro', label='End')
ax1.set_aspect('equal')
ax1.set_title('Brownian Motion of a Colloid Particle', fontsize=14, weight='bold')
ax1.set_xlabel('x (arbitrary units)')
ax1.set_ylabel('y (arbitrary units)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# MSD vs time
ax2.plot(times, msd, 'r-', linewidth=2)
ax2.set_title('Mean Squared Displacement vs Time', fontsize=14, weight='bold')
ax2.set_xlabel('Time')
ax2.set_ylabel('MSD = x² + y²')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("BROWNIAN MOTION SUMMARY")
print("="*70)
print("\\nKey facts:")
print("  - Random jiggling of visible particles in fluid")
print("  - Caused by countless invisible atomic collisions")
print("  - Einstein (1905) predicted MSD ~ 4 D t")
print("  - Perrin (1908) measured it and inferred Avogadro's number")
print("  - Direct, quantitative evidence that atoms EXIST")
print("="*70)"""),

    # CRYSTALS AS EVIDENCE
    nbf.v4.new_markdown_cell("""## 💎 Crystals as Evidence for Atoms

### 📖 Feynman's Text

> "We can see further evidence for atoms in the **structure of crystals**. In many cases the structures deduced by **x‑ray analysis** agree in their spatial 'shapes' with the forms actually exhibited by crystals as they occur in nature."

> "The angles between the various 'faces' of a crystal agree, within seconds of arc, with angles deduced on the assumption that a crystal is made of many 'layers' of atoms."

### 🔍 Key Idea

- Crystals have regular shapes (faces, edges, angles).
- X‑ray diffraction patterns can be explained if:
  - Atoms arranged in periodic lattices
  - Planes of atoms scatter x‑rays coherently
- The **macroscopic shape** matches the **microscopic lattice**.

This is powerful geometric evidence: large-scale shapes reflect atomic-scale order.

---"""),

    # CODE: SIMPLE CRYSTAL SHAPE
    nbf.v4.new_code_cell("""# Simple crystal shape vs atomic lattice visualization

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Left: atomic lattice
for i in range(8):
    for j in range(8):
        ax1.plot(i, j, 'ko', markersize=4)
ax1.set_title('Atomic Lattice (Top View)', fontsize=14, weight='bold')
ax1.set_aspect('equal')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.grid(True, alpha=0.2)

# Overlay some lattice planes
for n in [1, 3, 5, 7]:
    ax1.plot([0, 7], [n, n], 'r-', alpha=0.3)
    ax1.plot([n, n], [0, 7], 'b-', alpha=0.3)

# Right: crystal macroscopic shape
ax2.add_patch(Rectangle((0, 0), 4, 2, fill=False, edgecolor='black', linewidth=3))
ax2.add_patch(Rectangle((4, 2), 2, 3, fill=False, edgecolor='black', linewidth=3))
ax2.add_patch(Rectangle((1, 2), 3, 3, fill=False, edgecolor='black', linewidth=3))

ax2.set_xlim(-1, 7)
ax2.set_ylim(-1, 6)
ax2.set_aspect('equal')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title('Crystal Macroscopic Shape', fontsize=14, weight='bold')

plt.suptitle('Crystal Angles Reflect Atomic Lattice', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("CRYSTAL EVIDENCE SUMMARY")
print("="*70)
print("\\nKey points:")
print("  - Atoms arranged in regular lattice")
print("  - Planes of atoms -> flat crystal faces")
print("  - Angles between faces match lattice geometry")
print("  - X-ray diffraction confirms atomic periodicity")
print("="*70)"""),

    # BIOLOGY AND ATOMS
    nbf.v4.new_markdown_cell("""## 🧬 Biology and Atoms: "Everything that animals do, atoms do"

### 📖 Feynman's Text

> "Everything is made of atoms. That is the key hypothesis. The most important hypothesis in all of biology, for example, is that **everything that animals do, atoms do.**"

> "In other words, **there is nothing that living things do that cannot be understood from the point of view that they are made of atoms acting according to the laws of physics.**"

### 🔍 Radical Claim

This is a **strong reductionist** statement:

- Muscles moving → atoms rearranging
- Nerve signals → ions moving, membranes changing
- Memory → atomic states in neural networks
- Thought → atoms in a brain obeying physics

It does NOT say we *currently* understand all biology in atomic detail, but:

> It is the most **useful theory** for producing new ideas in biology.

This view underlies:

- Molecular biology
- Biochemistry
- Neuroscience
- Pharmacology

**Key idea:** No magic, no vital force—just atoms and laws.

---"""),

    # FINAL REFLECTION
    nbf.v4.new_markdown_cell("""## 🪞 "We Are a Pile of Atoms" – But Not "Merely"

### 📖 Feynman's Text

> "If a piece of steel or a piece of salt, consisting of atoms one next to the other, can have such interesting properties; if water—which is nothing but these little blobs, mile upon mile of the same thing over the earth—can form waves and foam, and make rushing noises and strange patterns as it runs over cement;"

> "If all of this, all the life of a stream of water, can be nothing but a pile of atoms, **how much more is possible?**"

> "Is it possible that that 'thing' walking back and forth in front of you, talking to you, is a great glob of these atoms in a very complex arrangement...?"

> "When we say we are a pile of atoms, we do not mean we are **merely** a pile of atoms, because a pile of atoms which is not repeated from one to the other might well have the possibilities which you see before you in the mirror."

### 🔍 Feynman's Philosophical Point

- Atoms are simple.
- Arrangements can be unimaginably complex.
- Complexity + laws of physics → emergent behavior.

**So:**
- You are a pile of atoms.
- BUT: arranged in a unique, non-repeating way.
- That arrangement has capacities: thought, emotion, creativity.

Feynman rejects:
- The idea that atoms make life "just mechanical."
- The idea that explaining life in atomic terms makes it less wonderful.

Instead:

> The atomic view makes life even more **marvelous**.

---"""),

    # SUMMARY
    nbf.v4.new_markdown_cell("""## 📊 Section 1-4 Summary & Chapter 1 Wrap-up

### 🎯 Main Points of Section 1-4

1. **Chemical reactions** = atoms changing partners, releasing/absorbing energy  
2. **Complex molecules** (like violet smell) have precisely known 3D structures  
3. **Brownian motion** and **crystals** provide strong evidence for atoms  
4. **Biology** can be understood in terms of atoms and physics  
5. **We are atoms**, but not "merely" atoms—complex arrangements give rise to everything we see

### 🧩 Chapter 1 Overall: "Atoms in Motion"

You now have:

- The **atomic hypothesis** as the one-sentence core
- States of matter (solid/liquid/gas) from atomic motion and forces
- Processes (evaporation, dissolution, chemical reactions)
- Evidence for atoms (Brownian motion, crystals)
- The connection to **biology** and **consciousness**

### 🌉 Forward Connections

- Volume I: Mechanics, radiation, heat → all built on atomic motion  
- Volume II: Electromagnetism → forces between charges in atoms  
- Volume III: Quantum mechanics → the deeper laws atoms obey

---

## 🎉 Congratulations!

You’ve completed **all of Chapter 1 – Atoms in Motion**, with:

- Detailed reading notes for each section
- Visualizations and simulations
- Deep conceptual and philosophical context

From here, we can:

- Build **02-examples-and-code.ipynb** for Chapter 1  
- Fill **06-flashcards.ipynb** with high-quality cards  
- Start logging this journey in **05-ai-qa-log.ipynb**  
- Or move on to **Chapter 2** when you’re ready.

*"If, in some cataclysm, all of scientific knowledge were to be destroyed..."*  
You now understand why Feynman chose **this** as the one sentence to save.

---""")
]

with open("04-reading-notes-section-1-4.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("✅ FIXED Section 1-4 COMPLETE!")
print(f"📍 Location: {target_dir}/04-reading-notes-section-1-4.ipynb")
print("\nWhat was created:")
print("  • Chemical reaction analysis (C + O2 -> CO, CO2)")
print("  • Violet smell molecule (α‑irone-like) visualization")
print("  • Brownian motion simulation")
print("  • Crystal lattice vs shape visualization")
print("  • Biology-from-atoms discussion")
print("  • Final philosophical wrap-up of Chapter 1")
print("\n🎉 Chapter 1 reading notes are now COMPLETE! Run all cells to see visualizations.")
