from src.models.session import Session
import json

def auth(login, mdp):
    s = Session(login, mdp)
    s.login()
    if s.logged:
        s.persist()
        return True
    return False

def logout():
    with open("session.json", "w") as f:
        json.dump({"email": ""}, f)