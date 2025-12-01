#!/usr/bin/env python3
"""
SCAFFOLD VOLUME 3: QUANTUM MECHANICS
Creates the directory structure and notebooks for ALL 21 Chapters of Volume 3.
"""

import nbformat as nbf
import os
import re

# -----------------------------------------------------------------------------
# 1. DATA: The Full Table of Contents for Volume 3
# -----------------------------------------------------------------------------
toc_data_vol3 = {
    1: ("Quantum Behavior", [
        "Atomic mechanics", "An experiment with bullets", "An experiment with waves", "An experiment with electrons", "The interference of electron waves", "Watching the electrons", "First principles of quantum mechanics", "The uncertainty principle"
    ]),
    2: ("The Relation of Wave and Particle Viewpoints", [
        "Probability wave amplitudes", "Measurement of position and momentum", "Crystal diffraction", "The size of an atom", "Energy levels", "Philosophical implications"
    ]),
    3: ("Probability Amplitudes", [
        "The laws for combining amplitudes", "The two-slit interference pattern", "Scattering from a crystal", "Identical particles"
    ]),
    4: ("Identical Particles", [
        "Bose particles and Fermi particles", "States with two Bose particles", "States with n Bose particles", "Emission and absorption of photons", "The blackbody spectrum", "Liquid helium", "The exclusion principle"
    ]),
    5: ("Spin One", [
        "Filtering atoms with a Stern-Gerlach apparatus", "Experiments with filtered atoms", "Stern-Gerlach filters in series", "Base states", "Interfering amplitudes", "The machinery of quantum mechanics", "Transforming to a different base", "Other situations"
    ]),
    6: ("Spin One-Half", [
        "Transforming amplitudes", "Transforming to a rotated coordinate system", "Rotations about the z-axis", "Rotations of 180 degrees and 90 degrees about y", "Rotations about x", "Arbitrary rotations"
    ]),
    7: ("The Dependence of Amplitudes on Time", [
        "Atoms at rest; stationary states", "Uniform motion", "Potential energy; energy conservation", "Forces; the classical limit", "The precession of a spin one-half particle"
    ]),
    8: ("The Hamiltonian Matrix", [
        "Amplitudes and vectors", "Resolving state vectors", "What are the base states of the world?", "How states change with time", "The Hamiltonian matrix", "The ammonia molecule"
    ]),
    9: ("The Ammonia Maser", [
        "The states of an ammonia molecule", "The molecule in a static electric field", "Transitions in a time-dependent field", "Transitions at resonance", "Transitions off resonance", "The absorption of light"
    ]),
    10: ("Other Two-State Systems", [
        "The hydrogen molecular ion", "Nuclear forces", "The hydrogen molecule", "The benzene molecule", "Dyes", "The Hamiltonian of a spin one-half particle in a magnetic field", "The spinning electron in a magnetic field"
    ]),
    11: ("More Two-State Systems", [
        "The Pauli spin matrices", "The spin matrices as operators", "The solution of the two-state equations", "The polarization states of the photon", "The neutral K-meson", "Generalization to N-state systems"
    ]),
    12: ("The Hyperfine Splitting in Hydrogen", [
        "Base states for a system with two spin one-half particles", "The Hamiltonian for the ground state of hydrogen", "The energy levels", "The Zeeman splitting", "The states in a magnetic field", "The projection matrix for spin one"
    ]),
    13: ("Propagation in a Crystal Lattice", [
        "States for an electron in a one-dimensional lattice", "States of definite energy", "Time-dependent states", "An electron in a three-dimensional lattice", "Other states in a lattice", "Scattering from imperfections in the lattice", "Trapping by a lattice imperfection", "Scattering amplitudes and bound states"
    ]),
    14: ("Semiconductors", [
        "Electrons and holes in semiconductors", "Impure semiconductors", "The Hall effect", "Semiconductor junctions", "Rectification at a semiconductor junction", "The transistor"
    ]),
    15: ("The Independent Particle Approximation", [
        "Spin waves", "Two spin waves", "Independent particles", "The benzene molecule", "More organic chemistry", "Other uses of the approximation"
    ]),
    16: ("The Dependence of Amplitudes on Position", [
        "Amplitudes on a line", "The wave function", "States of definite momentum", "Normalization of the states in x", "The Schrödinger equation", "Quantized energy levels"
    ]),
    17: ("Symmetry and Conservation Laws", [
        "Symmetry", "Symmetry and conservation", "The conservation laws", "Polarized light", "The disintegration of the Λ0", "Summary of the rotation matrices"
    ]),
    18: ("Angular Momentum", [
        "Electric dipole radiation", "Light scattering", "The annihilation of positronium", "Rotation matrix for any spin", "Measuring a nuclear spin", "Composition of angular momentum"
    ]),
    19: ("The Hydrogen Atom and The Periodic Table", [
        "Schrödinger’s equation for the hydrogen atom", "Spherically symmetric solutions", "States with an angular dependence", "The general solution for hydrogen", "The hydrogen wave functions", "The periodic table"
    ]),
    20: ("Operators", [
        "Operations and operators", "Average energies", "The average energy of an atom", "The position operator", "The momentum operator", "Angular momentum", "The change of averages with time"
    ]),
    21: ("The Schrödinger Equation in a Classical Context: A Seminar on Superconductivity", [
        "Schrödinger’s equation in a magnetic field", "The equation of continuity for probabilities", "Two kinds of momentum", "The meaning of the wave function", "Superconductivity", "The Meissner effect", "Flux quantization", "The dynamics of superconductivity", "The Josephson junction"
    ])
}

