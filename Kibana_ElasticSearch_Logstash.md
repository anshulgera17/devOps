# Elastic search, Kibana learning and setup
- Q1. What is ELK ?
- Q2. What is Elastic search and Kibana ?

- Download elastic search, Kibana and filebeat in windows, Unzip all folders
- Run .\elasticsearch batch file in /bin folder 
- check localhost:9200
- Then go to kibana folder and run `kibana.bat` file in `/bin` folder
- Check kibana dashboard using `localhost:5601`
- Then go to filebeat folder, File Beat config file /etc/filebeat/filebeat.yml
- `sudo filebeat modules enable aws /etc/filebeat/modules.d/aws.yml`
- and add aws s3 details in the above file

### filebeat.inputs:
```
filebeat.inputs:
- type: s3
  queue_url: https://sqs.us-east-1.amazonaws.com/123/test-queue
  access_key_id: '<access_key_id>'
  secret_access_key: '<secret_access_key>'
  session_token: '<session_token>'
or
filebeat.inputs:
- type: s3
  queue_url: https://sqs.us-east-1.amazonaws.com/123/test-queue
  access_key_id: '${AWS_ACCESS_KEY_ID:""}'
  secret_access_key: '${AWS_SECRET_ACCESS_KEY:""}'
  session_token: '${AWS_SESSION_TOKEN:""}'
Use IAM role ARN
filebeat.inputs:
- type: s3
  queue_url: https://sqs.us-east-1.amazonaws.com/123/test-queue
  role_arn: arn:aws:iam::123456789012:role/test-mb
Use shared AWS credentials file
filebeat.inputs:
- type: s3
  queue_url: https://sqs.us-east-1.amazonaws.com/123/test-queue
  credential_profile_name: test-fb
```