import unittest
import requests
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy(self):
        statement = "I am glad this happened"
        expected_output = {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.99, 'sadness': 0.0, 'dominant_emotion': 'joy'}
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_output['dominant_emotion'])

    def test_anger(self):
        statement = "I am really mad about this"
        expected_output = {'anger': 0.8, 'disgust': 0.1, 'fear': 0.05, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_output['dominant_emotion'])

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        expected_output = {'anger': 0.1, 'disgust': 0.8, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.1, 'dominant_emotion': 'disgust'}
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_output['dominant_emotion'])

    def test_sadness(self):
        statement = "I am so sad about this"
        expected_output = {'anger': 0.1, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.8, 'dominant_emotion': 'sadness'}
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_output['dominant_emotion'])

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        expected_output = {'anger': 0.0, 'disgust': 0.0, 'fear': 0.8, 'joy': 0.0, 'sadness': 0.1, 'dominant_emotion': 'fear'}
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_output['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()