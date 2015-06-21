__author__ = 'Ahmed Hani Ibrahim'
import numpy as np
from Player import Player
import CONSTANTS
from matplotlib import pyplot as plt

testFixedEps10 = Player(CONSTANTS.NUM_OF_BANDITS, epsilon=0.4)
testFixedEps10.runGame(CONSTANTS.NUM_OF_GAMES)

testFixedEps12 = Player(CONSTANTS.NUM_OF_BANDITS, epsilon=0.0)
testFixedEps12.runGame(CONSTANTS.NUM_OF_GAMES)

testDecayEps10 = Player(CONSTANTS.NUM_OF_BANDITS, epsilon=0.122)
testDecayEps10.runGame(CONSTANTS.NUM_OF_GAMES, epsilonDecayFactor=0.56, epsilonDecayStep=10)

testDecayEps20 = Player(CONSTANTS.NUM_OF_BANDITS, epsilon=0.2)
testDecayEps20.runGame(CONSTANTS.NUM_OF_GAMES, epsilonDecayFactor=0.9, epsilonDecayStep=100)

plt.figure()
plt.xlabel('Game #')
plt.ylabel('Average value')

plt.plot(testFixedEps10.AvgRewardValue, label='Fixed epsilon=0.4')
plt.plot(testFixedEps12.AvgRewardValue, label='Fixed epsilon=0.0')
plt.plot(testDecayEps10.AvgRewardValue, label='Decay epsilon=0.122')
plt.plot(testDecayEps20.AvgRewardValue, label='Decay epsilon=0.4')

plt.legend().draggable(True)
plt.show()