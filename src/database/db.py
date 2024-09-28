import sqlite3

DB_FILE = 'mappings.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_dota_accounts (
                        discord_id TEXT PRIMARY KEY,
                        dota_account_id INTEGER
                    )''')
    conn.commit()
    conn.close()

def register_dota_account(discord_id, dota_account_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''INSERT OR REPLACE INTO user_dota_accounts (discord_id, dota_account_id)
                      VALUES (?, ?)''', (discord_id, dota_account_id))
    conn.commit()
    conn.close()

def get_dota_account(discord_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT dota_account_id FROM user_dota_accounts WHERE discord_id = ?', (discord_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]
    return None

init_db()