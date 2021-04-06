from functools import reduce
from math import floor
import copy

def create_statement_data(invoice, plays):  # 중간 데이터 생성을 전담
    def play_for(a_performance):
        return plays[a_performance['playID']]

    def amount_for(a_performance):
        if a_performance['play']['type'] == 'tragedy':
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)
        elif a_performance['play']['type'] == 'comedy':
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']
        else:
            raise Exception(f'알수 없는 장르 {a_performance["play"]["type"]}')
        return result

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance['audience'] - 30, 0)
        if 'comedy' == a_performance['play']['type']:
            result += floor(a_performance['audience'] / 5)
        return result

    def total_amount(data):
        return reduce(lambda total, performance: total + performance['amount'], data['performances'], 0)

    def total_volume_credits(data):
        return reduce(lambda total, performance: total + performance['volume_credits'], data['performances'], 0)

    def enrich_performance(performances):
        result = copy.copy(performances)
        for performance in result:
            performance['play'] = play_for(performance)
            performance['amount'] = amount_for(performance)
            performance['volume_credits'] = volume_credits_for(performance)
        return result

    statement_data = {'customer': invoice['customer'], 'performances': enrich_performance(invoice['performances'])}
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    return statement_data