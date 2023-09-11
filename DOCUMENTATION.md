## Project Workflow 🔬

The project is a simple api made with Python that provides Create, Read, Update and Delete (CRUD) 
functionality on a django model named `Person`. There are two main endpoints; one for listing and 
creating instances and the other detail endpoint providing retrieve, update(partial or complete) 
and delete functionality.

When a request is made to an endpoint, the url is first scanned against the urls registered in the root urlconf 
(src/settings.py). After this, the respective view is invoked with the request data if any. The serializer class 
of the view comes into action serilizing the JSON data from the request, and converting it to a python object 
that can be saved in the database. In the reverse case, on get requests, the serializer converts python objects 
to JSON which is outputted as the response.

<br>

## Api Overview 🔬

Here are the routes for the api:
```
/api/persons/
/api/persons/<str:name>/
```

The `/api/persons/` route accepts the following request methods:

- `GET` : List out all `Person` model objects in the database
	- Returns JSON data of all `Person` instances

- `POST` : Create a new `Person` instance with the post data
	- Accepts JSON data
	- Returns JSON data of the created instance


And, the `/api/persons/<str:name>/` accepts the following request methods, 
where `<str:name>` is a dynamic value:

- `GET` : Retrive a `Person` instance with possessing the provided name
	- Returns JSON data of a `Person` instance

- `PUT` : Update all writeable fields in `Person` instance 
	- Accepts JSON data of all writable fields
	- Returns JSON data of the updated instance

- `PATCH` : Update some fields in the `Person` instance
	- Accepts JSON data of some fields to be updated
	- Returns JSON data of the updated instance

- `DELETE` : Delete the `Person` instance
	- No Return data

<br>

## Model OverView 🔬

The `Person` model possesses the following fields:

- `name` - CharField with the unique argument set to `True`. This field will be used as the lookup field for the detail 
endpoint.  
- `email` - EmailField, which comes with an EmailValidator and stores the email address of the instance.  
- `bio` - TextField with the `null` and `blank` arguments set to `True` and stores a short biography of the instance

<br>

## Modules used 🛠 
- `django` (the main module used in setting up the project, handling routes and other important logic)
- `djangorestframework` (a wrapper around django to provide features like a browsable api and high abstraction classes like viewsets)
- `python-decouple` (to retrieve sensitive information from a .env file)

<br>



## Example Usage 🚀

For this example, I'll be using the `httpie` module to make requests, but you could 
use the browsable api by visiting the endpoints on your browser, or the python requests module
or other tools like Postman.
```
pip install httpie
```

Okay, say we have a guy named _John_ we want to add to our database, we would make a post request
to `/api/persons/` as highlighted in the [api overview](#api-overview-). We would also send our post data as JSON, 
and the JSON would be deserialized to a python object and saved to the database.
```
http post :8000/api/persons/ name='John' email='johndboss@django.site' bio='I love cakes!' --json 
```
The `--json` flag ensures the post data is packaged as JSON.
  
Let's add some more people:
```
http post :8000/api/persons/ name='Yvonne' email='yvgirl@django.site' bio='Software engineer @ Google' --json 
```
```
http post :8000/api/persons/ name='Mark Essien' email='markessien@django.site' bio='Head mentor at HNG' --json 
```

Now that we have some objects in our database, let's update one of them.  
  
Let's say Yvonne got a new job at Deciphrexx Inc., let's try to update her bio. According to the api overview, 
we would make a `patch` or `put` request to the detail endpoint. Since we just want to update the bio field, 
we'll make a `patch` request.
```
http patch :8000/api/persons/Yvonne/ bio='Software engineer @ Deciphrexx Inc.' --json
```
  
Let's now assume we want some information about _Mark_, so we need to retrieve his information 
using the `/api/persons/<str:name>/` endpoint. Here's how we would do it: 
```
http get ':8000/api/persons/Mark Essien/'
```
OR
```
http get :8000/api/persons/Mark%20Essien/
```
Finally, let's delete an object from the database, say _John_:
```
http delete :8000/api/persons/John/
```
And finally, to list out the remaining objects in our database, we would make a get request to the `/api/persons/` 
endpoint.
```
http get :8000/api/persons/
```

<br>

And that's it! Through the api, we have successfully:

- Created `Person` objects
- Retrieved an instance by name
- Updated an instance
- Deleted an instance

Note: Always remember to add the trailing slash at the end of all endpoint urls to avoid 301 errors.
