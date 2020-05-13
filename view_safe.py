import sqlite3
import os
import sys


def main():
    print("Welcome to the safe! Please enter your password")
    password = "Barrys2e5!"  # Password
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


def access():
    print("-"*15)
    print("Files in the safe \n")
    cur.execute('SELECT name, ext FROM Files')
    rows = cur.fetchall()
    fdict = {fdict: [] for fdict in range(1, len(rows))}
    i = 1
    for row in rows:
        f = row[0] + row[1]
        print(str(i), '. ', f)
        fdict[i] = f
        i += 1
    print("-"*15)
    print("Enter the number of the file you want to access. Enter x to return to menu.")
    a = input()
    if a == 'x':
        return
    filename = fdict[int(a)]
    n, e = os.path.splitext(filename)
    cur.execute('SELECT file FROM Files WHERE name = ? and ext = ?', (n, e,))
    try:
        data = cur.fetchone()[0]
        abs = os.path.join(r'c:\Users\Akush\Desktop', filename)
        with open(abs, 'wb') as file:
            file.write(data)
        cur.execute('DELETE FROM Files WHERE name = ? and ext = ?', (n, e,))
        print("The file is on your desktop, remember to re-add to the safe folder after quitting the view safe.")
    except:
        print("File does not exist")


def delete():
    print("-"*15)
    print("Files in the safe")
    cur.execute('SELECT name, ext FROM Files')
    rows = cur.fetchall()
    fdict = {fdict: [] for fdict in range(1, len(rows))}
    i = 1
    for row in rows:
        f = row[0] + row[1]
        print(str(i), '. ', f)
        fdict[i] = f
        i += 1
    print("-"*15)
    print("Enter the number of the file you want to delete. Enter x to return to menu.")
    a = input()
    if a == 'x':
        return
    filename = fdict[int(a)]
    n, e = os.path.splitext(filename)
    try:
        cur.execute('DELETE FROM Files WHERE name = ? and ext = ?', (n, e,))
        print("File deleted.")
    except:
        print("File does not exist")


def quit():
    cur.close()
    conn.commit()
    sys.exit()


if __name__ == '__main__':
    # Filename for your safe
    conn = sqlite3.connect(r'C:\Users\akush\Desktop\Programming\Projects\Safe_Sql\safe.sqlite')
    cur = conn.cursor()  # create a cursor connection, use OOP to facilitate the connection in the main function
    main()
