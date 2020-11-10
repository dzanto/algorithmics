import copy

def get_world(string, words):
    cnt_list = [0 for i in range(len(words))]
    string.reverse()
    work_words = copy.deepcopy(words)
    for i in string:
        for num_wrd in range(len(work_words)):
            if len(work_words[num_wrd]) < 1:
                continue
            if i == work_words[num_wrd][-1]:
                work_words[num_wrd].pop()
                cnt_list[num_wrd] += 1

    for i in range(len(cnt_list)):
        if cnt_list[i] != len(words[i]):
            cnt_list[i] = 0

    max_world = max(cnt_list)
    if max_world == 0:
        return ''
    max_worlds = []
    for i in range(len(cnt_list)):
        if cnt_list[i] == max_world:
            max_worlds.append(words[i])

    str_max_worlds = [''.join(word) for word in max_worlds]

    str_max_worlds.sort()

    return str_max_worlds[0]


if __name__ == '__main__':
    string = list(input())
    number_of_words = int(input())
    words = []
    for i in range(number_of_words):
        words.append(list(input()))
    rez_world = get_world(string, words)
    print(rez_world)
