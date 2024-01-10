#!/usr/bin/python3
"""Base Module for the project:
    All other classes will inherit from here
"""


from datetime import datetime
import uuid


class BaseModel():
    """
    Defines attribiutes and methods for other classes

    Attrs: (public-instance)
        id: string - (assign with an uuid when an instance is created).

        created_at: datetime - assign with the current datetime at creation.

        updated_at: datetime - assign with the current datetime at creation.
            and it will be updated every time you change your object.


    Methods: (public-instance)
        save(self): update `updated_at` with the current datetime

        to_dict(self): create a dictionary representation with object type

        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    """

    def __init__(self, *args, **kwargs):
        """
        __init__ Method sets public-instance attribiutes
        """
        from models import storage

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        form = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, datetime.strptime(value, form))
                    elif key == "id":
                        setattr(self, key, str(value))
                    else:
                        setattr(self, key, value)

    def to_dict(self):
        """
        Return dictionary representation of instance
        """
        self_dict = self.__dict__.copy()
        self_dict["__class__"] = type(self).__name__
        self_dict["created_at"] = self_dict["created_at"].isoformat()
        self_dict["updated_at"] = self_dict["updated_at"].isoformat()

        return self_dict

    def save(self):
        """
        Update updated_at instance
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Return:
            str representation of the instance
        """
        rep = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return rep
