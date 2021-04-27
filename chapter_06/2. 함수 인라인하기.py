def rating(driver):
    return 2 if driver['number_of_late_deliveries'] > 5 else 1


if __name__ == '__main__':
    driver = {'number_of_late_deliveries': 6}
    print(rating(driver))
