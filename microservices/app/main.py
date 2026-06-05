from fastapi import FastAPI
from api.v1.routes.users import router as user_router
from api.v1.routes.hotels import router as hotels_router
from sqladmin import Admin
from worker import lifespan
from core.database.config import engine
from admin.views import UsersAdmin,HotelsAdmin,RoomsAdmin
import uvicorn

app = FastAPI(
    title="Microservice with FastAPI",
    lifespan=lifespan
)
app.include_router(user_router)
app.include_router(hotels_router)

admin = Admin(app=app,engine=engine)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)