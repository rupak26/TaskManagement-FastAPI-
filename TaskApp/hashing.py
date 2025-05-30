from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasing:
    def hashPassword(password):
        return pwd_context.hash(password)
    def verify(plain_password , hashed_password):
        return pwd_context.verify(plain_password , hashed_password)