import sqlite3


conn = sqlite3.connect('data.db')
cursor = conn.cursor()


def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            channel_id TEXT,
            channel_url TEXT,
            display_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS session (
            id INTEGER PRIMARY KEY,
            live_id TEXT,
            title TEXT,
            start_time TEXT,
            end_time TEXT,
            nb_users INTEGER,
            channel_url TEXT,
            display_name TEXT
        )
    ''')

def insert_live_session(v):
    cursor.execute("""
        INSERT INTO session (live_id, title)
        VALUES (?, ?)
    """, (
        v['id'],
        v['title']
    ))
    conn.commit()

# Insert some data
# data_to_insert = [
#     (1, 'Item A', 10.5),
#     (2, 'Item B', 20.0),
#     (3, 'Item C', 5.75)
# ]
# cursor.executemany("INSERT INTO temp_data (id, name, value) VALUES (?, ?, ?)", data_to_insert)
# conn.commit()

# cursor.execute("SELECT * FROM temp_data WHERE value > 10")
# results = cursor.fetchall()

# print("Query Results:")
# for row in results:
#     print(row)

def close_connection():
    conn.close()
