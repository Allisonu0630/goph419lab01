# tests/tests.py
"""
#Run with: python -m tests.tests
"""

import numpy as np
import os
import sys


from goph419lab01 import functions



def approx_equal(a, b, tol=1e-6):
    return abs(a - b) <= tol


def test_launch_angle_range_case():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02

    # expected using numpy reference
    def expected_launch_angle(r, a):
        sin2 = (1.0 + a) * (1.0 + a * (1.0 - r * r))
        if sin2 < 0.0 or sin2 > 1.0:
            raise ValueError("no solution")
        return np.arcsin(np.sqrt(sin2))

    expected_min = expected_launch_angle(ve_v0, (1 + tol_alpha) * alpha)
    expected_max = expected_launch_angle(ve_v0, (1 - tol_alpha) * alpha)

    computed = functions.launch_angle_range(ve_v0, alpha, tol_alpha)
    comp_min, comp_max = computed

    print("Expected (rad):", expected_min, expected_max)
    print("Computed (rad):", comp_min, comp_max)
    print("Expected (deg):", np.degrees(expected_min), np.degrees(expected_max))
    print("Computed (deg):", np.degrees(comp_min), np.degrees(comp_max))

    if approx_equal(expected_min, comp_min) and approx_equal(expected_max, comp_max):
        print("TEST PASS: launch_angle_range matches numpy")
    else:
        print("TEST FAIL: differences exceed tolerance.")
        print("Delta min:", abs(expected_min - comp_min))
        print("Delta max:", abs(expected_max - comp_max))


def numpy_test_arcsin_sqrt():
    print("\n Testing sqrt(x) against NumPy ")
    xs = np.linspace(0.0, 2.5, 10)
    for x in xs:
        approx = functions.sqrt(x)
        truth = np.sqrt(x)
        error = abs(approx - truth)
        status = "PASS" if error <= 1e-8 else "FAIL"
        print(f"  sqrt({x:.4f}): approx={approx:.8f}, true={truth:.8f}, error={error:.2e} [{status}]")

    print("\n Testing arcsin(x) against NumPy ")
    ys = np.linspace(0.0, 1.0, 10)
    for y in ys:
        approx = functions.arcsin(y)
        truth = np.arcsin(y)
        error = abs(approx - truth)
        status = "PASS" if error <= 1e-8 else "FAIL"
        print(f"  arcsin({y:.4f}): approx={approx:.8f}, true={truth:.8f}, error={error:.2e} [{status}]")


if __name__ == "__main__":
    test_launch_angle_range_case()
    numpy_test_arcsin_sqrt()
