from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import auth, models

db: Session = SessionLocal()
# Ce fichier ma servis pour recrypter un mot de passe par exemple ici j'ai recrypter le mot de passe de l'utilisateur avec l'email 
user = db.query(models.Employe).filter(models.Employe.email == "hugo.david@icloud.com").first()

if user:
    user.hashed_password = auth.get_password_hash("hugo123")
    db.commit()

db.close()
