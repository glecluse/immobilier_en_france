import unittest
from src.views.login import is_password_secure


class TestPasswordSecurity(unittest.TestCase):
    
    def test_too_short(self):
        self.assertEqual(is_password_secure("court"), "Le mot de passe doit contenir au moins 12 caractères.")

    def test_missing_uppercase(self):
        self.assertEqual(is_password_secure("long_sans_majuscule!"), "Le mot de passe doit contenir au moins une majuscule.")

    def test_missing_lowercase(self):
        self.assertEqual(is_password_secure("LONG_SANS_MINUSCULE!"), "Le mot de passe doit contenir au moins une minuscule.")

    def test_missing_digit(self):
        self.assertEqual(is_password_secure("Long_sans_chiffre!"), "Le mot de passe doit contenir au moins un chiffre.")

    def test_missing_special_character(self):
        self.assertEqual(is_password_secure("Long_sans_caractere_special1"), "Le mot de passe doit contenir au moins un caractère spécial (!@#$%^&*...).")

    def test_valid_password(self):
        self.assertEqual(is_password_secure("Mot_de_pass_long_securise1!"), "Mot de passe sécurisé.")

if __name__ == '__main__':
    unittest.main()
