import unittest
import fizzbuzz 

class MyTest(unittest.TestCase):
    def test_DecideHowToPrint(self):
        self.assertEqual(fizzbuzz.DecideHowToPrint(0), 0)
        self.assertEqual(fizzbuzz.DecideHowToPrint(1), 1)
        self.assertEqual(fizzbuzz.DecideHowToPrint(2), "BuzzFizz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(3), "Buzz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(4), 4)
        self.assertEqual(fizzbuzz.DecideHowToPrint(5), "Fizz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(6), "Buzz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(7), "BuzzFizz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(8), 8)
        self.assertEqual(fizzbuzz.DecideHowToPrint(9), "Buzz")
        self.assertEqual(fizzbuzz.DecideHowToPrint(10), "Fizz")
        
    def test_CheckIfPrime(self):
        self.assertEqual(fizzbuzz.CheckIfPrime(0), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(1), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(2), 1)
        self.assertEqual(fizzbuzz.CheckIfPrime(3), 1)
        self.assertEqual(fizzbuzz.CheckIfPrime(4), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(5), 1)
        self.assertEqual(fizzbuzz.CheckIfPrime(6), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(7), 1)
        self.assertEqual(fizzbuzz.CheckIfPrime(8), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(9), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(10), 0)
        self.assertEqual(fizzbuzz.CheckIfPrime(11), 1)
        
    
if __name__ == '__main__':
    unittest.main()