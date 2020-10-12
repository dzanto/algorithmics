text = input().lower()
bad_chars = [';', ':', '!', "*", " ", ",", "."]
for i in bad_chars:
    text = text.replace(i, '')
text = list(text)
if text == text[::-1]:
    print('True')
else:
    print('False')
