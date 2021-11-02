import boto3
import os, logging
#logger = get_task_logger(__name__)

from datetime import datetime
import time
from celery import Celery
from psycopg2 import connect

SQS_QUEUE = os.environ['SQS_QUEUE'] # like sqs.us-east-1.amazonaws.com/<accountid>/queuename
DB_NAME= os.environ['DB_NAME']
DB_USER= os.environ['DB_USER']
DB_PASSWORD= os.environ['DB_PASSWORD']
DB_HOST= os.environ['DB_HOST']
DB_PORT= os.environ['DB_PORT']


broker_url = f"sqs://@{SQS_QUEUE}"
queue_name = SQS_QUEUE.rsplit("/",1)[1]


app = Celery('batch', broker=broker_url)
app.conf.task_default_queue=queue_name

conn = connect(dbname=DB_NAME,host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
cur = conn.cursor()
##These are sample jobs kept as placeholders - these will be replaced with actual functional code.

@app.task( name="add")
def add(x):
    msg = f"processing record {x}"
    logging.info(msg)
    #cur.execute('select counter from my_tracker where id = (%s)',(x,))
    #res = cur.fetchone()
    #logging.info(f"counter value {res[0]} for id={x}")
    #nextval = res[0]+1
    
    #cur.execute('update my_tracker set counter = (%s) where id = (%s)',(nextval,x))
    #conn.commit()


@app.task(name="assigner")
def assigner(x):
    logging.info(f"assignment tookup at {x}")

    for i in range(100):
        add.s(i).delay()
    #cur.execute('select id from my_tracker')
    #rows = cur.fetchall()
    #for row in rows:
    #   logging.info(row[0])
    #  add.s(row[0]).delay()
