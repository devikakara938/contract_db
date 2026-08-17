from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token
)

from backend.app.schemas.user import (
    UserCreate,
    UserOut,
    UserUpdate
)

from backend.app.models.user import User
from backend.app.database import get_db
from backend.app.core.auth import get_current_user, require_role
from backend.app.core.roles import UserRole


router = APIRouter()


# REGISTER
@router.post("/register", response_model=UserOut)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed = get_password_hash(user.password)

    db_user = User(
        email=user.email,
        hashed_password=hashed
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# LOGIN
@router.post("/login")
def login_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_valid = verify_password(
        user.password,
        db_user.hashed_password
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "email": db_user.email,
        "role": db_user.role
    }


# GET ALL USERS
@router.get("/", response_model=list[UserOut])
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users


# GET USER BY ID
@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return db_user


# UPDATE USER
@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user.email is not None:
        existing_user = db.query(User).filter(
            User.email == user.email,
            User.id != user_id
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        db_user.email = user.email

    if user.password is not None:
        db_user.hashed_password = get_password_hash(
            user.password
        )

    if user.name is not None:
        db_user.name = user.name

    if user.department is not None:
        db_user.department = user.department

    if user.salary is not None:
        db_user.salary = user.salary

    db.commit()
    db.refresh(db_user)

    return db_user


# DELETE USER - ADMIN ONLY
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(
        require_role(UserRole.ADMINISTRATOR)
    )
):
    db_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(db_user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }