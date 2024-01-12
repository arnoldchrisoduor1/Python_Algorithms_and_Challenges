import unittest
from ranking import User

class TestUserClass(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_initial_state(self):
        self.assertEqual(self.user.rank, -8)
        self.assertEqual(self.user.progress, 0)

    def test_valid_rank(self):
        with self.assertRaises(ValueError):
            self.user.validate_rank(10)

    def test_increment_progress_same_rank(self):
        self.assertEqual(self.user.inc_progress(-7), 10)
        self.assertEqual(self.user.rank, -8)

    def test_increment_progress_lower_rank(self):
        self.assertEqual(self.user.inc_progress(-6), 40)
        self.assertEqual(self.user.rank, -8)

    def test_increment_progress_higher_rank(self):
        self.assertEqual(self.user.inc_progress(-4), 60)  # Corrected expected value
        self.assertEqual(self.user.rank, -7)

    def test_increment_progress_rank_upgrade(self):
        self.user.inc_progress(-4)
        self.assertEqual(self.user.progress, 60)  # Remaining progress towards the next rank
        self.assertEqual(self.user.rank, -7)

    def test_increment_progress_max_rank(self):
        self.user.inc_progress(8)
        self.assertEqual(self.user.progress, 60)  # Remaining progress towards the next rank
        self.assertEqual(self.user.rank, 8) 

    def test_increment_progress_invalid_rank(self):
        with self.assertRaises(ValueError):
            self.user.inc_progress(10)

if __name__ == '__main__':
    unittest.main()
