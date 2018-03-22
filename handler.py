import json
import datetime


def hello(event, context):
    body = {
        "date": datetime.datetime.today().isoformat()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def main():
    print(hello('event', 'context'))

if __name__ == "__main__":
    main()
