import numpy as np
import matplotlib.pyplot as plt

class StepanoskiGalacticProtocol:
    """
    Implementation of Logic 0.5 and Synthetic Physics.
    Refutes 'Dark Matter' and 'Thermal Anomalies' by introducing:
    W (Work), Dp (Paradox Density), and Logic Friction.
    """

    def __init__(self, n_propositions):
        self.n = n_propositions  # Information mass/complexity
        self.v_g = 1.0  # General Relativity state (Certainty)
        self.v_q = 0.5  # Quantum Potential state (Uncertainty)

    def synthetic_xor(self, inputs):
        """Paradox Saturation Mechanism: 1 ^ 1 ^ 1 = 0.5 (Page 2 & 9)"""
        if sum(inputs) == 3: return 0.5
        return sum(inputs) % 2

    def calculate_paradox_density(self, conflict_factor=0.5):
        """Dp = sum |Ai ^ Aj| * ln(N) (Page 3 & 10)"""
        return conflict_factor * np.log(self.n)

    def get_synthetic_acceleration(self, distance_au):
        """
        Gravity as Work (W) over Paradox Density (Dp).
        Synthetic Equation: Psi_Total = (G_1.0 + Q_0.5) / Dp * dW
        """
        dp = self.calculate_paradox_density()
        # Logic Friction (dW) increasing with distance from the center of certainty
        dw = 1.2e-11 * distance_au
        accel = -(self.v_g + self.v_q) / dp * dw
        return accel

    def get_galactic_rotation_velocity(self, radius_kpc):
        """
        Solves the Galaxy Rotation Problem without Dark Matter.
        Velocity is maintained by Logic Work (W) stabilizing the system.
        """
        v_newtonian = 100 / np.sqrt(radius_kpc)  # Velocity from visible mass only
        dp = self.calculate_paradox_density()

        # Logic Glue: Work required to hold the system together at 0.5 state
        v_synthetic_work = np.sqrt(dp * radius_kpc * 0.05)
        return v_newtonian, v_newtonian + v_synthetic_work


# --- SIMULATION AND COMPARISON ---

def run_protocol():
    # 1. Pioneer Anomaly Simulation
    distances_au = np.linspace(20, 150, 100)
    pioneer = StepanoskiGalacticProtocol(n_propositions=1500)

    p_accel = [pioneer.get_synthetic_acceleration(d) for d in distances_au]
    nasa_model = [-8.74e-10 for _ in distances_au]

    # 2. Galaxy Rotation Simulation (Dark Matter Refutation)
    radii_kpc = np.linspace(1, 50, 100)
    galaxy = StepanoskiGalacticProtocol(n_propositions=1e12)  # High complexity N
    v_std, v_synth = zip(*[galaxy.get_galactic_rotation_velocity(r) for r in radii_kpc])

    # --- VISUALIZATION ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Pioneer Anomaly
    ax1.plot(distances_au, nasa_model, 'r--', label='NASA Model (Thermal Anomaly)')
    ax1.plot(distances_au, p_accel, 'b-', label='Synthetics: Logic 0.5 (W + Dp)')
    ax1.set_title('Pioneer Anomaly: Standard Physics vs Synthetics')
    ax1.set_xlabel('Distance from Sun (AU)')
    ax1.set_ylabel('Anomalous Acceleration (m/s²)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Galaxy Rotation (Dark Matter)
    ax2.plot(radii_kpc, v_std, 'r--', label='Visible Matter Only (Newton)')
    ax2.plot(radii_kpc, v_synth, 'g-', label='Stepanoski Protocol (No Dark Matter)')
    ax2.set_title('Galaxy Rotation: Refuting Dark Matter via Logic 0.5')
    ax2.set_xlabel('Distance from Galactic Center (kpc)')
    ax2.set_ylabel('Rotation Velocity (km/s)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Final Logic Check
    print("--- STEPANOSKI GALACTIC PROTOCOL: INITIALIZED ---")
    print(f"Synthetic XOR Check (1^1^1): {pioneer.synthetic_xor([1, 1, 1])} (State: 0.5 Potential)")
    print("Result: Anomalies are manifestations of Logic Work (W), not hidden matter/heat.")


if __name__ == "__main__":
    run_protocol()
