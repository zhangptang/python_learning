# -*-coding:utf-8-*-
"""
双色球
"""
import random


def random_select():
    """
    随机选择一注
    :return:
    """
    select_balls = []
    red_balls = [x for x in range(1, 34)]
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(random.randint(1, 16))
    return select_balls


def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) -1:
            print(" |", end=' ')
        print(f'{ball}', end=' ')
    print()


def main():
    n = int(input('随机几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
