Templates are text files that can be used to generate text-based formats such as HTML or XML. Each template will contain some static data that is shared across the site, but can also contain placeholders for dynamic data. They contain variables and tags that control the behavior and what will appear as the final page. To begin to understand templates let's first look at variables.

## Variables

Variables are placed within a template so the engine is able to evaluate and place the correct data per request. In order to position a variable within a template it must be between two curly brackets. It can be any combination of alphanumeric characters and can include an underscore as long as it is not placed at the beginning.

```html
{{ dog.breed }}
```

In this example of a variable the template engine would look for the `dog` object and replace it with the `breed` as below.

```text
Great Dane
```

## Filters

Filters are a great way to control how the data appears when requested in a template. Since these filters are already created they provide an easy way to format data without having to write any special code. 

For example, let's say we have to print out the names of the dog breeds and we want to make sure the first letter of every name is capitalized.

```html
{{ dog.breed | capfirst }}
```

As you can see the variable is to the left of the pipe symbol `|` and the filter is on the right. This is just one of many filters that can be used to manipulate the data when using Django template filters.

## Tags

Tags are a little more advanced than variables and can be used to perform loops, create text, or even load information to be used by the variables.

For instance if we wanted to print out a list of dog breeds that were in each shelter the below code would be used.

```html
<ul>
    {% for dogs in shelter_list %}
        <li>{{ dogs.breed }}</li>
    {% endfor %}
<ul>
```

In this code we are using a `for` statement tag to loop through the `shelter_list` and print out all of the dog breeds, and then we close the tag by using `endfor`.

We can even go a little further and use `if`, `elif`, and `else` when needed. For example say we wanted to display how many dogs are waiting for adoption or have been adopted for the month of Dec. We first begin by providing a little more detail about this section of code by using the commenting `{# #}` tags, and then continue with the statements.

```html
{# Displays number of dogs waiting for adoption or adopted for December #}
{% if shelter_list %}
    Number of dogs that need adopting for Dec: {{ shelter_list | length }}
{% elif adopted_list %}
    Number of dogs that have been adopted in Dec: {{ adopted_list | length }}
{% else %}
    There are no dogs in the shelter for the month of Dec.
{% endif %}
```

By running this code if a `shelter_list` exists it returns the number of dogs on the list. If not, it skips over to the `adopted_list` to see if any dogs have been adopted. If these two lists do not exist then it skips to the else statement to execute. As you can see these statements work as expected but need to be between a curly bracket and percentage sign `{% if shelter_list %}` for the template engine to understand and process.
