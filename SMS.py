import time
from time import sleep
from urllib import response
from sinchsms import SinchSMS

def sendSMS():
    number = 'your_mobile_number'
    app_key = 'your_app_key'
    app_secret = 'your_app_secret'
    message = 'hello my message!!!!'
    client = SinchSMS(app_key, app_secret)
    print("sending '%s' to %s" % (message, number))
    response = client.send_message(number,message)
    message_id = response['messageId']
    response = client.check_status(message_id)

    while response['status'] != 'successful':
          print(response['status'])
          time.sleep(1)
          response = client.check_status(message_id)
          print(response['status'])

if __name__ == "__main__":
    sendSMS()