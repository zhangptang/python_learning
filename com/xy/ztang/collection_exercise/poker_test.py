# -*-coding:utf-8-*-
import random


class Card(object):
    """
     一张牌
     """

    def __init__(self, decor, face):
        """
         初始化
         :param decor: 花色
         :param face:  面值
         """
        self._decor = decor
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def decor(self):
        return self._decor

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return f'{self._decor}{face_str}'

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """
    一副牌
    """

    def __init__(self):
        self._cards = [Card(decor, face) for decor in '♠♥♣♦' for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """
        洗牌
        :return:
        """
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """
        发牌
        :return:
        """
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)


class Player(object):
    """
    玩家
    """

    def __init__(self, name):
        self._name = name
        self._cards_on_hands = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hands(self):
        return self._cards_on_hands

    def get(self, card):
        self._cards_on_hands.append(card)

    def arrange(self, card_key):
        """
        规整牌
        :param card_key:
        :return:
        """
        self._cards_on_hands.sort(key=card_key)


def sort_rule(card):
    """ 排序规则"""
    # return (card.decor, card.face)
    return card.face


def main():
    p = Poker()
    p.shuffle()
    players = [Player('一条'), Player('一筒'), Player('一万'), Player('一红中')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(f'{player.name}:', end=' ')
        player.arrange(sort_rule)
        print(player.cards_on_hands)


if __name__ == '__main__':
    main()
