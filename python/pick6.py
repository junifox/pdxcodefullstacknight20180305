import random

payout = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

def main():
    winning_ticket = pick6()
    earnings = 0
    expenses = 0

    for i in range(100000):
        ticket = pick6()
        expenses -= 2
        matches = num_matches(winning_ticket, ticket)
        earnings += payout[matches]
        balance = earnings + expenses
    print("Your total balance is" + str(balance))


main()
