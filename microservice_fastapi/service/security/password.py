from passlib.hash import argon2

def hashed_password(password: str) -> str:
    return argon2.hash(password)