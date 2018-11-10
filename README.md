# DJANGO PROJECT
## TODO Application

**IMPORTANT** - This project is goind to use django version 1.11  
```bash
sudo pip3 install django==1.11
```
---

1. Start by installing django
    ```bash
    $ sudo pip3 install django==1.11
    ```

2. Next create a django project.
    ```bash
    $ django-admin startproject django_todo .
    ```
    The reason for the dot at the end of the command line is for django to create 
the project in this directory.

3. Run the django server.
    ```bash
    $ python3 manage.py runserver $IP:$C9_PORT
    ```
    This will let us have access to the django project at 
    https://django-todo01-anthonybstudent.c9users.io

    $IP and $C9_PORT are environmental variables already set on cloud9.
    
4. Add 'django-todo01-anthonybstudent.c9users.io' to ALLOWED_HOSTS in `settings.py`.


Now try to access the project in a browser.

### Simplifying the run command
1. In cloud9 click on the cog wheel next to the root directory and check the 
     *Show Home in Favorites* and *Show Hidden Files*.

2. Find the file called `.bash_aliases` and open it.

3. Create the following alias:
    ```
    alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"
    ```
The ~/workspace/ will ensure that no matter what directory we are in we can always
run the project. For the alias to take effect, exit the bash terminal and 
open a new one. Reason: bash aliases files are loaded when the terminal is 
opened, so we need to re-open the terminal.

### Create an App for our project

1. We are going to create an app called todo
    ```bash
    $ django-admin startapp todo
    ```
    This creates a new folder called `todo` that will hold all the files for this app.

The **`views.py`** is the file which handels a **request** and **returns** a 
response to the browser. **All django view functions have to take a request as a 
parameter**. Example:
```python3
from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World!")
```

Now we need a way to connect this to the browser. This is done by using urlpatterns.

2. Open `django_todo/urls.py` and add a url pattern. We need to import the view 
that we have created.
```python3
from django.conf.urls import url
from django.contrib import admin
from todo.views import say_hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', say_hello),
]
```
This means that when we go to the root url, the say_hello view will be loaded.

---

### Using templates
1. create a `templates` directory.
2. create a `todo_list.html` file inside the templates directory.
3. put some boilerplate html and an h1 header.
4. Create a function in views.py that will return this template. This function 
will need to use the render function.
```python3
def get_todo_list(request):
    return render(request, 'todo_list.html')
```
5. Create a url pattern in `django/urls.py` and import the `get_todo_list`.
```python3
url(r'^todo_list/$', get_todo_list),
```

Up to this point we will get a **TemplateDoesNotExist** error. What we need to
do in order for django to read the templates directory is to register the 
app in the `settings.py`. Add todo app to the **INSTALLED_APPS** list.

*Might need to restart the server*.

---
### Explore sqlite3

```bash
$ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
django_migrations
sqlite> select * from django_migrations;
sqlite> .quit
```


### Do a migration

