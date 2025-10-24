import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "db"),
    database=os.getenv("DB_NAME", "todosdb"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASS", "postgres")
)

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL
)
""")
cur.execute("INSERT INTO todos (task) VALUES ('Learn Docker') ON CONFLICT DO NOTHING;")
cur.execute("INSERT INTO todos (task) VALUES ('Multi-stage Build') ON CONFLICT DO NOTHING;")
conn.commit()
cur.close()
conn.close()
print("Database initialized!")
