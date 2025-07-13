# This file is intended for Twilio WhatsApp API Router
from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Form, HTTPException
from twilio.rest import Client
from bot import get_groq_response
from dotenv import load_dotenv
from os import getenv

load_dotenv()

twilio_acc_sid = getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_no = getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(twilio_acc_sid, twilio_auth_token)

wp_router = APIRouter(prefix="/whatsapp", tags=["WhatsApp Twilio API"])

@wp_router.post("/send", response_class=PlainTextResponse)
async def receive_message(Body: str = Form(...), From: str = Form(...)):
    print(f"Getting message from {From}: {Body}")
    
    reply = get_groq_response(Body)
    
    try:
        message = client.messages.create(
            from_=twilio_whatsapp_no,
            body=reply,
            to=From
        )
        return PlainTextResponse("Message sent successfully to WhatsApp EcomAgent")
    
    except Exception as e:
        print("Error", e)
        raise HTTPException(status_code=500, detail="Internal Server Error, Failed to send or receive message from WhatsApp")




