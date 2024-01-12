#!/usr/bin/python3
"""class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Child cls of BaseModel to track users data

    Attrs: (public class)
        email: string: empty
        password: string: empty
        first_name: string: empty
        last_name: string: empty
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
