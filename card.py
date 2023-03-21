while True:
    card_number = input("Введите номер карты: ")
    if card_number.isdigit() and len(card_number) == 16 and (card_number.startswith('1234') or card_number.startswith('0987')):
        hidden_number = "**** **** **** " + card_number[-4:]
        print(hidden_number)
        break
    else:
        print("Номер карты должен содержать ровно 16 цифр и начинаться с 1234 или 0987. Попробуйте еще раз.")

