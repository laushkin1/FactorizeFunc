from time import monotonic, sleep
from multiprocessing import Pool


def factorize(number: str) -> list:
    res = []
    for i in filter(lambda x: number % x == 0, range(1, number+1)):
        res.append(i)
    return res


if __name__ == "__main__":

    numbers = (128, 255, 99999, 10651060)
    with Pool(processes=len(numbers)) as p:
        start_func = monotonic()
        date = p.map(factorize, numbers)
        end_func = monotonic()
    res_time = end_func - start_func
    print(f"Result of working with a multiprocessor:\n{date}\nTime: {res_time}\n")

    ####################################################
    start_func = monotonic()
    a = factorize(128)
    b = factorize(255)
    c = factorize(99999)
    d = factorize(10651060)
    end_func = monotonic()
    res_time = end_func - start_func
    print(f"Result of work without a multiprocessor:\n{a}\n{b}\n{c}\n{d}\nTime: {res_time}\n")
    ####################################################

    # # a, b, c, d = factorize(128, 255, 99999, 10651060)
    print("Start test...")
    sleep(1)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("The test has been successful")
