# SpenGUI 02/10/22 17:18pm
# run to get a random word from words.txt and display it in the google chrome brower

# PSA you NEED chrome installed for this code to work

import random
import webbrowser
randomWord = "place holder"

def load_words():
    with open('words.txt') as word_file:  # you NEED to down load the words and put them in the same folder for this to work
        valid_words = set(word_file.read().split())

def getNewWord():
    global randomWord
    if __name__ == '__main__':
        english_words = load_words()
        # demo print
        randomWord = random.choice(open('words.txt').read().split()).strip()

getNewWord()

m = ("https://www.google.co.uk/search?q=",randomWord," meaning")
url = "".join(m)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

webbrowser.get(chrome_path).open_new(url)
