"""Volume 2: Simplex

<Name>
<Date>
<Class>
"""

import numpy as np

# Problems 1-6
class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        minimize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    # Problem 1
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        self.c = c
        self.A = A
        self.b = b
        if not np.all(b >= 0):
            raise ValueError("Infeasible at the origin.")
        self._generatedictionary(c, A, b)


    # Problem 2
    def _generatedictionary(self, c, A, b):
        """Generate the initial dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.
        """
        m, n = A.shape
        I = np.eye(m)
        A_bar = np.hstack((A, I))
        c_bar = np.concatenate((c, np.zeros(m)))

        self.dictionary = np.zeros((m + 1, n + m + 1))
        self.dictionary[0, 1:] = c_bar
        self.dictionary[1:, 0] = b
        self.dictionary[1:, 1:] = -A_bar

        self.num_vars = n
        self.num_constraints = m
        self.basic_vars = list(range(n, n + m))
        self.nonbasic_vars = list(range(n))



    # Problem 3a
    def _pivot_col(self):
        """Return the column index of the next pivot column.
        """
        for j in range(1, self.dictionary.shape[1]):
            if self.dictionary[0, j] < 0:
                return j
        return None

    # Problem 3b
    def _pivot_row(self, col_index):
        """Determine the row index of the next pivot row using the ratio test
        (Bland's Rule).
        """
        ratios = []
        for i in range(1, self.dictionary.shape[0]):
            if self.dictionary[i, col_index] < 0:
                ratio = -self.dictionary[i, 0] / self.dictionary[i, col_index]
                ratios.append((ratio, i))

        if not ratios:
            raise ValueError("Linear program is unbounded.")

        # Bland's Rule: tie-break using smallest row index
        _, pivot_row = min(ratios, key=lambda x: (x[0], x[1]))
        return pivot_row

    # Problem 4
    def pivot(self):
        """Select the column and row to pivot on. Reduce the column to a
        negative elementary vector.
        """
        return NotImplementedError("Problem 4 Incomplete")

    # Problem 5
    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        raise NotImplementedError("Problem 5 Incomplete")

# Problem 6
def prob6(filename='productMix.npz'):
    """Solve the product mix problem for the data in 'productMix.npz'.

    Parameters:
        filename (str): the path to the data file.

    Returns:
        ((n,) ndarray): the number of units that should be produced for each product.
    """
    raise NotImplementedError("Problem 6 Incomplete")

    
"""test problem 1 and 2 and 3"""
if __name__ == "__main__":
    c = np.array([-3., -2.])
    A = np.array([
        [1., -1.],
        [3., 1.],
        [4., 3.]
    ])
    b = np.array([2., 5., 7.])

    solver = SimplexSolver(c, A, b)
    print("Initial dictionary:")
    print(solver.dictionary)
    pivot_col = solver._pivot_col()
    print(f"\nPivot Column Index: {pivot_col}")
    pivot_row = solver._pivot_row(pivot_col)
    print(f"Pivot Row Index: {pivot_row}")