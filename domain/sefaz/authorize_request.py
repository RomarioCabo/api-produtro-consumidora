from dataclasses import dataclass, field
from typing import List

from domain.sefaz.customer import Customer
from domain.sefaz.product import Product


@dataclass
class AuthorizeRequest:
    orderNumber: str = field(default=None)
    externalOrderNumber: str = field(default=None)
    customer: Customer = field(default=None)
    products: List[Product] = field(default_factory=list)
