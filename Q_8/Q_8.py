import numpy as np

#Gausian Method 
def gaussian_quadrature(a, b, case):
    weights = [5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]
    nodes = [-np.sqrt(3.0 / 5.0), 0.0, np.sqrt(3.0 / 5.0)]
    integral = 0.0
    
    #Itterating for (a)
    if case == "a":
        for i in range(len(nodes)):
            x0 = ((b - a) / 2) * nodes[i] + ((a + b) / 2)
            integral += ((b - a) / 2) * weights[i] * f1(x0)
        return integral

    #Itterating for (b)
    elif case == "b":
        for i in range(len(nodes)):
            x0 = ((b - a) / 2) * nodes[i] + ((a + b) / 2)
            integral += ((b - a) / 2) * weights[i] * f2(x0)
        return integral

    #Incase wrong choice is provided
    else:
        return "ERROR"

#Setting value of A
A = float(input("Set the value of A: "))

#Importance Function
def p(x):
    return A * np.exp(-x)

#Multiplying (a) with p(x)
def f1(x):
    return p(x) * (x**3 / 2) * np.exp(-x)

#Multiplying (b) with p(x)
def f2(x):
    return p(x) * (x**2 * (np.cos(x)**2))**-1

#Printing solutions
print("Integral of x^3/2*e^−x from 0 to 3 is =", gaussian_quadrature(0, 3, "a"))
print("Integral of 1/(x^2*cosx^2) from 0 to π is =", gaussian_quadrature(0, np.pi, "b"))
