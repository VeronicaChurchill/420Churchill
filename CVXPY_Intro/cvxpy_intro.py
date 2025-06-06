# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Veronica Churchill>
<MTH420>
<6/5/2025>
"""

import numpy as np
import cvxpy as cp

# Problem 1
def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable()
    y = cp.Variable()
    z = cp.Variable()
    
    objective = cp.Minimize(2*x + y + 3*z)
    constraints = [
        x + 2*y <= 3,
        y - 4*z <= 1,
        2*x + 10*y + 3*z >= 12,
        x >= 0,
        y >= 0,
        z >= 0
    ]
    
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    solution = np.array([x.value, y.value, z.value])
    return solution, optimal_value

    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [A @ x == b]
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    return x.value, optimal_value

    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(6)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c @ x)


    supply = np.array([
        [1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1]])
    supply_rhs = np.array([7, 2, 4])

    # Demand constraints
    demand = np.array([
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1]])
    demand_rhs = np.array([5, 8])

    constraints = [
        supply @ x <= supply_rhs,
        demand @ x == demand_rhs,
        x >= 0]
    
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    return x.value, optimal_value
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3)
    Q = np.array([
        [3, 2, 0.5],
        [2, 4, 1],
        [0.5, 1, 3]])
    r = np.array([3, 0, 1])
    objective = cp.Minimize(0.5 * cp.quad_form(x, Q) + r @ x)
    prob = cp.Problem(objective)
    optimal_value = prob.solve()
    return x.value, optimal_value
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n)
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    constraints = [
        cp.sum(x) == 1,
        x >= 0]
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    return x.value, optimal_value
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")
    
"""test problem 1"""
if __name__ == "__main__":
    print(prob1())
    
"""test problem 2"""
A = np.array([
    [1, 2, 1, 1],
    [0, 3, -2, -1]])
b = np.array([7, 4])
if __name__ == "__main__":
    print(l1Min(A, b))
    
"""test problem 3"""
if __name__ == "__main__":
    print(prob3())
    
"""test problem 4"""
if __name__ == "__main__":
    print(prob4())
    
"""test problem 5"""
if __name__ == "__main__":
    print(prob5(A, b))