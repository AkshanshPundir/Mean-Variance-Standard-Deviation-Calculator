import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        
        # Check dictionary keys and non-float fields directly
        self.assertEqual(actual['max'], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(actual['min'], [[0, 1, 2], [0, 3, 6], 0])
        self.assertEqual(actual['sum'], [[9, 12, 15], [3, 12, 21], 36])
        
        # Use almost equal checks for floating-point calculations
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(actual['mean'][0][j], [3.0, 4.0, 5.0][j])
                self.assertAlmostEqual(actual['mean'][1][i], [1.0, 4.0, 7.0][i])
        self.assertAlmostEqual(actual['mean'][2], 4.0)

    def test_edge_case(self):
        with self.assertRaises(ValueError):
            mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1])

if __name__ == "__main__":
    unittest.main()