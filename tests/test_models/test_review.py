#!/usr/bin/env python3
"""unittest for models/review
"""
import unittest
from models.review import Review
import models.review


class TestReview(unittest.TestCase):
    """Test ``Review`` model attr"""

    def test_module_doc(self):
        self.assertIsNotNone(models.review.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_place_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(type(review.place_id), str)

    def test_attribute_user_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertEqual(type(review.user_id), str)

    def test_attribute_text(self):
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        self.assertEqual(type(review.text), str)


if __name__ == "__main__":
    unittest.main()
