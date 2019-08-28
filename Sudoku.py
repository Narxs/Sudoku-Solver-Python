from copy import deepcopy
import pygame


from graphics import show

frame = [[4, 0, 0,  2, 7, 0,  0, 5, 0],
         [0, 2, 5,  0, 0, 0,  9, 0, 4],
         [0, 0, 7,  0, 0, 4,  0, 2, 1],

         [0, 1, 0,  0, 0, 6,  0, 8, 0],
         [0, 0, 0,  0, 0, 0,  0, 0, 0],
         [0, 4, 0,  5, 0, 0,  0, 9, 0],

         [7, 5, 0,  4, 0, 0,  2, 0, 0],
         [2, 0, 4,  0, 0, 0,  8, 6, 0],
         [0, 6, 0,  0, 2, 8,  0, 0, 5]]

Maybes = [1]
row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

item_mem = []
frame_mem = []
Maybes_mem = []

q = 0

for i in range(9):
    print(frame[i])

print("///////////////////////////")


def search(frame_search):

    maybes_search = []
    for n in range(9):
        for i_search in range(9):
            if frame_search[n][i_search] == 0:

                temp = []
                col_check = []
                square_check = []

                row_check = frame_search[n]
                for t in range(9):
                    col_check += [frame_search[t][i_search]]

                for k in range(int(n/3)*3, int(n/3)*3+3):
                    for l in range(int(i_search / 3) * 3, int(i_search / 3) * 3 + 3):
                        square_check += [frame_search[k][l]]

                for b in row:
                    if b in row_check:
                        pass
                    elif b in col_check:
                        pass
                    elif b in square_check:
                        pass
                    else:
                        temp += [b]
                maybes_search += [[n, i_search, temp]]
            else:
                pass
    return maybes_search


def what_row(maybes_what_row):

    for row_no in range(9):

        tots = {}
        maybes_row_temp = []

        for i_what_row in range(len(maybes_what_row)):

            if maybes_what_row[i_what_row][0] != row_no:
                pass
            else:
                maybes_row_temp += [maybes_what_row[i_what_row]]

        print(maybes_row_temp)
        if len(maybes_row_temp) != 0:

            for item in range(len(maybes_row_temp)):
                for no in range(len(maybes_row_temp[item][2])):

                    if maybes_row_temp[item][2][no] in tots:
                        tots[maybes_row_temp[item][2][no]] += 1
                    else:
                        tots[maybes_row_temp[item][2][no]] = 1
            print(tots)

            for key in tots:
                if tots[key] == 1:

                    print("Single location found for ", key, " updating")
                    for i in range(len(maybes_row_temp)):

                        if key in maybes_row_temp[i][2]:

                            print("Found in ", maybes_row_temp[i])
                            for n in range(len(maybes_what_row)):

                                if (maybes_row_temp[i][1] == maybes_what_row[n][1]) and (maybes_row_temp[i][0] == maybes_what_row[n][0]):

                                    print("Updating", maybes_what_row[n])
                                    maybes_what_row[n][2] = [key]
                                    print("Now ", maybes_what_row[n])

    return maybes_what_row


def what_col(maybes_what_col):

    for col_no in range(9):

        tots = {}
        maybes_temp = []

        for n_row in range(len(maybes_what_col)):

            if maybes_what_col[n_row][1] != col_no:
                pass
            else:
                maybes_temp += [maybes_what_col[n_row]]

        print(maybes_temp)
        if len(maybes_temp) != 0:

            for item in range(len(maybes_temp)):
                for no in range(len(maybes_temp[item][2])):

                    if maybes_temp[item][2][no] in tots:
                        tots[maybes_temp[item][2][no]] += 1
                    else:
                        tots[maybes_temp[item][2][no]] = 1
            print(tots)

            for key in tots:
                if tots[key] == 1:

                    print("Single location found for ", key, " updating")
                    for i_what_col in range(len(maybes_temp)):

                        if key in maybes_temp[i_what_col][2]:

                            print("Found in ", maybes_temp[i_what_col])
                            for n in range(len(maybes_what_col)):

                                if (maybes_temp[i_what_col][1] == maybes_what_col[n][1]) and (maybes_temp[i_what_col][0] == maybes_what_col[n][0]):

                                    print("Updating", maybes_what_col[n])
                                    maybes_what_col[n][2] = [key]
                                    print("Now ", maybes_what_col[n])

    return maybes_what_col


def what_square(maybes_what_square):

    for sq_row_no in range(3):
        for sq_col_no in range(3):

            tots = {}
            maybes_temp = []

            for n_what_square in range(len(maybes_what_square)):

                if (maybes_what_square[n_what_square][0] < sq_row_no * 3) or maybes_what_square[n_what_square][0] >= (sq_row_no * 3 + 3) or maybes_what_square[n_what_square][1] < (sq_col_no * 3) or maybes_what_square[n_what_square][1] >= (sq_col_no * 3 + 3):
                    pass
                else:
                    maybes_temp += [maybes_what_square[n_what_square]]

            print(maybes_temp)
            if len(maybes_temp) != 0:

                for item in range(len(maybes_temp)):
                    for no in range(len(maybes_temp[item][2])):

                        if maybes_temp[item][2][no] in tots:
                            tots[maybes_temp[item][2][no]] += 1
                        else:
                            tots[maybes_temp[item][2][no]] = 1
                print(tots)

                for key in tots:

                    if tots[key] == 1:

                        print("Single location found for ", key, " updating")
                        for i_what_square in range(len(maybes_temp)):

                            if key in maybes_temp[i_what_square][2]:

                                print("Found in ", maybes_temp[i_what_square])
                                for n in range(len(maybes_what_square)):

                                    if (maybes_temp[i_what_square][1] == maybes_what_square[n][1]) and (maybes_temp[i_what_square][0] == maybes_what_square[n][0]):

                                        print("Updating", maybes_what_square[n])
                                        maybes_what_square[n][2] = [key]
                                        print("Now ", maybes_what_square[n])

    return maybes_what_square


