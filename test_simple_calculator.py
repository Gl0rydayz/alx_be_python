import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Test with decimals/floats
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=1)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0, places=1)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(7, 3), 4)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        
        # Test with decimals/floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=1)
        self.assertAlmostEqual(self.calc.subtract(-1.5, -1.5), 0.0, places=1)
        
        # Test where result is negative
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 2), 14)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        
        # Test with decimals/floats
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=1)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2), -3.0, places=1)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test division by zero (should return None)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-7, 1), -7.0)
        
        # Test with decimals/floats
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=1)
        self.assertAlmostEqual(self.calc.divide(-9.6, 3.2), -3.0, places=1)
        
        # Test division resulting in repeating decimal
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333, places=4)

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Test very large numbers
        large_num = 1000000
        self.assertEqual(self.calc.add(large_num, large_num), 2000000)
        self.assertEqual(self.calc.multiply(large_num, 2), 2000000)
        
        # Test very small numbers (close to zero)
        small_num = 0.0001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 0.0002, places=4)
        
        # Test mixed integer and float operations
        self.assertEqual(self.calc.add(5, 2.5), 7.5)
        self.assertEqual(self.calc.subtract(10, 3.3), 6.7)

if __name__ == '__main__':
    unittest.main()