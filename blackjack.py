from time import sleep
import random

class Blackjack:
    def __init__(self):
        self.full_deck = {'1♧': 1, '2♧': 2, '3♧': 3, '4♧': 4, '5♧': 5, '6♧': 6, '7♧': 7, '8♧': 8, '9♧': 9, '10♧': 10, 'J♧': 10, 'Q♧': 10, 'K♧': 10, 'A♧': 11,
                          '1♤': 1, '2♤': 2, '3♤': 3, '4♤': 4, '5♤': 5, '6♤': 6, '7♤': 7, '8♤': 8, '9♤': 9, '10♤': 10, 'J♤': 10, 'Q♤': 10, 'K♤': 10, 'A♤': 11,
                          '1♢': 1, '2♢': 2, '3♢': 3, '4♢': 4, '5♢': 5, '6♢': 6, '7♢': 7, '8♢': 8, '9♢': 9, '10♢': 10, 'J♢': 10, 'Q♢': 10, 'K♢': 10, 'A♢': 11,
                          '1♡': 1, '2♡': 2, '3♡': 3, '4♡': 4, '5♡': 5, '6♡': 6, '7♡': 7, '8♡': 8, '9♡': 9, '10♡': 10, 'J♡': 10, 'Q♡': 10, 'K♡': 10, 'A♡': 11}
        self.deck_pop = []
        self.shuffled_deck = []

    def shuffle(self):
        wanna_play = input("Welcome to the table, would you like me to deal you in the next hand?\n('y'/'n' or 'q' to quit): ")
        if wanna_play.lower() == 'y':
            sleep(1.5)
            print("Glad you decided to join us. Shuffling the cards now")
            self.shuffled_deck = list(self.full_deck.items())
            random.shuffle(self.shuffled_deck)
            sleep(1.5)
            print("Cards have been shuffled! Let's PLAY!")
            sleep(1.5)
            self.dealer_cards()
        elif wanna_play.lower() == 'n' or wanna_play.lower() == 'q':
            sleep(2)
            print("Ya snooze, ya lose. You're missing out on a great game!")
            sleep(2)
            return
        else:
            print("Invalid selection. Try again")
            self.shuffle()

    def dealer_cards(self):
        dealer_value = 0

        first_card, first_value = self.shuffled_deck.pop()
        self.deck_pop.append((first_card, first_value))
        sleep(.5)
        print(f"The dealer is showing {first_card}")

        dealer_value = first_value

        second_card, second_value = self.shuffled_deck.pop()
        self.deck_pop.append((second_card, second_value))

        print(f"The dealer's second card is face down, you can't see it!")

        dealer_value = first_value + second_value

        if dealer_value == 21:
            self.dealer_win(dealer_value)

        if dealer_value > 21:
            self.win(dealer_value)

        self.user_cards(dealer_value)

    def user_cards(self, dealer_value):
        user_value = 0
        valueA = 0
        blackjack = False
        print("These are your cards, don't show them to anyone:")

        first_card, first_value = self.shuffled_deck.pop()
        print(first_card, first_value)
        user_value += first_value

        second_card, second_value = self.shuffled_deck.pop()
        print(second_card, second_value)
        user_value += second_value

        if first_card.startswith('A') and second_card[1:] in ('10', 'J', 'Q', 'K'):
            print("You got 21!")
            blackjack = True
            self.win(user_value, dealer_value)
        else:
            if first_card.startswith('A'):
                valueA = int(input("What would you like the value of your A to be? 1 or 11: "))
                if valueA == 1:
                    user_value -= 10
                else:
                    valueA == first_value
            elif second_card.startswith('A') and first_card[1:] in ('10', 'J', 'Q', 'K'):
                print("You got 21!")
                blackjack = True
                self.win(user_value, dealer_value)
            else:
                if second_card.startswith('A'):
                    valueA = int(input("What would you like the value of your A to be? 1 or 11: "))
                if valueA == 1:
                    user_value -= 10
                else:
                    valueA == second_value

        print(f"Your current total is {user_value}")

        if user_value == 21 or blackjack:
            self.win(user_value, dealer_value)
        elif user_value > 21:
            self.bust(user_value, dealer_value)
        else:
            self.hit_or_stay(user_value, dealer_value, valueA)

    def hit_or_stay(self, user_value, dealer_value, valueA):
        hitorstay = input("The goal is to get your total as close to 21 without going over, do you want another card ('HIT') or stick with what you have ('STAY')?:\n")
        if hitorstay.lower() == 'hit':
            self.hit(user_value, dealer_value, valueA)
        elif hitorstay.lower() == 'stay':
            self.stay(user_value, dealer_value)
        else:
            print("Invalid input. Please enter 'HIT' or 'STAY'")
            self.hit_or_stay(user_value, dealer_value, valueA)

    def hit(self, user_value, dealer_value, valueA):
        hit_card, hit_value = self.shuffled_deck.pop()
        self.deck_pop.append((hit_card, hit_value))
        print(f"Your next card is {hit_card} that is {hit_value}")

        user_value += hit_value

        if hit_card.startswith('A'):
            valueA = int(input("What would you like the value of your A to be? 1 or 11: "))
        if valueA == 1:
            user_value -= 10
        else:
            valueA == hit_value

        sleep(1.5)
        print(f"That brings you to a total of {user_value}")

        if user_value == 21:
            self.stay(user_value, dealer_value)

        if user_value > 21:
            self.bust(user_value, dealer_value)
        else:
            self.hit_or_stay(user_value, dealer_value, valueA)

    def stay(self, user_value, dealer_value):
        print("\nYour turn is over! You chose to stay.\n Now it's the dealer's turn!\n")
        sleep(1.5)
        if dealer_value > 21:
            self.win(user_value, dealer_value)

        elif dealer_value > user_value:
            self.dealer_win(user_value, dealer_value)

        elif dealer_value > 17 and dealer_value < 21:
            self.dealer_stay(user_value, dealer_value)

        elif dealer_value < 17:
            self.dealer_hit(user_value, dealer_value)

        elif dealer_value < user_value:
            self.win(user_value, dealer_value)

        elif dealer_value == user_value:
            self.push(user_value, dealer_value)

    def dealer_stay(self, user_value, dealer_value):
        print("The dealer is choosing to stay!")
        if dealer_value < user_value:
            self.win(user_value, dealer_value)
        else:
            self.dealer_win(user_value, dealer_value)

    def dealer_win(self, user_value, dealer_value):
        print(f"Dealer won this hand with {dealer_value}. Better luck next time!")
        sleep(1.5)
        if user_value == dealer_value:
            self.push(user_value, dealer_value)
        else:
            self.playagain()

    def dealer_hit(self, user_value, dealer_value):
        while dealer_value <= 17:
            print("\nThe dealer chose to hit! let's see!\n")
            dealer_hit_card, dealer_hit_value = self.shuffled_deck.pop()
            self.deck_pop.append((dealer_hit_card, dealer_hit_value))
            sleep(1.5)
            print(f"The dealer's card is...\n")
            sleep(1.5)
            print(dealer_hit_card)

            dealer_value += dealer_hit_value

        if dealer_value > 21:
            self.win(user_value, dealer_value)

        if dealer_value == user_value:
            self.push(user_value, dealer_value)

        if dealer_value >= 17:
            self.dealer_stay(user_value, dealer_value)

    def win(self, user_value, dealer_value):
        print(f"You win with {user_value}!  The dealer had {dealer_value}")
        sleep(2)
        self.playagain()

    def push(self, user_value, dealer_value):
        print(f"It's a PUSH! you had {user_value} and the dealer had {dealer_value}")
        sleep(2)
        self.playagain()

    def bust(self, user_value, dealer_value):
        print("BUST! Game over!")
        print(f"The dealer had {dealer_value}")

        sleep(2)
        self.playagain()

    def playagain(self):
        replay = input("Do you want to play again? ('y'/'n'):\n")
        if replay.lower() == 'y':
            if self.deck_pop:
                self.full_deck.update(self.deck_pop)
                self.deck_pop.clear()
            self.shuffle()
        elif replay.lower() == 'n':
            return
        else:
            print("Invalid selection. Try again")
            self.playagain()

game = Blackjack()
game.shuffle()
