from typing import Any, Dict, Optional
from pydantic import BaseModel


class UnifiedEvent(BaseModel):
    parser: str
    event: Optional[str] = None
    timestamp: Optional[str] = None
    host: Optional[str] = None
    vendor: Optional[str] = None
    product: Optional[str] = None
    user: Optional[str] = None
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    severity: Optional[str] = None
    data: Dict[str, Any] = {}