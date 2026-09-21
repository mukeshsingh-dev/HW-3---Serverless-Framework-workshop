import json
import os
import time
import uuid
from decimal import Decimal


def _table():
    import boto3
    return boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def create_order(event):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    data = json.loads(event.get("body") or "{}", parse_float=Decimal)
    order_id = data.get("orderId") or str(uuid.uuid4())
    data.update({"userId": user_id, "orderId": order_id})
    data.setdefault("status", "PLACED")
    data.setdefault("orderTime", str(time.time()))
    _table().put_item(
        Item={"userId": user_id, "orderId": order_id, "data": data},
        ConditionExpression="attribute_not_exists(orderId)",
    )
    return data


def lambda_handler(event, context):
    return {"statusCode": 200, "headers": {}, "body": json.dumps(create_order(event), default=str)}
