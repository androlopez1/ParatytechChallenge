# Paratytech challenge

RESTful api that services requests for netflix items. Built using flask, GCP datastore and click.

## Quickstart

To run the development version of the app

```bash
python main.py 
```

Go to `http://localhost:8080`. You will see the database filled with data.

Endpoints:
- '/' -> Read the data and call the "system_module_2" API using http
- '/load' -> Process to ingest data into the sytem (system_module_1)
- '/query' -> API to load and visualize the data using a REST API


## Running CLI client

Query data from the `system_module_2` server and see the responses.

```bash
$  python client.py "Mine 9"
show_id: s2704
title: Mine 9
director: Eddie Mensore
cast: Terry Serpico, Kevin Sizemore, Mark Ashworth, Clint James, Drew Starkey, Erin Elizabeth Burns
country: United States
date_added: April 6, 2020
rating: TV-MA
duration 83 min
listed_in: Dramas, Independent Movies
release_year: 2019
description: A methane explosion leaves a group of miners trapped two miles deep into the earth with a small oxygen supply and desperate for any means of survival.
```

## Deployment

To deploy the application in prod, a new .env file is required containing the instances ID's and prod server.

## Running Tests

To run all tests:

```bash
python -m pytest 
```

Remember to keep the application main server running in order to get the test responses correctly.

## Important Notes:
- The app is using threading module to achieve concurrency, however, another options could be considered depending on the requirements, like celery.
- The app is using application factory to reach modularization, scalability and maintainability.
- Could be a good idea to handle user sessions to improve concurrency, but time restrictions avoided the implementation.
- Due to limited quota of the free GCP resources, containers with docker were not implemented that could be the best option to deliver to QA and other stages.