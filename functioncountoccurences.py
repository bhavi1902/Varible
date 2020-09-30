def count_occurances(text):
  for i in range(len(text)):
    if len(text) == 0:
      break
    ch = text[0]
    if ch == ' ' or ch == '\t':
      continue
    print(ch + " - ", text.count(ch))
    text = text.replace(ch, '').strip()
n=input("Enter a string:")
count_occurances(n)