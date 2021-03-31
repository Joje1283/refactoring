from math import floor


def amount_for(performance, play):
    if play['type'] == 'tragedy':
        result = 40000
        if performance['audience'] > 30:
            result += 1000 * (performance['audience'] - 30)
    elif play['type'] == 'comedy':
        result = 30000
        if performance['audience'] > 20:
            result += 10000 + 500 * (performance['audience'] - 20)
        result += 300 * performance['audience']
    else:
        raise Exception(f'알수 없는 장르 {play["type"]}')
    return result


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'청구 내역 (고객명: {invoice["customer"]})\n'

    for performance in invoice['performances']:
        play = plays[performance['playID']]

        this_amount = amount_for(performance, play)

        volume_credits += max(performance['audience'] - 30, 0)
        if 'comedy' == play['type']:
            volume_credits += floor(performance['audience'] / 5)
        result += f' {play["name"]}: {this_amount / 100} ({performance["audience"]}석)\n'
        total_amount += this_amount
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

    print(statement(invoices[0], plays))
    """ 출력 결과
    청구 내역 (고객명: BigCo)
     Hamlet: 650.0 (55석)
     As You Like It: 580.0 (35석)
     Othello: 500.0 (40석)
    총액: 1730.0
    적립 포인트: 47점
    """