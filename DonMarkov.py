from configparser import ConfigParser
from generator import Markov
import requests

markov = Markov(3)
markov.train('data2.json')

config = ConfigParser()
config.read('config.ini')
WEBHOOK_URL = config.get('auth', 'WEBHOOK_URL_TEST')

data = {
  "text": markov.generate()
}

response = requests.post(WEBHOOK_URL, json=data)