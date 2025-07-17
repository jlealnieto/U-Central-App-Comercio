from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.productos import ProductoCreate, ProductoUpdate, ProductoResponse
from app.crud.productos import create_producto, get_producto, update_producto, delete_producto, get_all_productos

router = APIRouter()

@router.post("/productos/", response_model=ProductoResponse)
async def create_new_producto(producto: ProductoCreate):
    return await create_producto(producto)

@router.get("/productos/", response_model=List[ProductoResponse])
async def read_productos():
    return await get_all_productos()

@router.get("/productos/{producto_id}", response_model=ProductoResponse)
async def read_producto(producto_id: int):
    producto = await get_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return producto

@router.put("/productos/{producto_id}", response_model=ProductoResponse)
async def update_existing_producto(producto_id: int, producto: ProductoUpdate):
    updated_producto = await update_producto(producto_id, producto)
    if updated_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return updated_producto

@router.delete("/productos/{producto_id}", response_model=dict)
async def delete_existing_producto(producto_id: int):
    result = await delete_producto(producto_id)
    if not result:
        raise HTTPException(status_code=404, detail="Producto not found")
    return {"detail": "Producto deleted successfully"}