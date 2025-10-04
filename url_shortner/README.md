---

# URL Shortener

A simple URL shortener built with Python and FastAPI. It generates short codes for long URLs and redirects users to the original address.

## Features
- Generate unique short codes for any URL  
- Store mappings in a database (SQLite by default)  
- Redirect users from short links to the original URL  
- Easy to extend with analytics, custom aliases, or expiration dates  

## How it works
1. User submits a long URL to the `/shorten` endpoint.  
2. The service generates a random short code and stores the mapping.  
3. Visiting `/{code}` looks up the original URL and redirects the browser.  

## Quickstart
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Shorten a URL:
   ```bash
   POST http://127.0.0.1:8000/shorten
   Body: { "url": "https://example.com" }
   ```
4. Visit the short link:
   ```
   http://127.0.0.1:8000/<short_code>
   ```

## Next Steps
- Add analytics to track clicks  
- Support custom short codes  
- Deploy to a cloud platform with a custom domain  

---
