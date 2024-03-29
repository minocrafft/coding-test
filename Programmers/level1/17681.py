"""
[1차] 비밀지도

link: https://programmers.co.kr/learn/courses/30/lessons/17681
"""


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        wall = bin(arr1[i] | arr2[i])[2:].zfill(n)
        answer.append(wall.replace("0", " ").replace("1", "#"))

    return answer
