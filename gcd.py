#Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b): 
    while (b != 0):
        c = a
        a = b
        b = c %b
    return a

# Test the function
print(gcd(60, 96)) # = 12
print(gcd(20, 8)) # = 4