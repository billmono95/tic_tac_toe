griglia = ['-', '-', '-',
           '-', '-', '-',
           '-', '-', '-']
player1 = True

winner = None


def dgri():
    print(griglia[0] + ' | ' + griglia[1] + ' | ' + griglia[2])
    print(griglia[3] + ' | ' + griglia[4] + ' | ' + griglia[5])
    print(griglia[6] + ' | ' + griglia[7] + ' | ' + griglia[8])


dgri()


def fun():
    global player1
    global winner
    def play():

        if player1:
            H = input("Inserire un numero da 1-9: ")
            while (H != "1" and H !="2" and H!="3" and H!="4" and H!="5" and H!="6" and H!="7" and H!="8" and H!="9"):
                H = input("Inserire un numero da 1-9: ")
            H = int(H)-1
            while (griglia[H]!='-'):
                H = input("Numero già occupato: ")
                H = int(H) - 1
            griglia[H] = 'X'

        else:
            H = input("Inserire un numero da 1-9: ")
            while (H != "1" and H != "2" and H != "3" and H != "4" and H != "5" and H != "6" and H != "7" and H != "8" and H != "9"):
                H = input("Inserire un numero da 1-9: ")
            H = int(H)-1
            while (griglia[H]!='-'):
                H = input("Numero già occupato: ")
                H = int(H) - 1
            griglia[H] = 'O'

    play()

    dgri()


    if (griglia[0]== griglia[1] == griglia[2]!='-'):
         print("vincitore"+' '+winner)
    elif (griglia[3] == griglia[4]== griglia[5] != '-'):
        print("vincitore" + ' ' + winner)
    elif (griglia[6] == griglia[7] == griglia[8]!='-'):
         print("vincitore"+' '+winner)
    elif (griglia[0]==griglia[3] == griglia[6]!='-'):
         print("vincitore"+' '+winner)
    elif (griglia[1] == griglia[4] ==  griglia[7]!='-'):
         print("vincitore"+' '+winner)
    elif (griglia[2]== griglia[5] == griglia[8]!='-'):
         print("vincitore"+' '+winner)
    elif (griglia[0] == griglia[4] == griglia[8] != '-'):
         print("vincitore" + ' ' + winner)
    elif (griglia[2] == griglia[4] == griglia[6] != '-'):
        print("vincitore" + ' ' + winner)
    elif (griglia[0] != '-' and griglia[1] != '-' and griglia[2] != '-' and griglia[3] != '-' and griglia[4] != '-' and \
            griglia[5] != '-' and griglia[6] != '-' and griglia[7] != '-' and griglia[8] != '-'):
        print("fine del gioco: pareggio")
    else:
        if (player1 == True):
            player1 = False
            winner = 'O'
        elif (player1==False) :
            player1 = True
            winner = 'X'
        fun()



fun()
