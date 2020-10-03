#!/usr/bin/env python3
import os
import requests as requests
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

def clear_transcriptions(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    transcriptions = []
    sids = []
    transcriptions = client.transcriptions.list()
    for transcript in transcriptions:
        sids.append(transcript.sid)
    for sid in sids:
        client.transcriptions(sid).delete()
        print(sid)
    
    return None

if __name__ == "__main__":
    clear_transcriptions(account_sid, auth_token)