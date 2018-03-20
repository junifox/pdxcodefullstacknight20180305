def credit_card_validation(card_number):
    card_number = card_number.split()
    for i in range(len(card_number)):
        card_number[i] = int(card_number[i])
    check_digit = card_number.pop()
    card_number.reverse()
    for i in range(0,len(card_number),2):
        card_number[i] *=2
    for i in range(len(card_number)):
        if card_number[i] > 9:
            card_number[i] -= 9
    sum_num = sum(card_number)
    second_digit = int(list(str(sum_num))[1])
    return second_digit == check_digit


if __name__ == '__main__':
    credit_card = (input("Enter Your Credit Card Number: "))
    if (credit_card_validation(credit_card)):
        print("Valid Number")
    else:
        print("Invalid Number")
