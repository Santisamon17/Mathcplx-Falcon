# Test Calculadora de Numeros Complejos
# Por Santiago Sánchez Monroy
# Enero 2023

import unittest
import mathcplx
import math

class testmathcplx(unittest.TestCase):
    
    def test_sumacplx(self):
        c1 = [9,3]
        c2 = [1,5]
        self.assertEqual(mathcplx.sumacplx(c1,c2), [10,8])

    def test_restacplx(self):
        c1 = [4,8]
        c2 = [1,2]
        self.assertEqual(mathcplx.restacplx(c1,c2), [3,6])

    def test_productocplx(self):
        c1 = [5,2]
        c2 = [2,3]
        self.assertEqual(mathcplx.productocplx(c1,c2), [4,19])

    def test_divisioncplx(self):
        c1 = [5,2]
        c2 = [2,3]
        self.assertEqual(mathcplx.divisioncplx(c1,c2), [1.23076923077,0.84615384615])

    def test_modulo(self):
        c1 = [1,2]
        self.assertEqual(mathcplx.modulo(c1), math.sqrt(5))

    def test_cart_polar(self):
        c1 = [1,1]
        self.assertEqual(mathcplx.cart_polar(c1),[1.4142135623730951, 45.0])

    def test_polar_cart(self):
        c1 = [1.4185, 45.0]
        self.assertEqual(mathcplx.polar_cart(c1),[1.0030309691131178, 1.0030309691131178])

    def test_fase(self):
        c1 = [1,2]
        self.assertEqual(mathcplx.fase(c1),63.43494882292201)
        
if __name__ == '__main__':
    unittest.main()