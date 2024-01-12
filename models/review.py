#!/usr/bin/python3
"""class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Child cls of BaseModel to Review data

    Attrs: (public class)
        place_id: string - empty string: it will be the Place.id

        user_id: string - empty string: it will be the User.id

        text: string - empty string
    """

    user_id = ''
    place_id = ''
    text = ''
