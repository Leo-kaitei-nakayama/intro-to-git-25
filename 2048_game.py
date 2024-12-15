import Logic2048

if __name__ == '__main__':

    mat = Logic2048.game_starts()

while(True):
    x = input("Press the command :")

    if (x == 'A' or x == 'a'):
        mat, flag = Logic2048.move_up(mat)
        status = Logic2048.get_current_state(mat)
        print(status)

        if(status == "Game not over"):
            Logic2048.add_new_2(mat)

        else:
            break

    elif(x == "D" or x == 'd'):
        mat, flag = Logic2048.move_down(mat)
        status = Logic2048.get_current_state(mat)
        print(status)
        if(status == "Game not over"):
            Logic2048.add_new_2(mat)
        else:
            break

    elif(x == 'W' or x == 'w'):
        mat, flag = Logic2048.move_left(mat)
        status = Logic2048.get_current_state(mat)
        print(status)
        if(status == 'Game not over'):
            Logic2048.add_new_2(mat)
        else:
            break

    elif(x == "S" or x == 's'):
        mat, flag = Logic2048.move_right(mat)
        status = Logic2048.get_current_state(mat)
        print(status)
        if(status == 'Game not over'):
            Logic2048.add_new_2(mat)
        else:
            break              
    else:
        print('Invalid Key Passed')

    print(Logic2048.print_vertical(mat))