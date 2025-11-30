#!/usr/bin/env python3
"""
FIXED: Create COMPLETE reading notes for Section 1-2: Matter is Made of Atoms
Run from: volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion/
"""

import nbformat as nbf
from datetime import datetime
import os

# Ensure we're in the right directory
target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
os.chdir(target_dir)

print("\n🔨 Creating FIXED Section 1-2 Reading Notes...")
print(f"📁 Working directory: {os.getcwd()}\n")

nb = nbf.v4.new_notebook()

nb.cells = [
    # TITLE
    nbf.v4.new_markdown_cell(f"""# Volume 1, Chapter 1 – Atoms in Motion
## Section 1-2: Matter is Made of Atoms

**Date Started:** {datetime.now().strftime("%B %d, %Y")}  
**Source:** [FLP Vol I, Ch 1, §1-2](https://www.feynmanlectures.caltech.edu/I_01.html#Ch1-S2)

---

## 🌟 Overview

This is **THE** most important section in all of physics education. Feynman answers his own question from Section 1-1:

> **"If all scientific knowledge were destroyed, what ONE SENTENCE would you pass on?"**

**Answer:** The atomic hypothesis.

**What you'll learn:**
1. The atomic hypothesis - all things are made of atoms
2. Visualizing atoms at different scales (water → steam → ice)
3. How atomic motion explains heat, pressure, phase transitions
4. Why this ONE idea contains "enormous information"

---"""),

    # THE ONE SENTENCE
    nbf.v4.new_markdown_cell("""## 🎯 THE One Sentence: The Atomic Hypothesis

### 📖 Feynman's Text

> "If, in some cataclysm, all of scientific knowledge were to be destroyed, and only one sentence passed on to the next generations of creatures, what statement would contain the **most information in the fewest words**?"

> "I believe it is the **atomic hypothesis** (or the atomic fact, or whatever you wish to call it) that **all things are made of atoms—little particles that move around in perpetual motion, attracting each other when they are a little distance apart, but repelling upon being squeezed into one another.**"

> "In that one sentence, you will see, there is an **enormous amount of information** about the world, if just a little imagination and thinking are applied."

### 🔍 Unpacking the Information Density

**Let's break down what this ONE sentence tells us:**

| Component | What It Means | What You Can Derive |
|-----------|---------------|---------------------|
| **"All things are made of atoms"** | Matter is discrete, not continuous | • Chemistry (combinations)<br>• Counting (Avogadro's number)<br>• Molecular structure<br>• Finite divisibility |
| **"Little particles"** | Specific size scale | • Angstroms (10⁻¹⁰ m)<br>• Countable entities<br>• Statistical mechanics |
| **"Move around in perpetual motion"** | Never at rest (even at low T) | • Heat = motion<br>• Temperature = avg. kinetic energy<br>• Brownian motion<br>• Diffusion<br>• No absolute stillness |
| **"Attracting each other when apart"** | Forces at a distance | • Chemical bonds<br>• Van der Waals forces<br>• Surface tension<br>• Viscosity<br>• Why matter holds together |
| **"Repelling when squeezed"** | Contact forces | • Incompressibility of solids/liquids<br>• Atomic radius<br>• Why you don't fall through floor<br>• Elastic collisions |

**From this alone**, you can derive:
- ✅ States of matter (solid/liquid/gas)
- ✅ Phase transitions (melting/boiling/freezing)
- ✅ Pressure (collisions with walls)
- ✅ Temperature (average kinetic energy)
- ✅ Chemical reactions (rearrangements)
- ✅ Thermodynamics (statistical behavior)
- ✅ Much of chemistry and biology!

**This is why Feynman calls it THE most important statement.**

---"""),

    # SCALE JOURNEY
    nbf.v4.new_markdown_cell("""## 🔬 The Journey to Atomic Scale: Magnifying Water

### 📖 Feynman's Text

> "To illustrate the power of the atomic idea, suppose that we have a **drop of water a quarter of an inch on the side**."

> "If we look at it very closely we see nothing but water—smooth, continuous water."

### 🔍 The Three-Stage Magnification Journey

**Stage 1: Optical microscope (2,000×)**
- Drop now ~40 feet across (size of a room)
- See: "Small football-shaped things swimming" = **Paramecia**
- These are LIVING ORGANISMS (biology!)
- Still looks "smooth" overall

**Stage 2: Super-magnification (2,000× again = 4,000,000× total)**
- Drop now ~15 miles across!
- See: "A kind of teeming... like a crowd at a football game"
- No longer smooth - something is MOVING

**Stage 3: Final magnification (250× more = **1 billion times total**)**
- Now we see: **Individual atoms!** (Figure 1-1)
- Black circles = Oxygen atoms
- White circles = Hydrogen atoms
- Each O has 2 H's attached → H₂O molecule

**Key insight:** What looks perfectly smooth and continuous to our eyes is actually a **jiggling swarm of discrete particles**.

---"""),

    # CODE: SCALE VISUALIZATION (FIXED!)
    nbf.v4.new_code_cell("""# Visualize the magnification journey from drop to atoms

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

fig, axes = plt.subplots(1, 4, figsize=(18, 5))

# Stage 0: Original drop
ax0 = axes[0]
drop = Circle((0.5, 0.5), 0.3, color='lightblue', ec='darkblue', linewidth=2)
ax0.add_patch(drop)
ax0.text(0.5, 0.5, 'Water\\nDrop', ha='center', va='center', fontsize=14, weight='bold')
ax0.text(0.5, -0.1, '0.25 inch\\n(~6 mm)', ha='center', fontsize=10)
ax0.set_xlim(0, 1)
ax0.set_ylim(-0.2, 1)
ax0.set_aspect('equal')
ax0.axis('off')
ax0.set_title('Stage 0: Naked Eye', fontsize=13, weight='bold')

# Stage 1: Optical microscope (2000x)
ax1 = axes[1]
# Draw paramecium
paramecium = Ellipse((0.3, 0.6), 0.15, 0.08, angle=30, 
                     color='green', alpha=0.6, ec='darkgreen', linewidth=2)
ax1.add_patch(paramecium)
paramecium2 = Ellipse((0.7, 0.4), 0.12, 0.06, angle=-20,
                      color='green', alpha=0.6, ec='darkgreen', linewidth=2)
ax1.add_patch(paramecium2)

# Add cilia (simplified)
for i in range(8):
    angle = i * 45
    x = 0.3 + 0.1 * np.cos(np.radians(angle))
    y = 0.6 + 0.05 * np.sin(np.radians(angle))
    ax1.plot([0.3, x], [0.6, y], 'k-', linewidth=0.5, alpha=0.5)

ax1.text(0.3, 0.3, 'Paramecia!', fontsize=10, style='italic')
ax1.text(0.5, -0.1, '~40 feet across\\n(2,000x magnification)', ha='center', fontsize=9)
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.2, 1)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Stage 1: Optical Scope', fontsize=13, weight='bold')

# Stage 2: Extreme magnification (4 million x)
ax2 = axes[2]
# Draw "teeming" - many small dots
np.random.seed(42)
for _ in range(150):
    x, y = np.random.rand(2)
    ax2.plot(x, y, 'o', color='gray', markersize=2, alpha=0.6)

ax2.text(0.5, 0.5, '"Teeming"\\nlike a crowd', ha='center', va='center',
        fontsize=12, weight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
ax2.text(0.5, -0.1, '~15 miles across\\n(4,000,000x total)', ha='center', fontsize=9)
ax2.set_xlim(0, 1)
ax2.set_ylim(-0.2, 1)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Stage 2: Super Mag', fontsize=13, weight='bold')

# Stage 3: Atomic scale (1 billion x)
ax3 = axes[3]
# Draw water molecules (H2O)
molecules = [
    (0.2, 0.7), (0.5, 0.8), (0.8, 0.7),
    (0.35, 0.5), (0.65, 0.5),
    (0.2, 0.3), (0.5, 0.2), (0.8, 0.3)
]

for ox, oy in molecules:
    # Oxygen (black, larger)
    O = Circle((ox, oy), 0.06, color='black', zorder=3)
    ax3.add_patch(O)
    
    # Hydrogen atoms (white, smaller) - at 105 degree angle
    angle1, angle2 = 52.5, -52.5  # degrees from vertical
    h1x = ox + 0.09 * np.sin(np.radians(angle1))
    h1y = oy + 0.09 * np.cos(np.radians(angle1))
    h2x = ox + 0.09 * np.sin(np.radians(angle2))
    h2y = oy + 0.09 * np.cos(np.radians(angle2))
    
    H1 = Circle((h1x, h1y), 0.04, color='white', ec='black', linewidth=1, zorder=3)
    H2 = Circle((h2x, h2y), 0.04, color='white', ec='black', linewidth=1, zorder=3)
    ax3.add_patch(H1)
    ax3.add_patch(H2)

ax3.text(0.5, -0.1, 'Individual atoms!\\n(1,000,000,000x total)', ha='center', fontsize=9)
ax3.set_xlim(0, 1)
ax3.set_ylim(-0.2, 1)
ax3.set_aspect('equal')
ax3.axis('off')
ax3.set_title('Stage 3: Atomic Scale', fontsize=13, weight='bold')

# FIXED: Changed single quotes to double quotes to avoid apostrophe issue
plt.suptitle("Feynman Journey: From Droplet to Atoms", fontsize=16, weight='bold', y=1.02)
plt.tight_layout()
plt.show()

print("="*70)
print("MAGNIFICATION SUMMARY")
print("="*70)
print("\\nStage 0 -> 1: 2,000x (optical microscope)")
print("  See: Paramecia (living organisms)")
print("\\nStage 1 -> 2: 2,000x more (total: 4,000,000x)")
print("  See: 'Teeming' motion")
print("\\nStage 2 -> 3: 250x more (total: 1,000,000,000x)")
print("  See: Individual H2O molecules!")
print("\\nCheckmark: Smooth water is actually a jiggling swarm of atoms!")
print("="*70)"""),

    # FIGURE 1-1: WATER
    nbf.v4.new_markdown_cell("""## 💧 Figure 1-1: Water Magnified 1 Billion Times

### 📖 Feynman's Description

> "This is a picture of water magnified a billion times, but **idealized in several ways**:"

1. **Particles drawn simply** (sharp edges) - Real atoms have "fuzzy" electron clouds
2. **2D schematic** - Actually moving in 3D
3. **Static picture** - Really "continually jiggling and bouncing, turning and twisting"
4. **Stuck together** - Attracted to each other ("glued")
5. **Don't squeeze through** - Repel when too close

### 🔍 Key Properties from the Figure

**Molecular structure:**
- Black circles = **Oxygen** (O)
- White circles = **Hydrogen** (H)
- Each O has **exactly 2** H atoms → H₂O molecule

**Atomic sizes:**
- Radius: 1-2 × 10⁻⁸ cm = 1-2 **angstroms** (Å)
- **Memory aid:** "If an apple → Earth size, atoms → original apple size"

**Forces:**
- **Attraction** (at distance) → Water holds together
- **Repulsion** (when squeezed) → Water has volume, doesn't collapse

**Motion:**
- All atoms constantly **jiggling**
- This jiggling = **HEAT**

---"""),

    # CODE: WATER MOLECULE SIMULATION
    nbf.v4.new_code_cell("""# Simulate water molecules with realistic dynamics

import numpy as np
import matplotlib.pyplot as plt

# Water molecule parameters
H2O_angle = 104.5  # degrees (actual: 105 degrees 3 minutes)
OH_distance = 0.957  # Angstroms

class WaterMolecule:
    \"\"\"Represents a single H2O molecule\"\"\"
    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.vx = np.random.randn() * 0.02
        self.vy = np.random.randn() * 0.02
        self.angle = angle
        self.omega = np.random.randn() * 0.05  # Angular velocity
    
    def get_atom_positions(self):
        \"\"\"Calculate O and H positions\"\"\"
        # Oxygen at center
        O_pos = (self.x, self.y)
        
        # Hydrogens at 104.5 degree angle
        angle1 = self.angle + H2O_angle/2
        angle2 = self.angle - H2O_angle/2
        
        H1_x = self.x + OH_distance * np.cos(np.radians(angle1))
        H1_y = self.y + OH_distance * np.sin(np.radians(angle1))
        
        H2_x = self.x + OH_distance * np.cos(np.radians(angle2))
        H2_y = self.y + OH_distance * np.sin(np.radians(angle2))
        
        return O_pos, (H1_x, H1_y), (H2_x, H2_y)
    
    def update(self, dt=1.0, bounds=(10, 10)):
        \"\"\"Update position with random jiggling\"\"\"
        # Add random jiggling (thermal motion)
        self.vx += np.random.randn() * 0.01
        self.vy += np.random.randn() * 0.01
        
        # Damping (viscosity)
        self.vx *= 0.95
        self.vy *= 0.95
        
        # Update position
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        # Update angle
        self.angle += self.omega * dt
        self.omega *= 0.98  # Damping
        
        # Bounce off walls
        if self.x < 0 or self.x > bounds[0]:
            self.vx *= -0.8
            self.x = np.clip(self.x, 0, bounds[0])
        if self.y < 0 or self.y > bounds[1]:
            self.vy *= -0.8
            self.y = np.clip(self.y, 0, bounds[1])

# Create water molecules
np.random.seed(42)
n_molecules = 20
molecules = [WaterMolecule(np.random.rand()*10, np.random.rand()*10, 
                          np.random.rand()*360) 
            for _ in range(n_molecules)]

# Static visualization (since animation is complex in notebooks)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Frame 1: Initial positions
for mol in molecules:
    O, H1, H2 = mol.get_atom_positions()
    
    # Draw molecule
    ax1.plot([O[0], H1[0]], [O[1], H1[1]], 'gray', linewidth=1, alpha=0.5)
    ax1.plot([O[0], H2[0]], [O[1], H2[1]], 'gray', linewidth=1, alpha=0.5)
    ax1.scatter(*O, s=200, c='black', zorder=3, edgecolor='white', linewidth=1)
    ax1.scatter(*H1, s=100, c='white', zorder=3, edgecolor='black', linewidth=1)
    ax1.scatter(*H2, s=100, c='white', zorder=3, edgecolor='black', linewidth=1)

ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 11)
ax1.set_aspect('equal')
ax1.set_title('Water (Liquid) - Frame 1', fontsize=14, weight='bold')
ax1.set_xlabel('Position (Angstroms)', fontsize=11)
ax1.set_ylabel('Position (Angstroms)', fontsize=11)
ax1.grid(True, alpha=0.2)

# Frame 2: After some jiggling
for _ in range(50):
    for mol in molecules:
        mol.update(dt=0.1)

for mol in molecules:
    O, H1, H2 = mol.get_atom_positions()
    
    # Draw molecule
    ax2.plot([O[0], H1[0]], [O[1], H1[1]], 'gray', linewidth=1, alpha=0.5)
    ax2.plot([O[0], H2[0]], [O[1], H2[1]], 'gray', linewidth=1, alpha=0.5)
    ax2.scatter(*O, s=200, c='black', zorder=3, edgecolor='white', linewidth=1)
    ax2.scatter(*H1, s=100, c='white', zorder=3, edgecolor='black', linewidth=1)
    ax2.scatter(*H2, s=100, c='white', zorder=3, edgecolor='black', linewidth=1)

ax2.set_xlim(-1, 11)
ax2.set_ylim(-1, 11)
ax2.set_aspect('equal')
ax2.set_title('Water (Liquid) - Frame 2 (After Jiggling)', fontsize=14, weight='bold')
ax2.set_xlabel('Position (Angstroms)', fontsize=11)
ax2.set_ylabel('Position (Angstroms)', fontsize=11)
ax2.grid(True, alpha=0.2)

plt.suptitle('Water Molecules: Perpetual Jiggling Motion', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("WATER MOLECULE PROPERTIES")
print("="*70)
print(f"\\nH-O-H angle: {H2O_angle} degrees (actual: 105 degrees 3 minutes)")
print(f"O-H bond length: {OH_distance} Angstroms")
print(f"\\nKey insight: Molecules are ALWAYS moving (thermal motion)")
print("  -> This jiggling is what we call HEAT")
print("="*70)"""),

    # FIGURE 1-2: STEAM
    nbf.v4.new_markdown_cell("""## ☁️ Figure 1-2: Steam (Gas Phase)

### 📖 Feynman's Text

> "In Fig. 1–2 we have a picture of **steam**. This picture fails in one respect: at ordinary atmospheric pressure there certainly would not be as many as **three** water molecules in this figure."

> "Most squares this size would contain **none**—but we accidentally have two and a half or three in the picture (just so it would not be completely blank)."

### 🔍 Key Differences from Liquid Water

**Spacing:**
- Liquid: Molecules touching, tightly packed
- Gas: Molecules **far apart** (mostly empty space!)
- At 1 atm pressure: Huge distances between molecules

**Molecular details:**
- Angle drawn: 120° (for simplicity)
- **Actual angle: 105°3'** (very precisely measured!)
- O-H distance: **0.957 Å** (also precisely known)

> "So we know this molecule very well."

**This is profound:** By 1961, we knew the EXACT geometry of H₂O to incredible precision!

---"""),

    # CODE: STEAM VISUALIZATION
    nbf.v4.new_code_cell("""# Visualize steam (gas phase) - molecules far apart

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# LIQUID WATER - densely packed
np.random.seed(42)
n_liquid = 30
for _ in range(n_liquid):
    x = np.random.rand() * 10
    y = np.random.rand() * 10
    angle = np.random.rand() * 360
    
    # Oxygen
    ax1.scatter(x, y, s=200, c='black', zorder=3, edgecolor='white', linewidth=1)
    
    # Hydrogens
    h1x = x + 0.9 * np.cos(np.radians(angle + 52))
    h1y = y + 0.9 * np.sin(np.radians(angle + 52))
    h2x = x + 0.9 * np.cos(np.radians(angle - 52))
    h2y = y + 0.9 * np.sin(np.radians(angle - 52))
    
    ax1.plot([x, h1x], [y, h1y], 'gray', linewidth=1, alpha=0.4)
    ax1.plot([x, h2x], [y, h2y], 'gray', linewidth=1, alpha=0.4)
    ax1.scatter(h1x, h1y, s=80, c='white', zorder=3, edgecolor='black', linewidth=1)
    ax1.scatter(h2x, h2y, s=80, c='white', zorder=3, edgecolor='black', linewidth=1)

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.set_title('LIQUID WATER (Dense)', fontsize=14, weight='bold')
ax1.set_xlabel('Position', fontsize=11)
ax1.grid(True, alpha=0.2)
ax1.text(5, -1, f'{n_liquid} molecules in this space', ha='center', fontsize=10)

# STEAM - sparse, far apart
n_steam = 3  # Feynman: "2 and a half or 3"
steam_positions = [(2, 8), (7, 3), (4, 5)]

for x, y in steam_positions:
    angle = np.random.rand() * 360
    
    # Oxygen
    ax2.scatter(x, y, s=200, c='black', zorder=3, edgecolor='white', linewidth=1)
    
    # Hydrogens
    h1x = x + 0.9 * np.cos(np.radians(angle + 52))
    h1y = y + 0.9 * np.sin(np.radians(angle + 52))
    h2x = x + 0.9 * np.cos(np.radians(angle - 52))
    h2y = y + 0.9 * np.sin(np.radians(angle - 52))
    
    ax2.plot([x, h1x], [y, h1y], 'gray', linewidth=1, alpha=0.6)
    ax2.plot([x, h2x], [y, h2y], 'gray', linewidth=1, alpha=0.6)
    ax2.scatter(h1x, h1y, s=80, c='white', zorder=3, edgecolor='black', linewidth=1)
    ax2.scatter(h2x, h2y, s=80, c='white', zorder=3, edgecolor='black', linewidth=1)
    
    # Draw motion arrows
    arrow_len = 1.5
    arrow_angle = np.random.rand() * 360
    dx = arrow_len * np.cos(np.radians(arrow_angle))
    dy = arrow_len * np.sin(np.radians(arrow_angle))
    ax2.arrow(x, y, dx, dy, head_width=0.3, head_length=0.2, 
             fc='red', ec='red', alpha=0.5, linewidth=2)

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect('equal')
ax2.set_title('STEAM (Sparse)', fontsize=14, weight='bold')
ax2.set_xlabel('Position', fontsize=11)
ax2.grid(True, alpha=0.2)
ax2.text(5, -1, f'Only {n_steam} molecules (mostly empty!)', ha='center', fontsize=10, color='red')

plt.suptitle('Liquid vs. Gas: Density Difference', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("LIQUID vs. GAS DENSITY")
print("="*70)
print(f"\\nLiquid water: ~{n_liquid} molecules in box")
print(f"Steam (1 atm): ~{n_steam} molecules in SAME box")
print(f"\\nDensity ratio: ~{n_liquid/n_steam:.0f}:1")
print("\\n Checkmark: Gas is mostly EMPTY SPACE!")
print("="*70)"""),
]

with open("02-reading-notes-section-1-2.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"\n✅ FIXED Part 1 created: 02-reading-notes-section-1-2.ipynb")
print(f"📍 Location: {target_dir}")
print("\nFixed issues:")
print("  • Quote escaping in plt.suptitle (Feynman's -> Feynman)")
print("  • All code cells should now run without errors")
print("\nThis covers:")
print("  • The atomic hypothesis (THE one sentence)")
print("  • Magnification journey")
print("  • Water molecule structure")
print("  • Steam vs. liquid comparison")
print("\n🎯 Test this, then I'll create Part 2 (gas pressure, compression, ice, phase transitions)")
