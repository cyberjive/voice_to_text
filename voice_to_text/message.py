#!/usr/bin/env python3
import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


def message():
    #create an of the Client object instance
    client = Client(account_sid, auth_token)

    #return the most recent transcription ID from Twilios REST API
    transcription = client.transcriptions.list(limit=1)

    #get the sid of the voicemail and store it for our retrieval call
    sid = transcription[0].sid

    #fetch the transcription and assign it
    t = client.transcriptions(sid).fetch()
    #print the last message
    print(t.transcription_text)

    return None


if __name__ == "__main__":
	message()