from datetime import datetime, timedelta


# 예시1 : 유효번위를 벗어나는 변수가 없을 때
def print_owing(invoice):
    def print_banner():
        print("*****************")
        print("**** 고객 채무 ****")
        print("*****************")

    print_banner()

    # 미해결 채무를 계산한다.
    outstanding = calculate_outstanding(invoice)

    # 마감일(dueDate)을 기록한다.
    record_due_date(invoice)
    # 세부 사항을 출력한다.
    print_details(invoice, outstanding)


def calculate_outstanding(invoice):
    result = 0
    for o in invoice['orders']:
        result += o['amount']
    return result


def record_due_date(invoice):
    invoice['due_date'] = datetime.now() + timedelta(days=30)


def print_details(invoice, outstanding):
    print(f'고객명: {invoice["customer"]}')
    print(f'채무액: {outstanding}')
    print(f'마감일: {invoice["due_date"].strftime("%Y-%m-%d")}')


if __name__ == '__main__':
    print_owing({
        'customer': 'jaesik',
        'orders': [{'amount': 1000}, {'amount': 1000}, {'amount': 1000}],
    })
