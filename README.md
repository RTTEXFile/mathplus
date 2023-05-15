# M+
M+ - A small Python library for quick math formulas in the Python shell
# Example usage
```
>>> from mathplus import *
>>> M_CIRCLE_AREA
'(r**2)*pi'
>>> m_circle_area(7, True)   # (r, pi)
'49π'
>>> m_circle_area(7, 3.14)   # (r, pi)
153.86
>>> m_circle_area(7, "pi")   # (r, pi)
'49pi'
>>> m_fraction_simplify("9/3")   # (fraction)
'3/1'
>>> m_fraction_add("9/3", "3/8")   # (fraction1, fraction2)
'27/8'
>>> m_pythagorean_theorem(4, 3)   # (a, b)
5.0
>>> M_PYTHAGOREAN_THEOREM
'((a**2)+(b**2))**0.5'
```
