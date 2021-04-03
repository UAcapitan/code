import random
import os

class Encrypte:

    def __init__(self, file_address, flash_name):
        self.file_address = file_address
        self.flash_name = flash_name
        self.key = ''

    # Основной метод класса
    def encrypt_file_with_flash_drive(self):

        with open(self.file_address, 'r') as file:
            text_from_file = file.readlines()

        try:
            if self.check_key_file_on_flash_drive(self.flash_name):
                self.key = self.open_file_on_flash_drive(self.flash_name)
            else:
                self.create_file_on_flash_drive(self.flash_name)
                self.key = self.open_file_on_flash_drive(self.flash_name)
        except:
            print('Flash not found')
            input()
            exit()

        int_key = int(self.key)
        text_from_file = self.redact_string_text(text_from_file)
        new_text = self.encrypt_text(text_from_file, int_key)
        new_text = self.redact_string_text(new_text)
        self.save_new_text_in_file(new_text)

    # Зашифровать текст который в списке и возвращать в списке
    def encrypt_text(self, text_list: list, key:int) -> list:
        new_text_list = []
        for i in text_list:
            row_list = []
            for j in i:
                row_list.append(chr(ord(j) ^ key))
            new_text_list.append(''.join(row_list))
        return new_text_list

    # Открыть файл на флешке
    def open_file_on_flash_drive(self, name_flash_drive):
        with open(f'{name_flash_drive}:/key_for_encrypt.txt', 'r') as file:
            key = file.readline()
        return key

    # Создать файл на флешке
    def create_file_on_flash_drive(self, name_flash_drive):
        with open(f'{name_flash_drive}:/key_for_encrypt.txt', 'w') as file:
            key = str(random.randint(1,100))
            file.write(key)
        return True

    # Проверить существует ли файл на флешке
    def check_key_file_on_flash_drive(self, name_flash_drive):
        return os.path.isfile(f'{name_flash_drive}:/key_for_encrypt.txt')

    # Убрать или добавить перевод на новую строку
    def redact_string_text(self, text_list: list) -> list:
        new_string = []
        for row in text_list:
            if row[-1] == '\n':
                new_string.append(row[:-1])
            else:
                new_string.append(row + '\n')
        new_string[-1] = new_string[-1][:-1]
        return new_string

    # Сохранить новый текст в файле
    def save_new_text_in_file(self, text_in_file):
        with open(self.file_address, 'w') as file:
            file.write(''.join(text_in_file))

def main_app_block():
    file_address = input('File adress: ')
    flash_name = input('Flash name: ')
    encrypte = Encrypte(file_address=file_address, flash_name=flash_name)
    encrypte.encrypt_file_with_flash_drive()

main_app_block()