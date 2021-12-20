import redis
import time

redis_client = redis.Redis()

while True:
    redis_client.publish('channel1', message='Hello subscribers')
    time.sleep(1)


