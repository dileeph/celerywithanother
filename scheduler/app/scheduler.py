import logging, os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime

SQS_QUEUE = os.environ['SQS_QUEUE'] # like sqs.us-east-1.amazonaws.com/<accountid>/queuename
SCHEDULE = os.environ['BATCH_SCHEDULE'] # "hour=11&minute=07&day_of_week=thu,fri&day_of_month=1-7,15-21&month_of_year=*/3"

splitval = dict(map(lambda x: x.split('='), SCHEDULE.split('&')))
hour  = splitval['hour'] if 'hour' in splitval else '*'
minute = splitval['minute'] if 'minute' in splitval else '*'

day_of_week = splitval['day_of_week'] if 'day_of_week' in splitval else '*'
day_of_month = splitval['day_of_month'] if 'day_of_month' in splitval else '*'
month_of_year = splitval['month_of_year'] if 'month_of_year' in splitval else '*'


broker_url = f"sqs://@{SQS_QUEUE}"
queue_name = SQS_QUEUE.rsplit("/",1)[1]


app = Celery('batch', broker=broker_url)
app.conf.task_default_queue=queue_name

dt = datetime.now()
fmt = dt.strftime("%m/%d/%Y, %H:%M:%S")


app.conf.beat_schedule = {
        'refresh': {
            'task': 'assigner',
            'schedule': crontab(hour=hour, minute=minute, day_of_week=day_of_week, day_of_month=day_of_month, month_of_year=month_of_year),            
            'args': [fmt],
            }
        }