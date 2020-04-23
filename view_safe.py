import sqlite3
import os
import sys

def access():
    print("-"*15)
    print("Files in the safe")
    cur.execute('SELECT name, ext FROM Files')
    rows = cur.fetchall()
    for row in rows:
        f = row[0] + row[1]
        print(f)
    print("-"*15)
    print("Enter name of file to access, enter z to return to main menu")
    n = input()
    if n == 'z':
        return
    print("Enter extension of file to access, include the ., enter z to return to main menu")
    e = input()
    if e == 'z':
        return
    filename = n+e
    cur.execute('SELECT file FROM Files WHERE name = ? and ext = ?',(n,e,))
    try:
        data = cur.fetchone()[0]
        abs = os.path.join(r'c:\Users\Akush\Desktop',filename)
        with open(abs, 'wb') as file:
            file.write(data)
        cur.execute('DELETE FROM Files WHERE name = ? and ext = ?',(n,e,))
        print("The file is on your desktop, remember to re-add to the safe folder after quitting the view safe.")
    except:
        print("File does not exist")

def delete():
    print("-"*15)
    print("Files in the safe")
    cur.execute('SELECT name, ext FROM Files')
    rows = cur.fetchall()

    for row in rows:
        f = row[0] + row[1]
        print(f)

    print("-"*15)
    print("Enter name of file to delete, enter z to the main menu")
    n = input()
    if n == 'z':
        return
    print("Enter extension of file to delete, include the ., enter z to the main menu")
    e = input()
    if e == 'z':
        return
    try:
        cur.execute('DELETE FROM Files WHERE name = ? and ext = ?',(n,e,))
        print("File deleted.")
    except:
        print("File does not exist")

def quit():
    cur.close()
    conn.commit()
    sys.exit()

if __name__ == '__main__':
    conn = sqlite3.connect(r'C:\Users\akush\Desktop\Programming\Personal Projects\Safe_sql\safe.sqlite')
    cur = conn.cursor()
    print("Welcome to the safe! Please enter your password")
    password = "Barrys2e5!"
    while True:
        p = input()
        if p == password:
            break
        else:
            print("Incorrect, please re-enter")
            continue

    print("-"*15)
    while True:
        print("Commands:")
        print("a - Access the safe")
        print("d - Delete a file")
        print("q - Quit program")

        print("Enter your command exactly!")
        cm = input()

        if cm == 'a':
            access()
        elif cm == 'd':
            delete()

        elif cm == 'q':
            quit()
        else:
            print("Please re-enter!")
            continue
