While it is certainly possible to create applications which interact with a relational database directly, this can lead to duplicated and potentially insecure code. This led to the introduction of Object Relational Mappers (ORMs), which separate the database calls from your objects. This allows you as a developer to design objects to represent your data, and allow the ORM to manage the database operations for you.

Django has a built-in ORM, and is a core component of the framework. In this module we will explore the ORM, how to create model objects, and interact with the database through the ORM.

In this module you will learn:

- The purpose of an ORM
- How to setup and activate the Django SQLite database
- How to create and activate Django models
- Why the `__str__` method is an important addition in classes
- How to create and query data in your SQLite database

Prerequisites

- Basic understanding of Django
- Intermediate level knowledge of Python, including
  - [Package Management](https://docs.python.org/3/installing/index.html)
  - [Virtual Environments](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
  - [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- Understanding of HTML and CSS
- [Git](https://git-scm.com/)
