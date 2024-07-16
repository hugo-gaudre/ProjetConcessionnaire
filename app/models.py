from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Modele(Base):
    __tablename__ = "modeles"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), unique=True, index=True)
    cylindree = Column(String(255))

class Voiture(Base):
    __tablename__ = "voitures"
    id = Column(Integer, primary_key=True, index=True)
    immatriculation = Column(String(255), unique=True, index=True)
    date_mise_circulation = Column(Date)
    date_fabrication = Column(Date)
    modele_id = Column(Integer, ForeignKey("modeles.id"))
    modele = relationship("Modele")

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    telephone = Column(String(15))

class Employe(Base):
    __tablename__ = "employes"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(50))

class Vente(Base):
    __tablename__ = "ventes"
    id = Column(Integer, primary_key=True, index=True)
    voiture_id = Column(Integer, ForeignKey("voitures.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    employe_id = Column(Integer, ForeignKey("employes.id"))
    date_vente = Column(Date)
    voiture = relationship("Voiture")
    client = relationship("Client")
    employe = relationship("Employe")