```bash
$ python3 manage.py migrate
$ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session  
sqlite> select * from django_migrations;
1|contenttypes|0001_initial|2018-11-07 23:23:10.824666
2|auth|0001_initial|2018-11-07 23:23:10.875944
3|admin|0001_initial|2018-11-07 23:23:10.920879
4|admin|0002_logentry_remove_auto_add|2018-11-07 23:23:10.964876
5|contenttypes|0002_remove_content_type_name|2018-11-07 23:23:11.021572
6|auth|0002_alter_permission_name_max_length|2018-11-07 23:23:11.059361
7|auth|0003_alter_user_email_max_length|2018-11-07 23:23:11.108607
8|auth|0004_alter_user_username_opts|2018-11-07 23:23:11.154275
9|auth|0005_alter_user_last_login_null|2018-11-07 23:23:11.232213
10|auth|0006_require_contenttypes_0002|2018-11-07 23:23:11.249031
11|auth|0007_alter_validators_add_error_messages|2018-11-07 23:23:11.293092
12|auth|0008_alter_user_username_max_length|2018-11-07 23:23:11.336465
13|sessions|0001_initial|2018-11-07 23:23:11.371182
sqlite> .headers on
sqlite> .mode column
sqlite> select * from django_migrations;
id          app           name          applied                   
----------  ------------  ------------  --------------------------
1           contenttypes  0001_initial  2018-11-07 23:23:10.824666
2           auth          0001_initial  2018-11-07 23:23:10.875944
3           admin         0001_initial  2018-11-07 23:23:10.920879
4           admin         0002_logentr  2018-11-07 23:23:10.964876
5           contenttypes  0002_remove_  2018-11-07 23:23:11.021572
6           auth          0002_alter_p  2018-11-07 23:23:11.059361
7           auth          0003_alter_u  2018-11-07 23:23:11.108607
8           auth          0004_alter_u  2018-11-07 23:23:11.154275
9           auth          0005_alter_u  2018-11-07 23:23:11.232213
10          auth          0006_require  2018-11-07 23:23:11.249031
11          auth          0007_alter_v  2018-11-07 23:23:11.293092
12          auth          0008_alter_u  2018-11-07 23:23:11.336465
13          sessions      0001_initial  2018-11-07 23:23:11.371182
sqlite> .quit
```
---

### Create superuser

```bash
$ python3 manage.py createsuperuser
Username (leave blank to use 'ubuntu'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

password: ewqr5tMk 


```bash
$ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
sqlite> select * from auth_user;
1|pbkdf2_sha256$36000$urDjCTNXXi1r$Sxwj8/QhX7d24FtjJNrNRginx/Wq0IjZUJQIwqUD2ao=|2018-11-07 23:30:17.771336|1||||1|1|2018-11-07 23:29:13.101815|admin
sqlite> .headers on
sqlite> .mode column
sqlite> select * from auth_user;
id          password                                                                       last_login                  is_superuser  first_name  last_name   email       is_staff    is_active   date_joined                 username  
----------  -----------------------------------------------------------------------------  --------------------------  ------------  ----------  ----------  ----------  ----------  ----------  --------------------------  ----------
1           pbkdf2_sha256$36000$urDjCTNXXi1r$Sxwj8/QhX7d24FtjJNrNRginx/Wq0IjZUJQIwqUD2ao=  2018-11-07 23:30:17.771336  1                                                 1           1           2018-11-07 23:29:13.101815  admin 
.quit
```

We can save some configurations for sqlite3 in a hidden file stored in the home directory.
The file will be called `.sqliterc`.
In this file we can write the configuration properties that we want to always be on. Ex:
```
.headers on
.mode column
```

---

### Create our own model and migration

use the `todo/models.py`.

```python3
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
```

Then create a migration.
```bash
$ python3 manage.py makemigrations
Migrations for 'todo':
  todo/migrations/0001_initial.py
    - Create model Item
```
This generates a file that will contain configuration code for django to know
what to do when we ask it to migrate. It will create a table in our database 
based on the model we created earlier.

```bash
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo
Running migrations:
  Applying todo.0001_initial... OK
```

```bash
$ sqlite3 db.sqlite3
-- Loading resources from /home/ubuntu/.sqliterc

SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            todo_item                 
auth_user_user_permissions
sqlite> .quit
```
We can see the new **todo_item** table which was created.

We can now add this to the admin panel. Open `todo/admin.py`.

```python3
from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.register(Item)
```
Run the server if it is not already running.

At the moment, if we create items, they will be listed as *Item object*.
We can improve on this.
open the `models.py` and define how each object will be represented.

```python3
def __str__(self):
    return self.name
```
This will return the name of the object.

---

### Display data in web page

open views.py
```python3
from django.shortcuts import render, HttpResponse
from .models import Item

...

def get_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {"items": results})
```

In the todo_list.html template

```jinja
<table>
    {% for item in items %}
        <tr>
            {% if item.done %}
                <td><strike>{{ item.name }}</strike></td>
            {% else %}
                <td>{{ item.name }}</td>
            {% endif %}
            <td>{{ item.done }}</td>
        </tr>
    {% endfor %}
