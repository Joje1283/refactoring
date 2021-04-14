import copy


class Producer:  # 데이터 저장소
    def __init__(self, province, data):
        self._province = province
        self._cost = data['cost']
        self._name = data['name']
        self._production = data['production'] if data['production'] else 0

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, arg):
        self._cost = int(arg)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amount_str):
        # amount = int(amount_str)
        new_production = int(amount_str)
        self._province['total_production'] += new_production - self._production
        self._production = new_production


class Province:  # json 데이터로부터 지역 정보를 읽어오는 코드
    def __init__(self, doc):
        self._name = doc['name']
        self._producers = []
        self._total_production = 0
        self._demand = doc['demand']
        self._price = doc['price']
        for d in doc['producers']:
            self.add_producer(Producer(self, d))

    def add_producer(self, arg: Producer):
        self._producers.append(arg)
        self._total_production += arg.production

    @property
    def name(self):
        return self._name

    @property
    def producers(self):
        return copy.deepcopy(self._producers)

    @property
    def total_production(self):
        return self._total_production

    @total_production.setter
    def total_production(self, arg):
        self._total_production = arg

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, arg):
        self._demand = int(arg)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg)

    @property
    def shortfall(self):
        return self._demand - self.total_production * 2

    @property
    def profit(self):
        return self.demand_value - self.demand_cost

    @property
    def demand_value(self):
        return self.satisfied_demand * self.price

    @property
    def satisfied_demand(self):
        return min(self._demand, self.total_production)

    @property
    def demand_cost(self):
        remaining_demand = self.demand
        result = 0
        producers = sorted(self.producers, key=lambda a, b:a['cost'] - b['cost'])
        for producer in producers:
            contribution = min(remaining_demand, producer['production'])
            remaining_demand -= contribution
            result += contribution * producer['cost']
        return result


def sample_province_data():
    return {
        'name': 'Asia',
        'producers': [
            {'name': 'Byzantium', 'cost': 10, 'production': 9},
            {'name': 'Attalia', 'cost': 12, 'production': 10},
            {'name': 'Sinope', 'cost': 10, 'production': 6},
        ],
        'demand': 30,
        'price': 20
    }


if __name__ == '__main__':
    asia = Province(sample_province_data())
    print(asia.shortfall)
