from sqlalchemy.orm import Session
from . import models, schemas, auth

# Pour les modeles de voitures
def get_modele(db: Session, modele_id: int):
    return db.query(models.Modele).filter(models.Modele.id == modele_id).first()

def get_modeles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Modele).offset(skip).limit(limit).all()

def create_modele(db: Session, modele: schemas.ModeleCreate):
    db_modele = models.Modele(**modele.dict())
    db.add(db_modele)
    db.commit()
    db.refresh(db_modele)
    return db_modele

# Pour les voitures
def get_voiture(db: Session, voiture_id: int):
    return db.query(models.Voiture).filter(models.Voiture.id == voiture_id).first()

def get_voitures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Voiture).offset(skip).limit(limit).all()

def create_voiture(db: Session, voiture: schemas.VoitureCreate):
    db_voiture = models.Voiture(**voiture.dict())
    db.add(db_voiture)
    db.commit()
    db.refresh(db_voiture)
    return db_voiture

# Pour les Clients
def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Pour les Employés
def get_employe_by_email(db: Session, email: str):
    return db.query(models.Employe).filter(models.Employe.email == email).first()

def get_employe(db: Session, employe_id: int):
    return db.query(models.Employe).filter(models.Employe.id == employe_id).first()

def get_employes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employe).offset(skip).limit(limit).all()

def create_employe(db: Session, employe: schemas.EmployeCreate):
    hashed_password = auth.get_password_hash(employe.password)
    db_employe = models.Employe(
        nom=employe.nom, prenom=employe.prenom, email=employe.email, role=employe.role, hashed_password=hashed_password
    )
    db.add(db_employe)
    db.commit()
    db.refresh(db_employe)
    return db_employe

# Pour les Ventes
def get_vente(db: Session, vente_id: int):
    return db.query(models.Vente).filter(models.Vente.id == vente_id).first()

def get_ventes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vente).offset(skip).limit(limit).all()

def create_vente(db: Session, vente: schemas.VenteCreate):
    db_vente = models.Vente(**vente.dict())
    db.add(db_vente)
    db.commit()
    db.refresh(db_vente)
    return db_vente