</table>
```

---

Coding for empty list. There are two ways:

```jinja
{% if items %}
    <table>
        {% for item in items %}
            <tr>
                {% if item.done %}
                    <td><strike>{{ item.name }}</strike></td>
                {% else %}
                    <td>{{ item.name }}</td>
                {% endif %}
                <td>{{ item.done }}</td>
            </tr>
        {% endfor %}
    </table>
{% else %}
    Nothing to display
{% endif %}

<br>
<hr>
<br>

<table>
    {% for item in items %}
        <tr>
            {% if item.done %}
                <td><strike>{{ item.name }}</strike></td>
            {% else %}
                <td>{{ item.name }}</td>
            {% endif %}
            <td>{{ item.done }}</td>
        </tr>
    {% empty %}
        You have nothing to do.
    {% endfor %}
</table>
```

One uses an if statement to check if there is any data, the othe uses a jinja
empty tag. The empty tag works if there are no items in the for loop.

### Creating new items

We can already create new items from the admin site. We want to be able to create
them from our web page.

1. In todo_list.html create a link below our table. Point this link to an `Add`
url.
```html
<a href="/add">Add an Item</a>
```
I had to do the / at the start of the href otherwise it insisted to add this url
to the current one ending up with `/todo_list/add/`

2. Create a new template called `item_form.html`. Just put some boilerplate code
for now.

3. Create a view that will return this template.

4. Connect this up with a url.
    * We need to import the new view
        ```python3
        from todo.views import . . ., create_an_item
        ```
    * Then add a new url pattern
        ```python3
        url(r'^add/$', create_an_item),
        ```
    NB: if I had to call this url manually by typing it in the browser's address
    bar, I will need to have a pattern like `r'^add/$'`

5. Create a form in item_form.html
    ```html
    <form method="POST">
        <label for="id_name">Name: </label><br>
        <input type="text" id="id_name" name="name"/><br>
        <br>
        <label for="id_done">Done: </label><br>
        <input type="checkbox" id="id_done" name="done"/><br>
        <br>
        <button type="submit">Save</button>
    </form>
    ```
If we try to submit now, we get a **403** (Forbidden) error saying **CSRF 
verification failed**. To avoid this we need to add a **csrf token** to our form.
6. Add csrf token to form. This prevents cross-site scripting forgery. 
`{% csrf_token %}`

NB: Cross-site scripting is a kind of vulnerability where people can inject
javascript code into input elements and execute it.

7. Create functionality for the form. Add code to the `create_an_item` view 
to handel a POST request. 
    ```python3
    if request.method=='POST':
        return redirect(get_todo_list)
    ```
    We also need to import `redirect` from django.shortcuts.

    Now we need to add the item to the database.
    
    ```python3
    def create_an_item(request):
    if request.method=='POST':
        new_item = Item()
        new_item.name = request.POST.get('name')
        new_item.done = 'done' in request.POST
        new_item.save()
        return redirect(get_todo_list)
    return render(request, 'item_form.html')
    ```
    Notice the code for done. If  done is present in the request.POST, then it 
    will be true, otherwise it will be false.
    
### Creating from with Django itself

Django has a functionality to auto-generate a form from a model. It will automatically check
for blank fields. 

1. Create `forms.py` inside the todo app directory.
    ```python3
    from django import forms
    from .models import Item
    
    class ItemForm(forms.ModelForm):
        class Meta:
            model = Item
            fields = ('name', 'done')
    ```

2. Replace all the labels and inputs (keep the submit button) with `{{ form }}`.

3. We then need to pass that form from the view to the template.

4. In `views.py` import the form

5. Change the code inside the `request.method` to
    ```python3
    if request.method=='POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    ```

6. If it is not a POST request we want to return an empty form:
    ```html
    else:
        form = ItemForm()
        
    return render(request, 'item_form.html', {'form': form})
    ```
