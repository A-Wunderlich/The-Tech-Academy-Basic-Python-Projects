

import sqlite3

conn = sqlite3.connect('text.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lastname TEXT,\
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('text.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lastname, col_email) VALUES (?,?,?)", \
                ('Sarah','Jones','sarahjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lastname, col_email) VALUES (?,?,?)", \
                ('Sally','May','msmay.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lastname, col_email) VALUES (?,?,?)", \
                ('Kevin','Bacon','kbacon@rocketmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('text.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lastname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name:{}\nEmail:{}".format(item[0],item[1],item[2])
    print(msg)
conn.close()
