import datetime as dt
import json

import boto3

sfn = boto3.client('stepfunctions')

while True:
    # activity task
    arn_hello_task = 'arn:aws:states:eu-west-1:749785218022:activity:hello-task'

    hello_task = sfn.get_activity_task(activityArn=arn_hello_task)
    print(hello_task.keys())
    print(hello_task['input'])

    # sfn.send_task_heartbeat(taskToken=hello_task['taskToken'])

    try:
        result = {'result': 'Hello world from the worker', 'datetime': str(dt.datetime.now())}
        res = sfn.send_task_success(taskToken=hello_task['taskToken'],
                                    output=json.dumps(result))
        print('execution completed')
        print(res)

    except Exception as e:
        print('error')
