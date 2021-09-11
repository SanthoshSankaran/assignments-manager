# Assignments Manager

This API based assignments manager service contains three end points and is implemented using Flask micro web framework and psycopg2 for database connections.

1. GET Assignment object by ID
2. POST Create a new assignment
3. GET Search all assignments with a tag

There are certain characteristics to be addressed as part of this particular implementation.

1. How efficient is your code? What are some ways that you could improve performance?
  - Performance can be improved by indexing the data and normalizing the table data based on tags and region / country etc
2. Suppose we expect this API to be hit 1000s of times a second. How can we handle the load?
  - Load performance can be improved by using load balancers and database sharding
3. What if the 3rd party provider is not available? How resilient is our API?
  - The API service currently works on top of Flask and psycopg2 libraries, and uses raw SQL queries, hence it is relatively resilient to changing 3rd party providers.
4. What if we have a database of users and we wanted to make our API smarter by defaulting comparisons to always include the population of the current user's country. How could we accomplish this?
  - Load balancing and region specific sharding will help with this scenario
5. What if we wanted to keep a tally of the most frequently requested countries and have this be available to consumers. How could we accomplish this?
  - We can maintain a separate LRU cache (capacity of N) of countries and query the cache for the country names
