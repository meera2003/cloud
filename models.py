from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def  __repr__(self):
        return f"<User {self.username}>"


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String,nullable=False)
    contact = Column(String, nullable=False)
    email = Column(String)
    address = Column(String, nullable=False)
     