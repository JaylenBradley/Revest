from sqlalchemy.orm import Session
from ..models import Property
from ..schemas import PropertyCreate

def create_property(property: dict, db: Session):
    db_property = Property(**property)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def get_properties(skip: int, limit: int, db: Session):
    return db.query(Property).offset(skip).limit(limit).all()

def get_property(id: int, db: Session):
    return db.get(Property, id)

def update_property(id: int, property_data: dict, db: Session):
    db_property = get_property(id, db)
    if not db_property:
        return None

    for field, val in property_data.items():
        if hasattr(db_property, field):
            setattr(db_property, field, val)

    db.commit()
    db.refresh(db_property)
    return db_property

def delete_property(id: int, db: Session):
    db_property = get_property(id, db)
    if not db_property:
        return False

    db.delete(db_property)
    db.commit()
    return True