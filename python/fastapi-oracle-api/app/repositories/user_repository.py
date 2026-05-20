from app.models.user import User
from app.core.database import SessionLocal

def get_users():
    session = SessionLocal()
    return session.query(User).all()

def create_user(user: schemas.UserCreate):
    session = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
