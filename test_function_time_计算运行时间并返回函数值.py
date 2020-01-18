import time

def countTime(function, *args, **kwargs):
    start = time.time()
    result = function(*args, **kwargs)
    end = time.time()
    print("time: {}".format(end - start))

    return result