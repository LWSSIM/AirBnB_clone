#!/usr/bin/env python3
"""unittest for models/amenity
"""
import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity model attr"""

    def test_class_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_doc(self):
        self.assertIsNotNone(models.amenity.__doc__)

    def test_attribute_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertEqual(type(amenity.name), str)


if __name__ == "__main__":
    unittest.main()