def fill(frame_fill, maybes_fill):

    count = 0

    print("Checking rows")
    maybes_fill = what_row(maybes_fill)

    print("Checking columns")
    maybes_fill = what_col(maybes_fill)

    print("Checking squares")
    maybes_fill = what_square(maybes_fill)

    for u in range(len(maybes_fill)):

        if len(maybes_fill[u][2]) == 1:
            print("{}{} is now {}".format(maybes_fill[u][0], maybes_fill[u][1], maybes_fill[u][2][0]))
            frame_fill[maybes_fill[u][0]][maybes_fill[u][1]] = maybes_fill[u][2][0]
            count = 1
        else:
            pass

    if count == 0:
        return frame_fill
    else:
        return frame_fill


def change(frame_change, frame_prev_change):

    if frame_change == frame_prev_change:
        return False
    else:
        return True


def revert(Maybes, frame, item_mem, Maybes_mem, frame_mem, test):

    if test == True:
        print("===============================")
        print("REVERTING")

        # for n in range(len(Maybes)):
        #     print(Maybes[n]) #JUST FOR DEBUGGING
        print("===============================")


        Maybes = deepcopy(Maybes_mem)
        # print("Old Maybes")

        # for n in range(len(Maybes)):
        #     print(Maybes[n]) #JUST FOR DEBUGGING
        print("===============================")

        for n in range(len(Maybes)):
            print(item_mem,Maybes[n])
            if item_mem[0] == Maybes[n][0] and item_mem[1] == Maybes[n][1]:
                print("Removing wrong entry in {}{} of {} changing to {}".format(Maybes[n][0], Maybes[n][1], Maybes[n][2][0], item_mem[2][1]))
                Maybes[n][2] = [item_mem[2][1]]
                print(Maybes[n])

            break

        frame = deepcopy(frame_mem)

        print("Now frame is")

        for i in range(9):
            print(frame[i])

    return Maybes, frame, item_mem, Maybes_mem, frame_mem


def check(frame):

    for i in range(9):
        for n in range(9):
            for l in range(9):
                if frame[i][n] == frame[i][l] and frame[i][n] != 0 and n != l:
                    print(i,n, l, frame[i][n], frame[i][l])
                    print("A mistake has been made in row")
                    return True

    for i in range(9):
        for n in range(9):
            for l in range(9):
                if frame[n][i] == frame[l][i] and frame[n][i] != 0 and n != l:
                    print(n, i, frame[n][i], frame[l][i])
                    print("A mistake has been made in col")
                    return True

    for n in range(9):
        for i in range(9):
            for k in range(int(n/3)*3, int(n/3)*3+3):
                for l in range(int(i/3)*3, int(i/3)*3+3):
                    for m in range(int(n/3)*3, int(n/3)*3+3):
                        for o in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                            if frame[k][l] == frame[m][o] and frame[k][l] != 0 and [k,l] != [m,o]:
                                print("A mistake has been made in square")
                                return True

    return False


while len(Maybes) != 0:

    print("//////////////////////////////////")

    q += 1

    frame_prev = deepcopy(frame)
    total = 0

    Maybes = search(frame)

    if check(frame) == True:
        Maybes, frame, item_mem, Maybes_mem, frame_mem = revert(Maybes, frame, item_mem, Maybes_mem, frame_mem, True)

    if not check(frame) and len(Maybes) == 0:
        break

    frame = fill(frame, Maybes)

    if not change(frame, frame_prev):
        print("No change made, going to have to start guessing")
        print("***************************************************************************")
        frame_mem = deepcopy(frame)
        Maybes_mem = deepcopy(Maybes)

        count_1 = 0
        for m in range(len(Maybes)):
            print(Maybes[m], len(Maybes[m][2]))
            if len(Maybes[m][2]) == 2 and count_1 == 0:

                count_1 = 1
                item_mem = deepcopy(Maybes[m])
                Maybes[m][2] = [Maybes[m][2][0]]
                print("Changing {} to {}".format(item_mem, Maybes[m]))
                break

        frame = fill(frame, Maybes)

    else:
        print("Change made")

    print("Prev frame")
    for i in range(9):
        print(frame_prev[i])

    print("Pass", q)
    for i in range(9):
        print(frame[i])

    if q > 81 or not change(frame, frame_prev):
        print("Code ran for too long or no changes where made.")
        for i in range(len(Maybes)):
            print(Maybes[i])

        break

if not check(frame):
    print("Final frame")

    for i in range(9):
        print(frame[i])

    print("Finished")

show(frame)
