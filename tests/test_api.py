 
import unittest
from data.data_handler import fetch_crypto_data

class TestAPI(unittest.TestCase):
    def test_fetch_crypto_data(self):
        data = fetch_crypto_data()
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()
