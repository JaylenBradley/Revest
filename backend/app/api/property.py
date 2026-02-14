from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from ..core import get_db
from ..crud import property as property_crud
from ..schemas import PropertyCreate, PropertyUpdate, PropertyResponse

router = APIRouter(prefix="/property", tags=["Property"])

@router.post("", response_model=PropertyResponse)
async def create_property_handler(request: Request, data: PropertyCreate, db: Session = Depends(get_db)):
    try:
        property = property_crud.create_property(data.model_dump(), db)
        return property
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Property with this formatted address already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create property")


@router.get("", response_model=List[PropertyResponse])
async def get_properties_handler(request: Request, skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    try:
        properties = property_crud.get_properties(skip, limit, db)
        return properties
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve properties")


@router.get("/{id}", response_model=PropertyResponse)
async def get_property_handler(request: Request, id: int, db: Session = Depends(get_db)):
    try:
        property = property_crud.get_property(id, db)
        if not property:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return property
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve property")


@router.patch("/{id}", response_model=PropertyResponse)
async def update_property_handler(request: Request, id: int, data: PropertyUpdate, db: Session = Depends(get_db)):
    try:
        property = property_crud.update_property(id, data.model_dump(exclude_unset=True), db)
        if not property:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return property
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update property")


@router.delete("/{id}", status_code=204)
async def delete_property_handler(request: Request, id: int, db: Session = Depends(get_db)):
    try:
        deleted = property_crud.delete_property(id, db)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete property")