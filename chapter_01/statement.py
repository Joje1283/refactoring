from math import floor
import copy


def statement(invoice, plays):
    def play_for(a_performance):  # render_plain_text의 중첩 함수였던 play_for를 statement로 옮김
        return plays[a_performance['playID']]

    def enrich_performance(performances):
        result = copy.copy(performances)
        for performance in result:
            performance['play'] = play_for(performance)  # 중간 데이터에 연극 정보를 저장
        return result

    statement_data = {'customer': invoice['customer'], 'performances': enrich_performance(invoice['performances'])}
    return render_plain_text(statement_data, plays)


def render_plain_text(data, plays):
    def total_amount():
        result = 0
        for performance in data['performances']:
            result += amount_for(performance)
        return result

    def total_volume_credits():
        result = 0
        for performance in data["performances"]:
            result += volume_credits_for(performance)
        return result

    def usd(a_number):
        return f'${round(a_number / 100, 2):,}'

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance['audience'] - 30, 0)
        if 'comedy' == a_performance['play']['type']:
            result += floor(a_performance['audience'] / 5)
        return result

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

    result = f'청구 내역 (고객명: {data["customer"]})\n'

    for performance in data['performances']:
        result += f' {performance["play"]["name"]}: {usd(amount_for(performance))} ({performance["audience"]}석)\n'

    result += f'총액: {usd(total_amount())}\n'
    result += f'적립 포인트: {total_volume_credits()}점\n'
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
