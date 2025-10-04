from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import sqlite3, string, random

app = FastAPI()

# Database setup
conn = sqlite3.connect("urls.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS urls (short TEXT PRIMARY KEY, long TEXT)")
conn.commit()

class URLRequest(BaseModel):
    url: str

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.post("/shorten")
def shorten(req: URLRequest):
    code = generate_code()
    cursor.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (code, req.url))
    conn.commit()
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    cursor.execute("SELECT long FROM urls WHERE short=?", (code,))
    row = cursor.fetchone()
    if row:
        return RedirectResponse(row[0])  # real browser redirect
    raise HTTPException(status_code=404, detail="Not found")
