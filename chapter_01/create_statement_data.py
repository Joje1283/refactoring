from functools import reduce
from math import floor
import copy
from abc import ABCMeta, abstractmethod
from pipelist import On


class PerformanceCalculator(metaclass=ABCMeta):  # 추상 클래스
    def __init__(self, performance, play):
        self.performance = performance
        self.play = play

    @classmethod
    def create_performance_calculator(cls, performance, play):  # 생성자 대신 팩터리 함수를 이용한 인스턴스 반환
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
    def amount(self):  # 추상 메서드
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def __init__(self, *args, **kwargs):
        result = super(ComedyCalculator, self).__init__(*args, **kwargs)
        print('ComedyCalculator')

    @property
    def amount(self):  # 추상 메서드
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result

    @property
    def volume_credits(self):  # 오버라이드
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
        result['play'] = calculator.play  # 공연 이름 및 타입
        result['amount'] = calculator.amount  # 공연 견적 (가격)
        result['volume_credits'] = calculator.volume_credits  # 공연에 대한 적립 포인트
        return result

    statement_data = {'customer': invoice['customer'],
                      'performances': list(map(enrich_performance, invoice['performances']))}
    # list(On(invoice['performances']).map(enrich_performance))
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    return statement_data
