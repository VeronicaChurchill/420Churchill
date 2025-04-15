# python_intro.py
"""Python Essentials: Introduction to Python.
<Veronica Churchill>
<MTH420>
<4/11/2025>
"""


# Problem 1 (write code below)


# Problem 2
def sphere_volume(r):
    V= 4/3*3.14159*r**(3)
    return V
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def isolate(a, b, c, d, e):
    print(a, b, c, sep="     ", end=" ")
    print(d, e, sep=" ")
    return
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def first_half(my_string):
    if len(my_string) % 2 == 0:
        X = my_string[:(len(my_string)//2)]
    else:
        X = my_string[:(len(my_string)//2)]
    return X
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    raise NotImplementedError("Problem 4 Incomplete")

def backward(my_string):
    return my_string[::-1]
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def list_ops():
    my_list = ["bear", "ant", "cat", "dog"]
    my_list.append("eagle")
    my_list[2] = "fox"
    my_list.remove(my_list[1])
    my_list.sort(reverse=True)
    my_list[my_list.index('eagle')] = "hawk"
    my_list[-1] = (my_list[-1]+"hunter")
    return my_list
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def pig_latin(word):
    crying = ["a", "e", "i", "o", "u"]
    first_char = word[0]
    if word[0] in crying:
         word = (word+"hay")
    else:
        word = (word+first_char+"ay")
        word= word[1:]
    return word
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def palindrome():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product=i*j
            if str(product) == str(product)[::-1]:
                if product > max_palindrome:
                    max_palindrome = product
    return max_palindrome
    """ Find and return the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    raise NotImplementedError("Problem 7 Incomplete")

# Problem 8
def alt_harmonic(n):
    return sum([((-1)**(k+1)) /k for k in range(1, n+1)])
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    raise NotImplementedError("Problem 8 Incomplete")

    
"""test problem 1"""
if __name__ == "__main__" :
    print("Hello, world!")

"""test problem 2"""
if __name__ == "__main__" :
    print(sphere_volume(3))
    
"""test problem 3"""
if __name__ == "__main__" :
    isolate(1, 2, 3, 4, 5)
    
"""test problem 4a"""
if __name__ == "__main__" :
   print(first_half("my_stringg"))

"""test problem 4b"""
if __name__ == "__main__" :
   print(backward("python"))

"""test problem 5"""
if __name__ == "__main__" :
    print(list_ops())
    
"""test problem 6"""
if __name__ == "__main__" :
   print(pig_latin("aword"))

"""test problem 7"""
if __name__ == "__main__" :
   print(palindrome())

"""test problem 8"""
if __name__ == "__main__" :
   print(alt_harmonic(500000))