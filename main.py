# importerar funktioner från random-modulen för att använda för slumpmässiga tal
import random


# lista för att spara användarens antal gissningar varje omgång
user_amount_guess_highscore_list = []


# -------- OMGÅNGEN BÖRJAR ----------
# en evighetsloop som fortsätter så länge användaren vill spela
while True:

    # välkomstmeddelande till användaren med instruktioner.
    print('Välkommen till detta spel.')
    print('Jag tänker på en siffra mellan')
    print('1 och 99. Försökt att gissa rätt!')
    print(' ')
    print('Om du är nära kommer ett meddelande')
    print('att skrivas ut!')
    print('* --- * --- * --- * --- * --- * --- *')

    # datorns slumpmässigt genererade tal
    computer_random_number = random.randint(1, 99)

    # initierar variabeln för att spara användarens antal gissningar nuvarande omgång
    user_amount_guess_current_round = 0

    # -------- GISSNINGSOMGÅNG BÖRJAR ----------
    # en evighetsloop som fortsätter så länge användaren inte gissat rätt
    while True:

        # ett mellanrum för snygghet i konsolen
        print(' ')

        # Frågar efter och sparar användarens gissning.
        user_guess = int(input('Gissa på ett tal mellan 1 och 99!: '))

        # en enklare felhantering, men behöver förbättras - till exempel om användaren inte
        # skriver in ett heltal
        if user_guess < 1 or user_guess > 99:
            print(' ')
            print('Du behöver gissa på ett tal mellan 1 och 99!')
            continue

        # om användaren skriver in en godtagbar siffra ökas antalet gissningar för omgången med + 1
        user_amount_guess_current_round += 1

        # om användaren gissar rätt bryts loopen och vi går vidare till nästa del utanför
        if user_guess == computer_random_number:
            break

        # om användarens gissning är lägre än datorn uppmanas hen att gissa högre
        elif user_guess < computer_random_number:
            print(' ')
            print('Gissa på ett högre tal!')

        # om användarens gissning är högre än datorn uppmanas hen att gissa lägre
        elif user_guess > computer_random_number:
            print(' ')
            print('Gissa på ett lägre tal!')

        # räknar ut och sparar skillnaden mellan användarens gissning och datorns tal
        difference_between_user_and_computer = user_guess - computer_random_number

        # om användarens gissning är nära, skriver datorn ut ett extra meddelande
        if difference_between_user_and_computer > -6 and difference_between_user_and_computer < 6:
            print('Du är nära nu!')

        # eftersom att vi inte tagit emot rätt svar, fortsätter loopen

    # -------- OMGÅNGEN FÄRDIG ----------
    # sparar antalet gissningar från omgången
    user_amount_guess_highscore_list.append(user_amount_guess_current_round)

    # skriver ut ett grattis-meddelande om användarens vinst, med intressant information
    print(f'Bra jobbat! Du gissade rätt på {computer_random_number} med endast {user_amount_guess_current_round} '
          f'gissningar!')
    print(' ')

    # ger användaren möjligheten att spela igen
    print('Vill du spela igen? Ja / Nej')

    # initierar menyvalet som sedan avgörs i en enklare felhantering nedan
    user_menu_choice = ""

    # enklare felhantering för att samla in användarens korrekta svar
    while True:

        # tar emot och konverterar användarens svar till gemener
        user_menu_choice = input().lower()

        # om användarens svar varken är ja eller nej, skickas ett felmeddelande med hjälpande information ut
        # och loopen upprepar sig
        if user_menu_choice != 'ja' and user_menu_choice != 'nej':
            print('Du behöver skriva in: Ja eller Nej')
            continue

        # om vi tagit emot ett ja eller nej bryter vi loopen och programmet fortsätter
        else:
            break

    # om användaren säger ja, börjar hela loopen om
    if user_menu_choice == 'ja':

        print(' ')
        print('* --- * --- * --- * --- * --- * --- *')
        print('* --- * --- * NY OMGÅNG * --- * --- *')
        print('* --- * --- * --- * --- * --- * --- *')
        print(' ')
        continue

    # om användaren säger nej, avbryts loopen och programmet avslutas
    else:
        break

# sorterar highscore-listan från lägst till högst för att kunna ge användaren det lägsta antalet gissningar.
user_amount_guess_highscore_list.sort()

# skriver ut tackinformation tillsammans med antal gissningar från användarens bästa omgång.
print(' ')
print(f'Tack för att du spelade med mig! Din bästa omgång gissade du endast {user_amount_guess_highscore_list[0]}')
print('Hoppas vi ses igen!')
