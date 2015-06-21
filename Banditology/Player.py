__author__ = 'Ahmed Hani Ibrahim'
from Structures.MultipleArmedBandit import MultipleArmedBandit
import numpy as np


class Player(object):
    __Q = dict()
    __game = 0
    __epsilon = 0.0
    __numberOfBandits = 0
    __numberOfGames = dict()
    __rewardValue = 0.0
    __saveAction = []
    __saveActionValue = []

    @property
    def AvgRewardValue(self):
        pass
    @AvgRewardValue.getter
    def AvgRewardValue(self):
        return self.__saveActionAverageValue

    def __init__(self, numberOfBandits, epsilon):
        self.__numberOfBandits = numberOfBandits
        self.__epsilon = epsilon
        self.__game = MultipleArmedBandit(self.__numberOfBandits)
        self.__Q = dict()
        self.__numberOfGames = dict()
        self.__rewardValue = 0.0
        self.__saveAction = []
        self.__saveActionAverageValue = []

        for i in range(0, self.__numberOfBandits):
            self.__Q[i] = 100000
            self.__numberOfGames[i] = 0

    def runGame(self, games=1, epsilonDecayFactor=None, epsilonDecayStep=None):
        for game in range(0, games):
            if epsilonDecayFactor != None:
                if game % epsilonDecayStep == 0:
                    self.__epsilon *= epsilonDecayFactor

            bandit = None
            randomValue = np.random.random()

            if randomValue >= self.__epsilon:
                bandit = max(self.__Q, key=self.__Q.get)
            else:
                bandit = np.random.randint(0, self.__numberOfBandits)

            currentReward = self.__game.drawBanditData(bandit)
            self.__Q[bandit] += (1.0 / (1.0 + self.__numberOfGames[bandit])) * \
                                (currentReward - self.__Q[bandit])
            self.__numberOfGames[bandit] += 1
            self.__rewardValue += currentReward
            self.__saveAction.append(bandit)
            self.__saveActionAverageValue.append(float(self.__rewardValue / float(game + 1)))





