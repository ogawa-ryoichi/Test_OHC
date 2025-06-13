
import unittest
import subprocess

class TestTestAction(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(['python3', '/workspace/test_action.py'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "test action")

if __name__ == '__main__':
    unittest.main()
