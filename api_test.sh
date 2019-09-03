#!/bin/bash

curl http://127.0.0.1:5000/v1/mma/messages/all

curl http://127.0.0.1:5000/v1/mma/messages?id=1

curl -i -H "Content-Type: application/json" -X POST -d '{"id":1,"message": "hello Moe", "palindrome": "False"}' http://127.0.0.1:5000/v1/mma/messages

curl -i -H "Content-Type: application/json" -X DELETE -d '{"id":1}' http://127.0.0.1:5000/v1/mma/messages

curl -i -H "Content-Type: application/json" -X PUT -d '{"id":4,"message": "hello Mike", "palindrome": "False"}' http://127.0.0.1:5000/v1/mma/messages