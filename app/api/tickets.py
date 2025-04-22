from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime

#Model for a Ticket Type
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

#Model for a Customer 
class Customer(BaseModel):
    customer_id: str
    name: str
    email:str
    phone: Optional[str] = None

#Model for a Booking(Basemodel)
class Booking(BaseModel):
    booking_id:str
    customer_id: str
    event_id: str
    tier: str
    quantity: int
    total_price: float
    booking_time: datetime
    paid: bool = False
    payment_method: Optional[str] = None
    payment_time: Optional[datetime] = None
    status: Literal["Pending", "Confirmed", "Cancelled"] = "Pending"
    cancellation_time: Optional[datetime] = None
    cancellation_reason: Optional[str] = None
    refund_time: Optional[datetime] = None
    refund_amount: Optional[float] = None
    refund_status: Optional[Literal["Pending", "Processed", "Failed"]] = None
    refund_reason: Optional[str] = None
    refund_method: Optional[str] = None