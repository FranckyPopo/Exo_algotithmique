from distutils import command
import sqlite3
import rsa
import tkinter

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def recording(): 
    frame_main.grid_forget()
    frame_recording.grid(row=0, column=0, padx=180, pady=100)
    
    label_email = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse email")
    label_email.grid(row=0, column=0, sticky="w")
    
    enter_email = tkinter.Entry(frame_recording, bg="red")
    enter_email.grid(row=1, column=0, sticky="w")
    
    label_password = tkinter.Label(frame_recording, text="Veuillez entrer vôtre mot de passe")
    label_password.grid(row=2, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_recording)
    enter_password.grid(row=3, column=0, sticky="w")
    
    bnt_connection = tkinter.Button(frame_recording)
    bnt_connection.grid(row=4, column=0, sticky="w")
    

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
            
            conn.commit()
            conn.close()
        except sqlite3.Error:
            print("Une erreur est survenu dans le scripte SQL")
        else:
            print("Fin")
    else:
        print("Impossible de crée vôtre compte veuillez verifier vos différentes informations")
    
    
def connection():
    try:
        get_data = cursor.execute("SELECT * FROM users")
        data_users = get_data.fetchall()
        
        conn.commit()
        conn.close()
    except sqlite3.Error:
        print("Une erreur est survenu dans le scripte SQL")
    else:
        email = input("Veuillez entrer vôtre email: ")
        password = input("Veuillez entrer vôtre mot de passe: ")
        
        for user in data_users:
            if user[2] == email and user[3] == password:
                print("compte existe")
                break
        else:
            print("Le compte n'existe pas !")
    
    
window = tkinter.Tk()
window.geometry("480x320")
window.title("Popo Page")
window.resizable(False, False)

# Création des frames
frame_main = tkinter.Frame(window)
frame_main.grid(row=0, column=0, padx=180, pady=100)

frame_recording = tkinter.Frame(window)

bnt_connection = tkinter.Button(frame_main, text="Inscription", command=recording)
bnt_connection.grid(row=0, column=0, padx=3, pady=5)

bnt_recording = tkinter.Button(frame_main, text="Inscription")
bnt_recording.grid(row=1, column=0, padx=3, pady=5)

window.mainloop()