import sys


if __name__ == "__main__":
    try:
        token = [
            int(x, 16)
            for x in "66 34 6b 6d 6d 36 70 7c 3d 82 7f 70 82 6e 83 82 44 42 83 44 75 7b 7f 8c 89 0a".split(' ')
        ]
        token = [
            print(chr(row - index), end='')
            for index, row in enumerate(token)
        ]
    except:
        sys.exit()
