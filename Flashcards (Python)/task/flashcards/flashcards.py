import random

class FlashCard:
    """Term to remember. Definition on the back."""

    def __init__(self, FlashCards):
        print(f"The card:")
        while True:
            term = input()
            if FlashCards.term_exists(term):
                print('The card "{}" already exists. Try again:'.format(term))
            else:
                break

        print(f"The definition of the card:")
        while True:
            definition = input()
            if FlashCards.definition_exists(definition):
                print('The definition "{}" already exists. Try again:'.format(definition))
            else:
                break
        self.term = term
        self.definition = definition

    def __str__(self):
        return 'Term "{}" defined as "{}"'.format(self.term, self.definition)

class FlashCards:
    """Deck of cards with terms to remember"""
    deck = {}

    def __init__(self):
        pass

    def __str__(self):
        return str(self.deck)

    def add_card(self, FlashCard):
        self.deck[FlashCard.term] = FlashCard.definition
        print(f'The pair ("{FlashCard.term}":"{FlashCard.definition}") has been added')

    def remove_card(self):
        term = input('Which card?\n')
        if self.deck.pop(term, 'no card') == 'no card':
            print(f"Can't remove \"{term}\": there is no such card.")
        else:
            print('The card has been removed.')

    def export_file(self):
        file = open(input('File name:\n'), 'w')
        file.write(str(self.deck))
        file.close()
        print(f'{len(self.deck)} cards have been saved.')

    def import_file(self):
        try:
            file = open(input('File name:\n'), 'r')
        except FileNotFoundError:
            print('File not found.')
        else:
            import_fcs = eval(file.read())
            file.close()
            # add and merge
            self.deck.update(import_fcs)
            print(f'{len(import_fcs)} cards have been loaded.')

    def term_exists(self, term):
        return True if self.deck.get(term) is not None else False

    def definition_exists(self, definition):
        for def_ in self.deck.values():
            if def_ == definition:
                return True
        return False

    def check_answer(self, term, definition):
        print(f"Print the definition of \"{term}\":")
        answer = input()
        if definition == answer:
            print("Correct!")
        else:
            for term_, definition_ in self.deck.items():
                if definition_ == answer:
                    print('Wrong. The right answer is "{}", but your definition is correct for "{}"'
                          .format(definition, term_))
                    return
            print(f"Wrong. The right answer is \"{definition}\".")


class FlashCardsMenu:
    """Actionhandler for a game of FlashCards"""

    def __init__(self):
        fcs = FlashCards()
        action = []
        while True:
            action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
            if action == 'exit':
                break
            else:
                self.handle_action(action, fcs)
        print('Bye bye!\n')

    def handle_action(self, action, FlashCards):
        #add, remove, import, export, ask
        if action == 'add':
            fc = FlashCard(FlashCards)
            FlashCards.add_card(fc)
        elif action == 'remove':
            FlashCards.remove_card()
        elif action == 'import':
            FlashCards.import_file()
        elif action == 'export':
            FlashCards.export_file()
        elif action == 'ask':
            ask_nbr = int(input('How many times to ask?\n'))
            q = 0
            while q < ask_nbr:
                term, definition = random.choice(list(FlashCards.deck.items()))
                FlashCards.check_answer(term, definition)
                q += 1
        elif action == 'log':
            pass
        elif action == 'hardest card':
            pass
        elif action == 'reset stats':
            pass

# start the menu
menu = FlashCardsMenu()




