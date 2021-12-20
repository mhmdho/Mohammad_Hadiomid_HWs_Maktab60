import redis
import time

redis_client = redis.Redis()

p = redis_client.pubsub()
p.subscribe('channel1')


while True:
    message = p.get_message() + time.time
    if message:
        print(message['data'])
        time.sleep(0.1)


# 2nd way:
# while True:
#     p.listen().__next__()


# 3nd way:
# for message in p.listen():
#     print(message)