# 온도 측정값을 표현하는 데이터
station = {
    'name': 'ZB1',
    'readings': [
        {'temp': 47, 'time': '2016-11-10 09:10'},
        {'temp': 53, 'time': '2016-11-10 09:20'},
        {'temp': 58, 'time': '2016-11-10 09:30'},
        {'temp': 53, 'time': '2016-11-10 09:40'},
        {'temp': 51, 'time': '2016-11-10 09:50'},
    ]
}

operation_plan = {
    'temperature_floor': 50,
    'temperature_ceiling': 55
}


class NumberRange:
    def __init__(self, min, max):
        self._data = {'min': min, 'max': max}

    @property
    def min(self):
        return self._data['min']

    @property
    def max(self):
        return self._data['max']

    def contains(self, arg):
        return self.min <= arg <= self.max


# 정상 범위를 벗어난 측정값을 찾는 함수
def readings_outside_range(station, range=None):
    return list(filter(lambda x: not range.contains(x['temp']), station['readings']))


# 호출문
if __name__ == '__main__':
    range = NumberRange(operation_plan['temperature_floor'], operation_plan['temperature_ceiling'])
    alerts = readings_outside_range(station, range)
    print(alerts)
