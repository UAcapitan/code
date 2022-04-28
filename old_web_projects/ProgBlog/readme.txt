В папці files лежить весь код
А в папці database лежить дамп бази даних який потрібно залити в базу даних:
mysql -u USER -pPASSWORD DATABASE </path/to/dump.sql

В папке files лежит весь код
А в папке database лежит дамп базы данных который нужно залить в базу данных:
mysql -u USER -pPASSWORD DATABASE < /path/to/dump.sql

The files folder contains all the code
And the database folder contains a dump of the database that needs to be uploaded to the database:
mysql -u USER -pPASSWORD DATABASE </path/to/dump.sql