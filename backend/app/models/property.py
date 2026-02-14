from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, JSON, String, UniqueConstraint
from sqlalchemy.sql import func
from ..core import Base

class Property(Base):
    __tablename__ = "properties"
    __table_args__ = (
        UniqueConstraint("county", "assessor_id", name="unique_county_assessor"),
    )

    id = Column(Integer, primary_key=True, index=True)
    formatted_address = Column(String, unique=True, index=True)
    address_line1 = Column(String)
    address_line2 = Column(String)
    city = Column(String, index=True)
    state = Column(String, index=True)
    state_flips = Column(String)
    zip_code = Column(String)
    county  = Column(String)
    county_flips  = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    property_type = Column(String, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    square_footage = Column(Integer)
    lot_size = Column(Integer)
    year_built = Column(Integer)
    assessor_id = Column(String, index=True)
    legal_description = Column(String)
    subdivision = Column(String)
    zoning = Column(String)
    last_sale_date = Column(Date)
    last_sale_price = Column(Float)
    hoa = Column(JSON, nullable=True)
    features = Column(JSON, nullable=True)
    tax_assessments = Column(JSON, nullable=True)
    property_taxes = Column(JSON, nullable=True)
    history = Column(JSON, nullable=True)
    owner = Column(JSON, nullable=True)
    owner_occupied = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())