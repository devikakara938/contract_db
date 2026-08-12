from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.core.security import (
    get_password_hash,
    verify_password
)

from backend.app.schemas.user import (
    UserCreate,
    UserOut
)

from backend.app.models.user import User
from backend.app.database import get_db


router = APIRouter()


# REGISTER
@router.post("/register", response_model=UserOut)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Check whether email already exists
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Hash the password
    hashed = get_password_hash(user.password)

    # Create new user
    db_user = User(
        email=user.email,
        hashed_password=hashed
    )

    # Save user to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# LOGIN / PASSWORD VERIFICATION
@router.post("/login")
def login_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Find user by email
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify entered password with stored hashed password
    password_valid = verify_password(
        user.password,
        db_user.hashed_password
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "email": db_user.email
    }