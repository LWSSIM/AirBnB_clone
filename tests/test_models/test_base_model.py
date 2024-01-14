#!/usr/bin/env python3
"""
Unittest for ```base_model```
"""

from datetime import datetime
from models.base_model import BaseModel
import unittest
import uuid
import models.base_model


class TestBaseModel(unittest.TestCase):
    """Test the class ``BaseModel``"""

    def setUp(self):
        pass

    def test_module_doc(self):
        """Test module documentation"""
        self.assertIsNotNone(models.base_model.__doc__)

    def test_class_doc(self):
        """Test ``BaseModel`` class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docs(self):
        """Test methods in ``BaseModel`` for documentation"""
        methods = [
            BaseModel.__init__,
            BaseModel.__str__,
            BaseModel.save,
            BaseModel.to_dict,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_initial_attribute(self):
        """Test object id"""
        test_Base = BaseModel()
        test_Base_1 = BaseModel()

        # check if id and type
        self.assertTrue(hasattr(test_Base, "id"))
        self.assertIsNotNone(test_Base.id)
        self.assertIsInstance(test_Base.id, str)

        # Check if id is uuid
        self.assertTrue(uuid.UUID(test_Base.id))

        # Check if instances id uniqueness
        self.assertNotEqual(test_Base.id, test_Base_1.id)

        # Check if created_at
        self.assertTrue(hasattr(test_Base, "created_at"))
        self.assertIsNotNone(test_Base.created_at)
        self.assertIsInstance(test_Base.created_at, datetime)

        # Check if updated_at
        self.assertTrue(hasattr(test_Base, "updated_at"))
        self.assertIsNotNone(test_Base.updated_at)
        self.assertIsInstance(test_Base.updated_at, datetime)

        self.assertTrue(hasattr(test_Base, "__class__"))
        self.assertIsNotNone(test_Base.__class__)
        self.assertIsInstance(test_Base.__class__, object)

        # Check __str__ format
        _str = "[BaseModel] ({}) {}".format(test_Base.id, test_Base.__dict__)
        self.assertEqual(str(test_Base), _str)

        old = test_Base.updated_at
        test_Base.save()
        self.assertGreater(test_Base.updated_at, old)

        # Check that with arg
        test_with_arg = BaseModel("arg")
        self.assertNotIn("arg", test_with_arg.__dict__)

    def test_kwargs_input(self):
        """Test ``BaseModel`` kwargs initialization"""
        dic = {
            "id": "str_id",
            "created_at": "2024-01-09T10:34:56.789012",
            "updated_at": "2024-01-09T12:45:12.345678",
            "name": "Lwssim",
            "age": 8,
        }
        test_Base = BaseModel(**dic)

        self.assertEqual(test_Base.id, "str_id")
        self.assertEqual(test_Base.name, "Lwssim")
        self.assertEqual(test_Base.age, 8)
        self.assertIsInstance(test_Base.created_at, datetime)
        self.assertIsInstance(test_Base.updated_at, datetime)

    def test_kwargs_none(self):
        """Test None kwargs input """
        bad_kwarg = {None: None}
        with self.assertRaises(TypeError):
            bad_input = BaseModel(**bad_kwarg)
            self.assertIsNone(bad_input)

    def test_to_dict_and_data_type(self):
        """Test data type ``to_dict``"""
        test_Base = BaseModel()
        test_Base.name = "Lwssim"
        test_Base.age = "99"
        test_Base.wieght = 22
        test_Base._float = 88.2
        test_Base._bool = True

        test_dict = test_Base.to_dict()

        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(test_dict["id"], test_Base.id)
        self.assertEqual(test_dict["name"], "Lwssim")
        self.assertEqual(test_dict["age"], "99")
        self.assertEqual(test_dict["wieght"], 22)
        self.assertEqual(test_dict["_float"], 88.2)
        self.assertEqual(test_dict["_bool"], True)


if __name__ == "__main__":
    unittest.main()
