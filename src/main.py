import numpy as np
import matplotlib.pyplot as plt


# Function to calculate the electric charge based on the angle
def calculate_charge(theta):
    epsilon = 8.85e-12  # Vacuum permittivity (F/m)
    g = 9.81  # Gravitational acceleration (m/s²)
    length = 0.03  # Length of the foil (m)
    density = 0.027  # Aluminum density (kg/cm³)
    volume = 1.4 * 3.0 * 0.0018  # Leaf volume (cm³)
    mass = density * volume  # Mass of the foil (kg)

    return np.sqrt(16 * np.pi * epsilon * length ** 2 * mass * g * np.sin(theta) ** 2 * np.tan(theta))


# Arrays to store experimental data (to be populated later)
times = np.array([4.01, 5.5, 8.0, 12.69, 15.53, 20.10, 25.69, 33.51, 50.82, 60.94])  # Rubbing times in seconds
angles_between_leafs = np.array(
    [52.0, 30.18, 48.10, 50.45, 29.31, 50.19, 57.46, 44.20, 58.28, 50.24])  # Angles in degrees
angles_radians = np.radians(angles_between_leafs)  # Convert to radians
angles = (1 / 2) * angles_radians  # Theta

# Calculate charges based on angles
charges = calculate_charge(angles)
print(charges)

# --- Graphic 2: Electric charge vs Time ---
plt.figure(figsize=(10, 6))
plt.plot(times, charges, '--', color='green', label='Theoretical charge')
plt.scatter(times, charges, color='black', marker='o', label='Experimental points')
plt.xlabel('Rubbing time (s)')
plt.ylabel('Charge (C)')
plt.title('Electric charge vs Rubbing time')
plt.grid(alpha=0.5)
plt.legend()
# path1 = "C:\\Users\\yannk\\PycharmProjects\\electroscopeExperiment\\src\\assets\\Electric_Charge_vs_Time.png"
# plt.savefig(path1, dpi=300, format='png')
plt.show()

charges.sort()
angles.sort()

# --- Graphic 2: Electric charge vs Angle ---
plt.figure(figsize=(10, 6))
plt.plot(angles, charges, '--', color='blue', label='Theoretical charge')
plt.scatter(angles, charges, color='black', marker='o', label='Experimental points')
plt.xlabel('Angle (rad)')
plt.ylabel('Charge (C)')
plt.title('Electric charge vs Angle')
plt.grid(alpha=0.5)
plt.legend()
# path2 = "C:\\Users\\yannk\\PycharmProjects\\electroscopeExperiment\\src\\assets\\ElectricCharge_vs_Angle.png"
# plt.savefig(path2, dpi=300, format='png')
plt.show()
