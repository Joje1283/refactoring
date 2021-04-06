from create_statement_data import create_statement_data


def usd(a_number):
    return f'${round(a_number / 100, 2):,}'


def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data):
    result = f'청구 내역 (고객명: {data["customer"]})\n'

    for performance in data['performances']:
        result += f' {performance["play"]["name"]}: {usd(performance["amount"])} ({performance["audience"]}석)\n'

    result += f'총액: {usd(data["total_amount"])}\n'
    result += f'적립 포인트: {data["total_volume_credits"]}점\n'
    return result


def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))


def render_html(data):
    result = f'<h1>청구 내욕 (고객명: ${data["customer"]}</h1>\n'
    result += '<table>\n'
    result += '<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>'
    for performance in data['performances']:
        result += f'  <tr><td>{performance["play"]["name"]}</td><td>({performance["audience"]}석)</td>'
        result += f'<td>{usd(performance["amount"])}</td></tr>\n'
    result += "</table>\n"
    result += f'<p>총액: <em>{usd(data["total_amount"])}</em></p>\n'
    result += f'<p>적립 포인트: <em>{data["total_volume_credits"]}</em>점</p>\n'
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

    # print(statement(invoice, plays))
    print(html_statement(invoice, plays))
    """ 출력 결과
    청구 내역 (고객명: BigCo)
     Hamlet: $650.0 (55석)
     As You Like It: $580.0 (35석)
     Othello: $500.0 (40석)
    총액: $1,730.0
    적립 포인트: 47점
    """
