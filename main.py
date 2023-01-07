import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def factorial(x: int):
    if x <= 1:
        return 1
    result = x * factorial(x-1)
    return result


if __name__ == '__main__':

    num = int(input('input number for calculate factorial: '))
    print(f'Result = {factorial(num)}')
