from fastapi import FastAPI, Depends
from config import engine
from models.models import Base
from routers import auth, todos, users
from company import companyapis, dependencies

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(companyapis.router,
                   prefix='/companyapis',
                   tags=['companysapis'],
                   dependencies=[Depends(dependencies.get_token_header)],
                   responses={418: {'description': 'Internal use Only'}})
