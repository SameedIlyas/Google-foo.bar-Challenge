from fractions import Fraction

def solution(pegs):
    n = len(pegs)
    even = n % 2 == 0
    
    r = (1 if even else -1) * pegs[-1] - pegs[0]

    for i in range(1, n - 1):
        r += 2 * ((-1) ** (i + 1)) * pegs[i]

    # Calculate the radius of the first gear
    radius = Fraction(2 * r, 3 if even else 1)

    # Check if it's possible to find radii for the rest of the gears
    for i in range(1, n):
        radius = pegs[i] - pegs[i - 1] - radius
    #check if the radius is above 1
        if radius < 1:
            return [-1, -1]

    # Return the simplified fraction for the first radius
    return [2 * radius.numerator, radius.denominator]
