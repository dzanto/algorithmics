def solution(mini, maxi):
    # print(mini, maxi)
    if round(mini, 5) == round(maxi, 5):
        return round(mini, 5)

    rez = ((mini + maxi) / 2) ** 2

    if rez > 2:
        maxi = ((mini + maxi) / 2)
    else:
        mini = ((mini + maxi) / 2)

    return(solution(mini, maxi))


if __name__ == "__main__":
    print(solution(1, 2))
