#!/usr/bin/python3
"""class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Child cls of BaseModel to state city data

    Attrs: (public class)
        name: string: empty
        state_id: string - empty string:
            it will be the State.id
    """

    name = ''
    state_id = ''