7. To format the form, in `item_form.html` we can say `{{ form.as_p }}` which
    will render it as paragraphs.

    Alternatives include lists and tables:
    ```html
    <ul>{{ form.as_ul }}</ul>
    <table>{{ form.as_table }}</table>
    ```


### Edit Item

1. In `todo_list.html` add another column to the list table. This will hold an edit
link for each individual item.

    We can change that link to a form.
    ```
    <td>
        <form>
            <input type="submit" value="Edit"/>
        </form>
    </td>
    ```
    
    Add a method of GET to this form and action of edit which means that it refers
    to a url called edit.
    ```
    <form method="GET" action="/edit">
        <input type="submit" value="Edit"/>
    </form>
    ```
    Now we need to make this edit to point to a specific item by passing its id.

2. Create a new `edit` function for the view.
    We need to import `get_object_or_404` from `django.shortcuts`.
    ```python3
    def edit_an_item(request, id):
        item = get_object_or_404(Item, pk=id)
        form = ItemForm(instance=item)
        return render(request, 'item_form.html', {'form': form})
    ```

3. Create a url for this view.  
    make sure to import the view  
    from todo.views import . . . , edit_an_item  
    Then the pattern will be like this:  
    ```url(r'^edit/(?P<id>\d+)$', edit_an_item),```  
    \d is a single digit, + means multiple, \d+ means multiple digits.  
    the ?P<id> identifies the digits specified by \d+ to be the argument
    for the id parameter that will be passed to the view function.

4. Add logic to the view to save the changes.  
    ```python3
    def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)
    
    if request.method=='POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})
    ```
### Adding Done/Not Done toggle button

1. Add another column in the table to hold a toggle button:  
    ```
    <td>
        <form method="POST" action="/toggle/{{ item.id }}">
            {% csrf_token %}
            <input type="submit" value="Toggle"/>
        </form>
    </td>
    ```
2. Create the toggle view that will toggle the done state.
    ```python3
    def toggle_status(request, id):
        item = get_object_or_404(Item, pk=id)
        item.done = not item.done
        item.save()
        return redirect(get_todo_list)
    ```
3. Create url:
    import toggle_status view  
    `url(r'toggle/(?P<id>\d+)$', toggle_status)`

---
## TESTING

When an app is created a test.py file is automatically created. This imports `TestCase`
from `django.test`.
```python3
from django.test import TestCase
```

1. Create a Test class and write a simple test to check that everything is working
as expected. Do this in a Red-Green-Refactor way.  
**NB: test names should begin with `test_` otherwise django will not find them and 
they will not be executed**.
```python3
class TestDjango(TestCase):
    
    def test_is_this_thing_on(self):
        self.assertEqual(1, 0)
```

2. Run this from terminal and should fail.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_is_this_thing_on (todo.tests.TestDjango)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/workspace/todo/tests.py", line 7, in test_is_this_thing_on
    self.assertEqual(1, 0)
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

3. Now change the assertion for `1 Equals 1`.

```bash
```python3
self.assertEqual(1, 1)
```

4. Run this again and the test passes.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

### Creating tests for different parts

Creating a test for our form.  
1. Create these files: 
    * `test_forms.py`
    * `test_views.py`
    * `test_models.py`

2. In test_forms.py, import `TestCase` from django.test. We will also need to import
our form which we called `ItemForm`. Create a test class.
```python3
from django.test import TestCase
from .forms import ItemForm

class TestToDoItemForm(TestCase):
```

3. Create a test to check that we can create an item with name only. Create a 
new form inside this test and instantiate it with a dictionary. Then assertEqual
that the  form is valid.
```python3
class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Test' })
        self.assertTrue(form.is_valid())
```

4. Run the test.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
Destroying test database for alias 'default'...
```
Remember we had the other test in tests.py. That is way it says it ran 2 tests.

