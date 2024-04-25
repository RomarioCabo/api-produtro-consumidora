from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    sku: int
    amount: int
    value: Decimal
    icmsValue: Decimal
    pisValue: Decimal
    difaulValue: Decimal
    fcpIcmsValue: Decimal
