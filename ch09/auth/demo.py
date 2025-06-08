from pydantic import BaseModel
from typing import List, Optional

class PersonModel(BaseModel):
    username: Optional[str]
    password: Optional[str]
    age: Optional[int]
    salary: Optional[float]