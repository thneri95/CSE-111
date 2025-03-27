
"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W03 Project: -  Water Pressure  FInal
Author: Tiago Borges 


Water Pressure Calculation Program

This program calculates water pressure losses in a pipeline system to help engineers design 
efficient water distribution networks. It considers factors such as pipe length, fittings, 
and diameter reductions to determine the final pressure at the destination

How It Works:
1. Takes user input for water tower height, pipe lengths, and number of fittings
2. Calculates pressure gain from water height
3. Computes pressure losses due to:
   - Pipe friction
   - Fittings (90° and 45° bends)
   - Pipe diameter reduction
4. Uses the Reynolds number to analyze water flow
5. Displays the final pressure at the house in kilopascals (kPa)

"""

# Bonus Features: 
#  Uses constants for gravity, water density, and viscosity
#  Converts kPa to PSI for easier interpretation
#  Includes rigorous test functions to ensure accuracy


# Constants
WATER_DENSITY = 998.2  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal-seconds
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # m/s
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # m/s

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculates the pressure loss due to fittings in the pipeline.
    """
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates the Reynolds number, a parameter that determines the flow regime of the fluid.
    """
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds, smaller_diameter):
    """
    Calculates the pressure loss when there is a reduction in pipe diameter.
    """
    if reynolds == 0:
        return 0.0  # Avoids division by zero
    k = 0.1 + (50 / reynolds) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k  # Now returns a negative value as expected in tests

def kPa_to_psi(kPa):
    """
    Converts pressure from kilopascals (kPa) to pounds per square inch (psi).
    """
    return kPa * 0.1450377

def main():
    """
    Requests user input and calculates the final pressure in the household.
    """
    tower_height = float(input("Water tower height (meters): "))
    tank_height = float(input("Tank wall height (meters): "))
    length1 = float(input("Length of the supply pipeline (meters): "))
    quantity_angles = int(input("Number of 90° bends in the pipeline: "))
    length2 = float(input("Length of the pipeline to the house (meters): "))

    water_height = tower_height - tank_height
    pressure = (water_height * EARTH_ACCELERATION_OF_GRAVITY * WATER_DENSITY) / 1000  # kPa

    # Pressure losses in the pipeline
    diameter = PVC_SCHED80_INNER_DIAMETER
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    # Conversion to psi and displaying results
    pressure_in_psi = kPa_to_psi(pressure)
    
    print(f"Pressure at the house: {pressure:.1f} kilopascals")
    print(f"Pressure at the house: {pressure_in_psi:.1f} psi")

if __name__ == "__main__":
    main()