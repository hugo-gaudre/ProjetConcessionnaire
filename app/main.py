from fastapi import FastAPI, Depends, HTTPException, status, Request, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import timedelta
from jose import JWTError, jwt
from . import crud, models, schemas, auth
from .database import SessionLocal, engine

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
    if not token.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = token[len("Bearer "):]  # Remove "Bearer " from the token

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_employe_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.get_employe_by_email(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/modeles/", response_model=List[schemas.Modele])
def read_modeles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    modeles = crud.get_modeles(db, skip=skip, limit=limit)
    return modeles

@app.post("/modeles/", response_model=schemas.Modele)
def create_modele(modele: schemas.ModeleCreate, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    return crud.create_modele(db=db, modele=modele)


# Voitures
@app.get("/voitures/", response_model=List[schemas.Voiture])
def read_voitures(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    voitures = crud.get_voitures(db, skip=skip, limit=limit)
    return voitures

@app.post("/voitures/", response_model=schemas.Voiture)
def create_voiture(voiture: schemas.VoitureCreate, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    return crud.create_voiture(db=db, voiture=voiture)

# Clients
@app.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    return crud.create_client(db=db, client=client)

# Employes
@app.get("/employes/", response_model=List[schemas.Employe])
def read_employes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    employes = crud.get_employes(db, skip=skip, limit=limit)
    return employes

@app.post("/employes/", response_model=schemas.Employe)
def create_employe(employe: schemas.EmployeCreate, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    return crud.create_employe(db=db, employe=employe)

# Ventes
@app.get("/ventes/", response_model=List[schemas.Vente])
def read_ventes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    ventes = crud.get_ventes(db, skip=skip, limit=limit)
    return ventes

@app.post("/ventes/", response_model=schemas.Vente)
def create_vente(vente: schemas.VenteCreate, db: Session = Depends(get_db), token: str = Header(...)):
    current_user = get_current_user(token, db)
    return crud.create_vente(db=db, vente=vente)