def print_grid():
    new_simple_grid = ''.join(grid[0]) + ''.join(grid[1]) + ''.join(grid[2])
    print('---------')
    print('|', new_simple_grid[0], new_simple_grid[1], new_simple_grid[2], '|')
    print('|', new_simple_grid[3], new_simple_grid[4], new_simple_grid[5], '|')
    print('|', new_simple_grid[6], new_simple_grid[7], new_simple_grid[8], '|')
    print('---------')

def is_winner(letter):
    triple_letter = letter * 3

    # Check lines
    for i in range(3):
        line = ''.join(grid[i])
        if line == triple_letter:
            return True

    # Check columns
    for i in range(3):
        column = ''.join([grid[0][i], grid[1][i], grid[2][i]])
        if column == triple_letter:
            return True

    # Check diagonals
    diagonal1 = ''.join([grid[0][0], grid[1][1], grid[2][2]])
    if diagonal1 == triple_letter:
        return True

    diagonal2 = ''.join([grid[2][0], grid[1][1], grid[0][2]])
    if diagonal2 == triple_letter:
        return True

# Print empty grid
print('---------')
print('|       |')
print('|       |')
print('|       |')
print('---------')

# Setup
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
move_pending = True
move_count = 0

# Start game loop
xturn = True
while True:
    if is_winner('X'):
        print('X wins')
        break
    elif is_winner('O'):
        print('O wins')
        break
    elif move_count == 9:
        print('Draw')
        break
    else:
        move_pending = True

    # If game is on, then ask for a move
    while move_pending:
        print('Make a move')
        move = input()

        try:
            row = move[0]
            col = move[2]
            row_int = int(row) - 1 # ValueError
            col_int = int(col) - 1 # ValueError
            if grid[row_int][col_int] != ' ': # IndexError
                print('This cell is occupied! Choose another one!')
            else:
                if xturn:
                    grid[row_int][col_int] = 'X'
                    xturn = False
                else:
                    grid[row_int][col_int] = 'O'
                    xturn = True

                move_pending = False
                print_grid()
        except ValueError:
            print('You should enter numbers!')
        except IndexError:
            print('Coordinates should be from 1 to 3!')
