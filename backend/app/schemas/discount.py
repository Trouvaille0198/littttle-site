from typing import List, Optional
from pydantic import BaseModel


class Discount(BaseModel):
    name: str
    link: str
    img_url: str
    discount: str
    current_price: str
    previous_price: str
