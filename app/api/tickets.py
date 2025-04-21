from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime

#Model fro a Ticket Type
class TicketType(BaseModel):
    type: Literal["VIP", "Regular", "Early Bird","Student"]
    price: float
    available_quantity: Optional[int] = None
    
#Model for a Event(BaseModel)
class Event(BaseModel):
    event_id: str
    title: str
    description: Optional[str] = None
    location: str
    date: datetime
    has_capacity_limit:bool = False
    max_capacity: Optional[int] = None
    ticket_tiers : List[TicketTier] = []
    organizer: str
    preferences: Optional[List[str]] = []