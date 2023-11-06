# integrantes
# Andres feipe castrillon martinez (2380664)
# Johan Alexander Castro Zapata (2380818)
# santiago lopez ramirez  (2380798)
        

# ATM

tarjetas = [
    {"numero": "1234567890", "clave": "1234", "saldo": 10000},
    {"numero": "0987654321", "clave": "4321", "saldo": 5000},
    {"numero": "5678901234", "clave": "5678", "saldo": 20000}
]

menu = """
    Select Option
        1 : Withdraw Money
        2 : Nothing
    """

def pull_money():
    card = input("Enter Number of Card: ")
    print("Reading.....")
    a = 0
    for tarjeta in tarjetas:
        n_card = tarjeta['numero']
        if card in n_card:
            a = 1
            password = input("Enter Password: ")
            if password == tarjeta['clave']:
                if tarjeta['saldo'] >= 10000:
                    while True:
                        try:
                            cash = int(input('Enter the amount: '))
                            if cash <= tarjeta['saldo']:
                                saldo = tarjeta["saldo"] - cash
                                print("\n...Count money...\n")
                                print("\tWithdraw the money")
                                print('Your New Saldo is: {}'.format(saldo))
                            else:
                                print("I'm sorry. I don't have enough money")
                            break
                        except NameError:
                            print("Enter only numbers")
                        except ValueError:
                            print("Enter only numbers int")
                else:
                    print("I'm Sorry, You don't Have money")
                break
            else:
                print('Password Incorrect')
                break
        else:
            continue
    if a == 0:
        print("Oh, Card Incorrect")
    else:
        print("Thanks you")


if __name__ == '__main__':
    # Cree las tarjetas
    print(menu)
    n = int(input())
    if n == 1:
        pull_money()
    else:
        print('Thank You, Come Back Soon')


   
    
