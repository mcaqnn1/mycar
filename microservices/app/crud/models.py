from crud.base import BaseService
from models.users import Users
from models.hotels import Hotels
from models.rooms import Rooms

class UsersDAO(BaseService):
    model = Users

class HotelsDAO(BaseService):
    model = Hotels

class RoomsDAO(BaseService):
    model = Rooms