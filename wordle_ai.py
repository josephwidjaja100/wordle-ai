def state(guess, answer):
  res = []
  for i in range(5):
    score = 0
    for j in range(5):
      if(guess[i] == answer[j]):
        if(i == j):
          score = max(score, 2)
        else:
          score = max(score, 1)

    res.append(score)

  return res

def filter(words, guess, score):
  # "Wordle is very strict and fair with its letters. If you repeat a letter more than it appears, then the excess will be highlighted in grey"
  # Ok for v1 but need to fix bugs

  for i in range(5):
    for j in range(5):
      if(i != j and guess[i] == guess[j] and score[i] > 0 and score[j] == 0):
        score[j] = 1

  res = []
  for word in words:
    ok = True
    for i in range(5):
      if(score[i] == 2 and word[i] != guess[i]):
        ok = False
      elif(score[i] == 1 and (word[i] == guess[i] or guess[i] not in word)):
        ok = False
      elif(score[i] == 0 and (guess[i] in word)):
        ok = False

    if(ok):
      res.append(word)

  return res

def state_mat(guesses, answers):
  mat = [[None for _ in range(len(answers))] for _ in range(len(guesses))]

  cnt = 0
  for i in range(len(guesses)):
    for j in range(len(answers)):
      cnt += 1;
      mat[i][j] = str(state(guesses[i], answers[j]))

  return mat

def all_mat(guesses, answers):
  mat = [[0 for _ in range(len(answers))] for _ in range(len(guesses))]
  st_mat = state_mat(guesses, answers)

  for i in range(len(guesses)):
    d = {}
    for j in range(len(answers)):
      s = st_mat[i][j]
      if(d.get(s)):
        d[s] += 1
      else:
        d[s] = 1

    for j in range(len(answers)):
      s = st_mat[i][j]
      mat[i][j] = d[s]

  return mat

def next_word(guesses, answers):
  mat = all_mat(guesses, answers)
  d = {}

  mn = 20000
  for i in range(len(guesses)):
    # amt = 0
    # for j in range(len(mat)):
    #   amt += mat[i][j]
    # amt /= len(mat)
    # amt = round(amt, 6)

    amt = 0
    for j in range(len(answers)):
      amt = max(amt, mat[i][j])

    mn = min(mn, amt)

    if(d.get(amt)):
      d[amt].append(guesses[i])
    else:
      d[amt] = [guesses[i]]

  return d[mn]
