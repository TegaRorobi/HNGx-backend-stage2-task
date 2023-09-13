## Project Overview 🔬

The project is a simple api made with Python that provides Create, Read, Update and Delete (CRUD) 
functionality on a `Person` django model. There are two main endpoints; one for listing and 
creating instances and the other detail endpoint providing retrieve, update (partial or complete) 
and delete functionality.

<br>

## Model OverView 🔬

The `Person` model possesses the following fields:

- `name` - Character field with unique values that serves as the lookup field in the detail endpoint  
- `email` - Email field storing the email address of the instance  
- `bio` - Text field storing a short biography of the instance  

<br>

## Api Overview 🔬

Here are the routes for the api:
```
/api/persons/
/api/persons/<str:user_id>/
```

The `/api/persons/` route accepts the following request methods:

- `GET` : List out all `Person` instances in the database
- `POST` : Create a new `Person` instance with the post data


And, the `/api/persons/<str:user_id>/` accepts the following request methods, 
where `<str:user_id>` is a dynamic value that will be used to retrieve a specific instance.  
**Note**: _user\_id_ can either be the name or the id of the object.

- `GET` : Retrive a `Person` instance possessing the provided dynamic name
- `PUT` : Update all writeable fields in `Person` instance 
- `PATCH` : Update some fields in the `Person` instance
- `DELETE` : Delete the `Person` instance

<br>

## Modules used 🛠 
- django
- djangorestframework
- python-decouple

<br>

## Getting started 🚀

### Step 1
Open up your favourite terminal (powershell, command prompt, etc...)

### Step 2
Clone the github repository
```
git clone https://github.com/TegaRorobi/HNGx-backend-stage2-task.git
```

### Step 3
Navigate to the project folder
```
cd HNGx-backend-stage2-task/
```

### Step 4
Create a virtual environment and install the requirements
- Windows
```
pip install -r requirements.txt
```
- Mac/Linux
```
python3 -m pip3 install -r requirements.txt
```

### Step 5
Run a development server on port 8000 (or any port of your choice)
- Windows
```
python manage.py runserver 8000
```
- Mac/Linux
```
python3 manage.py runserver 8000
```
