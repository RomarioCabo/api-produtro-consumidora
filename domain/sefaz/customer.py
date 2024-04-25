from dataclasses import dataclass, field


@dataclass
class Customer:
    id: str = field(default=None)
    name: str = field(default=None)
    document: str = field(default=None)
    documentType: str = field(default=None)
    personType: str = field(default=None)
    address: str = field(default=None)
    addressNumber: str = field(default=None)
    addressComplement: str = field(default=None)
    district: str = field(default=None)
    city: str = field(default=None)
    state: str = field(default=None)
    country: str = field(default=None)
    zipCode: str = field(default=None)
    ibgeCode: str = field(default=None)
    phoneNumber: str = field(default=None)
    email: str = field(default=None)
