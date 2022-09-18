
import os
import random
import sqlite3
from termcolor import colored
from googletrans import Translator


class EnglishApp():
    def __init__(self) -> None:
        self.connect = sqlite3.connect("Desktop/EdMix/English/words.db")
        self.cursor = self.connect.cursor()
        self.translator = Translator()

    def run(self) -> None:
        try:
            self.main()
        except KeyboardInterrupt:
            self.close()

    def main(self) -> None:
        while True:
            mode = self.select_mode()

            match mode[1]:
                case 1: n = 0
                case 2: n = 100
                case 3: n = 30

            match mode[0]:
                case 1: self.training_to_english(n)
                case 2: self.training_from_english(n)
                case 3: self.add_words()
       
    def get_word(self, amount: int = 0) -> list:
        print("-"*29)
        print()
        if amount == 0:
            self.cursor.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1;")
            return self.cursor.fetchone()
        else:
            self.cursor.execute("SELECT * FROM words;")
            return random.choice(self.cursor.fetchall()[::-1][:amount])

    def select_mode(self) -> int:
        while True:
            for mode in [
                "1. To English",
                "2. From English",
                "3. Add new words"
            ]:
                print(mode)
            print()

            mode = int(input("Select mode: "))

            match mode:
                case 1 | 2:
                    for amount_item in [
                        "\n1. All words",
                        "2. 100 words",
                        "3. 30 words"
                    ]:
                        print(amount_item)
                    print()

                    amount = int(input("Select amount of words: "))
                    if amount in range(1,4):
                        return [mode, amount]
                case 3:
                    return [mode, 0]

    def training_to_english(self, amount: int) -> None:
        while True:
            word = self.get_word(amount)
            answer = input(f"{word[1]} - ")

            print()

            if answer == 'q':
                break

            if answer.lower() == word[0].lower():
                print(colored(f"{word[1]} - {answer}", "green"))
            else:
                print(colored(f"{word[1]} - {answer}", "red"))
                print(colored(f"{word[1]} - {word[0]}", "green"))
            
            print()

    def training_from_english(self, amount: int) -> None:
        while True:
            word = self.get_word(amount)
            answer = input(f"{word[0]} - ")

            print()

            if answer == 'q':
                break

            if answer.lower() == word[1].lower():
                print(colored(f"{word[0]} - {answer}", "green"))
            else:
                print(colored(f"{word[0]} - {answer}", "red"))
                print(colored(f"{word[0]} - {word[1]}", "green"))
            
            print()

    def add_words(self) -> None:
        print("\n" + "-"*29 + "\n")
        words = input("Words:\n\n").split(",")

        for word in words:
            if word.strip():
                translated = self.translator.translate(word, src="en", dest="ru").text
                self.cursor.execute(f"INSERT INTO words VALUES ('{word.strip()}','{translated}');")

        self.connect.commit()

        print("\nNew words were added")
        print("\n" + "-"*29 + "\n")

    def close(self) -> None:
        self.cursor.close()
        self.connect.commit()
        self.connect.close()


if __name__ == "__main__":
    app = EnglishApp()
    app.run()
