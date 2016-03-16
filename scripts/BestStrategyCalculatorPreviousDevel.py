# -*- coding: utf-8 -*-

from Features import *
from BestStrategyCalculator import Strategy


def add_already_calculated(bsc, tagger):
    bsc.add_test(Strategy(Feature1(), Feature2()))
