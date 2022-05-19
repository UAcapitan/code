import sys

# print(sys.argv) # аргументы перед файлом при запуске с консоли
print(sys.builtin_module_names, end='\n\n') # модули
print(sys.exec_prefix, end='\n\n') # каталог python
print(sys.executable, end='\n\n') # интерпретатор python
# sys.exit() #выход с приложения
print(sys.flags, end='\n\n') # флаги командной строки
print(sys.getdefaultencoding(), end='\n\n') # кодировка
print(sys.getfilesystemencoding(), end='\n\n') # кодировка системы
print(sys.getrefcount(r'C:\Users\Ed\Desktop\EdMix\Code\training_modules\sys\sys_training.py'), end='\n\n') # количество ссылок на объект
print(sys.getrecursionlimit(), end='\n\n') # лимит рекурсий
print(sys.getsizeof(r'C:\Users\Ed\Desktop\EdMix\Code\training_modules\sys\sys_training.py'), end='\n\n') # размер объекта в байтах
print(sys.getswitchinterval(), end='\n\n') # интервал переключения потоков
print(sys.getwindowsversion(), end='\n\n') # кортеж с описанием версии Windows
print(sys.hash_info, end='\n\n') # информация о параметрах хеширования
print(sys.implementation, end='\n\n') # информация о запущеном интерпретаторе
print(sys.intern('Python'), end='\n\n') # возвращает интернированую строку
print(sys.maxunicode, end='\n\n') # максимальное число бит для символа Unicode
# print(sys.modules) # словарь с модулями
l = [i for i,j in sys.modules.items()]
print(l, end='\n\n')
print(sys.path, end='\n\n') # пути к модулям 
print(sys.platform, end='\n\n') # информация об ОС
print(sys.prefix, end='\n\n') # папка установки интерпретатора python
sys.setrecursionlimit(700) # установка лимита рекурсии
sys.setswitchinterval(0.0075) # установка интервала переключения потока
print(sys.version, end='\n\n') # версия Python
print(sys.api_version, end='\n\n') # версия API Python
print(sys.winver, end='\n\n') # номер версии Python для реестра Windows