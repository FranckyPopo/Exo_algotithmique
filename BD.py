import sqlite3
import tkinter
from tkinter import messagebox

def display_recording():
    frame_main.place_forget()
    frame_recording.place(x=150, y=80)
    
    
def display_connection():
    frame_connection.place(x=150, y=180)
    frame_main.place_forget()
    frame_recording.place_forget()


def check_recording():
    frame_main.place_forget()
    
    last_name = enter_last_name.get()
    firs_name = enter_firs_name.get()
    email = enter_email.get()
    password = enter_password.get()
    password_2 = enter_password_2.get()
    
    if last_name and firs_name and email and (password == password_2):
        data_user = {
            "last_name": last_name,
            "firs_name": firs_name,
            "email": email,
            "password": password_2
        }
        
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
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
            messagebox.showinfo("Inscription", "Vous venez de crée un compte")
            label_error.config(fg="white")
            
    else:
        label_error.config(fg="red")

    
def check_connection():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        get_data = cursor.execute("SELECT * FROM users")
        data_users = get_data.fetchall()
        conn.commit()
        conn.close()
    except sqlite3.Error:
        print("Une erreur est survenu dans le scripte SQL")
    else:
        email = enter_email_connection.get()
        password = enter_password_connection.get()
        
        for user in data_users:
            if user[2] == email and user[3] == password:
                frame_x.place(x=125, y=200)
                frame_connection.place_forget()
                break
        else:
            label_error_2.config(fg="red")


def back_recording():
    frame_recording.place_forget()
    frame_main.place(x=250, y=150)


def back_connection():
    frame_connection.place_forget()
    frame_main.place(x=250, y=150)
    
    
window = tkinter.Tk()
window.geometry("720x480")
window.title("Popo Page")
window["bg"] = "white"
window.resizable(False, False)

# Frame principale
frame_main = tkinter.Frame(window, bg="white")
frame_main.place(x=250, y=150)

bnt_recording = tkinter.Button(frame_main, text="Inscription", relief="flat", command=display_recording)
bnt_recording.grid(row=0, column=0, ipadx=10, ipady=5)

bnt_conn = tkinter.Button(frame_main, text="Connection", relief="flat", command=display_connection)
bnt_conn.grid(row=1, column=0, ipadx=10, ipady=5)

# Frame d'inscription
frame_recording = tkinter.Frame(window, bg="white")

label_last_name = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse nom", bg="white")
label_last_name.grid(row=0, column=0, sticky="w")
enter_last_name = tkinter.Entry(frame_recording, bg="white")
enter_last_name.grid(row=1, column=0, sticky="w")

label_firs_name = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse prénom", bg="white")
label_firs_name.grid(row=2, column=0, sticky="w")
enter_firs_name = tkinter.Entry(frame_recording)
enter_firs_name.grid(row=3, column=0, sticky="w")

label_email = tkinter.Label(frame_recording, text="Veuillez entrer vôtre addresse email", bg="white")
label_email.grid(row=4, column=0, sticky="w")
enter_email = tkinter.Entry(frame_recording)
enter_email.grid(row=5, column=0, sticky="w")

label_password = tkinter.Label(frame_recording, text="Veuillez entrer vôtre mot de passe", bg="white")
label_password.grid(row=7, column=0, sticky="w")
enter_password = tkinter.Entry(frame_recording)
enter_password.grid(row=8, column=0, sticky="w")

label_password_2 = tkinter.Label(frame_recording, text="Veuillez confirmer le mot de passe", bg="white")
label_password_2.grid(row=9, column=0, sticky="w")
enter_password_2 = tkinter.Entry(frame_recording)
enter_password_2.grid(row=10, column=0, sticky="w")

label_error = tkinter.Label(frame_recording, text="Veuillez remplir tout les champ", bg="white", fg="white")
label_error.grid(row=11, column=0, sticky="w")

bnt_recording = tkinter.Button(frame_recording, text="S'inscrire", command=check_recording)
bnt_recording.grid(row=12, column=0, sticky="w", ipadx=3, ipady=2)

bnt_back = tkinter.Button(frame_recording, text="Retour", command=back_recording)
bnt_back.grid(row=13, column=0, sticky="w", ipadx=3, ipady=2)

# frame de connection
frame_connection = tkinter.Frame(window, bg="white")
label_email_connection = tkinter.Label(frame_connection, text="Veuillez entrer vôtre addresse nom", bg="white")
label_email_connection.grid(row=0, column=0, sticky="w")
enter_email_connection = tkinter.Entry(frame_connection, bg="white")
enter_email_connection.grid(row=1, column=0, sticky="w")

label_password_connection = tkinter.Label(frame_connection, text="Veuillez entrer vôtre mot de passe", bg="white")
label_password_connection.grid(row=2, column=0, sticky="w")
enter_password_connection = tkinter.Entry(frame_connection, bg="white")
enter_password_connection.grid(row=3, column=0, sticky="w")

label_error_2 = tkinter.Label(frame_connection, text="Une erreur est survenue lors de la connection", bg="white", fg="white")
label_error_2.grid(row=4, column=0, sticky="w")

bnt_connection = tkinter.Button(frame_connection, text="Se connecter", command=check_connection, bg="white")
bnt_connection.grid(row=5, column=0, sticky="w", ipadx=3, ipady=2)

bnt_back_connection = tkinter.Button(frame_connection, text="Retour", command=back_connection)
bnt_back_connection.grid(row=6, column=0, sticky="w", ipadx=3, ipady=2)

# frame monsieur x
frame_x = tkinter.Frame(window)
label_x = tkinter.Label(frame_x, text="Bienvenue monsieur x", font=("Roboto", 36, "bold"))
label_x.grid(row=0, column=0)

window.mainloop()