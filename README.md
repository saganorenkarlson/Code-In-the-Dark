## Code In the Dark

## Functional and technological specification 
### Client-side:
Vue.js
Pinia for state management

### Server-side:
Django 
Firebase for authentication

### Functional specfication
We want to create a web application that allows the user to log in and from there take part in a daily challange of code in the dark.
The user has a profile that keeps track of its performance and if times allow the users can become friends.

We plan that the evaluation of the code will be basic in the beginning but can be futher developed. 

Link to figma prototype: https://www.figma.com/proto/kGLrRHCKZPP7NV7EzJRaXM/Untitled?page-id=0%3A1&node-id=1-2&viewport=490%2C177%2C0.12&scaling=min-zoom&starting-point-node-id=1%3A2&show-proto-sidebar=1

## To run

### Start vue.js
In terminal from client/vueapp run
```
npm run serve
```

### Start Django for connection to MongoDB
In terminal from django run
```
python manage.py runserver
```

### Start Django for connection to Celery
In terminal from django run
```
celery -A django_rest_api_tasks.celery worker --pool=solo -l info
```
and in another one
```
celery -A django_rest_api_tasks beat  -l info
```