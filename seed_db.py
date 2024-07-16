from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud, auth

db: Session = SessionLocal()

modele1 = schemas.ModeleCreate(nom="Model S", cylindree="3000cc")
modele2 = schemas.ModeleCreate(nom="Model X", cylindree="2000cc")
crud.create_modele(db, modele=modele1)
crud.create_modele(db, modele=modele2)

voiture1 = schemas.VoitureCreate(immatriculation="123-ABC", date_mise_circulation="2023-07-01", date_fabrication="2023-06-01", modele_id=1)
voiture2 = schemas.VoitureCreate(immatriculation="456-DEF", date_mise_circulation="2023-08-01", date_fabrication="2023-07-01", modele_id=2)
crud.create_voiture(db, voiture=voiture1)
crud.create_voiture(db, voiture=voiture2)

client1 = schemas.ClientCreate(nom="Gaudre", prenom="Hugo", email="hugo.gaudre@example.com", telephone="1234567890")
client2 = schemas.ClientCreate(nom="Smith", prenom="Antoine", email="antoine.smith@example.com", telephone="0987654321")
crud.create_client(db, client=client1)
crud.create_client(db, client=client2)

employe1 = schemas.EmployeCreate(nom="Admin", prenom="Admin", email="admin@example.com", role="manager", password="password")
employe2 = schemas.EmployeCreate(nom="Vendeur", prenom="Vendeur", email="vendeur@example.com", role="vendeur", password="password")
crud.create_employe(db, employe=employe1)
crud.create_employe(db, employe=employe2)

vente1 = schemas.VenteCreate(voiture_id=1, client_id=1, employe_id=1, date_vente="2023-07-10")
vente2 = schemas.VenteCreate(voiture_id=2, client_id=2, employe_id=2, date_vente="2023-08-10")
crud.create_vente(db, vente=vente1)
crud.create_vente(db, vente=vente2)

db.close()
