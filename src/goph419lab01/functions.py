# src/goph419lab01/functions.py
"""
GOPH419 Lab 1:
 - sqrt(x): get positive square root for 0.0 <= x <= 2.5 using Taylor series
 - arcsin(x): arcsin for 0.0 <= x <= 1.0 
 - launch_angle(ve_v0, alpha)
 - launch_angle_range(ve_v0, alpha, tol_alpha)
"""

from __future__ import annotations
import math
from typing import Tuple
import numpy as np

# ---------------------------------------------------------------------------
# 1: Implement sqrt(x) using Taylor expansion
# ---------------------------------------------------------------------------

def sqrt(x):
    """
    Calculate square root of a real positive number
    between 0.0 and 2.5 using a series expansion.

    Parameters
    ----------
    x : float
        Input value (0.0 <= x <= 2.5).

    Returns
    -------
    float
        Approximation of sqrt(x).

    Raises
    ------
    ValueError
        If x is outside the domain.
    """
    if not (0.0 <= x <= 2.5):
        raise ValueError("Input must be between 0.0 and 2.5")

    if x == 0.0:
        return 0.0

    base_points = [0.5, 1.0, 1.5, 2.0]
    a = min(base_points, key=lambda b: abs(b - x))
    sqrt_a = math.sqrt(a)
    h = x - a

    # series variables:
    k = 0
    fact_k = 1.0
    prod_k = 1.0
    coef_k = 1.0
    term_k = sqrt_a
    sum_k = term_k

    while True:
        k += 1
        fact_k *= k                           # factorial term
        prod_k *= (0.5 - (k - 1))             # product term
        coef_k = prod_k / fact_k / (a**k)     # coefficient
        term_k = coef_k * (h**k) * sqrt_a
        new_sum = sum_k + term_k

        # convergence (8 sig digs)
        if abs(new_sum - sum_k) < 1e-8:
            break
        sum_k = new_sum

    return sum_k

# ---------------------------------------------------------------------------
# 2: arcsin(x) 
# ---------------------------------------------------------------------------
def arcsin(x, tol=1e-10, max_iter=1000):
    """
    Calculating arcsin(x) for real positive numbers between 0.0 and 1.0

    Parameters
    ----------
    x : float
        Input value (0.0 <= x <= 1.0).

    Returns
    -------
    float
        Approximation of arcsin(x).

    Raises
    ------
    ValueError
        If x isn't in domain.
    """
    if not (0.0 <= x <= 1.0):
        raise ValueError("x must be in [0, 1]")

    if x == 0.0:
        return 0.0
    if x == 1.0:
        return math.pi / 2

    sum_sq = 0.0
    n = 1

    while n <= max_iter:
        numerator = (2 * x) ** (2 * n)
        denominator = n**2 * (math.factorial(2 * n) / (math.factorial(n) ** 2))
        term = numerator / denominator
        sum_sq_new = sum_sq + term

        if abs(term) < tol:
            break

        sum_sq = sum_sq_new
        n += 1

    return math.sqrt(0.5 * sum_sq)

# ---------------------------------------------------------------------------
# 3: launch_angle(ve_v0, alpha)
# ---------------------------------------------------------------------------
def launch_angle(ve_v0: float, alpha: float) -> float:
    """
    Compute the launch angle (rad) with ve/v0 and alpha.
    Formula: sin^2(phi0) = (1 + alpha) * (1 + alpha*(1 - (ve/v0)^2))
      phi0 = arcsin( sqrt(sin^2(phi0)) )
    """
    if alpha < 0.0:
        raise ValueError("alpha must be non-negative")
    if ve_v0 < 0.0:
        raise ValueError("ve_v0 must be non-negative")

    r = ve_v0
    sin2 = (1.0 + alpha) * (1.0 + alpha * (1.0 - r * r))

    if sin2 < 0.0:
        raise ValueError("launch_angle: sin^2 < 0 (no real solution)")
    if sin2 > 1.0 + 1e-12:
        raise ValueError("launch_angle: sin^2 > 1 (no feasible solution)")

    sin_phi = sqrt(sin2)
    phi0 = arcsin(sin_phi)
    return phi0

# ---------------------------------------------------------------------------
# 4: launch_angle_range(ve_v0, alpha, tol_alpha)
# ---------------------------------------------------------------------------
def launch_angle_range(ve_v0: float, alpha: float, tol_alpha: float) -> np.ndarray:
    """
    Calculate the range of launch angles.
      - phi_min:(1+tol_alpha)*alpha
      - phi_max: (1-tol_alpha)*alpha
    """
    if tol_alpha < 0.0 or tol_alpha >= 1.0:
        raise ValueError("tol_alpha must be in [0, 1)")

    alpha_plus = (1.0 + tol_alpha) * alpha
    alpha_minus = (1.0 - tol_alpha) * alpha

    phi_min = launch_angle(ve_v0, alpha_plus)
    phi_max = launch_angle(ve_v0, alpha_minus)
    return np.array([phi_min, phi_max])

