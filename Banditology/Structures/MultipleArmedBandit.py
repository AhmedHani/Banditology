__author__ = 'Ahmed Hani Ibrahim'

from Structures.ArmedBandit import ArmedBandit


class MultipleArmedBandit(object):
    __numberOfBandits = 0
    __bandits = dict()

    def __init__(self, numberOfBandits):
        self.__numberOfBandits = numberOfBandits
        self.__bandits = dict()

        for i in range(0, self.__numberOfBandits):
            self.__bandits[i] = ArmedBandit(i, self.__numberOfBandits)

    def drawBanditData(self, banditIndex):
        return self.__bandits[banditIndex].printData()

