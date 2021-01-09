from nltk.corpus import cmudict
from numpy import random
import pandas as pd
from action import Action


class Haiku(Action):



    def __init__(self, seven_file, five_file):
        super().__init__('%haiku', "Sends a haiku made from your chat!")
        self.sevens = seven_file
        self.fives = five_file
        self.word_dictionary = cmudict.dict()


    def brute_count(self,word):
        count = 0
        vowels = 'aeiouy'
        punctuation = """.!?:,"'*"""
        word = word.lower()
        word = ''.join([l if l not in punctuation else '' for l in word]) #remove punctuation
        if word == '':
            return 0

        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count += 1
        if count == 0:
            count += 1
        return count


    def count_syllables(self, word):
        word = word.lower()

        try:
            return [len(list(y for y in x if y[-1].isdigit()))
                   for x in self.word_dictionary[word.lower()]][0]  # digits indicate new syllable
        except KeyError:
            return self.brute_count(word)


    def count_line(self, line):
        if line is None:
            return 0
        return sum([self.count_syllables(word)
                    for word in line.split() ])


    def save_line(self, line):
        syl_count = self.count_line(line)
        path = ''

        if syl_count == 5:
            path = self.fives
        elif syl_count == 7:
            path = self.sevens
        else:
            return

        try:
            with open(path, 'a') as f:
                f.write(line.replace('\n', ' ') + '\n')
        except:
            pass


    def pick_lines(self, path, n=None):
        with open(path, 'r') as f:
            content = f.readlines()[:]  ##cut the header
        return random.choice(content, size=n)


    def write_haiku(self):
        first, third = self.pick_lines(self.fives, 2)
        second = self.pick_lines(self.sevens)

        return f"{first}{second}{third}" #file already contains newline characters


    def do(self):
        return write_haiku()


    def preprocess(self, message):
        self.save_line(message)
