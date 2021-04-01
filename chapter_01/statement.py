from math import floor


def amount_for(a_performance):
    if play_for(a_performance)['type'] == 'tragedy':
        result = 40000
        if a_performance['audience'] > 30:
            result += 1000 * (a_performance['audience'] - 30)
    elif play_for(a_performance)['type'] == 'comedy':
        result = 30000
        if a_performance['audience'] > 20:
            result += 10000 + 500 * (a_performance['audience'] - 20)
        result += 300 * a_performance['audience']
    else:
        raise Exception(f'알수 없는 장르 {play_for(a_performance)["type"]}')
    return result


def play_for(a_performance):
    return plays[a_performance['playID']]


def volume_credits_for(a_performance):
    result = 0
    result += max(a_performance['audience'] - 30, 0)
    if 'comedy' == play_for(a_performance)['type']:
        result += floor(a_performance['audience'] / 5)
    return result


def statement(invoice):
    total_amount = 0
    volume_credits = 0
    result = f'청구 내역 (고객명: {invoice["customer"]})\n'

    for performance in invoice['performances']:
        volume_credits += volume_credits_for(performance)
        result += f' {play_for(performance)["name"]}: {amount_for(performance) / 100} ({performance["audience"]}석)\n'
        total_amount += amount_for(performance)
    result += f'총액: {total_amount/100}\n'
    result += f'적립 포인트: {volume_credits}점\n'
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

    print(statement(invoices[0]))
    """ 출력 결과
    청구 내역 (고객명: BigCo)
     Hamlet: 650.0 (55석)
     As You Like It: 580.0 (35석)
     Othello: 500.0 (40석)
    총액: 1730.0
    적립 포인트: 47점
    """