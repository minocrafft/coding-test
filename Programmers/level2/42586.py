"""
기능개발

link: https://programmers.co.kr/learn/courses/30/lessons/42586
"""
import math


def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100.0 - x) / y) for x, y in zip(progresses, speeds)]
    complete = 0

    for i in range(len(day)):
        if day[i] > day[complete]:
            answer.append(i - complete)
            complete = i
    answer.append(len(day) - complete)

    return answer
