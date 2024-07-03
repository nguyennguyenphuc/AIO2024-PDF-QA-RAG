import unittest
from src.rag_pipeline import initialize_rag_system


class TestRAGPipeline(unittest.TestCase):
    def test_initialize_rag_system(self):
        rag_system = initialize_rag_system()
        self.assertIsNotNone(rag_system)


if __name__ == '__main__':
    unittest.main()
