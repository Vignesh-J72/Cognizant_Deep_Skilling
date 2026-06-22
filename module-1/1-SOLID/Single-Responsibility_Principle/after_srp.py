class WhatsappManager:
    def __init__(self,message):
        self.message=message
    
    def sendWhatsapp(self,Number):
        print("Sending message to the whatsapp number:", Number)

class FacebookManager: 
     def __init__(self,message):
        self.message=message  
     def sendFacebook(self,Profile):
        print("Sending message to the facebook profile: ",Profile)

class SMSManager:
    def __init__(self,message):
        self.message=message
    def sendSMS(self,Number):
        print("Sending message to the phone number: ",Number)

if __name__=="__main__":
    message="Hi. How have you been?"
    Facebook_messenger=FacebookManager(message)
    Facebook_messenger.sendFacebook("Johnny Bravo")
    Whatsapp_messenger=WhatsappManager(message)
    Whatsapp_messenger.sendWhatsapp("0000000000")
    SMS_messenger=SMSManager(message)
    SMS_messenger.sendSMS("0000000000")