NB: If we had to use `self.assertFalse(form.is_valid())`, this test would fail
as the form is valid.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F.
======================================================================
FAIL: test_can_create_an_item_with_just_a_name (todo.test_forms.TestToDoItemForm)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/workspace/todo/test_forms.py", line 8, in test_can_create_an_item_with_just_a_name
    self.assertFalse(form.is_valid())
AssertionError: True is not false

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

5. Test that item will not be created if we do not provide a name. In other words,
name is required. Check that we get the correct message in this case. Create
A new test and pass in a dictionary with nothing in the name's value.  
```python3
def test_correct_message_for_missing_name(self):
    form = ItemForm({'name': ''})
    self.assertTrue(form.is_valid())
```

6. Asserting that form is valid will return an error as expected.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F.
======================================================================
FAIL: test_correct_message_for_missing_name (todo.test_forms.TestToDoItemForm)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/workspace/todo/test_forms.py", line 13, in test_correct_message_for_missing_name
    self.assertTrue(form.is_valid())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

7. Reafactor to say that form is not valid by expecting a False and this time the
test will pass.
```python3
self.assertFalse(form.is_valid())
```
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
Destroying test database for alias 'default'...
```
8. We also want to assert that there is an error in the name and that we get
a message back saying "This field is required." It will look for an exact match 
so watch out for spelling, case and full stops. This is a standard piece of text
when form validation fails.
```python3
self.assertEqual(form.errors['name'], [u'This field is required.'])
```
notice the error caused by missing full stop.
```.bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F.
======================================================================
FAIL: test_correct_message_for_missing_name (todo.test_forms.TestToDoItemForm)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/workspace/todo/test_forms.py", line 15, in test_correct_message_for_missing_name
    self.assertEqual(form.errors['name'], [u'This field is required'])
AssertionError: ['This field is required.'] != ['This field is required']

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
9. Run the test with correct assert message and it will pass.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
Destroying test database for alias 'default'...
```

10. Test we can create a new item and set done to True immediately.
```python3
def test_can_create_an_item_with_name_and_done_set_to_true(self):
    form = ItemForm({'name': 'Testing Done', 'done': True})
    self.assertTrue(form.is_valid())
```

```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
Destroying test database for alias 'default'...
```

---
### Test views
* We are going to the correct location.
* We have the correct url.
* The correct template is used.

1. The root should return a 200 status code
    ```python3
    from django.test import TestCase
    
    class TestViews(TestCase):
        def test_get_home_page(self):
            page = self.client.get("/")
            self.assertEqual(page.status_code, 400)
    ```
2. Test and Failed as expected.
    ```bash
    $ python3 manage.py test
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ...F.
    ======================================================================
    FAIL: test_get_home_page (todo.test_views.TestViews)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/ubuntu/workspace/todo/test_views.py", line 7, in test_get_home_page
        self.assertEqual(page.status_code, 400)
    AssertionError: 200 != 400
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.011s
    
    FAILED (failures=1)
    Destroying test database for alias 'default'...
    ```
3. Refactor
    ```python3
    self.assertEqual(page.status_code, 200)
    ```
4. And test passes
    ```bash
    $ python3 manage.py test
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.010s
    
    OK
    Destroying test database for alias 'default'...
    ```

5. Refactored root view to display the todo_list.html template.
```python3
self.assertTemplateUsed(page, "todo_list.html")
```

6. Test - pass
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.014s

OK
Destroying test database for alias 'default'...
```

NB: the `todo_list` url is redirecting and thus return a status code of 301. In
this case it does not use a template to generate the status code.  
It was because in urlpatterns it is `todo_list/`. It needs to be exact. Now it works.



7. Test the template used. ~~Now I am not using a template on the root but I
am using a template on `todo_list`.~~  
I will redo the above tests and the template test on `todo_list`.
```python3
def test_get_todo_list(self):
    page = self.client.get("/todo_list/")
    self.assertEqual(page.status_code, 200)
    self.assertTemplateUsed(page, "todo_list.html")
```
Test pass.
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.017s

