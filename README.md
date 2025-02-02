# Take Home Engineering Challenge

Commercial Software Engineering is a very practical team at Microsoft and this extends to the way that we work with you to find out if this team is a great fit for you. We want you to come away with a great understanding of the work that we actually do day to day and what it is like to work with us.

So instead of coding at a whiteboard with someone watching over your shoulder under high pressure, which is not a thing we often do, we instead discuss code that you have written previously when we meet.

## My Solution

My solution parses the data from the given csv file, and creates a dictionary from it. Each line number is the key, and the values are the flatted truck data allocated by property (csv column).

There are two more dictionaries included. One represents all of the unique locaionid's acting as keys and the list of truck id's as the value. The other is the same, but for block id's. This ensures that the trucks are essentially indexed based on location and block. This makes getting and adding trucks an easy O(1) computation, causing read and writes to be fast on the backend. All of this functionality is included in CSVReader.py and FoodTrucks.py

The REST API in app.py is as simple as dedicating three routes that a client can hit.

1. [GET /location/[locationid]] Getting all trucks by locationid
2. [GET block/[block]] Getting all trucks by block
3. [POST] Adding a new truck from user request data (which much have locationid, block, and Applicant properties)

This API allows us to use the backend functions already created in FoodTrucks.py to get and add trucks.

Sample test cases are also included to test the reading from the csv file as well as getting and adding new trucks from/to the in memory dictionaries. The test cases use sample data, which is a slightly modified version of the first 10 trucks in the main csv file. The data was modified in a way that not all locationid's and blocks are unique. This was done to test getting multiple trucks from one locationid or block.

## Guidelines

- This is meant to be an assignment that you spend approximately three hours of dedicated, focused work. Do not feel like you need to overengineer the solution with dozens of hours to impress us. Be biased toward quality over quantity, simplicity over complexity.

- Think of this like an open source project. Create a repo on Github, use git for source control, and use README.md to document what you built for the newcomer to your project.

- Our team builds, alongside our customers and partners, systems engineered to run in production. Given this, please organize, design, test, deploy, and document your solution as if you were going to put into production. We completely understand this might mean you can't do as much in the time budget. Be biased for production-ready over features.

- Think out loud in your submission's documentation. Document tradeoffs, the rationale behind your technical choices, or things you would do or do differently if you were able to spend more time on the project or do it again.

- Our team meets our customers where they are in terms of software engineering platforms, frameworks, tools, and languages. This means you have wide latitude to make choices that express the best solution to the problem given your knowledge and favorite tools. Make sure to document how to get started with your solution in terms of setup.

## The Problem

Our San Francisco team loves to eat. They are also a team that loves variety, so they also like to discover new places to eat.

In fact, we have a particular affection for food trucks. One of the great things about Food Trucks in San Francisco is that the city releases a list of them as open data.

Your assignment is to make it possible for us to find a food truck no matter where our work takes us in the city.

Feel free to tackle this problem in a way that demonstrates your expertise of an area -- or takes you out of your comfort zone.

## Technical Requirements

### Interface

You can write a simple REST service that returns a set of food trucks (our team is fluent in JSON).

### Expected Data Size

Design the solution assuming that the dataset includes data from many cities with millions of records.

### Data Schema

San Francisco's food truck open dataset is [located here](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat/data) and there is an endpoint with a [CSV dump of the latest data here](https://data.sfgov.org/api/views/rqzj-sfat/rows.csv). We've included a [copy of this data](./Mobile_Food_Facility_Permit.csv) in this repo as well.

### Programming Language

You are welcome to use any language frameworks or libraries you like.

### Data Storage

You don’t need to use a database to store food truck data. Instead, your REST Service should use language native data structures (ie _Set, List, Map, Stack, Heap, etc_) to implement the in-memory data store. Please avoid using query and/or ORM frameworks(_ie Linq, Hibernate_).

### Service Requirements

Your REST service should make it possible to:

- Add a new food truck.
- Retrieve a food truck based on the `locationid` field.
- Get all food trucks for a given `block`.

### Testing

You are welcome to use your unit testing framework of choice to validate the in-memory data store and service functionality.

Good luck! Please send a link to your solution on Github back to us at least 12 hours before your interview so we can review it before we speak.
