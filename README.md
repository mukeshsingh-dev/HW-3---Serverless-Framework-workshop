Serverless Patterns — Module 3
This project implements the Orders service with AWS SAM and Python: DynamoDB, API Gateway, a shared Lambda layer, and create/get/list/edit/cancel operations.

Build and deploy in an AWS SAM environment:

sam build
sam deploy --guided
Run local unit tests:

pytest -q
