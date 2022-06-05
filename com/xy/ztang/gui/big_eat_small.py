# -*-coding:utf-8-*-
from random import randint

import pygame

from com.xy.ztang.gui.ball import Color, Ball


def main():
    # 定义用来装所有球的容器
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # 标题
    pygame.display.set_caption('大蛇吃小蛇')
    x, y = 50, 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
        screen.fill((242, 242, 242))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
