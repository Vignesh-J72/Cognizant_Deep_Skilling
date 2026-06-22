class CommunicationManager:
    def __init__(self,message):
        self.message=message
    
    def sendWhatsapp(self,Number):
        print("Sending message through whatsapp to number ",Number)
    
    def sendFacebook(self,Profile):
        print("Sending message to the facebook profile: ",Profile)
    
    def sendSMS(self,Number):
        print("Sending message to the phone number: ",Number)


if __name__=="__main__":
    message="Hi. How have you been?"
    Facebook_messenger=CommunicationManager(message)
    Facebook_messenger.sendFacebook("Big joey")
    Whatsapp_messenger=CommunicationManager(message)
    Whatsapp_messenger.sendWhatsapp("0000000000")
    SMS_messenger=CommunicationManager(message)
    SMS_messenger.sendSMS("0000000000")
    

    
    