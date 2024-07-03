import unittest
from src.language_model import get_language_model


class TestLanguageModel(unittest.TestCase):
    def test_get_language_model(self):
        model_pipeline = get_language_model()
        self.assertIsNotNone(model_pipeline)


if __name__ == '__main__':
    unittest.main()
