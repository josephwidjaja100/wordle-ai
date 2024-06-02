from wordle_ai import next_word, filter
from words import get_guesses, get_answers
import time
from datetime import datetime
from wordfreq import word_frequency as wfrq
import loading

def try_word():
  valid = False
  while(not valid):
    word = input("Enter Chosen Word: ")
    if(len(word) == 5):
      ok = True
      for i in range(5):
        if(not word[i].isalpha()):
          ok = False

      if(ok):
        return word

    print("Invalid. Please try again.")

def get_res():
  res = []
  valid = False
  while(not valid):
    line = input("Enter Result: ").strip().split()
    if(len(line) == 1):
      if(len(line[0]) == 5):
        ok = True
        for i in range(len(line[0])):
          if(not line[0][i].isdigit() or int(line[0][i]) < 0 or int(line[0][i]) > 2):
            ok = False

        if(ok):
          for i in range(len(line[0])):
            res.append(int(line[0][i]))

          valid = True

    elif(len(line) == 5):
      ok = True
      for i in range(5):
        if(not line[i].isdigit() or int(line[i]) < 0 or int(line[i]) > 2):
          ok = False

      if(ok):
        for i in range(5):
          res.append(int(line[i]))

        valid = True

    if(not valid):
      print("Invalid. Please try again.")

  return res

guesses = get_guesses()
answers = get_answers()

start = True
print("Words Possible: " + str(len(guesses)))
while(True):
  begin_time = datetime.now()
  load = loading.Loader(animation="pong").start()

  if(start):
    opt = ['aesir', 'arise', 'raise', 'reais', 'serai']
  else:
    opt = next_word(guesses, answers)

  mx_freq = 0
  mx_word = ""

  ok = False
  for word in opt:
    if(word in answers):
      ok = True
      break

  if(ok):
    res = []
    for word in opt:
      if(word in answers):
        res.append(word)
  else:
    res = opt[::]

  for word in res:
    frq = wfrq(word, 'en')
    mx_freq = max(mx_freq, frq)
    if(frq == mx_freq):
      mx_word = word

  # time.sleep(2)

  load.stop()
  end_time = datetime.now()

  print("Optimal Words: " + str(opt))
  print("Recommended Word: " + mx_word)
  print("Processing Time: " + str(end_time - begin_time))

  word = try_word()
  state = get_res()

  guesses = filter(guesses, word, state)
  answers = filter(answers, word, state)

  if(state == [2, 2, 2, 2, 2]):
    print("Solved!")
    break;
  else:
    if(len(guesses) == 0 or len(answers) == 0):
      print("No valid words :(")
      break;

    print("Words Possible: " + str(len(guesses)))

  start = False
