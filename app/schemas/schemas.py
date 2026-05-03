from pydantic import BaseModel
from datetime import date

# add to portfolio schema
class AddDomain(BaseModel):
    user_id: int
    domain_name: str
    buy_price: float
    buy_date: date
