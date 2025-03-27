"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W03 Project: - Test Water Pressure Final
Author: Tiago Borges  
"""

import pytest
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == pytest.approx(0.000, rel=1e-2)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0.000, rel=1e-2)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, rel=1e-2)
    assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, rel=1e-2)
    assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, rel=1e-2)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == 0
    assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, rel=1e-3)
    assert reynolds_number(0.048692, 1.75) == pytest.approx(84922, rel=1e-3)
    assert reynolds_number(0.286870, 1.65) == pytest.approx(471729, rel=1e-3)
    assert reynolds_number(0.286870, 1.75) == pytest.approx(500318, rel=1e-3)

    
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if reynolds_number == 0:  # Avoid division by zero
        return 0.0  
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return k


def test_kPa_to_psi():
    assert kPa_to_psi(0.0) == pytest.approx(0.0, rel=1e-3)
    assert kPa_to_psi(1.0) == pytest.approx(0.1450377, rel=1e-3)
    assert kPa_to_psi(100.0) == pytest.approx(14.50377, rel=1e-3)
    assert kPa_to_psi(158.7) == pytest.approx(23.0390389, rel=1e-3)
    assert kPa_to_psi(1000.0) == pytest.approx(145.0377, rel=1e-3)

if __name__ == "__main__":
    pytest.main()
