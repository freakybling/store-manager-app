import sqlite3

#adding a database file.
def connect():
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS perfume_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                stock INTEGER,
                price REAL)
                """)
    conn.commit()
    conn.close()

#function for adding a perfume
def add_perfume(name, stock, price):
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO perfume_inventory (name, stock, price) VALUES (?,?,?)", (name, stock, price))
    conn.commit()
    conn.close()

#get all perfumes:
def get_all_perfumes():
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM perfume_inventory")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


#search perfume name:
def search_perfume(name):
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM perfume_inventory WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#update perfume:
def update_perfume(id,stock,price):
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("UPDATE perfume_inventory SET stock = ?, price = ? WHERE id = ?", (stock, price, id))
    conn.commit()
    conn.close()

def delete_perfume_by_id(id):
    conn = sqlite3.connect("perfumes.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM perfume_inventory WHERE id = ?", (id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    connect()
    # print("Database connected and table created (if not existed already).")