OK
Destroying test database for alias 'default'...
```

8. Add test for `/add/`, both status_code and template used:
```python3
def test_get_add_item_page(self):
    page = self.client.get("/add/")
    self.assertEqual(page.status_code, 200)
    self.assertTemplateUsed(page, "item_form.html")
```
```bash$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

NB: I can make these test a bit more verbose and easier to read by adding
print statements:
```python3
def test_get_add_item_page(self):
    print("\n==========")
    print("test_get_add_item_page")
    page = self.client.get("/add/")
    self.assertEqual(page.status_code, 200)
    print("test_get_add_item_page -- Status code PASS")
    self.assertTemplateUsed(page, "item_form.html")
    print("test_get_add_item_page -- Template PASS")
```

The output now will be like:
```bash
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
==========
test_get_add_item_page
test_get_add_item_page -- Status code PASS
test_get_add_item_page -- Template PASS
.
==========
test_get_home_page
test_get_home_page -- Status code PASS
test_get_home_page -- Template PASS
.
==========
test_get_todo_list
test_get_todo_list -- Status code PASS
test_get_todo_list -- Template PASS
..
----------------------------------------------------------------------
Ran 7 tests in 0.023s

OK
Destroying test database for alias 'default'...
```
test for edit  


### Testing models



## COVERAGE

When we run our tests we do not know how much of our code is being tested.  

Install coverage
```bash
$ sudo pip3 install coverage
```

Then we run our tests we run it through `coverage run` instead of python3:
```bash
$ coverage run manage.py test
```
We can also use coverage to generate a report
```bash
$ coverage report
```
By default this will test all the code including that which is generated by
Django. We only want it to test the files in the todo directory

```bash
$ coverage run --source=todo manage.py test
$ coverage report
Name                              Stmts   Miss  Cover
-----------------------------------------------------
todo/__init__.py                      0      0   100%
todo/admin.py                         3      0   100%
todo/apps.py                          3      3     0%
todo/forms.py                         6      0   100%
todo/migrations/0001_initial.py       6      0   100%
todo/migrations/__init__.py           0      0   100%
todo/models.py                        6      1    83%
todo/test_forms.py                   13      0   100%
todo/test_models.py                  21      0   100%
todo/test_views.py                   51      0   100%
todo/tests.py                         4      0   100%
todo/views.py                        31     12    61%
-----------------------------------------------------
TOTAL                               144     16    89%
```

We see from the results that most files are 100% tested except for views.py 
(61%), models.py (83%) and apps.py(0%).

We can better better reports by generating an html report

```bash
$ coverage html
```
This will generate a new folder called `htmlcov`. Inside this there is an
`index.html` which is the entry file. We can run this file and open it in the 
browser. (*Make sure Django server is not running*.)  
This web page has links for each file which when clicked will show us the code 
and which is covered and which is not.  

Let us improve coverage. 

models.py -- we are not testing the string representation. Add a test for this.
We defined this to be equal to the name of the item.

```python3
def test_item_as_a_string(self):
    print("\n==========")
    print("test_item_as_a_string")
    item = Item(name='Create a Test')
    item.save()
    self.assertEqual("Create a Test", str(item))
    print("test_item_as_a_string -- String representation PASS")
```
Now re run coverage and see if we have 100% for models.py

```bash
$ coverage run --source=todo manage.py test
$ coverage report
Name                              Stmts   Miss  Cover
-----------------------------------------------------
todo/__init__.py                      0      0   100%
todo/admin.py                         3      0   100%
todo/apps.py                          3      3     0%
todo/forms.py                         6      0   100%
todo/migrations/0001_initial.py       6      0   100%
todo/migrations/__init__.py           0      0   100%
todo/models.py                        6      0   100%
todo/test_forms.py                   13      0   100%
todo/test_models.py                  28      0   100%
todo/test_views.py                   51      0   100%
todo/tests.py                         4      0   100%
todo/views.py                        31     12    61%
-----------------------------------------------------
TOTAL                               151     15    90%
$ coverage html
```

