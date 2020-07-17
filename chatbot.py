from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from wit import Wit
import sys
import json
import time

access_token = 'TAFEVEZXXZNSBTKPAH3KKTAB2GPJIULQ'
client = Wit(access_token)

#Below variables would be taken from the app, examples are given for the
#purpose of this code

accname = 'Aydan'
collection_status = 2 #taken from collection segments on confluence page
bill_id = 'Rogers'
bill_amount = 250


def get_message():
    client_text = input()
    resp = str(client.message(client_text))
    resp = resp.replace("\'", "\"")
    return resp
    
def get_intent(resp):
    data = json.loads(resp)
    if (str(data["intents"]) == "[]"):
        print("I'm sorry, I didn't get that")
        return get_intent(get_message())
    return data["intents"][0]["name"]
    
def end_conversation():
    print("Did this solve your problem?")
    if(get_intent(get_message()) == "yes"):
        time.sleep(0.5)
        print("I'm glad to hear it. Thanks for banking with Scotia")
    else:
        time.sleep(0.5)
        print("Sorry I couldn't help out, you can speak with a human representative at 1 (800) 472-6842")


print(f'Hi {accname}, I noticed you have some concerns with an upcoming bill payment from {bill_id} for ${bill_amount}. I’d like to know more about your problem and how I can assist you!')
message = get_intent(get_message())
if(message == "overdraft"):
    time.sleep(0.5)
    print("I see you have some concerns about account overdraft. Let me take a look at your account")
    time.sleep(0.5)
    if collection_status == 1:
        print("Looks like that hasn't been an issue for you. If you want to protect your account, I recommend Scotiabank overdraft protection. Take a look here https://bb.scotiabank.com/personal/chequing-and-savings/overdraft-protection.html") 
    elif collection_status < 5:
        print("Based on your good history as a Scotiabank customer, I'm able to waive the fee this time")
    else:
        print("If you're having repeated issues with payment, try speaking with a representative or going to a branch")
    end_conversation()
elif(message == "unable_to_pay"):
    time.sleep(0.5)
    print("If you need cash quickly, try applying for a line of credit or loan")
    time.sleep(0.5)
    print("Here's where you can get started https://www.scotiabank.com/ca/en/personal/loans-lines/line-of-credit/scotialine-personal-line-of-credit-students.html")
    end_conversation()
else:
    print("sorry, I can't help with that right now")


