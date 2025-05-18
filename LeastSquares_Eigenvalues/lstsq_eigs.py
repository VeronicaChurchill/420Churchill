# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Veornica Churchill>
<MTH420>
<5/17/2025>
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = np.linalg.qr(A)
    x = la.solve_triangular(R, Q.T @ b)
    return x
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load("housing.npy")
    x = data[:, 0]  # years
    y = data[:, 1]  # housing price index

    # Build the Vandermonde matrix for a line: [1, x]
    A = np.column_stack((np.ones_like(x), x))

    # Solve least squares using np.linalg.lstsq
    coeffs = np.linalg.lstsq(A, y, rcond=None)[0]

    # Evaluate the fitted line
    x_vals = np.linspace(x.min(), x.max(), 500)
    y_vals = coeffs[0] + coeffs[1] * x_vals

    # Plot
    plt.scatter(x, y, label="Data", color="blue")
    plt.plot(x_vals, y_vals, label="Least Squares Line", color="red")
    plt.xlabel("Year")
    plt.ylabel("Housing Price Index")
    plt.title("Least Squares Line Fit")
    plt.legend()
    plt.grid(True)
    plt.show()

    #raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("housing.npy")
    x = data[:, 0]
    y = data[:, 1]

    degrees = [3, 6, 9, 12]
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    for ax, deg in zip(axes.ravel(), degrees):
        # Build Vandermonde matrix
        A = np.vander(x, deg + 1, increasing=True)

        # Solve least squares
        coeffs = np.linalg.lstsq(A, y, rcond=None)[0]

        # Evaluate polynomial
        x_vals = np.linspace(x.min(), x.max(), 500)
        A_plot = np.vander(x_vals, deg + 1, increasing=True)
        y_vals = A_plot @ coeffs

        # Plot
        ax.scatter(x, y, label="Data", s=10)
        ax.plot(x_vals, y_vals, label=f"Degree {deg} Fit", color="red")
        ax.set_title(f"Polynomial Degree {deg}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Housing Index")
        ax.grid(True)
        ax.legend()

    fig.suptitle("Polynomial Least Squares Fits")
    plt.tight_layout()
    plt.show()

    #raise NotImplementedError("Problem 3 Incomplete")


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")

"""test problem 1"""
if __name__ == "__main__":
    A = np.array([[1, 1],
              [1, 2],
              [1, 3]])
    b = np.array([1, 2, 2])
    x = least_squares(A, b)
    print(x)
    
"""test problem 2 & 3"""
if __name__ == "__main__":
    line_fit()
    polynomial_fit()