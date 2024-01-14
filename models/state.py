#!/usr/bin/python3
"""class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Child cls of BaseModel to state amenity data

    Attrs: (public class)
        name: string: empty
    """

    name = ''
