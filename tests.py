import unittest
from main import reverse_array

class ReverseTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_array([1,2,3,4]), [4,3,2,1])

# class LinkedListTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual()

if __name__ == '__main__':
    unittest.main()
