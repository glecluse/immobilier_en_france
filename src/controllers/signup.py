from src.models.session import Session


def signup(login, mdp):
    print("[signup] Création de session...")
    s = Session(login, mdp)

    created = s.signin()
    print("[signup] Résultat de s.signin() :", created)

    if created:
        s.logged = True
        s.persist()
        print("[signup] Inscription réussie.")
        return True
    else:
        print("[signup] Échec de l'inscription (déjà existant ?)")
        return False
