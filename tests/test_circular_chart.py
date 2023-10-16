import sys
import os
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from functions.plotting.circular_chart import *

import unittest

class Test_circular_chart(unittest.TestCase):
	def test_make_plot(self):
            df = pd.DataFrame({"RJ": [1, 2, 3]})
            fig, ax = plt.subplots(2)
			
            expected_output = "etnia invalida"
            self.assertEqual(make_plot(df, "titulo", "caju", ax), expected_output)

            expected_output = "o titulo e a etnia precisam de ser strings"
            self.assertEqual(make_plot(df, "titulo", 5, ax), expected_output)
	

if __name__ == "__main__":
	unittest.main()