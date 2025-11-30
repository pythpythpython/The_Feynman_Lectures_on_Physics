#!/usr/bin/env python3
"""
Create COMPLETE reading notes for Section 1-3: Atomic Processes
Dynamic processes: evaporation, dissolution, equilibrium

Run from: volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion/
"""

import nbformat as nbf
from datetime import datetime
import os

target_dir = "/workspaces/The_Feynman_Lectures_on_Physics/volume-1-mechanics-radiation-heat/chapters/ch01-atoms-in-motion"
os.chdir(target_dir)

print("\n🔨 Creating COMPLETE Section 1-3 Reading Notes...")
print(f"📁 Working directory: {os.getcwd()}\n")

nb = nbf.v4.new_notebook()

nb.cells = [
    # TITLE
    nbf.v4.new_markdown_cell(f"""# Volume 1, Chapter 1 – Atoms in Motion
## Section 1-3: Atomic Processes

**Date Started:** {datetime.now().strftime("%B %d, %Y")}  
**Source:** [FLP Vol I, Ch 1, §1-3](https://www.feynmanlectures.caltech.edu/I_01.html#Ch1-S3)

---

## 🌟 Overview

Section 1-3 shifts from **static structures** (states of matter) to **dynamic processes**:

**Key Themes:**
1. Processes are always happening at the atomic level
2. Equilibrium = balanced opposing processes (not stillness!)
3. Evaporation as molecular escape
4. Dissolution as ion migration
5. Temperature affects process rates

**Central Insight:** What looks "dead" to our eyes is vibrant molecular chaos underneath!

---"""),

    # INTRO TO PROCESSES
    nbf.v4.new_markdown_cell("""## 🔄 From Structure to Process

### 📖 Feynman's Text

> "So much for the description of solids, liquids, and gases from the atomic point of view. However, the atomic hypothesis also **describes processes**, and so we shall now look at a number of processes from an atomic standpoint."

### 🔍 Shift in Perspective

**Section 1-2:** STATIC view
- What IS water/steam/ice?
- Structure at one moment in time

**Section 1-3:** DYNAMIC view
- What HAPPENS at surfaces?
- Processes unfolding over time
- Equilibrium as dynamic balance

**Key processes we'll explore:**
1. **Evaporation** - water escaping into air
2. **Dissolution** - salt breaking apart in water
3. **Equilibrium** - balanced rates in/out

---"""),

    # FIGURE 1-5: EVAPORATION
    nbf.v4.new_markdown_cell("""## 💨 Figure 1-5: Evaporation (Water in Air)

### 📖 Feynman's Text

> "What happens at the surface of the water? We shall now make the picture more complicated—and more realistic—by imagining that the surface is in air."

> "Above the surface we find a number of things: First of all there are **water molecules, as in steam**. This is water vapor, which is always found above liquid water."

### 🔍 The Surface: A Battleground

**Below surface (liquid water):**
- H₂O molecules packed tightly
- Jiggling continuously

**Above surface (air):**
- **Water vapor** (H₂O escaped from liquid)
- **Nitrogen** (N₂ molecules, ~78% of air)
- **Oxygen** (O₂ molecules, ~21% of air)
- **Other gases** (CO₂, Ar, etc.)

**At the surface:**
- Continuous molecular warfare!
- Some water molecules gain enough energy to escape
- Some vapor molecules collide and stick back

**The fundamental question:** Can you tell if this is evaporating or condensing just by looking at one moment?

**Answer:** NO! You need to compare RATES (molecules leaving vs. returning).

---"""),

    # CODE: EVAPORATION SIMULATION
    nbf.v4.new_code_cell("""# Simulate evaporation dynamics at water surface

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# LEFT: Water surface with air above
# Define regions
water_level = 5
ax1.axhline(y=water_level, color='blue', linewidth=3, alpha=0.3, 
           label='Water surface')
ax1.fill_between([0, 10], 0, water_level, color='lightblue', alpha=0.3)
ax1.text(5, 2.5, 'LIQUID\\nWATER', ha='center', va='center', 
        fontsize=14, weight='bold', color='blue')
ax1.text(5, 8, 'AIR\\n(+ water vapor)', ha='center', va='center',
        fontsize=14, weight='bold', color='gray')

# Water molecules in liquid (dense)
np.random.seed(42)
for _ in range(40):
    x = np.random.rand() * 10
    y = np.random.rand() * 4.5
    ax1.add_patch(Circle((x, y), 0.15, color='blue', alpha=0.6, zorder=2))

# Water molecules in vapor (sparse)
for _ in range(8):
    x = np.random.rand() * 10
    y = 5.5 + np.random.rand() * 4.5
    ax1.add_patch(Circle((x, y), 0.15, color='blue', alpha=0.4, zorder=2))

# Air molecules (N2, O2)
for _ in range(15):
    x = np.random.rand() * 10
    y = 5.5 + np.random.rand() * 4.5
    mol_type = np.random.choice(['N2', 'O2'])
    color = 'gray' if mol_type == 'N2' else 'red'
    ax1.add_patch(Circle((x, y), 0.12, color=color, alpha=0.5, zorder=2))

# Molecules escaping (arrows up)
escape_x = [2, 5, 8]
for ex in escape_x:
    ax1.arrow(ex, 4.5, 0, 0.8, head_width=0.2, head_length=0.15,
             fc='green', ec='green', linewidth=2.5, alpha=0.7, zorder=3)
    ax1.text(ex+0.3, 5, 'ESCAPE', fontsize=8, color='green', weight='bold')

# Molecules returning (arrows down)
return_x = [3.5, 6.5]
for rx in return_x:
    ax1.arrow(rx, 6, 0, -0.8, head_width=0.2, head_length=0.15,
             fc='orange', ec='orange', linewidth=2.5, alpha=0.7, zorder=3)
    ax1.text(rx+0.3, 6.5, 'RETURN', fontsize=8, color='orange', weight='bold')

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.set_title('Figure 1-5: Evaporation at Water Surface', fontsize=14, weight='bold')
ax1.axis('off')
ax1.legend(loc='upper right', fontsize=10)

# RIGHT: Rate comparison (equilibrium vs. evaporating)
conditions = ['Closed\\n(Equilibrium)', 'Open + Fan\\n(Evaporating)']
rate_escaping = [50, 50]  # Escaping rate stays same
rate_returning = [50, 10]  # Returning rate drops with fan

x_pos = np.arange(len(conditions))
width = 0.35

bars1 = ax2.bar(x_pos - width/2, rate_escaping, width, 
               label='Escaping', color='green', alpha=0.7, edgecolor='black', linewidth=2)
bars2 = ax2.bar(x_pos + width/2, rate_returning, width,
               label='Returning', color='orange', alpha=0.7, edgecolor='black', linewidth=2)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{int(height)}', ha='center', va='bottom', fontsize=11, weight='bold')

ax2.set_ylabel('Rate (molecules/sec)', fontsize=12, weight='bold')
ax2.set_title('Evaporation Rates: Equilibrium vs. Net Evaporation', 
             fontsize=14, weight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(conditions, fontsize=11)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim(0, 60)

# Annotate net effect
ax2.text(0, 55, 'Net = 0\\n(No change)', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
ax2.text(1, 55, 'Net = +40\\n(Evaporating!)', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.5))

plt.suptitle('Evaporation: Dynamic Molecular Process', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("EVAPORATION: KEY INSIGHTS")
print("="*70)
print("\\n1. Molecules ALWAYS escaping (depends on water jiggling)")
print("2. Molecules ALWAYS returning (depends on vapor density)")
print("3. Equilibrium: Rate out = Rate in (looks static, is dynamic!)")
print("4. Net evaporation: Rate out > Rate in (blow air away)")
print("5. Net condensation: Rate in > Rate out (humid air)")
print("\\n Checkmark: Evaporation is NOT molecules 'deciding to leave'")
print("   It is a STATISTICAL imbalance of random processes!")
print("="*70)"""),

    # EVAPORATIVE COOLING
    nbf.v4.new_markdown_cell("""## 🌡️ Evaporative Cooling: Why Blowing Cools Soup

### 📖 Feynman's Text

> "Which molecules leave? When a molecule leaves it is due to an **accidental, extra accumulation of a little bit more than ordinary energy**, which it needs if it is to break away from the attractions of its neighbors."

> "Therefore, since those that leave have **more energy than the average**, the ones that are left have **less average motion than they had before**. So the liquid **gradually cools** if it evaporates."

### 🔍 The Energy Selection Effect

**Escaping molecules:**
- Need EXTRA energy to overcome attraction
- Only the "hot" (fast-moving) ones escape
- This is statistical: occasional energy fluctuation

**Left-behind molecules:**
- Average energy DECREASES
- Temperature = average kinetic energy
- Result: **Liquid cools!**

**Returning molecules:**
- Fall into attractive potential well
- Speed up as they approach surface
- Crash in and **generate heat**

**Equilibrium:** Cooling from escapes = Heating from returns → No net temperature change

**Net evaporation:** More escaping (taking energy) → **Cooling!**

**Real-world examples:**
- Sweating cools you
- Blowing on soup cools it
- Wet skin feels cold in wind
- Dogs pant to cool down

---"""),

    # CODE: ENERGY DISTRIBUTION
    nbf.v4.new_code_cell("""# Visualize energy distribution and evaporative cooling

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import maxwell

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# LEFT: Maxwell-Boltzmann distribution with escape threshold
v = np.linspace(0, 5, 1000)
T = 300  # Kelvin
# Maxwell-Boltzmann distribution (simplified)
distribution = maxwell.pdf(v, scale=np.sqrt(T/100))

# Escape threshold (need extra energy)
v_escape = 3.5
escaping_fraction = distribution[v > v_escape]

ax1.plot(v, distribution, 'b-', linewidth=3, label='All molecules')
ax1.fill_between(v[v > v_escape], 0, distribution[v > v_escape],
                color='red', alpha=0.3, label='Can escape')
ax1.axvline(x=v_escape, color='red', linestyle='--', linewidth=2,
           label=f'Escape threshold')
ax1.axvline(x=np.average(v, weights=distribution), color='green',
           linestyle='--', linewidth=2, label='Average energy')

ax1.set_xlabel('Molecular Speed (arbitrary units)', fontsize=12, weight='bold')
ax1.set_ylabel('Number of Molecules', fontsize=12, weight='bold')
ax1.set_title('Energy Distribution: Who Can Escape?', fontsize=14, weight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Annotate
ax1.annotate('Only high-energy\\nmolecules escape!',
            xy=(4, distribution[int(0.8*len(v))]), xytext=(4.2, 0.3),
            fontsize=10, weight='bold', color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

# RIGHT: Temperature vs. time during evaporation
time = np.linspace(0, 100, 1000)
# Exponential cooling
T_initial = 350  # K (77 C, hot soup)
T_room = 293  # K (20 C)
tau = 30  # time constant
T_evap = T_room + (T_initial - T_room) * np.exp(-time/tau)

# Without evaporation (slower cooling)
tau_no_evap = 50
T_no_evap = T_room + (T_initial - T_room) * np.exp(-time/tau_no_evap)

ax2.plot(time, T_evap, 'b-', linewidth=3, label='With evaporation\\n(blowing on soup)')
ax2.plot(time, T_no_evap, 'r--', linewidth=3, label='Without evaporation\\n(covered)')
ax2.axhline(y=T_room, color='gray', linestyle=':', linewidth=2,
           label=f'Room temp ({T_room} K)', alpha=0.5)

ax2.set_xlabel('Time (seconds)', fontsize=12, weight='bold')
ax2.set_ylabel('Temperature (K)', fontsize=12, weight='bold')
ax2.set_title('Evaporative Cooling Over Time', fontsize=14, weight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(290, 360)

plt.suptitle('Why Blowing on Soup Cools It', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("EVAPORATIVE COOLING SUMMARY")
print("="*70)
print(f"\\nInitial soup temp: {T_initial} K ({T_initial-273:.0f} C)")
print(f"Room temperature: {T_room} K ({T_room-273:.0f} C)")
print(f"\\nWith evaporation (blowing): Cools to room temp in ~{tau*3:.0f} sec")
print(f"Without evaporation: Cools to room temp in ~{tau_no_evap*3:.0f} sec")
print(f"\\nSpeedup factor: {tau_no_evap/tau:.1f}x faster!")
print("\\n Checkmark: High-energy molecules leave -> Average energy drops -> Cooling!")
print("="*70)"""),

    # DISSOLUTION
    nbf.v4.new_markdown_cell("""## 🧂 Figure 1-6 & 1-7: Salt Dissolving in Water

### 📖 Feynman's Text

> "Now we go on to another process. In Fig. 1–6 we see, from an atomic point of view, a **solid dissolving in water**. If we put a crystal of salt in the water, what will happen?"

> "Salt is a solid, a crystal, an **organized arrangement** of 'salt atoms.'"

### 🔍 NaCl Crystal Structure (Figure 1-7)

**Not atoms, but IONS:**
- **Na⁺** (sodium ion) = sodium atom minus 1 electron
- **Cl⁻** (chlorine ion) = chlorine atom plus 1 electron

**Crystal structure:**
- Face-centered cubic lattice
- Alternating Na⁺ and Cl⁻
- Held together by **electrostatic attraction**
- Each Na⁺ surrounded by 6 Cl⁻ (and vice versa)

**Lattice parameter (a):**
- Rocksalt (NaCl): a = 5.64 Å
- Distance between nearest neighbors: d = a/2 = 2.82 Å

**Key insight:** There is NO "molecule of salt"!
- In the crystal, just an infinite array
- In solution, separate Na⁺ and Cl⁻ ions

---"""),

    # CODE: SALT CRYSTAL
    nbf.v4.new_code_cell("""# Visualize NaCl crystal structure and dissolution

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle

fig = plt.figure(figsize=(16, 7))

# LEFT: 3D crystal structure
ax1 = fig.add_subplot(121, projection='3d')

# Create NaCl lattice
a = 1.0  # Lattice parameter (normalized)
positions_Na = []
positions_Cl = []

# Simple cubic with alternating Na/Cl
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i + j + k) % 2 == 0:
                positions_Na.append([i*a, j*a, k*a])
            else:
                positions_Cl.append([i*a, j*a, k*a])

positions_Na = np.array(positions_Na)
positions_Cl = np.array(positions_Cl)

# Plot ions
ax1.scatter(positions_Na[:, 0], positions_Na[:, 1], positions_Na[:, 2],
           s=300, c='gold', edgecolors='black', linewidth=2, label='Na+', alpha=0.8)
ax1.scatter(positions_Cl[:, 0], positions_Cl[:, 1], positions_Cl[:, 2],
           s=400, c='lightgreen', edgecolors='black', linewidth=2, label='Cl-', alpha=0.8)

# Draw some bonds
for na in positions_Na:
    for cl in positions_Cl:
        dist = np.linalg.norm(na - cl)
        if np.isclose(dist, a, atol=0.1):  # Nearest neighbors
            ax1.plot([na[0], cl[0]], [na[1], cl[1]], [na[2], cl[2]],
                    'gray', linewidth=1, alpha=0.3)

ax1.set_xlabel('X', fontsize=11, weight='bold')
ax1.set_ylabel('Y', fontsize=11, weight='bold')
ax1.set_zlabel('Z', fontsize=11, weight='bold')
ax1.set_title('Figure 1-7: NaCl Crystal Structure', fontsize=14, weight='bold')
ax1.legend(fontsize=11, loc='upper left')

# RIGHT: Dissolution process
ax2 = fig.add_subplot(122)

# Draw water surface and crystal
crystal_y = 3
ax2.axhline(y=crystal_y, color='brown', linewidth=2, linestyle='--',
           label='Crystal surface', alpha=0.5)

# Solid crystal (bottom)
for i in range(5):
    for j in range(3):
        x = 1 + i * 0.6
        y = 0.5 + j * 0.6
        ion_type = (i + j) % 2
        color = 'gold' if ion_type == 0 else 'lightgreen'
        size = 250 if ion_type == 0 else 300
        ax2.scatter(x, y, s=size, c=color, edgecolor='black', linewidth=1.5, zorder=2)

# Ions escaping into water
escaping_positions = [(2.5, 3.5), (3.8, 4.2), (1.8, 4.5)]
for i, (ex, ey) in enumerate(escaping_positions):
    color = 'gold' if i % 2 == 0 else 'lightgreen'
    size = 250 if i % 2 == 0 else 300
    label_text = 'Na+' if i % 2 == 0 else 'Cl-'
    
    ax2.scatter(ex, ey, s=size, c=color, edgecolor='black', linewidth=1.5, zorder=3)
    ax2.arrow(ex-0.3, ey-0.5, 0, 0.4, head_width=0.15, head_length=0.1,
             fc='blue', ec='blue', linewidth=2, alpha=0.6)

# Water molecules (simplified)
for _ in range(15):
    wx = 0.5 + np.random.rand() * 4
    wy = 3.5 + np.random.rand() * 3
    ax2.scatter(wx, wy, s=80, c='lightblue', alpha=0.4, zorder=1)

ax2.text(2.5, 6.5, 'Water with dissolved ions', ha='center',
        fontsize=11, weight='bold',
        bbox=dict(boxstyle='round', facecolor='cyan', alpha=0.3))
ax2.text(2.5, 1.5, 'Solid NaCl crystal', ha='center',
        fontsize=11, weight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax2.set_xlim(0, 5)
ax2.set_ylim(0, 7)
ax2.set_aspect('equal')
ax2.set_title('Figure 1-6: Salt Dissolving in Water', fontsize=14, weight='bold')
ax2.axis('off')
ax2.legend(loc='upper right', fontsize=10)

plt.suptitle('NaCl Crystal Structure and Dissolution', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("SALT DISSOLUTION")
print("="*70)
print("\\nCrystal structure:")
print("  - Face-centered cubic (FCC)")
print("  - Lattice parameter a = 5.64 Angstroms")
print("  - Nearest neighbor distance d = a/2 = 2.82 Angstroms")
print("\\nDissolution process:")
print("  1. Water molecules approach crystal surface")
print("  2. H2O attracts ions electrically:")
print("     - O (negative) attracts Na+ (positive)")
print("     - H (positive) attracts Cl- (negative)")
print("  3. Ions jiggle loose from crystal")
print("  4. Ions become surrounded by water (hydration)")
print("\\n Checkmark: No 'salt molecule' exists - just Na+ and Cl- ions!")
print("="*70)"""),

    # EQUILIBRIUM CONCEPT
    nbf.v4.new_markdown_cell("""## ⚖️ Dynamic Equilibrium: Process, Not Stillness

### 📖 Feynman's Text

> "Can we tell from this picture whether the salt is **dissolving** in water or **crystallizing** out of water? Of course we **cannot tell**, because while some of the atoms are leaving the crystal other atoms are rejoining it."

> "The process is a **dynamic one**, just as in the case of evaporation, and it depends on whether there is **more or less salt in the water than the amount needed for equilibrium**."

### 🔍 Equilibrium ≠ Static

**Common misconception:** Equilibrium means "nothing happening"

**Reality:** Equilibrium means **balanced opposing processes**

**For dissolution:**
- Rate of ions leaving crystal
- = Rate of ions returning to crystal
- → No NET change (but continuous activity!)

**Three possible scenarios:**

| Scenario | Rate Out | Rate In | Result |
|----------|----------|---------|--------|
| **Unsaturated** | High | Low | Net dissolving |
| **Equilibrium** | Equal | Equal | No net change |
| **Supersaturated** | Low | High | Net crystallization |

**Temperature effect:**
- Increase T → Both rates increase
- Which increases MORE? **Hard to predict!**
- Most substances: dissolve more at higher T
- Some (e.g., calcium sulfate): dissolve LESS at higher T

**This is profound:** Equilibrium is NOT equilibrium of forces, but of **rates**!

---"""),

    # CODE: EQUILIBRIUM DYNAMICS
    nbf.v4.new_code_cell("""# Simulate dynamic equilibrium: dissolution vs. crystallization

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# LEFT: Time evolution to equilibrium
time = np.linspace(0, 100, 1000)

# Unsaturated -> Equilibrium
salt_unsaturated = 0 + 50 * (1 - np.exp(-time/20))

# Supersaturated -> Equilibrium
salt_supersaturated = 80 - 30 * (1 - np.exp(-time/20))

# Equilibrium line
equilibrium_conc = 50

ax1.plot(time, salt_unsaturated, 'b-', linewidth=3,
        label='Starting unsaturated (dissolving)')
ax1.plot(time, salt_supersaturated, 'r-', linewidth=3,
        label='Starting supersaturated (crystallizing)')
ax1.axhline(y=equilibrium_conc, color='green', linestyle='--', linewidth=2,
           label=f'Equilibrium ({equilibrium_conc} g/L)', alpha=0.7)

ax1.set_xlabel('Time (minutes)', fontsize=12, weight='bold')
ax1.set_ylabel('Salt Concentration (g/L)', fontsize=12, weight='bold')
ax1.set_title('Approaching Equilibrium from Both Sides', fontsize=14, weight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 100)

# Annotate
ax1.annotate('Net dissolving\\n(rate out > rate in)',
            xy=(20, 25), xytext=(30, 10),
            fontsize=9, color='blue', weight='bold',
            arrowprops=dict(arrowstyle='->', color='blue', lw=2),
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
ax1.annotate('Net crystallizing\\n(rate in > rate out)',
            xy=(20, 65), xytext=(30, 80),
            fontsize=9, color='red', weight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            bbox=dict(boxstyle='round', facecolor='pink', alpha=0.5))

# RIGHT: Rate comparison at different concentrations
concentrations = [10, 30, 50, 70, 90]  # g/L
# Rate out depends mostly on temperature (constant here)
rate_dissolving = [40, 40, 40, 40, 40]
# Rate in depends on concentration in solution
rate_crystallizing = [5, 20, 40, 60, 80]

ax2.plot(concentrations, rate_dissolving, 'b-o', linewidth=3, markersize=10,
        label='Rate dissolving (out of crystal)')
ax2.plot(concentrations, rate_crystallizing, 'r-s', linewidth=3, markersize=10,
        label='Rate crystallizing (into crystal)')

# Mark equilibrium
eq_idx = 2  # Where rates cross
ax2.plot(concentrations[eq_idx], rate_dissolving[eq_idx], 'g*',
        markersize=20, label='Equilibrium', zorder=5)

ax2.set_xlabel('Salt Concentration (g/L)', fontsize=12, weight='bold')
ax2.set_ylabel('Rate (ions/second)', fontsize=12, weight='bold')
ax2.set_title('Rates vs. Concentration', fontsize=14, weight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

# Shade regions
ax2.fill_between(concentrations[:eq_idx+1], 0, 100,
                color='blue', alpha=0.1, label='Dissolving region')
ax2.fill_between(concentrations[eq_idx:], 0, 100,
                color='red', alpha=0.1, label='Crystallizing region')

plt.suptitle('Dynamic Equilibrium: Balanced Rates, Continuous Activity', 
            fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

print("\\n" + "="*70)
print("DYNAMIC EQUILIBRIUM")
print("="*70)
print(f"\\nEquilibrium concentration: {equilibrium_conc} g/L")
print(f"\\nAt equilibrium:")
print(f"  Rate dissolving = {rate_dissolving[eq_idx]} ions/sec")
print(f"  Rate crystallizing = {rate_crystallizing[eq_idx]} ions/sec")
print(f"  Net change = 0 (but process continues!)")
print(f"\\nBelow equilibrium ({concentrations[0]} g/L):")
print(f"  Rate dissolving > Rate crystallizing -> Net dissolving")
print(f"\\nAbove equilibrium ({concentrations[-1]} g/L):")
print(f"  Rate crystallizing > Rate dissolving -> Net crystallizing")
print("\\n Checkmark: Equilibrium is DYNAMIC, not static!")
print("="*70)"""),

    # GAS DISSOLUTION
    nbf.v4.new_markdown_cell("""## 🫧 Air Dissolving in Water (The Diver's Problem)

### 📖 Feynman's Text

> "Not only does the water go into the air, but also, from time to time, one of the oxygen or nitrogen molecules will come in and 'get lost' in the mass of water molecules, and work its way into the water. **Thus the air dissolves in the water**; oxygen and nitrogen molecules will work their way into the water and the water will contain air."

> "If we suddenly take the air away from the vessel, then the air molecules will leave more rapidly than they come in, and in doing so will **make bubbles**. **This is very bad for divers**, as you may know."

### 🔍 The Bends (Decompression Sickness)

**Normal conditions:**
- Air pressure = 1 atm
- Some O₂ and N₂ dissolved in blood/tissues
- Equilibrium maintained

**Deep diving:**
- Water pressure increases (~1 atm per 10 meters depth)
- Diver breathes compressed air
- MORE O₂ and N₂ dissolve in blood (higher pressure!)

**Rapid ascent (BAD!):**
- Pressure drops quickly
- Dissolved gases suddenly SUPERSATURATED
- Can't escape fast enough → **Form bubbles IN blood/tissues**
- Bubbles block blood vessels → Pain, paralysis, death!

**Safe ascent:**
- Rise slowly
- Allow gases to diffuse out through lungs
- No bubble formation

**Modern solution:** Decompression stops (pause at depths to let gas escape)

---"""),

    # SUMMARY
    nbf.v4.new_markdown_cell("""## 📊 Section 1-3 Summary & Takeaways

### 🎯 Main Points

1. **Processes, not just structures**
   - Atomic view explains HOW things happen
   - Everything is dynamic at molecular level

2. **Evaporation** (Figure 1-5):
   - Molecules escape when they gain extra energy
   - Equilibrium: rate out = rate in
   - Net evaporation: blow away vapor
   - Evaporative cooling: high-energy molecules leave

3. **Dissolution** (Figures 1-6, 1-7):
   - NaCl crystal: alternating Na⁺ and Cl⁻ ions
   - Water pulls ions away (electrical attraction)
   - No "salt molecule" in crystal
   - Equilibrium: dissolving rate = crystallizing rate

4. **Dynamic equilibrium**:
   - NOT stillness, but balanced opposing rates
   - Can approach from either direction
   - Temperature affects both rates

5. **Air in water**:
   - O₂ and N₂ dissolve under pressure
   - Rapid decompression → bubbles (the bends!)
   - Divers must ascend slowly

### 🌉 Connections to Later Chapters

- **Ch 5:** Energy conservation in phase transitions
- **Ch 40:** Statistical mechanics of evaporation
- **Ch 41:** Diffusion and random walks
- **Ch 44:** Chemical equilibrium and Le Chatelier
- **Ch 52 (Vol II):** Electrostatics and ionic bonding

### ❓ Deep Questions for Reflection

1. **Thermodynamic:** Why does evaporative cooling work? (Energy distribution)

2. **Statistical:** What determines escape threshold? (Binding energy vs. kT)

3. **Chemical:** Why do some salts dissolve less at higher temperature?

4. **Medical:** How do hyperbaric chambers treat the bends?

5. **Everyday:** Why does a fan cool you even if air temperature = body temperature?

6. **Philosophical:** Is "equilibrium" ever truly static in nature?

### 💡 Feynman's Core Message

> **"What looks like a dead, uninteresting thing...really contains a dynamic and interesting phenomenon which is going on all the time."**

**Nothing is truly static.** At the molecular level, everything is perpetual motion, continuous exchange, dynamic balance.

---

## 🔜 What's Next?

**Section 1-4:** Chemical Reactions - Atoms rearranging into new molecules

Ready to see atoms NOT just moving, but **transforming**! 🚀

---

*"To our eyes, our crude eyes, nothing is changing, but if we could see it a billion times magnified, we would see that from its own point of view it is always changing."* — Richard Feynman""")
]

# Save notebook
with open("03-reading-notes-section-1-3.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("✅ Section 1-3 COMPLETE!")
print(f"📍 Location: {target_dir}/03-reading-notes-section-1-3.ipynb")
print("\nWhat was created:")
print("  • Dynamic processes (evaporation, dissolution)")
print("  • Evaporative cooling mechanism")
print("  • NaCl crystal structure visualization")
print("  • Dynamic equilibrium concept")
print("  • The bends (decompression sickness)")
print("  • Complete summary with connections")
print("\n🎉 Ready to study! Run all cells to see visualizations.")
print("\n📚 Next: Section 1-4 (Chemical Reactions)?")
