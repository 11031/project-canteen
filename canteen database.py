import sqlite3


con=sqlite3.connect('canteen124543.db')
cursor=con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Cold_Dish(Id integer primary key,name text, price real, quantity real)')
cursor.execute('CREATE TABLE IF NOT EXISTS Hot_Dish(Id integer primary key, name text, price real,quantity real)')
cursor.execute('CREATE TABLE IF NOT EXISTS Sweets(Id integer primary key, name text, price real)')
cursor.execute('CREATE TABLE IF NOT EXISTS Drinks(Id integer primary key, name text, price real)')
cursor.execute('CREATE TABLE IF NOT EXISTS Quantity(Name_Food text primary key,ingredients text)')
con.commit()
con.close()


def join_Cold():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    cursor.execute('''SELECT quantity
        FROM Cold_Dish
        INNER JOIN Quantity
        ON Cold_Dish.quantity=Quantity.ingredients
    ''')
    con.commit()
    con.close()

def join_hot():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    cursor.execute('''SELECT quantity
        FROM Hot_Dish
        INNER JOIN Quantity
        ON Hot_Dish.quantity=Quantity.ingredients
    ''')
    con.commit()
    con.close()

def Add_Cold():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    da="INSERT INTO Cold_Dish(Id,name,price,quantity) VALUES(?,?,?,?)"
    cursor.execute()
    con.commit()
    con.close()


def Add_Hot():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    da="INSERT INTO Hot_Dish(Id,name,price,quantity) VALUES(?,?,?,?)"
    cursor.execute()
    con.commit()
    con.close()

def Add_sweets():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    da="INSERT INTO Sweets(Id,name,price) VALUES(?,?,?)"
    cursor.execute()
    con.commit()
    con.close()

def Add_drinks():
    con=sqlite3.connect('canteen124.db')
    cursor=con.cursor()
    da="INSERT INTO Drinks(Id,name,price) VALUES(?,?,?)"
    cursor.execute()
    con.commit()
    con.close()
   
    







