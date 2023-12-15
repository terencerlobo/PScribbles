import sqlite3


conn = sqlite3.connect('newdata.db') # creating the db
    create_table_query = ''' create table if not exists personal(ID string, FirstName string, Surame string, Phonenumber string) '''#creating the table if it wont exist
    conn.execute(create_table_query) # running the create table query

    insert_query = ''' insert into personal(ID,FirstName,Surame,phonenumber) values(?,?,?,?)'''
    insert_tuple = (entry1.get(),entry2.get(),entry3.get(),entry4.get())
    cursor = conn.cursor()
    cursor.execute(insert_query,insert_tuple)
    conn.commit()
    conn.close()