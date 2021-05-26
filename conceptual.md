### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.
PostgreSQL is used as the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications.

- What is the difference between SQL and PostgreSQL?
SQL server is a database management system which is mainly used for e-commerce and providing different data warehousing solutions. PostgreSQL is an advanced version of SQL which provides support to different functions of SQL like foreign keys, subqueries, triggers, and different user-defined types and functions.

- In `psql`, how do you connect to a database?
psql database_name

- What is the difference between `HAVING` and `WHERE`?
WHERE Clause is used to filter the records from the table based on the specified condition. HAVING Clause is used to filter record from the groups based on the specified condition.

- What is the difference between an `INNER` and `OUTER` join?
Joins in SQL are used to combine the contents of different tables. ... The major difference between inner and outer joins is that inner joins result in the intersection of two tables, whereas outer joins result in the union of two tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
The key difference between a left outer join, and a right outer join is that in a left outer join it's the table in the FROM clause whose all rows are returned. Whereas, in a right outer join we are returning all rows from the table specified in the join clause.

- What is an ORM? What do they do?
(ORM) is a technique that lets you query and manipulate data from a database using an object-oriented paradigm. When talking about ORM, most people are referring to a library that implements the Object-Relational Mapping technique, hence the phrase "an ORM".

An ORM library is a completely ordinary library written in your language of choice that encapsulates the code needed to manipulate the data, so you don't use SQL anymore; you interact directly with an object in the same language you're using.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

- What is CSRF? What is the purpose of the CSRF token?
Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated. CSRF attacks exploit the trust a Web application has in an authenticated user.


- What is the purpose of `form.hidden_tag()`?
The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration.
