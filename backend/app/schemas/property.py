from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Dict, Optional
from datetime import date

class PropertyBase(BaseModel):
    formatted_address: Optional[str] = Field(None, alias="formattedAddress")
    address_line1: Optional[str] = Field(None, alias="addressLine1")
    address_line2: Optional[str] = Field(None, alias="addressLine2")
    city: Optional[str] = None
    state: Optional[str] = None
    state_flips: Optional[str] = Field(None, alias="stateFlips")
    zip_code: Optional[str] = Field(None, min_length=5, max_length=5, alias="zipCode")
    county: Optional[str] = None
    county_flips: Optional[str] = Field(None, alias="countyFips")
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    property_type: Optional[str] = Field(None, alias="propertyType")
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    square_footage: Optional[int] = Field(None, alias="squareFootage")
    lot_size: Optional[int] = Field(None, alias="lotSize")
    year_built: Optional[int] = Field(None, alias="yearBuilt")
    assessor_id: Optional[str] = Field(None, alias="assessorID")
    legal_description: Optional[str] = Field(None, alias="legalDescription")
    subdivision: Optional[str] = None
    zoning: Optional[str] = None
    last_sale_date: Optional[date] = Field(None, alias="lastSaleDate")
    last_sale_price: Optional[float] = Field(None, alias="lastSalePrice")
    hoa: Optional[Dict[str, Any]] = None
    features: Optional[Dict[str, Any]] = None
    tax_assessments: Optional[Dict[str, Any]] = Field(None, alias="taxAssessments")
    property_taxes: Optional[Dict[str, Any]] = Field(None, alias="propertyTaxes")
    history: Optional[Dict[str, Any]] = None
    owner: Optional[Any] = None
    owner_occupied: Optional[bool] = Field(None, alias="ownerOccupied")


class PropertyCreate(PropertyBase):
    ...


class PropertyUpdate(PropertyBase):
    ...


class PropertyResponse(PropertyBase):
    id: int

    model_config = ConfigDict(from_attributes=True)