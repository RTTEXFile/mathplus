#!/usr/bin/python

import math

# everything starts with "m_" because this is intended to be loaded with "from mathplus import *"

_INTERNAL_PI_PRECISION = 3.14
M_PI_SYMBOL = "π"
M_PYTHAGOREAN_THEOREM = "((a**2)+(b**2))**0.5"
M_PYTHAGOREAN_THEOREM_REV = "((c**2)-(a**2))**0.5"
M_TRIANGLE_AREA = "(a*h)/2"
M_CIRCLE_AREA = "(r**2)*pi"
M_CIRCLE_CIRCUMFERENCE = "2*r*pi"
M_SQUARE_AREA = "a**2"
M_SQUARE_PERIMETER = "a*4"
M_RECTANGLE_AREA = "a*b"
M_RECTANGLE_PERIMETER = "2*a+2*b"
M_CUBE_VOLUME = "a**3"
M_CUBE_SURFACE_AREA = "(a**2)*6"
M_TRAPEZOID_AREA = "((a+b)*h)/2"
M_CYLINDER_VOLUME = "pi*(r**2)*h"
M_CYLINDER_SURFACE_AREA = "2*pi*(r**2) + 2*pi*r*h"
M_CONE_VOLUME = "(1/3)*pi*(r**2)*h"
M_CONE_SURFACE_AREA = "pi*r*(r+l)"
M_CONE_HEIGHT = "(V*3)/((r**2)*pi)"

def _eval_with_pi(equation: str, globals: dict, pi): # does not account for if equation requires pi**2
    globals["math"] = math
    if "pi" not in equation:
        return eval(equation, globals)
    if isinstance(pi, str):
        globals["pi"] = 1
        return str(eval(equation, globals)) + pi
    elif pi == True:
        globals["pi"] = 1
        return str(eval(equation, globals)) + M_PI_SYMBOL
    else:
        globals["pi"] = pi
        return eval(equation, globals)

def _find_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def _find_lcm(a: int, b: int) -> int:
    return a * b // _find_gcd(a, b)

def m_equation(equation: str):
    problem, answer = equation.split("=")
    solutions = []
    for x in range(-5000, 5001):
        x_value = x/10
        if _eval_with_pi(problem, {"x": x_value}, _INTERNAL_PI_PRECISION) == _eval_with_pi(answer, {"x": x_value}, _INTERNAL_PI_PRECISION):
            solutions.append(x_value)
    
    if len(solutions) == 0:
        return "Couldn't find a solution."
    elif len(solutions) == 1:
        return int(solutions[0])
    elif len(solutions) == 10001:
        return "All solutions are correct."
    else:
        return solutions

def m_fraction_simplify(fraction: str):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    gcd = _find_gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return str(numerator) + "/" + str(denominator)

def m_fraction_add(fraction1: str, fraction2: str) -> str:
    numerator1, denominator1 = fraction1.split("/")
    numerator2, denominator2 = fraction2.split("/")
    numerator1 = int(numerator1)
    denominator1 = int(denominator1)
    numerator2 = int(numerator2)
    denominator2 = int(denominator2)
    lcm = _find_lcm(denominator1, denominator2)
    numerator1 *= lcm // denominator1
    numerator2 *= lcm // denominator2
    numerator = numerator1 + numerator2
    gcd = _find_gcd(numerator, lcm)
    numerator //= gcd
    denominator = lcm // gcd
    return str(numerator) + "/" + str(denominator)

def m_fraction_subtract(fraction1: str, fraction2: str) -> str:
    numerator1, denominator1 = fraction1.split("/")
    numerator2, denominator2 = fraction2.split("/")
    numerator1 = int(numerator1)
    denominator1 = int(denominator1)
    numerator2 = int(numerator2)
    denominator2 = int(denominator2)
    lcm = _find_lcm(denominator1, denominator2)
    numerator1 *= lcm // denominator1
    numerator2 *= -lcm // denominator2
    numerator = numerator1 + numerator2
    gcd = _find_gcd(numerator, lcm)
    numerator //= gcd
    denominator = lcm // gcd
    return str(numerator) + "/" + str(denominator)

def m_pythagorean_theorem(a: int, b: int) -> int:
    return _eval_with_pi(M_PYTHAGOREAN_THEOREM, {"a": a, "b": b}, _INTERNAL_PI_PRECISION)

def m_pythagorean_theorem_rev(c: int, a: int) -> int:
    return _eval_with_pi(M_PYTHAGOREAN_THEOREM_REV, {"c": c, "a": a}, _INTERNAL_PI_PRECISION)

def m_triangle_area(a: int, h: int) -> int:
    return _eval_with_pi(M_TRIANGLE_AREA, {"a": a, "h": h}, _INTERNAL_PI_PRECISION)

def m_circle_area(r: int, pi):
    return _eval_with_pi(M_CIRCLE_AREA, {"r": r}, pi)
    
def m_circle_circumference(r: int, pi):
    return _eval_with_pi(M_CIRCLE_CIRCUMFERENCE, {"r": r}, pi)

def m_square_area(a: int):
    return _eval_with_pi(M_SQUARE_AREA, {"a": a}, _INTERNAL_PI_PRECISION)

def m_square_perimeter(a: int):
    return _eval_with_pi(M_SQUARE_PERIMETER, {"a": a}, _INTERNAL_PI_PRECISION)

def m_rectangle_diagonal(a: int, b: int):
    return m_pythagorean_theorem(a, b)

def m_cube_surface_area(a: int):
    return _eval_with_pi(M_CUBE_SURFACE_AREA, {"a": a}, _INTERNAL_PI_PRECISION)

def m_rectangle_area(a: int, b: int):
    return _eval_with_pi(M_RECTANGLE_AREA, {"a": a, "b": b}, _INTERNAL_PI_PRECISION)

def m_rectangle_perimeter(a: int, b: int):
    return _eval_with_pi(M_RECTANGLE_PERIMETER, {"a": a, "b": b}, _INTERNAL_PI_PRECISION)

def m_trapezoid_area(a: int, b: int, h: int):
    return _eval_with_pi(M_TRAPEZOID_AREA, {"a": a, "b": b, "h": h}, _INTERNAL_PI_PRECISION)

def m_cylinder_surface_area(r: int, h: int, pi):
    return _eval_with_pi(M_CYLINDER_SURFACE_AREA, {"r": r, "h": h}, pi)

def m_cylinder_volume(r: int, h: int, pi):
    return _eval_with_pi(M_CYLINDER_VOLUME, {"r": r, "h": h}, pi)

def m_cone_surface_area(r: int, l: int, pi):
    return _eval_with_pi(M_CONE_SURFACE_AREA, {"r": r, "l": l}, pi)

def m_cone_volume(r: int, h: int, pi):
    return _eval_with_pi(M_CONE_VOLUME, {"r": r, "h": h}, pi)

def m_cone_height(r: int, V: int, pi):
    return _eval_with_pi(M_CONE_HEIGHT, {"r": r, "V": V}, pi)
