from fastapi import FastAPI
from app.database import engine
from app.routers import productos

app = FastAPI()

# Create the database tables
@app.on_event("startup")
async def startup():
    import app.models.productos
    app.models.productos.Base.metadata.create_all(bind=engine)

app.include_router(productos.router)