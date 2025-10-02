import resend
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set API key (make sure your .env has RESEND_API_KEY=your_key_here)
resend.api_key = os.getenv("RESEND_API_KEY")

def mail(to: str, subject: str):
    params: resend.Emails.SendParams = {
        "from": "<onboarding@resend.dev>",
        "to": [to],
        "subject": subject,
        "html": "<p>it works!</p>"
    }
    email = resend.Emails.send(params)
    return email

# Example usage
automail = mail("your mail", "Hello from Resend")
print(automail)
