'''
    T.M
    Homework #1.1
'''

def multiple_finder(a, b, c):
    if (a > b):
        more, less = a, b
    else:
        more, less = b, a

    return (more-1) // c - less // c

a = int(input("a - "))
b = int(input("b - "))
c = int(input("c - "))

print("multiples {}".format(multiple_finder(a, b, c)))