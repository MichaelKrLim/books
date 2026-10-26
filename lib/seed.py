from lib.connection import create_connection

def seed(filepath):
    conn = create_connection()
    commands=open(filepath, 'r').read()
    with conn.cursor() as cur:
        cur.execute(commands)
    conn.commit()
    conn.close()
