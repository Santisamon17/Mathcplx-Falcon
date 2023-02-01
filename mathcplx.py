# Calculadora de Numeros Complejos
# Por Santiago Sánchez Monroy
# Enero 2023

import math

def sumacplx(c1, c2):
    return [c1[0] + c2[0], c1[1] + c2[1]]


def restacplx(c1, c2):
    return [c1[0] - c2[0], c1[1] - c2[1]]


def productocplx(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]


def divisioncplx(c1, c2):
    num = productocplx(c1, conjugado(c2))
    denom = productocplx(c2, conjugado(c2))
    real = num[0] / denom[0]
    imaginario = num[1] / denom[0]
    return [real, imaginario]


def conjugado(c1):
    return [c1[0], c1[1]*-1]


def modulo(c1):
    return math.sqrt(c1[0]**2 + c1[1]**2)



def cart_polar(c1):
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def polar_cart(c1):
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def fase(c1):
    return math.degrees(math.atan2(c1[1], c1[0]))