
text = '''
    Just
    Some
    Text
    For
    Testing
    This
    Method
'''
len_max = len(max(text.split(), key=lambda x: len(x)))

for t in text.split():
    print(t.rjust(len_max))
