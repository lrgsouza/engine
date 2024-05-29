
import xmlrunner
import os
import unittest
from modules.dice.dice import Dice


#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestDice(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.dice = Dice()

  def testDiceOutOfRange(self):
    self.assertIn(self.dice.roll(), range(1, 7))

  def testDiceGenProbability(self):
    # gera 100 numeros entre 1 e 6 e valida a probabilidade de 1 a 3 e 4 a 6
    nums = [self.dice.roll() for _ in range(100)]
    count_1_3 = count_4_6 = 0
    for num in nums:
      if num in range(1, 4):
        count_1_3 += 1
      elif num in range(4, 7):
        count_4_6 += 1
    self.assertGreater(count_1_3, 40)
    self.assertGreater(count_4_6, 40)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDice('testDiceGenProbability'))
    suite.addTest(TestDice('testDiceOutOfRange'))
    return suite

if __name__ == '__main__':
    # Ensure the directory exists
    output_dir = 'test-reports'
    os.makedirs(output_dir, exist_ok=True)
    
    # Run the tests
    runner = xmlrunner.XMLTestRunner(output=output_dir)
    runner.run(suite())