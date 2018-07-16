

def check_sum(line):
    return line == 3 or line == 12


def horizontal_win(arr):
    # winner = None
    for i in range(len(arr)):
        line = sum(arr)
        if check_sum(line):
            return True
    return False
        # if sum(arr[i]) == 3:
        #     winner = 1
        # elif sum(arr[i]) == 12:
        #     winner = 2


# def up_down(arr):

    # for i in range(len(arr)):



