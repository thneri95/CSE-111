
"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W03 Project: Test Flow - Milestone
Author: Tiago Borges 
"""



def water_column_height(tower_height, tank_height):
    """Calcula a altura da coluna de água a partir da altura da torre e da parede do tanque."""
    return tower_height + (3/4) * tank_height

def pressure_gain_from_water_height(height):
    """Calcula a pressão gerada pela altura da coluna de água devido à gravidade terrestre."""
    water_density = 998.2  # kg/m³
    gravity = 9.80665  # m/s²
    return (water_density * gravity * height) / 1000  

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calcula a perda de pressão causada pelo atrito da água dentro do tubo."""
    water_density = 998.2  # kg/m³
    return - (friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
