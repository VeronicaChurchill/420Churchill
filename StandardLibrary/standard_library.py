# standard_library.py
"""Python Essentials: The Standard Library.
<Veronica Churchill>
<MTH420>
<4/17/2025>
"""

from math import sqrt


# Problem 1
def prob1(L): 
    
    return min(L), max(L), sum(L)/len(L)
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    int_1=2
    int_2=int_1
    int_2 = int_2 + 1
    
    str_1= "lalala"
    str_2=str_1
    str_2=str_2 + str_2
    
    list_1=[88, 99, 121, 77]
    list_2=list_1
    list_2[3] = 132
    
    tuple_1= (1, 2, 3, 4)
    tuple_2=tuple_1
    # tuple_2[3] = 5
    
    set_1= {5, 7, 9}
    set_2=set_1
    set_2.add(11)
    return "integers, strings, and tuples are immutable while lists and sets are mutable."

    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
from math import sqrt
def product(a,b):
    return a*b
def summ(a,b):
    return a+b
def hypot(a, b):
    
    return sqrt(summ(product(a,a),product(b,b)))
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
from itertools import combinations
def power_set(A):
    my_list=[set()]
    lists=list(A)
    for i in range(len(lists)):
        for subset in combinations(lists, i+1):
            my_list.append(set(subset))
    return my_list
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")

"""test problem 1"""
if __name__ == "__main__":
    L = [12, 11, 29, 6, 2, 107]
    print(prob1(L))
    
"""test problem 2"""
if __name__ == "__main__":    
    print(prob2())
    
    """test problem 3"""
if __name__ == "__main__":
    a=3
    b=4
    print(hypot(a,b))
    
"""test problem 2"""
if __name__ == "__main__":
    A= {"a" , "b", "c", "d"} 
    print(power_set(A))