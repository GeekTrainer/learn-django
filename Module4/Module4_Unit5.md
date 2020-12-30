Template inheritance is key in keeping specific features or layouts the same throughout a website. By using this technique a developer can speed up the process of creating website pages by not using the same but slightly modified template numerous times.

## Extending templates

To demonstrate the process of template inheritance we will be creating a simple HTML page that will be used for the layout of our site. Before creating this page we first have to create another folder within our app **dog_shelters** called **templates**. After creating the **templates** folder create a file within the folder and name it **basic_layout.html**. In this file is where the code will be entered under the comment `<!-- TODO - Create the basic_layout.html template located in the templates folder -->`.

```html
<!-- TODO - Create the basic_layout.html template -->
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel='stylesheet' href="static/css/layout.css">
    <title>{% block title %}Adopt A Dog Today{% endblock %}</title>
</head>
<body>
    <!-- Sidebar -->
    <div class="w3-sidebar w3-light-grey w3-bar-block" style="width:25%">
    <h3 class="w3-bar-item">Menu</h3>
        <div id="sidebar">
            {% block sidebar %}
                <a href="home" class="w3-bar-item w3-button">Home</a>
            {% endblock %}
        </div>
    </div>
    <!-- Page Content -->
    <div style="margin-left:25%">
        <div class="w3-container w3-teal">
            <h1 style="text-align: center;">Adopt A Dog Today</h1>
        </div>   
        <div id="content">
            {% block content %}{% endblock %}
        </div>
    </div>     
</body>
</html>
```

When looking at the above HTML page take notice of the three sections that contain the word `block`.

```html
{% block title %}
{% block sidebar %}
{% block content %}
```
By tagging these sections with the `block` variable it tells the template engine that the child templates are able to override this information. 

Now that the layout page of our site is finished we can create the site home page. Within the **templates** folder create another file and name it **index.html** and save the code under the comment `<!-- TODO - Create the index.html template within the templates folder -->`.

```html
<!-- TODO - Create the index.html template -->
{% extends "basic_layout.html" %}

{% block sidebar %}
  {{ block.super}}
  <a href="shelter_spotlight" class="w3-bar-item w3-button">Shelter Spotlight</a>
{% endblock %}

{% block content %}
  <h2 style="text-align: center; margin-top: 100px;">Welcome to Adopt A Dog Today!</h2>
  <div style="width: 850px; margin: auto; text-align: center; margin-top: 50px;">
    <p>We created this site to collect and list all of the dog shelters that exist within the United States. 
      By using our site you are now able to look at every dog within a shelter to find the perfect match for you.</p>
  </div>
  <div style="width: 850px; margin: auto; text-align: center; margin-top: 50px;">
    <h3>There are a total of <span style="color: red;"> {{ num_shelters }} </span> shelter(s) that have <span  style="color: red;"> {{ num_dogs }} </span> dog(s) ready for adoption.</h3>
  </div>
{% endblock %}
```
As you can see at the top of the template we have extended the **basic_layout.html** page. By extending this page we can keep the same formatting and modify it where needed. In this instance we want to add a new nav link in the `sidebar` block, and the page content within the `content` block. Since we did not want to override the default title from the **basic_layout** page the `title` block was not added.

Next we need to add the second page to the website called **shelter_spotlight.html** which will also be stored in the **templates** folder. After creating the file input the below code under the comment `<!-- TODO - Create the shelter_spotlight.html template -->`.

```html
<!-- TODO - Create the shelter_spotlight.html template -->
{% extends "index.html" %}

{% block title %}Shelter Spotlight{% endblock %}

{% block content %}

    {% for entry in get_dogs %}
        <div style="width: 850px; margin: auto; text-align: center; margin-top: 50px;">
            {% for shelter in get_shelters %}
                {% if shelter.id == entry.shelter_id %}
                    Location: {{ shelter.shelter_name }} in {{ shelter.shelter_location }}
                {% endif %}
            {% endfor %}
            <h2>{{ entry.dog_name }}</h2>
            <img src="{{ entry.dog_image.url }}" alt="" width="500" height="600">
            <h4>{{ entry.dog_breed }}</h4>
            <h4>{{ entry.dog_description }}</h4>
        </div>
    {% endfor %}
    
{% endblock %}
```
From the first line of code you can see this template will now extend the main page **index.html**. For this new page it will override the `title` and also the `content` block with the spotlighted dogs information and image. Also, since we did not need to change or add anything to the site navigation the `sidebar` block was not included.

When working with child templates and extending content from the parent be aware of the following:

- When using **extends** it needs to be the first template tag in order to work correctly.
- Child templates don't have to use all of the parent blocks.
- If you start duplicating content across multiple templates then consider adding it to the parent as a block.

## Using the **block.super** variable

While it is extremely helpful to override data from the parent template, what happens if we would like to keep some of the content from the parent page? In order to do that just add a `{{ block.super}}` variable to our child template.

```html
{% block sidebar %}
  {{ block.super}}
  <a href="shelter_spotlight" class="w3-bar-item w3-button">Shelter Spotlight</a>
{% endblock %}
```
The above example was taken from the **index.html** file, and as you can see it contains a `{{ block.super }}` in the `{% block sidebar %}` section of the code. Since the website home link was supplied in the **basic_layout.html** file we want to carry that over to this new page. By adding this variable we are not only able to carry over the **home** link but also add the new **shelter_spotlight** link.