Now we have 100% coverage of models.py

We can now test the POST submissions from the forms in views.py

---
Code used
```
python3 manage.py test
coverage run --source=todo manage.py test
coverage report
coverage html
```
---

### Go for 100% coverage

It is not necessary to have 100% if that means testing files generated by
django. For this example we will test apps.py which is generated by django and 
we did not change it.

Create test_apps.py


Now we have 100% coverage

```bash
$ coverage report
Name                              Stmts   Miss  Cover
-----------------------------------------------------
todo/__init__.py                      0      0   100%
todo/admin.py                         3      0   100%
todo/apps.py                          3      0   100%
todo/forms.py                         6      0   100%
todo/migrations/0001_initial.py       6      0   100%
todo/migrations/__init__.py           0      0   100%
todo/models.py                        6      0   100%
todo/test_apps.py                     9      0   100%
todo/test_forms.py                   23      0   100%
todo/test_models.py                  28      0   100%
todo/test_views.py                   77      0   100%
todo/tests.py                         4      0   100%
todo/views.py                        31      0   100%
-----------------------------------------------------
TOTAL                               196      0   100%
```

## Exploring Heroku and Deployment

Heroku toolbelt - default tool provided by Heroku.

```bash
$ heroku
Usage: heroku COMMAND

Help topics, type heroku help TOPIC for more details:

 access          manage user access to apps
 addons          tools and services for developing, extending, and operating your app
 apps            manage apps
 auth            heroku authentication
 authorizations  OAuth authorizations
 buildpacks      manage the buildpacks for an app
 certs           a topic for the ssl plugin
 ci              run an application test suite on Heroku
 clients         OAuth clients on the platform
 config          manage app config vars
 container       Use containers to build and deploy Heroku apps
 domains         manage the domains for an app
 drains          list all log drains
 features        manage optional features
 git             manage local git repository for app
 keys            manage ssh keys
 labs            experimental features
 local           run heroku app locally
 logs            display recent log output
 maintenance     manage maintenance mode for an app
 members         manage organization members
 notifications   display notifications
 orgs            manage organizations
 pg              manage postgresql databases
 pipelines       manage collections of apps in pipelines
 plugins         manage plugins
 ps              manage dynos (dynos, workers)
 redis           manage heroku redis instances
 regions         list available regions
 releases        manage app releases
 run             run a one-off process inside a Heroku dyno
 sessions        OAuth sessions
 spaces          manage heroku private spaces
 status          status of the Heroku platform
 teams           manage teams
 update          update CLI
 webhooks        setup HTTP notifications of app activity
 ```
 
 ---
 
 ### Add some packages
 
 
**Install:*  
* Gunicorn -- will be used to run the application on the server
* psycopg2 -- allows us to connect to PostgreSQL database

Freeze packages into requirements.txt

$ sudo pip3 install gunicorn
$ sudo pip3 install psycopg2
$ pip3 freeze --local > requirements.txt


Before creating the app make sure that git is initialised. In this way
when the app is created, heroku will generate the necessary remotes. Otherwise
these have to be created manually.

```bash
git init
git add .
git commit -m"Initial commit."
```

We might want to .gitignore some files.



Create a new heroku app.

```bash
$ heroku login
$ heroku apps
$ heroku create ab-django-todo1 --region eu
Creating ⬢ ab-django-todo1... done, region is eu
https://ab-django-todo1.herokuapp.com/ | https://git.heroku.com/ab-django-todo1.git
```

NB: If git was not initialised before the app was created, then we need to 
initialise it now:
```bash 
$ git remote -v
fatal: Not a git repository (or any of the parent directories): .git
$ git init
Initialized empty Git repository in /home/ubuntu/workspace/.git/
(master) $ git remote -v
(master) $ git add .
(master) $ git status
......
(master) $ git commit -m"Initial commit."
[master (root-commit) c2f7900] Initial commit.
 48 files changed, 14185 insertions(+)
 .......
(master) $ git status
On branch master
nothing to commit, working tree clean

(master) $ git remote add heroku https://git.heroku.com/ab-django-todo1.git                                      
(master) $ git remote -v
heroku  https://git.heroku.com/ab-django-todo1.git (fetch)
heroku  https://git.heroku.com/ab-django-todo1.git (push)
(master) $ heroku apps
=== play@anthonybonello.co.uk Apps
ab-django-todo1 (eu)
```

