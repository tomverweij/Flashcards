class flashcard:
    """A deck of cards to help remember stuff"""
    all_flashcards = []
    size = 0

    def __init__(self, term, definition):
        while term in self.all_flashcards:
            print('The term "{}}" already exists. Try again:'.format(term))
            term = input()
        else:
            self.term = term
        self.definition = definition
        flashcard.all_flashcards.append(self)

    def check_answer(self, answer):
        if self.definition == answer:
            print("Correct!")
        else:
            print(f"Wrong. The right answer is \"{self.definition}\".")


print("Input the number of cards:")
flashcard.size = int(input())

count = 0
while count < flashcard.size:
    print(f"The term for card #{count+1}:")
    term = input()
    print(f"The definition for card #{count+1}:")
    definition = input()
    fc = flashcard(term, definition)
    count += 1

for fc in flashcard.all_flashcards:
    print(f"Print the definition of \"{fc.term}\":")
    answer = input()
    fc.check_answer(answer)



