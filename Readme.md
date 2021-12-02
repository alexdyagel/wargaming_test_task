# Wargaming API tests

Prerequisites:
Make sure you have docker installed

## Prepare test data

Fill config.json file with application id and access token
Example:
{
  "application_id": "9eac9a2b2924bb0ace0a7834dea646e0",
  "access_token": "d5b08361f6f4af4d35a77dc14dd8455be584b806"
}

## Run tests

To run all tests in project you can just run next two commands from root directory. 

    docker build -t <some_name> . 
    docker run <some_name>

