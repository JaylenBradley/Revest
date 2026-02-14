import requests
from app.core import settings, get_db
from app.crud import create_property
from app.schemas import PropertyCreate

headers = {
    'accept' : 'application/json',
    'X-Api-Key' : settings.rentcast_api_key
}

batch_size = int(input("How many properties to do want to ingest (1-500)? "))
while batch_size < 1 or batch_size > 500:
    int(input("Invalid number: How many properties to do want to ingest (1 - 500)? "))

response = requests.get(
    "https://api.rentcast.io/v1/properties/random",
    headers=headers,
    params = {"limit" : batch_size}
)

db = next(get_db())
successful = 0

for property in response.json():
    try:
        pydantic_property = PropertyCreate(**property)
        create_property(pydantic_property.model_dump(), db)
        successful += 1
    except Exception as e:
        print(f"Failed to create property {e}")
    finally:
        db.close()

print(f"Number of properties successfully ingested: {successful}")