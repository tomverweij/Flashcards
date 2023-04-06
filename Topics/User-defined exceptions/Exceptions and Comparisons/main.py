class WordError(Exception):
    pass
    # def __str__(self):
        # print("yo, worderror")

def check_w_letter(word):
    if 'w' in word:
        raise WordError
    else:
        return word


# word = input()
# check_w_letter(word)