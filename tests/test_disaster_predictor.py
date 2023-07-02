import sys
sys.path.append('D:/google_hackathon/project/VoilaDisasterPredictor/app')
import disaster_predictor as disaster_predictor_app
import unittest
class DisasterPredictorAppTests(unittest.TestCase):
    def setUp(self):
        self.app = disaster_predictor_app.DisasterPredictorApp()
    
    def test_getWidget(self):
        widget = self.app.getWidget()
        self.assertIsNotNone(widget)