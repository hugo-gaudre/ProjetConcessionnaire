from app.database import engine, Base
from app.models import Modele, Voiture, Client, Employe, Vente

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully")

if __name__ == "__main__":
    init_db()
