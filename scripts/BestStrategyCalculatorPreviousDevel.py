# -*- coding: utf-8 -*-

from scripts.BestStrategyCalculatorHelpers.BestStrategyCalculator import Strategy
from scripts.Features.Features import *


def add_already_calculated(bsc, tagger):
    bsc.add_test(Strategy(Feature1(), Feature2()))
