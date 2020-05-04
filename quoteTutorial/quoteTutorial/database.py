import sqlite3

conn = sqlite3.connect('myquotes.db') 
#connect() will connect the piplines to myquotes.db database, if not present, it will create a new one

curr = conn.cursor()

# curr.execute("""create table quotes_db(
#                 quotes text,
#                 author text,
#                 tag text
#                 )""") # execute() is used to execute sql statements

curr.execute("""insert into quotes_db values('Only those are allowed to kill who are ready to die themselves','Lelouch Lamperouge','sacrificial,inspirational')""")

conn.commit()
conn.close()