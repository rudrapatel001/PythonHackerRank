S = input()
try:
    int_val = int(S)
    print(int_val)
except ValueError:
    print('Bad String')
    