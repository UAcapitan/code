from zipfile import ZipFile

with ZipFile('test.zip','w') as zf:
    zf.write('text_1.txt')
    zf.write('text_2.txt')
    zf.write('text_3.txt')