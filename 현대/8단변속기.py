import sys

test_list = list(map(int, sys.stdin.readline().split()))

test_list_ascending = sorted(test_list)
test_list_descending = sorted(test_list, reverse = True)

if test_list == test_list_ascending:
    print("ascending")
elif test_list == test_list_descending:
    print("descending")
else:
    print("mixed")