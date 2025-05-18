# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Veronica Churchill>
<MTH420>
<5/17/2025>
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    A = np.random.normal(size=(n, n))
    row_means = np.mean(A, axis=1)
    return np.var(row_means)
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    ns = np.arange(100, 1001, 100)
    variances = [var_of_means(n) for n in ns]

    print("Matrix sizes:", ns)
    print("Variances:", variances)
    
    plt.plot(ns, variances, marker='o')
    plt.xlabel("n (matrix size)")
    plt.ylabel("Variance of Row Means")
    plt.title("Variance of Row Means vs Matrix Size")
    plt.grid(True)
    plt.show()
    return
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.plot(x, np.arctan(x), label='arctan(x)')

    plt.title("Trig Functions on [-2π, 2π]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    return
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 0.999, 500)
    x2 = np.linspace(1.001, 6, 500)

    y1 = 1 / (x1 - 1)
    y2 = 1 / (x2 - 1)

    plt.plot(x1, y1, 'm--', lw=4)
    plt.plot(x2, y2, 'm--', lw=4)

    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    plt.title("Plot of f(x) = 1 / (x - 1)")
    plt.grid(True)
    plt.show()
    return
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 1000)

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot(x, np.sin(x), 'g-')
    axs[0, 0].set_title("sin(x)")
    axs[0, 0].axis([0, 2*np.pi, -2, 2])

    axs[0, 1].plot(x, np.sin(2*x), 'r--')
    axs[0, 1].set_title("sin(2x)")
    axs[0, 1].axis([0, 2*np.pi, -2, 2])

    axs[1, 0].plot(x, 2*np.sin(x), 'b--')
    axs[1, 0].set_title("2sin(x)")
    axs[1, 0].axis([0, 2*np.pi, -2, 2])

    axs[1, 1].plot(x, 2*np.sin(2*x), 'm:')
    axs[1, 1].set_title("2sin(2x)")
    axs[1, 1].axis([0, 2*np.pi, -2, 2])

    fig.suptitle("Sine Function Variants")
    plt.tight_layout()
    plt.show()
    return
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    # Domain setup
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    y = np.linspace(-2*np.pi, 2*np.pi, 400)
    X, Y = np.meshgrid(x, y)

    # Compute g(x, y) = sin(x)sin(y)/(xy), with care around zero
    with np.errstate(divide='ignore', invalid='ignore'):
        G = np.sin(X) * np.sin(Y) / (X * Y)
        G[np.isnan(G)] = 0  # Replace undefined values at (0, 0) with 0

    # Plot setup
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Heat map
    heat = axs[0].imshow(G, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi],
                         origin='lower', cmap='plasma', aspect='auto')
    axs[0].set_title("Heat Map of g(x, y)")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")
    fig.colorbar(heat, ax=axs[0])

    # Contour map
    levels = np.linspace(-1, 1, 30)  # Customize number of contour levels
    contour = axs[1].contourf(X, Y, G, levels=levels, cmap='viridis')
    axs[1].set_title("Contour Map of g(x, y)")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("y")
    fig.colorbar(contour, ax=axs[1])

    # Save the plot instead of showing it (if needed)
    # plt.savefig("prob6_plot.png")
    plt.tight_layout()
    plt.show()
    return
    raise NotImplementedError("Problem 6 Incomplete")

    
    #The window would not show up for just plt.show(), so to check I had to do plt.savefig() for each problem.