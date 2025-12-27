'''
This file is used to perform unit testing on
emotion_detection.py application
'''

# Import the package
from EmotionDetection.emotion_detection import emotion_detector

# Import unittest library
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        # Test case1 for dominant emotion: joy
        test_joy = emotion_detector("I am glad this happened")
        self.assertEqual(test_joy['dominant_emotion'], 'joy')

        # Test case2 for dominant emotion: anger
        test_anger = emotion_detector("I am really mad about this")
        self.assertEqual(test_anger['dominant_emotion'], 'anger')

        # Test case3 for dominant emotion: disgust
        test_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_disgust['dominant_emotion'], 'disgust')

        # Test case4 for dominant emotion: sadness
        test_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(test_sadness['dominant_emotion'], 'sadness')

        # Test case5 for dominant emotion: fear
        test_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_fear['dominant_emotion'], 'fear')

# Run all unittest cases when the script is executed
if __name__ == '__main__':
    unittest.main()