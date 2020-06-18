from celery import Celery
from time import sleep

app= Celery('app', backend='rpc://', broker='amqp://localhost')


@app.task
def add(x,y):
    sleep(5)
    return x+y 


# add.apply_async([3,4],countdown=10,expire=20)
# res =  add.delay(5,8)
# res.ready()==True
# res.get()
