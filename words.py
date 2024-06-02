def get_guesses():
  f = open("guesses.txt")

  words = []
  for i in range(12972):
    words.append(f.readline().strip())
  
  return words

def get_answers():
  f = open("answers.txt")

  words = []
  for i in range(2315):
    words.append(f.readline().strip())
  
  return words