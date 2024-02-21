from EmotionDetection.emotion_detection import emotion_predictor
import unittest

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        result1 = emotion_predictor("I am glad this happened")
        result2 = emotion_predictor("I am really mad about this")
        result3 = emotion_predictor("I feel disgusted just hearing about this")
        result4 = emotion_predictor("I am so sad about this")
        result5 = emotion_predictor("I am really afraid that this will happen")

        self.assertEqual(result1["dominant_emotion"],"joy")
        self.assertEqual(result2["dominant_emotion"],"anger")
        self.assertEqual(result3["dominant_emotion"],"disgust")
        self.assertEqual(result4["dominant_emotion"],"sadness")
        self.assertEqual(result5["dominant_emotion"],"fear")

unittest.main()