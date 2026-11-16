
from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for positive sentiment
        casos = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear" } 
        for texto, esperado in casos.items():
            resultado = emotion_detector(texto)
            self.assertEqual(resultado['dominant_emotion'], esperado)

unittest.main()
