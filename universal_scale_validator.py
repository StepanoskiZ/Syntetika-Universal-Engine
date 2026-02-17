import math


# ==============================================================================
# S-OS: UNIVERSAL SCALE VALIDATOR
# Author: Zoran Stepanoski
# Part of the Synthetics (Logic 0.5) Framework
# ==============================================================================

class UniversalValidator:
    def __init__(self):
        self.G = 6.67430e-11  # Gravitational Constant
        self.S = 8.74e-10  # THE STEPANOSKI CONSTANT

    def analyze_entity(self, name, mass_kg, radius_m, category):
        print(f"\n--- ANALYZING: {name} ({category}) ---")

        # Calculate Newtonian Acceleration (a_g)
        if radius_m > 0:
            a_newton = (self.G * mass_kg) / (radius_m ** 2)
        else:
            a_newton = 0

        # Ratio of Universal Logic (S) to Gravity (a_g)
        if a_newton == 0:
            ratio = float('inf')
        else:
            ratio = self.S / a_newton

        print(f"  Newtonian Gravity (a_g): {a_newton:.4e} m/s^2")
        print(f"  Stepanoski Logic (S):    {self.S:.4e} m/s^2")

        # S-OS Logic Diagnosis
        if ratio > 1000:
            print("  >> DOMAIN: QUANTUM / BIOLOGICAL")
            print("  >> DIAGNOSIS: S >> a_g. Information/Logic (0.5) dominates physical form.")
        elif ratio < 0.01:
            print("  >> DOMAIN: NEWTONIAN REALITY (1.0)")
            print("  >> DIAGNOSIS: a_g >> S. Physical mass enforces absolute certainty.")
        else:
            print("  >> DOMAIN: THE GREY ZONE (TRANSITIONAL)")
            print("  >> DIAGNOSIS: a_g and S are in conflict. High capacity for emergent complexity.")


if __name__ == "__main__":
    validator = UniversalValidator()
    print("===============================================================")
    print("   S T E P A N O S K I   U N I V E R S A L   V A L I D A T O R ")
    print("===============================================================")

    # Test cases representing the full range of the Universe
    validator.analyze_entity("HIV Virus", 1e-18, 60e-9, "Micro")
    validator.analyze_entity("Human Being", 70, 1.0, "Macro")
    validator.analyze_entity("Planet Earth", 5.97e24, 6.371e6, "Planetary")

    # The Cosmic Proof: Coma Galaxy Cluster
    mass_coma = 1e15 * 1.989e30
    radius_coma = 10 * 3.086e22
    validator.analyze_entity("Coma Galaxy Cluster", mass_coma, radius_coma, "Cosmic")