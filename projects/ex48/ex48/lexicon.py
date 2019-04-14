def scan(text):
    words = text.split()
    result = []

    directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
    verbs = ('go', 'stop', 'kill', 'eat')
    stops = ('the', 'in', 'of', 'from', 'at', 'it')
    nouns = ('door', 'bear', 'princess', 'cabinet')

    for word in words:
        if word in directions:
            word_append = 'direction', word
        elif word in verbs:
            word_append = 'verb', word
        elif word in stops:
            word_append = 'stop', word
        elif word in nouns:
            word_append = 'noun', word
        elif convert_number(word):
            word_append = 'number', word
        else:
            word_append = 'error', word

        result.append(word_append)

    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

sentence = input("Please input the sentence: \n")
print(scan(sentence))