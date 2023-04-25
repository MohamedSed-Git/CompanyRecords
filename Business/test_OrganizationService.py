from Persistence.DataStore import DataStore

import unittest


class TestDataStore(unittest.TestCase):
    def test_get_all_records(self):
        data = DataStore()
        result = data.getAllRecords()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
