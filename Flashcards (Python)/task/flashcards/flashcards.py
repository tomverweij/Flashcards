import random
import sys
import shutil
import argparse

# tx to https://github.com/sergey-shirnin/LoggingStd_In-Out
class LoggerOut:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.filename = filename

    def write(self, message):
        self.terminal.write(message)
        with open(self.filename, "a") as file:
            print(message, file=file, flush=True, end='')

    def flush(self):
        pass


class LoggerIn:
    def __init__(self, filename):
        self.terminal = sys.stdin
        self.filename = filename

    def readline(self):
        entry = self.terminal.readline()
        with open(self.filename, "a") as file:
            print(entry.rstrip(), file=file, flush=True)
        return entry



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
        self.mistakes = 0

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
        self.deck[FlashCard.term] = [FlashCard.definition, FlashCard.mistakes]
        print(f'The pair ("{FlashCard.term}":"{FlashCard.definition}") has been added')

    def remove_card(self):
        term = input('Which card?\n')
        if self.deck.pop(term, 'no card') == 'no card':
            print(f"Can't remove \"{term}\": there is no such card.")
        else:
            print('The card has been removed.')

    def export_file(self, export_to=''):
        if export_to == '':
            file = open(input('File name:\n'), 'w')
        else:
            file = open(export_to, 'w')

        file.write(str(self.deck))
        file.close()
        print(f'{len(self.deck)} cards have been saved.')

    def import_file(self, import_file=''):
        try:
            if import_file == '':
                file = open(input('File name:\n'), 'r')
            else:
                file = open(import_file, 'r')
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
            if def_[0] == definition:
                return True
        return False

    def check_answer(self, term, data):
        print(f"Print the definition of \"{term}\":")
        answer = input()
        definition = data[0]
        if definition == answer:
            print("Correct!")
        else:
            # up the mistakes
            self.deck[term] = [data[0], data[1] + 1]
            # and check how wrong
            for term_, definition_ in self.deck.items():
                if definition_[0] == answer:
                    print('Wrong. The right answer is "{}", but your definition is correct for "{}"'
                          .format(definition, term_))
                    return
            print(f"Wrong. The right answer is \"{definition}\".")

    def reset_stats(self):
        for data in self.deck.values():
            # reset the mistake counter to zero
            data[1] = 0
        print("Card statistics have been reset.")

    def hardest_card(self):
        # order by most mistakes first
        try:
            sorted_deck = dict(sorted(self.deck.items(), key=lambda item: item[1][1], reverse=True))
            # set highest mistake number
            highest = self.deck.get(next(iter(sorted_deck)))[1]
        except StopIteration:
            highest = 0

        if highest == 0:
            print("There are no cards with errors.")
            return

        highest_list = []
        for fc in sorted_deck.items():
            if fc[1][1] == highest:
                highest_list.append(fc[0])
            else:
                break
        if len(highest_list) == 1:
            print(f'The hardest card is "{highest_list[0]}". You have {highest} errors answering it')
        else:
            highest_list_formatted = str(", ".join('"{}"'.format(i) for i in highest_list))
            print(f'The hardest cards are {highest_list_formatted}')


class FlashCardsMenu:
    """Actionhandler for a game of FlashCards"""

    def __init__(self):
        fcs = FlashCards()
        action = []
        # opening a log file capturing stdin and stdout
        # to copy from with write_log()
        default_log = 'default.txt'
        sys.stdout = LoggerOut(default_log)
        sys.stdin = LoggerIn(default_log)

        parser = argparse.ArgumentParser()
        parser.add_argument("--import_from")
        parser.add_argument("--export_to")
        args = parser.parse_args()

        if args.import_from is not None:
            fcs.import_file(args.import_from)

        while True:
            action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
            if action == 'exit':
                if args.export_to is not None:
                    fcs.export_file(args.export_to)
                print('Bye bye!\n')
                break
            else:
                self.handle_action(action, fcs)

    def handle_action(self, action, fcs):
        #add, remove, import, export, ask
        if action == 'add':
            fc = FlashCard(fcs)
            fcs.add_card(fc)
        elif action == 'remove':
            fcs.remove_card()
        elif action == 'import':
            fcs.import_file()
        elif action == 'export':
            fcs.export_file()
        elif action == 'ask':
            ask_nbr = int(input('How many times to ask?\n'))
            q = 0
            while q < ask_nbr:
                term, data = random.choice(list(fcs.deck.items()))
                fcs.check_answer(term, data)
                q += 1
        elif action == 'log':
            self.write_log()
        elif action == 'hardest card':
            fcs.hardest_card()
        elif action == 'reset stats':
            fcs.reset_stats()

    def write_log(self):
        file_name = input("File name:\n")
        shutil.copyfile('default.txt', file_name)
        print("The log has been saved.")

# start the menu
menu = FlashCardsMenu()




