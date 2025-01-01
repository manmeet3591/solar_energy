# Using the paper: https://iopscience.iop.org/article/10.1088/1748-9326/ac5a67#erlac5a67s2

import numpy as np

# Constants
B = 1.0  # Efficiency coefficient (area * efficiency of solar panels & inverter)
T_ref = 25.0  # Reference temperature in °C
alpha = -0.004  # Temperature coefficient of power (%/°C)

# Function to compute temperature-dependent efficiency reduction factor
def temperature_efficiency(T, T_ref=T_ref, alpha=alpha):
    """
    Compute temperature efficiency reduction factor.
    """
    return 1 + alpha * (T - T_ref)

# Function to compute PV power
def compute_pv_power(irradiance, temperature, B=B, T_ref=T_ref, alpha=alpha):
    """
    Calculate solar PV power output.

    Parameters:
    irradiance: float or np.array
        Surface irradiance (W/m^2).
    temperature: float or np.array
        Ambient temperature (°C).
    B: float
        Baseline efficiency coefficient.
    T_ref: float
        Reference temperature in °C.
    alpha: float
        Temperature coefficient of power (%/°C).

    Returns:
    pv_power: float or np.array
        Computed solar PV power (kW for a 1kW peak system).
    """
    # Compute temperature efficiency factor
    efficiency_factor = temperature_efficiency(temperature, T_ref, alpha)
    
    # Calculate PV power
    pv_power = B * irradiance * efficiency_factor
    return pv_power

# Example usage
if __name__ == "__main__":
    # Example data
    irradiance_values = np.array([500, 800, 1000, 200])  # in W/m^2
    temperature_values = np.array([20, 25, 30, 35])  # in °C

    # Compute PV power
    pv_power_output = compute_pv_power(irradiance_values, temperature_values)
    
    # Print results
    print("Irradiance (W/m^2):", irradiance_values)
    print("Temperature (°C):", temperature_values)
    print("PV Power Output (kW):", pv_power_output)
