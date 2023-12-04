---
title: Sayari Python SDK
category: 653044fd9479c1000c221860
---
# Introduction
Welcome to the Sayari Graph SDK for Python. The goal of this project is to get you up and running as quickly as possible so you can start benefiting from the power of Sayari Graph. In the new few sections you will learn how to setup and use the Sayari Graph SDK. We also document some example use cases to show how easy it is to build the power of Sayari Graph into your application.

# Setup
## Prerequisites
The only thing you need to start using this SDK are your Client_ID and Client_Secret provided to you by Sayari. (@Aleks to add info about getting these creds)

## Installation
To install the SDK, simply run `pip install sayari --extra-index-url https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/simple/`
(The cmd above will change once this SDK is available publicly)

# Quickstart
This section will walk you through a basic example of connecting to Sayari Graph, resolving and entity, and getting that entity's detailed information.

## Connecting
To connect to Sayari Graph, simply create a client object by calling the SDK's 'Connect' method and passing in your client ID and secret. **Note**: For security purposes, it is highly recommended that you don't hardcode your client ID and secret in your code. Instead, simply export them as environment variables and use those.
```python
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
```

## Resolving an entity
Now that we have a client, we can use the Resolution method to find an entity. To do this we pass in the fields we want to match on. Full documentation of this endpoint can be seen in the API docs.

A request to resolve an entity with the name field matching "Victoria Beckham" is shown below:
```python
resolution = client.resolution.resolution(name="Victoria Beckham")
```

## Getting entity information
The resolution results themselves do contain some information about the entities found, but to get all the details for that entity we need to call the "get entity" endpoint.

A request to view the first resolved entity (best match) from the previous request would look like this:
```python
entity_details = client.entity.get_entity(resolution.data[0].entity_id)
```

## Complete example
After the steps above you should be left with code looks like this. We can add one final line to print all the fields of the resolved entity to see what it looks like.
```python
import os
from sayari import Connection

# NOTE: To connect you must provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables

# Create a client that is authed against the API
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# resolve by name
resolution = client.resolution.resolution(name="Victoria Beckham")

# get the entity details for the resolved entity
entity_details = client.entity.get_entity(resolution.data[0].entity_id)
print(entity_details)
```

# Advanced
When interacting with the API directly, there are a few concepts that you need to handle manually. The SDK takes care of these things for you, but it is important to understand them if you want to use the SDK properly.

## Authentication and token management
As you can see from the API documentation, there is an endpoint provided for authenticating to Sayari Graph which will return a bearer token. This token is then passed on all subsequent API calls to authenticate them. The SDK handles this process for you by first requesting the token and then adding it to all subsequent requests.

In addition to simplifying the connection process, the SDK is also designed to work in long-running application and keep the token up to date by rotating it before it expires. This is all handled behind the scenes by the client object itself and should require no additional action by the user.

## Rate limiting
Some Sayari Graph endpoints are more compute intensive than others. To adequately allocate resources across customers and prevent service degradation, individual users are rate limited. It is very unlikely that you would ever encounter these limits when making requests manually or even in a single-threaded application. Typically, rate limiting will only come into play when making multiple API requests at the same time.

When a request is rate limited, the API will respond back with a 429 status code as well as a 'Retry-After' response header that tells you how long to wait before making a subsequent request (i.e. 5s).

To make things simpler, the SDK handles this for you and will automatically wait and retry requests if a 429 is received.

# Tutorials
You should now have all the tools you need to start using the Sayari Graph Go SDK yourself. If you would like additional inspiration, please consider the following use-case-specific tutorials.

## Screening

## Investigations

## Trade Analysis

# Examples
**Please see the API documentation for detailed explanations of all the request and response bodies**. Our documentation site (along with valid client ID and secret) can be used to make requests against our API to get a sense for how the API behaves.

In addition to the API documentation, the SDK code itself is a great resource for understanding the structure of Sayari Graph API requests and responses. Objects in the code should have helpful names and comments detailing their significance.

What follows is a list of invocation examples for each of the SDK functions. Again, this is not an exhaustive demonstration if its capabilities, but rather a minimal example to help you get started.

## Top Level SDK functions
As mentioned above, this SDK provides some convenience functions beyond those available purely via the Sayari Graph API.

### Connection
The client connection is an authenticated API client which supplies the methods for the rest of the SDK's functionality. In addition to handling the authentication, this client object will also handle re-authentication in cases where the client is longer-lived then the duration of the initial authentication request.

To create a client connection, simply provide the client ID and secret
```python
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
```

### Screen CSV
One of the most common use cases for the Sayari Graph API is screening entities for potential risks. Because of this, the SDK includes tooling to simplify this process.

The 'screen_csv' function takes in the path for a CSV containing entities to screen, and returns those entities and their associated risks. For this to work properly, the CSV must only contain columns that map to entity attributes. Valid names for those columns are as follows: (column names are case and spacing insensitive)
- Name
- Identifier
- Country
- Address
- Date Of Birth
- Contact
- Entity Type

Once your CSV is property formatted, using the screen function is as simple as providing the path to the CSV.
```python
risky_entities, non_risky_entities, unresolved = client.screen_csv("examples/entities_to_screen.csv")
```

As you can see from this example, the first object returned is a list of entities that do have risks, the next is a list of entities without risks, and the third is a list of rows from the CSV that were unable to be resolved.

## Entity
### Get Entity
```python
entityDetails = client.entity.get_entity(myEntityID)
```

### Entity Summary
```python
entitySummary = client.entity.entity_summary(myEntityID)
```

## Record
### Get Record
Note: record ID's must be URL escaped
```python
record = client.record.get_record(urllib.parse.quote(myRecordID, safe=''))
```

## Resolution
### Resolution
```python
resolution = client.resolution.resolution(name="search term")
```

## Search
### Search Entity
```python
entitySearchResults = client.search.search_entity(q="search term")
```
### Search Record
```python
recordSearch = client.search.search_record(q="search term")
```

## Source
### List Sources
```python
sources = client.source.list_sources()
```
### Get Source
```python
firstSource = client.source.get_source(mySourceID)
```

## Traversal
### Traversal
```python
traversal = client.traversal.traversal(myEntityID)
```
### UBO
```python
ubo = client.traversal.ubo(myEntityID)
```
### Ownership
```python
ownership = client.traversal.ownership(myEntityID)
```
### Watchlist
```python
watchlist = client.traversal.watchlist(myEntityID)
```
### Shortest Path
```python
shortestPath = client.traversal.shortest_path(entities=[myFirstEntityID, mySecondEntityID])
```

## Trade
### Shipment Search
```python
shipments = client.trade.search_shipments(q="search term")
```
### Supplier Search
```python
suppliers = client.trade.search_suppliers(q="search term")
```
### Buyer Search
```python
buyers = client.trade.search_buyers(q="search term")
```
