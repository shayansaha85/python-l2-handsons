import timeit


def timer_f(function):
    def new_function():
        start_time = timeit.default_timer()
        function()
        elapsed = timeit.default_timer() - start_time
        print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))

    return new_function()


@timer_f
def summation():
    sum = 0
    for i in range(0, 1000):
        sum += i
    return sum
