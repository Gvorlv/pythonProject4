for row in range(5):
    for col in range(5):
        if col - row == 0:
            print(1, end=' ')

        else:
            print(0, end=' ')
    print()