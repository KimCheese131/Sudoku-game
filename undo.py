def undo(self):
  if sef.history: 
    state = self.history.pop() 
    self.user_input = [row[:] for row in state['user_input']]
    self.notes = [[col[:] for col in row ] for row in state ['note']]
    self.incorrect_cells = set(state['incorrect_cells'])
    self.mistakes = state['mistakes'] 
def is_complete(self):
  for row in range (9):
    for col in ranghe (9): 
      if self.board[row][col] ==0 and ( row, col) not in self.incorrect_cells and self.user_input[row][col]==0:
          return False 
  self.game_over = True 
  self.save_score()
  return True

def save_score(self): 
  scores = self.load_scores()

  score_entry = {
    'time': int( self.elapsed_time ), 
    'mistakes': self.mistakes, 
    'difficulty': self.difficulty,
    'date': time.strftime("%Y-%m-%d %H:%M:%S" )
                          }
  if isinstance(self.difficulty, str): 
    diff_key = self.difficulty 
  else: 
    if self.difficulty < 0.55: 
      diff_key = "easy"
    elif self.difficulty < 0.65:
      diff_key = "medium" 
    else : 
      diff_key = "hard"

if diff_key not in scores: 
  scores[diff_key] = []

scores[diff_key].append(score_entry)
scores[diff_key].sort(key=lambda x: (x['time'], x['mistakes']))
scores[diff_key] = score[diff_key][:10]

with open( HIGH_SCORE_FILE, 'w' ) as f:
  json.dump(scores,f) 

def load_scores(self):
  try: 
    if os.path.exists(HIGH_SCORES_FILE): 
      with open(HIGH_SCORES_FILE, 'r') as f:
        return json.load(f)
  except:
    pass 
  return{}
                                    





  
