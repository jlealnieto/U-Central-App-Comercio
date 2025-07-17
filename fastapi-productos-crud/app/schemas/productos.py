from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    categoria: str
    imagen_guia: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True