Looking at information about the heroku app from the toolbelt

```bash 
(master) $ heroku apps
=== play@anthonybonello.co.uk Apps
ab-django-todo1 (eu)

(master) $ heroku dashboard
 ▸    Add apps to this dashboard by favoriting them with heroku apps:favorites:add
See all add-ons with heroku addons
See all apps with heroku apps --all

See other CLI commands with heroku help



(master) $ heroku help
```

### Create a new database on heroku

Heroku uses addons for setting up databases.

```bash 
(master) $ heroku addons:create heroku-postgresql:hobby-dev
Creating heroku-postgresql:hobby-dev on ⬢ ab-django-todo1... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-animate-27919 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation
```
We specify the database we want and the level of subscription we want.

### Connecting to the remote database

In heroku dashboard go to the settings tab and click on `Reveal Config Vars`.
We see that a variable entry was added:
`DATABASE_URL : postgres://lqlyhqrorqqbis:dadc7a299f8468918e2a75ac48aada500cd59c010fc453220e2f7a0fe88020a0@ec2-54-246-86-167.eu-west-1.compute.amazonaws.com:5432/dm1ijrs49r7h7`

It contains the url for the database. Install `dj_database_url` which allows us to 
parse database urls. Update the `requirements.txt`.

In our project terminal:
```bash
(master) $ sudo pip3 install dj_database_url
Downloading/unpacking dj-database-url
  Downloading dj_database_url-0.5.0-py2.py3-none-any.whl
Installing collected packages: dj-database-url
Successfully installed dj-database-url
Cleaning up...
(master) $ pip3 freeze --local >requirements.txt
```

Run heroku config to see the details about the database.
```bash 
(master) $ heroku config
=== ab-django-todo1 Config Vars
DATABASE_URL: postgres://lqlyhqrorqqbis:dadc7a299f8468918e2a75ac48aada500cd59c010fc453220e2f7a0fe88020a0@ec2-54-246-86-167.eu-west-1.compute.amazonaws.com:5432/dm1ijrs49r7h7
```

### Update settings.py file

Look for the databases configuration. Comment out the existing database which 
points to sqlite. Replace it with the following code. Remember to import 
dj_database_url.

```python3 
import dj_database_url


DATABASES = {
    'default': dj_database_url.parse("postgres://lqlyhqrorqqbis:dadc7a299f8468918e2a75ac48aada500cd59c010fc453220e2f7a0fe88020a0@ec2-54-246-86-167.eu-west-1.compute.amazonaws.com:5432/dm1ijrs49r7h7")
}
```

The string passed to the parser comes from heroku's config variables. This can
be accessed from the `dashboard > settings` tab, or by using the `heroku config` 
in the terminal.

Now we need to migrate our model to this new database.

```bash 
(master) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
  Applying todo.0001_initial... OK
```
We have successfully connected to a postgres database hosted on heroku through 
django.


### Adding github


Created a new repository on github. Git is already initialised locally. Add a new 
remote.

```bash 
(master) $ git remote add origin https://github.com/abonello/django-todo-ci_tutorial.git
(master) $ git remote -v
heroku  https://git.heroku.com/ab-django-todo1.git (fetch)
heroku  https://git.heroku.com/ab-django-todo1.git (push)
origin  https://github.com/abonello/django-todo-ci_tutorial.git (fetch)
origin  https://github.com/abonello/django-todo-ci_tutorial.git (push)


(master) $ git add .
(master) $ git commit -m"connecting to postgres."
(master) $ git push origin master

```