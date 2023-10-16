import sys
import os
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from utils import *

import unittest

class Test_utils(unittest.TestCase):
	def test_check_ethnicity(self):
		expected_output = True
		self.assertEqual(check_ethnicity("amarela"), expected_output)

		expected_output = "tipo incorreto"
		self.assertEqual(check_ethnicity(2), expected_output)

	def test_get_label_rotation(self):
		rotacao, alinhamento = get_label_rotation(np.pi, np.pi/2)

		expected_output = 450.0
		self.assertEqual(rotacao, expected_output)
		
		expected_output = "right"
		self.assertEqual(alinhamento, expected_output)

		expected_output = "tipo incorreto"
		self.assertEqual(get_label_rotation("123", "123"), expected_output)

	def test_add_labels(self):
		self.assertEqual(add_labels(5, 6, 7, 8, 9), 'Algum parâmetro tem o tipo incorreto')

		angles = np.array([1.2])
		values = np.array([])
		labels = np.array(['coisa'])
		labels = labels.astype(object)
		fig, ax = plt.subplots(figsize=(20, 10))
		self.assertEqual(add_labels(angles, values, labels, 0.5, ax), 'Algum array está vazio')

if __name__ == "__main__":
	unittest.main()