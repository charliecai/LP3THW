from lexicon import *

class ParserError(Exception):
    pass

class Sentence(object):
    
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

class WordList(object):
    def __init__(self, word_list):
        self.word_list = word_list

    def peek(self):
        if self.word_list:
            word = self.word_list[0]
            return word[0]

    def match(self, expecting):
        if self.word_list:
            word = self.word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self, word_type):
        while self.peek() == word_type:
            self.match(word_type)

    def parse_subject(self):
        self.skip('stop')
        next_word = self.peek()

        if next_word == 'noun':
            return self.match('noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

    def parse_verb(self):
        self.skip('stop')

        if self.peek() == 'verb':
            return self.match('verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_object(self):
        self.skip('stop')
        next_word = self.peek()

        if next_word == 'noun':
            return self.match('noun')
        elif next_word == 'direction':
            return self.match('direction')
        else:
            raise ParserError("Expected a noun or direction next.")

def parse_sentence(word_list):
    subj = word_list.parse_subject()
    verb = word_list.parse_verb()
    obj = word_list.parse_object()

    return Sentence(subj, verb, obj)



something = input("Please input the something: \n")
x = scan(something)
print("Something scaned: ", x)

word_list = WordList(x)
Sentence = parse_sentence(word_list)
print(Sentence.subject, Sentence.verb, Sentence.object)