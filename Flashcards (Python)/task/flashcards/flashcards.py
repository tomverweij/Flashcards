class FlashCard:

    def __init__(self, FlashCards):
        print(f"The term for card #{len(FlashCards.deck) + 1}:")
        while True:
            term = input()
            if FlashCards.term_exists(term):
                print('The term "{}" already exists. Try again:'.format(term))
            else:
                break

        print(f"The definition for card #{len(FlashCards.deck) + 1}:")
        while True:
            definition = input()
            if FlashCards.definition_exists(definition):
                print('The definition "{}" already exists. Try again:'.format(definition))
            else:
                break
        self.term = term
        self.definition = definition
        # add it to the deck
        FlashCards.add_card(self)

    def __str__(self):
        return 'Term "{}" defined as "{}"'.format(self.term, self.definition)


class FlashCards:
    deck = {}

    def __init__(self):
        pass

    def __str__(self):
        return str(self.deck)

    def add_card(self, FlashCard):
        self.deck[FlashCard.term] = FlashCard.definition

    def term_exists(self, term):
        return False if self.deck.get(term) is None else True

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

# initialize deck
fcs = FlashCards()
print("Input the number of cards:")
init_length = int(input())

# enter the required amount of cards
while len(fcs.deck) < init_length:
    fc = FlashCard(fcs)
    fcs.add_card(fc)

# check answers
for term, definition in fcs.deck.items():
    fcs.check_answer(term, definition)


