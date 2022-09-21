
import datetime
import random
import sqlite3
from termcolor import colored
from googletrans import Translator


class EnglishApp():
    def __init__(self) -> None:
        self.connect = sqlite3.connect("Desktop/EdMix/English/words.db")
        self.cursor = self.connect.cursor()
        self.translator = Translator()


        # self.save_stats()
        self.data = self.load_stats()

        self.run()

    def run(self) -> None:
        try:
            self.main()
        except:
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
                case 'm': self.menu()
       
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
                "3. Add new words\n"
                "\nm. Menu"
            ]:
                print(mode)
            print()

            mode = input("Select mode: ")

            if mode.isdigit():
                mode = int(mode)

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
                case 3 | 'm':
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
                self.add_point()
            else:
                print(colored(f"{word[1]} - {answer}", "red"))
                print(colored(f"{word[1]} - {word[0]}", "green"))
                self.minus_points()
            
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
                self.add_point()
            else:
                print(colored(f"{word[0]} - {answer}", "red"))
                print(colored(f"{word[0]} - {word[1]}", "green"))
                self.minus_points()
            
            print()

    def add_words(self) -> None:
        print("\n" + "-"*29 + "\n")
        words = input("Words:\n\n").split(",")

        for word in words:
            if word.strip():
                translated = self.translate_word(word)
                self.cursor.execute(f"INSERT INTO words VALUES ('{word.strip()}','{translated}');")

        self.connect.commit()

        print("\nNew words were added")
        print("\n" + "-"*29 + "\n")

    def translate_word(self, word: str) -> str:
        try:
            translated = self.translator.translate(word, src="en", dest="ru").text
            if translated == word:
                translated = self.translator.translate(word, src="ru", dest="en").text
        except:
            return input(f"{word} - ")
        return translated

    def close(self) -> None:
        self.save_stats()

        self.cursor.close()
        self.connect.commit()
        self.connect.close()

    # In development
    def menu(self):
        for point in [
            "\nMenu:\n",
            "1. Day goals",
            "2. Statistics",
            "3. The last n-words"
        ]:
            print(point)
        
        print()

        choiced_point = int(input("Select point: "))

        print()

        match choiced_point:
            case 1: self.show_goals()
            case 2: self.show_statistics()
            case 3: self.show_last_words()

    def load_stats(self) -> dict:

        results = []

        for command in [
            "SELECT date, correct, incorrect, points FROM day WHERE id=1;",
            "SELECT COUNT(english) FROM words;",
            "SELECT SUM(correct) FROM statistics;",
            "SELECT * FROM level WHERE id=1;"
        ]:
            self.cursor.execute(command)
            results.append(list(self.cursor.fetchone()))

        if None in results[2]:
            results[2] = [0]

        return {
            "day": results[0],
            "amount_of_words": results[1],
            "all_correct_words": results[2],
            "level": results[3]
        }

    def save_stats(self):
        today = datetime.date.today().strftime("%d.%m.%Y")

        self.cursor.execute(f"SELECT * FROM day WHERE date='{today}';")
        day = self.data['day']

        if len(self.cursor.fetchall()) == 1:
            command = f"UPDATE day SET correct={day[1]}, incorrect={day[2]}, points={day[3]} WHERE id=1;"
            self.cursor.execute(command)
        else:
            self.cursor.execute(f"UPDATE day SET date='{today}', correct=0, incorrect=0, points=0 WHERE id=1;")

        self.cursor.execute(f"SELECT * FROM statistics WHERE date='{today}';")
        correct = self.data['all_correct_words'][0]
        if len(self.cursor.fetchall()) == 1:
            self.cursor.execute(f"UPDATE statistics SET correct={correct} WHERE date='{today}';")
        else:
            self.cursor.execute(f"INSERT INTO statistics VALUES ('{today}', {correct});")

        level = self.data['level']
        command = f"UPDATE level SET level={level[1]}, points={level[2]} WHERE id=1;"
        self.cursor.execute(command)

    def show_goals(self):        
        for row in [
            "-"*29 + "\n",
            "Day goals\n",
            f"Today words are correct: {self.data['day'][1]}/150",
            f"Today words are incorrect: {self.data['day'][2]}",
            f"Points: {self.data['day'][3]}/50",
            "\n" + "-"*29
        ]:
            print(row)

        input()

    def show_statistics(self):
        for row in [
            "-"*29 + "\n",
            "Statistics\n",
            f"Level: {self.data['level'][1]}",
            f"Total words are correct: {self.data['all_correct_words'][0]}",
            f"All words in vocabulary: {self.data['amount_of_words'][0]}",
            "\n" + "-"*29
        ]:
            print(row)
        input()

    def show_last_words(self):
        words_amount = int(input("Amount of words: "))
        self.cursor.execute("SELECT * FROM words;")
        words = self.cursor.fetchall()[::-1][:words_amount][::-1]
        print("-"*29 + "\n")
        for word in words:
            print(f"{word[0]} - {word[1]}")
        print("\n" + "-"*29)

        input()

    def add_point(self):
        self.increase_level()

        self.data['day'][1] += 1
        self.data['all_correct_words'][0] += 1
        if self.data['day'][3] < 50:
            self.data['day'][3] += 1

    def minus_points(self):
        self.data['day'][2] += 1
        if 0 < self.data['day'][3] < 50:
            self.data['day'][3] -= 1

    def increase_level(self):
        if self.data['day'][3] == 49:
            self.data['level'][2] += 50

        if self.data['day'][1] == 149:
            self.data['level'][2] += 50

        points_level = self.data['level'][2] // 500

        if self.data['level'][1] < points_level:
            self.data['level'][1] = points_level
    

if __name__ == "__main__":
    EnglishApp()
