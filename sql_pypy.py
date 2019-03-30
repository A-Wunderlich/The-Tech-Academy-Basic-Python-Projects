import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS txt_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fname TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
txtList = [file for file in fileList if file.endswith('.txt') ]

conn = sqlite3.connect('drill.db')
       
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO txt_files(fname) VALUES (?)", \
                (txtList[0],))
    cur.execute("INSERT INTO txt_files(fname) VALUES (?)", \
                (txtList[1],))
    conn.commit()
conn.close()

print(txtList)
