__author__ = 'Ahmed Hani Ibrahim'
import numpy as np


class ArmedBandit(object):
    __mue = 0.0
    __sigma = 0.0

    def __init__(self, mue, sigma):
        self.__mue = mue
        self.__sigma = sigma

    def printData(self):
        return np.random.normal(self.__mue, self.__sigma)
