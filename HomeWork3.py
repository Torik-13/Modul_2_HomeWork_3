cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in cars:
    print('Я езжу на автомабиле марки', i)
    if i != "BMW":
        cars_count += 10
        print(cars_count)
