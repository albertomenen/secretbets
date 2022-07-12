from replit import clear

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for  bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"El ganador es {winner} con una apuesta de {highest_bid}")

while not bidding_finished:
    name= input( "Como te llamas?")
    price = int(input("Cual es tu apuesta? $"))
    # Aqui declaramos que las apuestas estan asociadas.
    bids[name] =  price
    should_continue = input("Hay alguna otra apuesta? Pon 'Si'  o 'No'")
    if should_continue == "No":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Si"
    # Esta es la función para reiniciar
        clear()

        bids = {

        "Alberto": 123,
        "Pepe":345,
        "Toni":234,
        "Vivis":654
        }

        find_highest_bidder(bids)
