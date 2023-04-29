# worker_safety
## we can now test the API using tools such as cURL or Postman. For example, i am using the following cURL commands to post a new worker and get a list of workers:
curl -H "Content-Type: application/json" -X POST -d '{"name":"karthik","age":21,"address":"vizag","contact_info":"...","medical_history":"...","safety_breaches":1}' http://localhost:8000/api/workers/create/
