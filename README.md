# Paratytech challenge

RESTful api that services requests for netflix items. Built using flask and click.

## Quickstart

To run the development version of the app

```bash
python main.py 
```

Go to `http://localhost:8080`. You will see the database filled with data.

Endpoints:
- '/' -> Read the data and call the "system_module_2" API using http
- '/load' -> Process to ingest data from the attached file into the sytem (system_module_1)
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

To run all tests, run

```bash
python -m pytest 
```

## Important Notes:
- The app is using threading module to achieve concurrency, however, another options could be considered depending on the requirements, like celery.
- The app is using application factory to reach modularization and scalability.
- Could be a good idea to handle user sessions to improve concurrency, but time restrictions avoid the implementation.
- Due to time limit cuota of the free GCP respurces, containers with docker were not implemented that could be the best option to deploy to QA and other stages.