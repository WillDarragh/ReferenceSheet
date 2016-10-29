from math import sin, cos, asin

def lawOfSines(A, a, B):
    # for any angle/side length pairs (A, a) and (B, b) the following holds:
    # sin(A) / a = sin(B) / b
    # this finds b
    return sin(B) * a / sin(A)

def lawOfCosines(b, c, A):
    # a^2 = b^2 + c^2 - 2 * b * c * cos(A)
    # Finds a
    return (b * b + c * c - 2 * b * c * cos(A)) ** 0.5
