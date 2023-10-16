import sys
import os
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from selecting_data import *

import unittest

class Test_selecting_data(unittest.TestCase):
	def test_select_data(self):
            df = pd.DataFrame({"RJ": [1, 2, 3]})
		
            expected_output = "etnia invalida"
            self.assertEqual(select_data(df, "caju"), expected_output)

            expected_output = "a etnia precisa de ser uma string"
            self.assertEqual(select_data(df, 5), expected_output)
	

if __name__ == "__main__":
	unittest.main()