# -----------------------------------------------------------------------------
# 2. HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def create_notebook(path, title, content_md):
    nb = nbf.v4.new_notebook()
    nb.cells = [nbf.v4.new_markdown_cell(f"# {title}\n\n{content_md}")]
    with open(path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

def clean_filename(text):
    # Remove special chars and replace spaces with underscores
    s = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', s)

# Set base path to Volume 3 folder
base_path = "/workspaces/The_Feynman_Lectures_on_Physics/volume-3-quantum-mechanics/chapters"

# -----------------------------------------------------------------------------
# 3. EXECUTION LOOP
# -----------------------------------------------------------------------------
print(f"🚀 Starting Scaffolding for Volume 3 (Chapters 1-21) in: {base_path}")

if not os.path.exists(base_path):
    try:
        os.makedirs(base_path)
        print(f"📁 Created Base Directory: {base_path}")
    except FileNotFoundError:
        # Fallback to current directory if workspace path doesn't exist
        base_path = "./volume-3-quantum-mechanics/chapters"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        print(f"⚠️ Base path adjusted to: {base_path}")

for ch_num, (ch_title, sections) in toc_data_vol3.items():
    
    # A. Create Directory
    slug = clean_filename(ch_title)
    dir_name = f"ch{ch_num:02d}-{slug}"
    full_dir_path = os.path.join(base_path, dir_name)
    
    if not os.path.exists(full_dir_path):
        os.makedirs(full_dir_path)
        print(f"📁 Created: {dir_name}")
    else:
        print(f"📂 Exists: {dir_name}")
        
    # B. Create Section Notebooks
    for idx, sec_title in enumerate(sections, 1):
        sec_filename = f"Section_{ch_num}-{idx}_{sec_title.replace(' ', '_')}.ipynb"
        # Remove potential invalid chars from filename
        sec_filename = re.sub(r'[^\w\.-]', '', sec_filename) 
        
        sec_path = os.path.join(full_dir_path, sec_filename)
        
        if not os.path.exists(sec_path):
            create_notebook(
                sec_path, 
                f"Section {ch_num}-{idx}: {sec_title}", 
                f"**Reading Notes** for Volume 3, Chapter {ch_num}, Section {idx}.\n\n> Insert key takeaways and equations here."
            )

    # C. Create Standard Activity Files
    
    # 1. Master Dashboard
    dash_path = os.path.join(full_dir_path, "Overview_Master_Dashboard.ipynb")
    if not os.path.exists(dash_path):
        create_notebook(
            dash_path,
            f"🗺️ Vol 3 Chapter {ch_num} Master Overview: {ch_title}",
            "## The Command Center\n\nUse this notebook to navigate your reading notes, exercises, and logs."
        )

    # 2. QA Journal
    log_path = os.path.join(full_dir_path, "Log_AI_QA_Journal.ipynb")
    if not os.path.exists(log_path):
        create_notebook(
            log_path,
            f"📓 AI Learning Journal: {ch_title}",
            "## A Socratic Dialogue\n\nRecord your questions and AI insights here."
        )

    # 3. Flashcards
    flash_path = os.path.join(full_dir_path, "Activity_Flashcards.ipynb")
    if not os.path.exists(flash_path):
        create_notebook(
            flash_path,
            f"🧠 Flashcards: {ch_title}",
            "*(Placeholder)* Interactive flashcards will be generated here."
        )

    # 4. Exercise Bank
    ex_path = os.path.join(full_dir_path, "Activity_Exercise_Bank.ipynb")
    if not os.path.exists(ex_path):
        create_notebook(
            ex_path,
            f"🏋️ Exercise Bank: {ch_title}",
            "## Problems & Solutions\n\nTest your understanding of the chapter concepts here."
        )

print("\n⚛️ VOLUME 3 SCAFFOLDING COMPLETE! Quantum Mechanics awaits.")
