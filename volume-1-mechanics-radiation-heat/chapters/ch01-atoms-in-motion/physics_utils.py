"""
Physics utilities for Feynman Lectures studies
Created: November 19, 2025
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
