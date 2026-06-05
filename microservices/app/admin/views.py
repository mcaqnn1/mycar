from sqladmin import ModelView
from models.users import Users
from models.hotels import Hotels
from models.rooms import Rooms

class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    can_delete = False
    name = "User"
    name_plural = "Users"

class HotelsAdmin(ModelView,model=Hotels):
    column_list = [
        Hotels.name, 
        Hotels.location,
        Hotels.services,
        Hotels.room_quantity,
        Hotels.rooms
    ]
    can_delete = False
    name="Hotel"
    name_plural="Hotels"

class RoomsAdmin(ModelView,model=Rooms):
    column_list = [
        Rooms.name,
        Rooms.description,
        Rooms.price,
        Rooms.quantity
    ]
    can_delete = False
    name = "Room"
    name_plural = "Rooms"