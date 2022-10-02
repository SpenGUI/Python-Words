import random
import webbrowser
randomWord = "place holder"

def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

def getNewWord():
    global randomWord
    if __name__ == '__main__':
        english_words = load_words()
        # demo print
        randomWord = random.choice(open('words.txt').read().split()).strip()

getNewWord()

marge = ("https://www.dictionary.com/browse/",randomWord)
url = "".join(marge)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

webbrowser.get(chrome_path).open_new(url)
