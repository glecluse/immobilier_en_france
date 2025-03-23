from src.controllers.signup import signup
from src.controllers.auth import auth

print("==== TEST INSCRIPTION ====")
res = signup("jean@test.com", "Password123!")
print("Inscription réussie ?" , res)

print("\n==== TEST CONNEXION ====")
res = auth("jean@test.com", "Password123!")
print("Connexion réussie ?" , res)
