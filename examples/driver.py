# examples/driver.py
"""
Driver:
 - test launch_angle_range at the test point
 - create two plots and save them under figures/
   1. ve_v0=2.0, plot min/max launch angles vs alpha (alpha range)
   2. alpha=0.25, plot min/max launch angles vs ve_v0 (ve range)
"""

import os
import sys
import pathlib
import numpy as np
import matplotlib.pyplot as plt


from goph419lab01 import functions

FIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "figures"))

os.makedirs(FIG_DIR, exist_ok=True)


def run_basic_test():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02
    print("Running basic test: ve_v0=2.0, alpha=0.25, tol_alpha=0.02")
    phi_range = functions.launch_angle_range(ve_v0, alpha, tol_alpha)
    print(f"Computed phi_range (radians): {phi_range}")
    print(f"Computed phi_range (degrees): {np.degrees(phi_range)}")
    return phi_range


def plot_alpha_variation():
    # Holding ve_v0 = 2.0, alpha will vary
    ve_v0 = 2.0
    tol_alpha = 0.04
    alphas = np.linspace(0.001, 1.0, 200)  # from very small to 1.0
    phi_min = []
    phi_max = []
    for a in alphas:
        try:
            phi = functions.launch_angle_range(ve_v0, a, tol_alpha)
            phi_min.append(phi[0])
            phi_max.append(phi[1])
        except ValueError:
            phi_min.append(np.nan)
            phi_max.append(np.nan)

    plt.figure(figsize=(8, 5))
    plt.plot(alphas, np.degrees(phi_min), label="min launch angle (deg)")
    plt.plot(alphas, np.degrees(phi_max), label="max launch angle (deg)")
    plt.xlabel("alpha (fraction of Earth's radius)")
    plt.ylabel("Launch angle (degrees)")
    plt.title(f"Launch angle range vs alpha (ve_v0={ve_v0}, tol_alpha={tol_alpha})")
    plt.legend()
    plt.grid(True)
    fpath = os.path.join(FIG_DIR, "launch_angle_vs_alpha.png")
    plt.savefig(fpath, bbox_inches="tight")
    plt.close()
    print(f"Saved plot: {fpath}")


def plot_ve_variation():
    # Holding alpha = 0.25, vary ve_v0
    alpha = 0.25
    tol_alpha = 0.04
    ve_vals = np.linspace(0.5, 6.0, 250)
    phi_min = []
    phi_max = []
    for v in ve_vals:
        try:
            phi = functions.launch_angle_range(v, alpha, tol_alpha)
            phi_min.append(phi[0])
            phi_max.append(phi[1])
        except ValueError:
            phi_min.append(np.nan)
            phi_max.append(np.nan)

    plt.figure(figsize=(8, 5))
    plt.plot(ve_vals, np.degrees(phi_min), label="min launch angle (deg)")
    plt.plot(ve_vals, np.degrees(phi_max), label="max launch angle (deg)")
    plt.xlabel("ve / v0")
    plt.ylabel("Launch angle (degrees)")
    plt.title(f"Launch angle range vs ve/v0 (alpha={alpha}, tol_alpha={tol_alpha})")
    plt.legend()
    plt.grid(True)
    fpath = os.path.join(FIG_DIR, "launch_angle_vs_ve_v0.png")
    plt.savefig(fpath, bbox_inches="tight")
    plt.close()
    print(f"Saved plot: {fpath}")


def main():
    phi_range = run_basic_test()
    plot_alpha_variation()
    plot_ve_variation()
    print("Driver finished.")


if __name__ == "__main__":
    main()
