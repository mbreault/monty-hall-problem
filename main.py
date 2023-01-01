import random

def monty_hall_problem(switch_door):
  # randomly select the door behind which the prize is hidden
  doors = ['goat', 'goat', 'prize']
  random.shuffle(doors)
  chosen_door = random.choice(doors)

  # Monty Hall shows the contestant a goat behind one of the doors
  doors.remove(chosen_door)
  if chosen_door == 'prize':
    doors.remove('goat')
  else:
    doors = ['goat']

  # the contestant has the option to switch doors
  if switch_door:
    if chosen_door == 'goat':
      chosen_door = 'prize'
    else:
      chosen_door = 'goat'

  # return True if the contestant wins, False otherwise
  return chosen_door == 'prize'

def main():
    # simulate the Monty Hall problem n times with door switching
    wins = 0
    n = 10000
    for i in range(n):
        if monty_hall_problem(True):
            wins += 1

    win_percentage = wins / n * 100
    print(f'Contestant won {wins} times out of {n} ({win_percentage:.2f}%) when switching doors.')

    # simulate the Monty Hall problem n times without door switching
    wins = 0
    for i in range(n):
        if monty_hall_problem(False):
            wins += 1

    win_percentage = wins / n * 100
    print(f'Contestant won {wins} times out of {n} ({win_percentage:.2f}%) when not switching doors.')

if __name__ == '__main__':
    main()

