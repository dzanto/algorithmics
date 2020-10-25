f = open('input.txt', 'r')
xy = [int(item) for item in f.read().splitlines()]
# print(xy)
maxi = max(xy)
mini = min(xy)
# print(maxi)

def kvadrat(maxi, mini):
    ostatok = maxi % mini
    if ostatok == 0:
        return print(mini)
    else:
        maxi = mini
        mini = ostatok
        kvadrat(maxi, mini)


kvadrat(maxi, mini)
