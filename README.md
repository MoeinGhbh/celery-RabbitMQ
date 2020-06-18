# Use Celery module to work with RabbitMQ (AMQP) broker

## steps:

---

    1- sudo apt-get install python3-venv
    2- python3 -m venv env
    3- pip install celery
    4- sudo pip3 freeze > requirments.txt
    5- pip install flower
       a- flower -A app --p port=5555
       b- celery flower -A app --address=127.0.0.1 --p port=5555
       c- celery flower -A proj --broker=amqp://guest:guest@localhost:5672//


    5- in Terminal => python => from app import add => 
                add.apply_async([3,4])
                add.apply_async([3,4], countdown=10)
    6- source env/bin/activate => celery worker -A app -l info




    celery shell                => make ability to work same terminal
    celery status               => show active nodes
    celery purge                => delete all activity
    celery inspect active       => show all activities
    celery inspect scheduled    => show scheduled activity 

