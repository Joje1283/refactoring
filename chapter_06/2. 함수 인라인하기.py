def rating(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1


def more_than_five_late_deliveries(driver):
    return driver['number_of_late_deliveries'] > 5


if __name__ == '__main__':
    driver = {'number_of_late_deliveries': 6}
    print(rating(driver))
