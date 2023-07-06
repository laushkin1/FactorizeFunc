from time import monotonic
from multiprocessing import Pool



def factorize(*numbers) -> list:
    res = []
    for num in numbers:
        n = 2
        numbers_list = [1, ]
        while True:
            if num == n:
                numbers_list.append(n)
                break
            elif num % n == 0:
                numbers_list.append(n)
            n += 1
        res.append(numbers_list)
    return res
    


if __name__ == "__main__":
    
    numbers = (128, 255, 99999, 10651060)
    with Pool(processes=len(numbers)) as p:
        start_func = monotonic()
        date = p.map(factorize, numbers)
        end_func = monotonic()
    res_time = end_func - start_func
    print(res_time)
    print(date)
        

    ####################################################
    # start_func = monotonic()
    # a, b, c, d = factorize(128, 255, 99999, 10651060)
    # end_func = monotonic()
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # res_time = end_func - start_func
    # print(res_time) 
    ####################################################
    
    
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    
