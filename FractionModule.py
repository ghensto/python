""" The "Fraction" module is a module that provides support for rational
number arithmetic. It can be usde to construct a fraction from a pair of
integers, from another rational number, from a decimal number or from a
string. It is also a class that inherits from the abstract base class
numbers.Rational, and implements all of the methods and operations from
that class. This module will be really helpful when working with rational
numbers like giving the exact answer instead of a decimal number. It can
also be used when working the Gcds"""

# This program imports the fraction module and shows how it can be used
# Abiola ADIMI

import fractions

def main():

# Create fractions from separate numerator and denominator values

    print('Fractions from separate numerator and denominator values: ')
    for n, d in [ (1, 2), (2, 4), (3, 6) , (3, 8), (7, 49), (35, 7), (5, 125)]:
        f = fractions.Fraction(n, d)
        print ("{}/{} = {}".format(n, d, f))

# Create fractions from decimal or floating notation

    print('\nFractions from decimal or floating notation: ')
    for s in [ '0.5', '1.5', '2.0', '0.45', '4.3', '12.4', '1.33' ]:
        f = fractions.Fraction(s)
        print ("{} = {}".format(s, f))

#Finds gcd of two numbers
    print('\nGcd of two numbers')
    for a,b in [(20,45), (32,43), (12, 144), (34, 54), (90, 35), (35, 7), (50, 14)]:
        f = fractions.gcd(a, b)
        print("The gcd of {} and {} is {}.".format(a,b,f))

if __name__ == "__main__": main()
