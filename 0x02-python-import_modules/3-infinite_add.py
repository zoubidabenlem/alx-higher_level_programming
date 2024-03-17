#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    size = len(sys.argv) - 1
    if size == 0:
        print("{}".format(sum))
        sys.exit()
    for i in range(1, size + 1):
        sum += int(sys.argv[i])
print("{}".format(sum))
