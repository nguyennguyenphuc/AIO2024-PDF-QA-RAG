import unittest
from src.vector_database import create_vector_db


class TestVectorDatabase(unittest.TestCase):
    def test_create_vector_db(self):
        vector_db = create_vector_db('./tests/YOLOv10_Tutorials.pdf')
        self.assertIsNotNone(vector_db)


if __name__ == '__main__':
    unittest.main()
