# n_deti = int(input())
# jad = list(map(int, input().split()))
# m_pen = int(input())
# razmer = list(map(int, input().split()))
# satisfied = 0

n_deti = input()
jad = [int(i) for i in input().split()]
m_pen = input()
size = [int(i) for i in input().split()]
satisfied = 0
size.sort()
if len(jad) <= len(size):
    jad.sort()
    size = size[-len(jad)::]
    for j in range(len(jad)-1, -1, -1):
        if jad[j] > size[-1]:
            continue
        else:
            size.pop(-1)
            satisfied += 1
else:
    jad.sort(reverse=True)
    jad = jad[-len(size)::]
    jad.sort()
    for j in range(len(jad)-1, -1, -1):
        if jad[j] > size[-1]:
            continue
        else:
            size.pop(-1)
            satisfied += 1
print(satisfied)

# for i in jad:
#     cnt = 0
#     while cnt < len(size):
#         if i <= size[cnt]:
#             satisfied += 1
#             size.pop(cnt)
#             break
#         else:
#             cnt += 1
# print(satisfied)

# jad.sort(reverse=True)
# razmer.sort()
# if len(jad) <= len(razmer):
#     razmer = razmer[-len(jad)::]
#     cnt = len(razmer) - 1
#     for j in range(len(jad)-1, -1, -1):
#         for r in range(len(razmer)-1, -1, -1):
#             if jad[j] <= razmer[r]:
#                 satisfied += 1
#                 # razmer.pop(r)
#                 break
# else:
#     jad = jad[-len(razmer)::]
#     jad.sort()
#     cnt = len(jad) - 1
#     for i in range(len(razmer)-1, -1, -1):
#         for j in range(len(jad)-1, -1, -1):
#             if razmer[i] >= jad[j]:
#                 satisfied += 1
#                 # jad.pop(j)
#                 break
# print(satisfied)
# # print(razmer)
# # print(jad)
#
# #1
# # if len(jad) <= len(razmer):
# #     jad.sort(reverse=True)
# #     for i in jad:
# #         if i <= max(razmer):
# #             razmer.remove(max(razmer))
# #             satisfied += 1
# #     print(satisfied)
# # else:
# #     razmer.sort()
# #     for i in razmer:
# #         if i >= min(jad):
# #             jad.remove(min(jad))
# #             satisfied += 1
# #     print(satisfied)
#
# #2
# # if len(jad) <= len(razmer):
# #     for i in jad:
# #         if i in razmer:
# #             razmer.remove(i)
# #             jad.remove(i)
# #             satisfied += 1
# #     jad.sort(reverse=True)
# #     for i in jad:
# #         if i <= max(razmer):
# #             razmer.remove(max(razmer))
# #             satisfied += 1
# #     print(satisfied)
# # else:
# #     for i in razmer:
# #         if i in jad:
# #             jad.remove(i)
# #             razmer.remove(i)
# #             satisfied += 1
# #     razmer.sort()
# #     for i in razmer:
# #         if i >= min(jad):
# #             jad.remove(min(jad))
# #             satisfied += 1
# #
# #     print(satisfied)
