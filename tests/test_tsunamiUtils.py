import unittest
import sys
sys.path.append('D:/google_hackathon/project/VoilaDisasterPredictor/model')
from earthquake import tsunamiUtils
class TsunamiPredictorUtils(unittest.TestCase):
    def setUp(self):
        pass
    def test_getTsunamiLinearRegressionResults(self):
        result = tsunamiUtils.getTsunamiLinearRegressionResult('Logistic Regression', 1, 0, 0, 0, 0, 'CI', 0, 0, 0, 'ml', 0, 0, 0)
        self.assertEqual(result[0], 0)