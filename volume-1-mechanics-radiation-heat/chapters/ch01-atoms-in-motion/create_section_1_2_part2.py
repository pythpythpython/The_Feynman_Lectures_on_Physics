#!/usr/bin/env python3
"""
Part 2: Complete Section 1-2 with gas pressure, ice, and phase transitions
Appends to existing 02-reading-notes-section-1-2.ipynb
"""

import nbformat as nbf
from datetime import datetime
import os

target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
os.chdir(target_dir)

print("\n🔨 Adding Part 2 to Section 1-2 notebook...")
print(f"📁 Working directory: {os.getcwd()}\n")

# Load existing notebook
with open("02-reading-notes-section-1-2.ipynb", 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Add new cells
new_cells = [
    # GAS PRESSURE
    nbf.v4.new_markdown_cell("""## ⚗️ Figure 1-3: Gas Pressure from Molecular Collisions

### 📖 Feynman's Text

> "Let us see what some of the properties of steam vapor or any other gas are. The molecules, being separated from one another, will **bounce against the walls**."

> "When they bombard the wall, this pushes the wall away. (Of course we would have to push the wall back.) This means that the gas exerts a **jittery force** which our coarse senses (not being ourselves magnified a billion times) feel only as an **average push**."

### 🔍 The Piston Model

**Setup:** Cylinder with movable piston + gas molecules inside

**What happens:**
- Molecules move randomly in all directions
- They collide with the piston constantly
- Each collision pushes the piston outward
- We experience this as **pressure** (force per area)

**Key insight:** Pressure is not continuous—it's billions of tiny impacts averaged out!

---"""),

    # CODE: GAS PRESSURE VISUALIZATION
    nbf.v4.new_code_cell("""# Visualize gas pressure from molecular collisions

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# LEFT: Piston with molecules
ax1.add_patch(Rectangle((0, 0), 10, 8, fill=False, edgecolor='black', linewidth=3))
ax1.add_patch(Rectangle((0, 8), 10, 0.5, facecolor='gray', edgecolor='black', linewidth=2))
ax1.text(5, 8.25, 'PISTON', ha='center', va='center', fontsize=12, weight='bold')

# Add gas molecules with velocity arrows
np.random.seed(42)
n_molecules = 15
for _ in range(n_molecules):
    x = np.random.rand() * 10
    y = np.random.rand() * 7.5
    
    # Molecule
    ax1.add_patch(Circle((x, y), 0.2, color='blue', alpha=0.6))
    
    # Velocity arrow
    vx = (np.random.rand() - 0.5) * 2
    vy = (np.random.rand() - 0.5) * 2
    ax1.arrow(x, y, vx, vy, head_width=0.2, head_length=0.15, 
             fc='red', ec='red', alpha=0.5, linewidth=1.5)

# Show collisions with top
collision_x = [2, 5, 8]
for cx in collision_x:
    ax1.plot([cx, cx], [7.8, 8], 'yellow', linewidth=3, alpha=0.8)
    ax1.arrow(cx, 9, 0, 0.5, head_width=0.3, head_length=0.2,
             fc='orange', ec='orange', linewidth=2)

ax1.text(5, 9.8, 'Force on piston\\n(many collisions/sec)', 
        ha='center', fontsize=10, weight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 11)
ax1.set_aspect('equal')
ax1.set_title('Gas Molecules Colliding with Piston', fontsize=14, weight='bold')
ax1.axis('off')

# RIGHT: Pressure vs. density relationship
densities = np.array([10, 20, 30, 40, 50])  # arbitrary units
pressures = densities * 1.0  # P proportional to density

ax2.plot(densities, pressures, 'o-', linewidth=3, markersize=10, 
        color='darkblue', label='Ideal gas')
ax2.plot([0, 50], [0, 50], 'r--', linewidth=2, alpha=0.5, 
        label='Perfect proportionality')

ax2.set_xlabel('Density (molecules per volume)', fontsize=12, weight='bold')
ax2.set_ylabel('Pressure (force per area)', fontsize=12, weight='bold')
ax2.set_title('Pressure Proportional to Density', fontsize=14, weight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 55)
ax2.set_ylim(0, 55)

plt.suptitle('Figure 1-3: Understanding Gas Pressure', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("GAS PRESSURE: KEY INSIGHTS")
print("="*70)
print("\\n1. Pressure = Force / Area from molecular collisions")
print("2. Double density -> Double collisions -> Double pressure")
print("3. Increase temperature -> Faster molecules -> Higher pressure")
print("4. Compress gas -> Molecules gain energy -> Temperature rises")
print("\\n Checkmark: Pressure is statistical (average of billions of impacts)")
print("="*70)"""),

    # COMPRESSION AND TEMPERATURE
    nbf.v4.new_markdown_cell("""## 🔥 Compression Heats Gas, Expansion Cools It

### 📖 Feynman's Text

> "Let us consider another situation. Suppose that the piston moves inward, so that the atoms are slowly compressed into a smaller space. **What happens when an atom hits the moving piston?**"

> "Evidently it **picks up speed** from the collision. You can try it by bouncing a ping-pong ball from a forward-moving paddle, for example, and you will find that it comes off with more speed than that with which it struck."

### 🔍 Mechanical Energy Transfer

**Moving piston inward (compression):**
- Molecules hit advancing piston
- Bounce back with MORE speed
- Temperature INCREASES

**Moving piston outward (expansion):**
- Molecules hit receding piston  
- Bounce back with LESS speed
- Temperature DECREASES

**Real-world examples:**
- Bicycle pump gets hot when compressing air
- Aerosol cans get cold when spraying (expansion)
- Diesel engines compress air to ignite fuel!

---"""),

    # CODE: COMPRESSION SIMULATION
    nbf.v4.new_code_cell("""# Simulate compression heating and expansion cooling

import numpy as np
import matplotlib.pyplot as plt

# Simulate compression cycle
volumes = np.linspace(10, 5, 50)  # Compress to half volume
volumes_expand = np.linspace(5, 10, 50)  # Expand back

# For ideal gas: PV = nRT, and if we compress adiabatically PV^gamma = const
# For simplicity, assume PV^1.4 = const (air)
gamma = 1.4
P0, V0, T0 = 1.0, 10.0, 300  # Initial: 1 atm, 10 L, 300 K

# Compression
P_compress = P0 * (V0 / volumes)**gamma
T_compress = T0 * (V0 / volumes)**(gamma - 1)

# Expansion
P_expand = P_compress[-1] * (volumes_expand[0] / volumes_expand)**gamma
T_expand = T_compress[-1] * (volumes_expand[0] / volumes_expand)**(gamma - 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Pressure vs. Volume
ax1.plot(volumes, P_compress, 'r-', linewidth=3, label='Compression')
ax1.plot(volumes_expand, P_expand, 'b--', linewidth=3, label='Expansion')
ax1.set_xlabel('Volume', fontsize=12, weight='bold')
ax1.set_ylabel('Pressure', fontsize=12, weight='bold')
ax1.set_title('Pressure During Compression/Expansion', fontsize=14, weight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.invert_xaxis()  # Show compression left-to-right

# Temperature vs. Volume
ax2.plot(volumes, T_compress, 'r-', linewidth=3, label='Compression')
ax2.plot(volumes_expand, T_expand, 'b--', linewidth=3, label='Expansion')
ax2.axhline(y=T0, color='green', linestyle=':', linewidth=2, 
           label=f'Initial temp ({T0} K)', alpha=0.5)
ax2.set_xlabel('Volume', fontsize=12, weight='bold')
ax2.set_ylabel('Temperature (K)', fontsize=12, weight='bold')
ax2.set_title('Temperature During Compression/Expansion', fontsize=14, weight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.invert_xaxis()

plt.suptitle('Adiabatic Compression and Expansion', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("COMPRESSION & EXPANSION SUMMARY")
print("="*70)
print(f"\\nInitial: V = {V0} L, T = {T0} K, P = {P0} atm")
print(f"\\nAfter compression to V = {volumes[-1]} L:")
print(f"  Temperature: {T_compress[-1]:.1f} K (increase of {T_compress[-1]-T0:.1f} K)")
print(f"  Pressure: {P_compress[-1]:.2f} atm")
print(f"\\nAfter expansion back to V = {volumes_expand[-1]} L:")
print(f"  Temperature: {T_expand[-1]:.1f} K (back to ~{T0} K)")
print(f"  Pressure: {P_expand[-1]:.2f} atm")
print("\\n Checkmark: Compress -> Heat, Expand -> Cool")
print("="*70)"""),

    # FIGURE 1-4: ICE
    nbf.v4.new_markdown_cell("""## ❄️ Figure 1-4: Ice (Solid Phase with Crystalline Order)

### 📖 Feynman's Text

> "We now return to our drop of water and look in another direction. Suppose that we **decrease the temperature** of our drop of water. Suppose that the jiggling of the molecules of the atoms in the water is steadily decreasing."

> "We know that there are forces of attraction between the atoms, so that after a while they will not be able to jiggle so well. What will happen at very low temperatures is indicated in Fig. 1–4: **the molecules lock into a new pattern which is ice.**"

### 🔍 The Ice Structure

**Key features:**

1. **Definite positions** - Each atom has a specific place
2. **Long-range order** - Position at one end determines position millions of atoms away
3. **Hexagonal symmetry** - Explains 6-sided snowflakes!
4. **Open structure** - Many "holes" in the crystal
5. **Less dense than water** - Ice floats! (Very unusual)

**Why ice is special:**
- Most substances: solid is DENSER than liquid (atoms pack tighter)
- Water/ice: solid is LESS dense (open crystal structure collapses when melted)
- This is why ice floats—and why life on Earth exists!

---"""),

    # CODE: ICE STRUCTURE VISUALIZATION
    nbf.v4.new_code_cell("""# Visualize ice crystalline structure (hexagonal symmetry)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# LEFT: Ice structure (hexagonal lattice)
# Create hexagonal pattern
def hexagon_coords(center_x, center_y, radius):
    angles = np.linspace(0, 2*np.pi, 7)
    return [(center_x + radius * np.cos(a), center_y + radius * np.sin(a)) 
            for a in angles]

# Central hexagon
hex_centers = hexagon_coords(5, 5, 2)

# Draw molecules in hexagonal pattern
for cx, cy in hex_centers[:-1]:  # Exclude duplicate last point
    # Oxygen (black)
    ax1.add_patch(Circle((cx, cy), 0.25, color='black', zorder=3))
    
    # Hydrogens (white, simplified)
    for angle in [30, 150]:  # Two H at different angles
        hx = cx + 0.4 * np.cos(np.radians(angle))
        hy = cy + 0.4 * np.sin(np.radians(angle))
        ax1.add_patch(Circle((hx, hy), 0.15, color='white', 
                            edgecolor='black', linewidth=1, zorder=3))
    
    # Bonds (dashed lines showing hydrogen bonds)
    for cx2, cy2 in hex_centers[:-1]:
        if (cx, cy) != (cx2, cy2):
            dist = np.sqrt((cx-cx2)**2 + (cy-cy2)**2)
            if 1.8 < dist < 2.2:  # Neighboring molecules
                ax1.plot([cx, cx2], [cy, cy2], 'b--', 
                        linewidth=1, alpha=0.3)

# Central molecule
ax1.add_patch(Circle((5, 5), 0.25, color='black', zorder=3))
for angle in [30, 150]:
    hx = 5 + 0.4 * np.cos(np.radians(angle))
    hy = 5 + 0.4 * np.sin(np.radians(angle))
    ax1.add_patch(Circle((hx, hy), 0.15, color='white',
                        edgecolor='black', linewidth=1, zorder=3))

# Highlight hexagonal symmetry
hex_outline = Polygon(hex_centers[:-1], fill=False, 
                     edgecolor='red', linewidth=3, linestyle='-')
ax1.add_patch(hex_outline)

ax1.text(5, 0.5, 'Hexagonal Symmetry\\n(60 degree rotations)', 
        ha='center', fontsize=10, weight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.set_title('ICE: Crystalline Structure (Hexagonal)', fontsize=14, weight='bold')
ax1.axis('off')

# RIGHT: Why ice floats (density comparison)
phases = ['Ice\\n(0 deg C)', 'Water\\n(4 deg C)', 'Water\\n(100 deg C)']
densities = [0.917, 1.000, 0.958]  # g/cm^3
colors = ['lightblue', 'blue', 'red']

bars = ax2.bar(phases, densities, color=colors, edgecolor='black', linewidth=2)
ax2.axhline(y=1.0, color='green', linestyle='--', linewidth=2, 
           label='Water at 4 deg C (max density)', alpha=0.7)
ax2.set_ylabel('Density (g/cm³)', fontsize=12, weight='bold')
ax2.set_title('Ice is LESS Dense than Water!', fontsize=14, weight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim(0.9, 1.05)

# Annotate bars
for bar, d in zip(bars, densities):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height + 0.01,
            f'{d:.3f}', ha='center', va='bottom', fontsize=11, weight='bold')

plt.suptitle('Figure 1-4: Ice Structure and Density Anomaly', 
            fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("ICE: KEY PROPERTIES")
print("="*70)
print("\\n1. Hexagonal crystal structure (6-fold symmetry)")
print("2. Open lattice with holes -> LESS dense than water")
print("3. Ice floats (density = 0.917 g/cm³ vs water 1.000 g/cm³)")
print("4. Atoms vibrate in place (solid has heat too!)")
print("5. At absolute zero: Minimum vibration remains")
print("\\nWhy this matters:")
print("  -> Ice floating insulates lakes in winter")
print("  -> Life survives beneath frozen surface")
print("  -> Earth's climate depends on this anomaly!")
print("="*70)"""),

    # ABSOLUTE ZERO
    nbf.v4.new_markdown_cell("""## 🌡️ Absolute Zero and Quantum Effects

### 📖 Feynman's Text

> "Now although ice has a 'rigid' crystalline form, its temperature can change—**ice has heat**. If we wish, we can change the amount of heat. What is the heat in the case of ice?"

> "The atoms are not standing still. They are **jiggling and vibrating**. So even though there is a definite order to the crystal—a definite structure—all of the atoms are vibrating 'in place.'"

> "As we decrease the temperature, the vibration decreases and decreases until, **at absolute zero, there is a minimum amount of vibration that the atoms can have, but not zero.**"

### 🔍 Quantum Mechanical Minimum Motion

**Classical expectation:** At T = 0 K, everything stops moving

**Quantum reality:** **Zero-point energy** - atoms ALWAYS vibrate!

**Heisenberg Uncertainty Principle:**
\\[
\\Delta x \\cdot \\Delta p \\geq \\frac{\\hbar}{2}
\\]

- If \\(\\Delta x = 0\\) (perfectly localized), then \\(\\Delta p = \\infty\\) (infinite momentum uncertainty)
- Atoms MUST have some motion even at absolute zero!

**Helium exception:**
- Even at 0 K, helium stays LIQUID (at normal pressure)
- Zero-point motion is enough to keep it from freezing
- Must apply ~25 atm pressure to solidify helium

**This is purely quantum mechanical** - no classical explanation!

---"""),

    # SUMMARY
    nbf.v4.new_markdown_cell("""## 📊 Section 1-2 Summary & Takeaways

### 🎯 Main Points

1. **The Atomic Hypothesis** - THE one sentence with maximum information:
   - All things are made of atoms
   - In perpetual motion
   - Attract at distance, repel when squeezed

2. **Magnification journey** - Water drop to atomic scale:
   - 2,000× → Paramecia (biology)
   - 4,000,000× → "Teeming" motion
   - 1,000,000,000× → Individual H₂O molecules

3. **Liquid water** (Figure 1-1):
   - Molecules touching, jiggling
   - Attraction holds them together
   - Jiggling = HEAT

4. **Steam/gas** (Figure 1-2):
   - Molecules FAR apart (mostly empty!)
   - Pressure = molecular collisions with walls
   - P ∝ density, P ∝ temperature
   - Compression heats, expansion cools

5. **Ice/solid** (Figure 1-4):
   - Crystalline order (long-range structure)
   - Hexagonal symmetry → snowflakes
   - LESS dense than water (floats!)
   - Vibration even at absolute zero (quantum!)

### 🌉 Connections to Later Chapters

- **Ch 4-5:** Energy conservation (heat = kinetic energy of atoms)
- **Ch 39-40:** Kinetic theory of gases (formalized pressure/temperature)
- **Ch 41:** Brownian motion (direct evidence for atoms)
- **Ch 44:** Laws of thermodynamics (statistical behavior)
- **Ch 1 (Vol III):** Quantum mechanics (zero-point energy, uncertainty)

### ❓ Deep Questions for Reflection

1. **Historical:** How was the atomic hypothesis proven? (Einstein 1905, Perrin 1908)

2. **Philosophical:** If "heat is motion," what is temperature at absolute zero?

3. **Biological:** Why is ice floating crucial for life on Earth?

4. **Chemical:** How do chemical bonds form from "attracting when apart"?

5. **Quantum:** Why does Heisenberg uncertainty prevent absolute rest?

6. **Engineering:** How do diesel engines use compression heating?

### 💡 The Power of ONE Sentence

From "atoms in perpetual motion, attracting/repelling," we derived:

✅ States of matter (solid, liquid, gas)  
✅ Phase transitions (melting, boiling, freezing)  
✅ Pressure (collisions)  
✅ Temperature (kinetic energy)  
✅ Heat (atomic motion)  
✅ Thermal expansion  
✅ Compression/expansion effects  
✅ Crystal structure  
✅ Density anomalies (ice)  
✅ Quantum zero-point motion

**THIS is why Feynman calls it the MOST important scientific statement!**

---

## 🔜 What's Next?

**Section 1-3:** "Atomic Processes" - Chemical reactions, brownian motion, evaporation

**Section 1-4:** "Chemical Reactions" - Rearrangements of atoms in molecules

Ready to continue the atomic journey! 🚀

---

*"In that one sentence, you will see, there is an enormous amount of information about the world, if just a little imagination and thinking are applied."* — Richard Feynman""")
]

# Append new cells to notebook
nb.cells.extend(new_cells)

# Save updated notebook
with open("02-reading-notes-section-1-2.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("✅ Part 2 COMPLETE! Section 1-2 notebook is now finished.")
print(f"📍 Location: {target_dir}/02-reading-notes-section-1-2.ipynb")
print("\nWhat was added:")
print("  • Gas pressure from molecular collisions (Figure 1-3)")
print("  • Compression heating / expansion cooling")
print("  • Ice crystalline structure (Figure 1-4)")
print("  • Hexagonal symmetry explanation")
print("  • Density anomaly (why ice floats)")
print("  • Absolute zero and zero-point energy")
print("  • Complete summary with deep questions")
print("\n🎉 Section 1-2 is PRODUCTION-READY!")
print("\n📚 Next: Continue to Section 1-3, or work on other notebooks?")
