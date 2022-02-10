import sqlite3
import rsa

def recording():
    last_name = input("veuillez entrer vôtre nom: ")
    firs_name = input("veuillez entrer vôtre prénom: ")
    email = input("veuillez entrer vôtre email: ")
    password = input("veuillez entrer vôtre mot de passe: ")
    password_2 = input("veuillez confirmer le mot de passe: ")
    
    if last_name and firs_name and email and (password == password_2):
        # Le programme crype le mot de passe
        priv_key, pub_key = rsa.newkeys(512)
        password_encrypt = rsa.encrypt(password_2.encode(), pub_key)
        
        data_user = {
            "last_name": last_name,
            "firs_name": firs_name,
            "email": email,
            "password": password_encrypt
        }
        
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                last_name text,
                firs_name text,
                email text,
                password text
                )
            """
            )
            cursor.execute("INSERT INTO users VALUES (:last_name, :firs_name, :email, :password)", data_user)
            
            connection.commit()
            connection.close()
        except sqlite3.Error:
            print("Une erreur est survenu dans le scripte SQL")
        else:
            print("Fin")
    else:
        print("Impossible de crée vôtre compte veuillez verifier vos différentes informations")
    
recording()