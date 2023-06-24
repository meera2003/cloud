from fastapi import FastAPI, status, HTTPException, Depends
from database import get_db, engine
import models
from sqlalchemy.orm import Session 

app = FastAPI()

users = []

models.Base.metadata.create_all(bind=engine)


@app.get('/')
def home():
    return "This is a home page"

@app.get('/about')
def about(name: str, surname: str):
    return f"This is a about page for {name} {surname}"


@app.get('/signup', status_code=201)
def create_user(username: str, password: str, email: str, db: Session = Depends(get_db)):
    new_user = models.User(username=username, password=password, email=email)
    db.add(new_user)
    db.commit()

    print("********************************")
    print(users)
    print("********************************")
    return "User created"


@app.get('/login')
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    print("User", user)
    if user:
        if user.password == password:
            return "Sign in successful"
    
    return "Username or password incorrect"

@app.get('/delete-profile', status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(username: str, password: str):
    for i,user in enumerate(users):
        if user['username'] == username and user['password'] == password:
            del users[i]
            return "user profile deleted successfully"
    
    raise HTTPException(status.HTTP_404_NOT_FOUND ,detail="Username or password incorrect")


@app.get('/update-password')
def delete_profile(username: str, old_password: str, new_password: str):
    for i,user in enumerate(users):
        if user['username'] == username and user['password'] == old_password:
            user['password'] = new_password
            users[i] = user
            return "user password updated successfully"
        
    raise HTTPException(status.HTTP_404_NOT_FOUND ,detail="Username or password incorrect")


