import json
import random

class Markov(object):

    def __init__(self, order):
        self.order = order
        self.group_size = self.order + 1
        self.text = None
        self.graph = {}

    def train(self, filename):
        with open(filename, 'r') as f:
            self.text = json.load(f)

        for phraseType in self.text:
          for proverb in self.text[phraseType]:
              prov = proverb.split()
              prov = prov + prov[:self.order]
              for i in range(len(prov)-self.order):
                  key = tuple(prov[i:i + self.order])
                  value = prov[i + self.order]
                  #print("Key: {} \t Value: {}".format(key, value))
                  if key in self.graph:
                      self.graph[key].append(value)
                  else:
                      self.graph[key] = [value]

    def generate(self):
        seed = random.choice([proverb for phraseType in self.text for proverb in self.text[phraseType]]).split()
        result = seed[:self.order]
        # Method 1: Choose a maximum length based on seed (could also be a fixed length)
        #for i in range(len(seed)):
        # Method 2: Finish whenever the phrase ends in a dot
        while result[-1][-1] != '.':
            state = tuple(result[-self.order:])
            next_word = random.choice(self.graph[state])
            result.append(next_word)
            if len(result) > 1000:
              break

        return " ".join(result)

if __name__ == '__main__':
    markov = Markov(3)
    markov.train('data2.json')
    print(markov.generate())
