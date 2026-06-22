#Behaviorial

#Observer
class Newsletter:
    def __init__(self):
        self.subscribers=[]

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, headline):
        for i in self.subscribers:
            i.update(headline)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, headline):
        print(f"Hi {self.name},New article published:{headline}")

#Strategy
class CreditCardPayment:
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class UPIPayment:
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")

class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy=payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


tech_newsletter=Newsletter()
A=Subscriber("A")
B=Subscriber("B")

tech_newsletter.subscribe(A)
tech_newsletter.subscribe(B)
tech_newsletter.notify_subscribers("New article on google")

cart1=ShoppingCart(UPIPayment())
cart1.checkout(100)
cart2=ShoppingCart(CreditCardPayment())
cart2.checkout(250)
