from functools import reduce
from math import floor
import copy
from abc import ABCMeta, abstractmethod


class PerformanceCalculator(metaclass=ABCMeta):
    def __init__(self, performance, play):
        self.performance = performance
        self.play = play

    @classmethod
    def create_performance_calculator(cls, performance, play):
        if play['type'] == 'tragedy':
            return TragedyCalculator(performance, play)
        elif play['type'] == 'comedy':
            return ComedyCalculator(performance, play)
        else:
            raise Exception(f'알 수 없는 장르: {play["type"]}')

    @abstractmethod
    def amount(self):
        pass

    @property
    def volume_credits(self):
        return max(self.performance['audience'] - 30, 0)


class TragedyCalculator(PerformanceCalculator):
    def __init__(self, *args, **kwargs):
        result = super().__init__(*args, **kwargs)
        print('TragedyCalculator')

    @property
    def amount(self):
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def __init__(self, *args, **kwargs):
        result = super(ComedyCalculator, self).__init__(*args, **kwargs)
        print('ComedyCalculator')

    @property
    def amount(self):
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result

    @property
    def volume_credits(self):
        result = super().volume_credits
        result += floor(self.performance['audience'] / 5)
        return result


def create_statement_data(invoice, plays):
    def play_for(a_performance):
        return plays[a_performance['playID']]

    def total_amount(data):
        return reduce(lambda total, performance: total + performance['amount'], data['performances'], 0)

    def total_volume_credits(data):
        return reduce(lambda total, performance: total + performance['volume_credits'], data['performances'], 0)

    def enrich_performance(performance):
        calculator = PerformanceCalculator.create_performance_calculator(performance, play_for(performance))
        result = copy.copy(performance)
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volume_credits'] = calculator.volume_credits
        return result

    statement_data = {'customer': invoice['customer'],
                      'performances': list(map(enrich_performance, invoice['performances']))}
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    return statement_data
