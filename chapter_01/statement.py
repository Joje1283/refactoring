from functools import reduce
from math import floor
import copy


def statement(invoice, plays):
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
    return render_plain_text(statement_data, plays)


def render_plain_text(data, plays):
    def usd(a_number):
        return f'${round(a_number / 100, 2):,}'

    result = f'청구 내역 (고객명: {data["customer"]})\n'

    for performance in data['performances']:
        result += f' {performance["play"]["name"]}: {usd(performance["amount"])} ({performance["audience"]}석)\n'

    result += f'총액: {usd(data["total_amount"])}\n'
    result += f'적립 포인트: {data["total_volume_credits"]}점\n'
    return result


if __name__ == '__main__':
    plays = {
        'hamlet': {'name': 'Hamlet', 'type': 'tragedy'},
        'as-like': {'name': 'As You Like It', 'type': 'comedy'},
        'othello': {'name': 'Othello', 'type': 'tragedy'}
    }

    invoices = [
        {
            'customer': 'BigCo',
            'performances': [
                {'playID': 'hamlet', 'audience': 55},
                {'playID': 'as-like', 'audience': 35},
                {'playID': 'othello', 'audience': 40},
            ]
        }
    ]

    invoice = invoices[0]

    print(statement(invoice, plays))
    """ 출력 결과
    청구 내역 (고객명: BigCo)
     Hamlet: $650.0 (55석)
     As You Like It: $580.0 (35석)
     Othello: $500.0 (40석)
    총액: $1,730.0
    적립 포인트: 47점
    """
