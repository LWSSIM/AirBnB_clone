#!/usr/bin/python3
"""UnitTest for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """

    def __init__(self, *arg, **kwargs):
        super(TestBaseModel, self).__init__()
        self.key = "BaseModel"
        self.value = BaseModel


if __name__ == '__main__':
    unittest.main()
