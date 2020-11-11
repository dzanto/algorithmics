import queue
import copy


def encrypt(string, template):

    dic_templ = {i: 0 for i in template}
    work_dic = copy.deepcopy(dic_templ)
    for i in template:
        dic_templ[i] += 1

    q = queue.Queue(maxsize=len(template))
    for i in template:
        q.put(0)

    count = 0

    for i in string:
        q_get = q.get()
        if q_get in template:
            work_dic[q_get] -= 1
        if i in template:
            work_dic[i] += 1
        q.put(i)
        if work_dic == dic_templ:
            count += 1
    return count


if __name__ == '__main__':
    string = list(input())
    template = list(input())
    print(encrypt(string, template))
