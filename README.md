# Job Offer API
A Django Rest Framework API that provides a CRUD to the model "JobOffer" and serves them as a REST API


## Starting

### 1) Preparation
Create a virtual environment and then install the requirements:

pip install django
pip install djangorestframework

### 2) Initiate the database

python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py createsuperuser

After creating a superuser, enter the admin and create a few Job Offers

### 3) Start playing around

Start the server:
python .\manage.py runserver

You have two endpoings:

api/jobs <--- List/Creates job offers
api/jobs/<int:pk> <--- Gets/Puts/Deletes a job offer

