#!/usr/bin/env python3
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)


@app.route("/record", methods=["POST"])
def record():
    """ Returns TwiML which prompts the caller to record a message"""
    # Define TwiML response object
    response = VoiceResponse()

    # Make sure this is the first call to our URL and record and transcribe
    if 'RecordingSid' not in request.form:
        # Use <Say> verb to provide an outgoing message
        response.say("Hello, please leave your message after the tone.")

        # Use <Record> verb to record incoming message and set the transcribe argument to true
        response.record(transcribe_callback="/message")
                        #transcribe=True)

        #return status message
        print(str(response))
    else:
        # Hang up the call
        print("Hanging up...")
        response.hangup()
    return str(response)


@app.route("/message", methods=["POST"])
def message():
    """ Creates a client object and returns the transcription text to an SMS message"""
    #create a client object and pass it our secure authentication variables
    client = Client()

    #return the most recent transcription ID from Twilios REST API
    transcription = client.transcriptions.list(limit=1)

    #get the sid of the voicemail and store it for our retrieval call
    sid = transcription[0].sid

    #fetch the transcription and assign it
    t = client.transcriptions(sid).fetch()
    
    #create a text message and send ourselves the text
    m = client.messages \
        .create(
            body = str(t.transcription_text),
            from_='<your-twilio-phone-number>',
            to='<your-personal-phone-number>'
        )
    print(t.transcription_text)
    print(m.sid)
    return str(sid)


if __name__ == "__main__":
    app.run()