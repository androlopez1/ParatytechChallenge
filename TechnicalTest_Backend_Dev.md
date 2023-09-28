# Technical test

The idea is to provide a solution that customers can use to get information from a csv file and create an API to visualize the data.

The system has two parts:

- Ingestion of the file data.
- Create an API to load and visualize the data using a REST API.

## High level requirements

It is required to have:

- Process to ingest data from the attached file into the system (known as `system_module_1` from now on).
- Server architecture for scalability and stability (known as `system_module_2` from now on).

### Ingestion processing

`system_module_1` should be implemented as a python script using Python 3. This script will read the data and call the "system_module_2" API using http.


### REST-API

`system_module_2`'s server should offer a REST API that can be consumed by an application, or potentially any other services.

This has to be created using python 3 Flask in Google App Engine (Google Cloud).

See https://cloud.google.com/appengine/docs/standard/python3/building-app

It should include at least 2 endpoints, one to load the data and another one to Query the data.

You can decide how to persist the data in the server using any of the available solutions in Google Cloud (Datastore, SQL, storage).

## Task

Assume I am a business man with an idea. I need you to create the product. The task is to build that system (`system_module_1` and `system_module_2`).

Important things:

- The goal is to have a production-ready solution.
- Take whichever decisions you need in order to build the product.
- Think that this system will be delivered to a integration team, QA team, delivery team...
- Pay attention to the user experience too.
- Concurrent sessions must be supported.
- Example of interaction is just a draft with the only purpose of showing the idea to the developer. Feel free to implement it in other way, with different requests, etc.
- The outcome of this task should have "Open Source" quality.


### BONUS_EXERCISE (Optional)

Create a client as a CLI application for customers to query data from the `system_module_2` server and show the responses.

```bash
$ ./cli title "Ganglands"
    To protect his family from a powerful drug lord, skilled thief Mehdi and his expert team of robbers are pulled into a violent and deadly turf war.
```


## Notes
If you think that something is required but, because of time constraints, it is not worthy to fully implement it, you can skip it and just prepare a good description of what should have been done, why, how, etc.




