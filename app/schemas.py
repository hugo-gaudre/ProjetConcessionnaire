from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ModeleBase(BaseModel):
    nom: str
    cylindree: str

class ModeleCreate(ModeleBase):
    pass

class Modele(ModeleBase):
    id: int

    class Config:
        from_attributes = True

class VoitureBase(BaseModel):
    immatriculation: str
    date_mise_circulation: date
    date_fabrication: date
    modele_id: int

class VoitureCreate(VoitureBase):
    pass

class Voiture(VoitureBase):
    id: int
    modele: Modele

    class Config:
        from_attributes = True

class ClientBase(BaseModel):
    nom: str
    prenom: str
    email: str
    telephone: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        from_attributes = True

class EmployeBase(BaseModel):
    nom: str
    prenom: str
    email: str
    role: str

class EmployeCreate(EmployeBase):
    password: str

class Employe(EmployeBase):
    id: int

    class Config:
        from_attributes = True

class VenteBase(BaseModel):
    voiture_id: int
    client_id: int
    employe_id: int
    date_vente: date

class VenteCreate(VenteBase):
    pass

class Vente(VenteBase):
    id: int
    voiture: Voiture
    client: Client
    employe: Employe

    class Config:
        from_attributes = True
