# ecommerce-backend
Django backend for eCommerce project

This project is built using Django REST Framework to provide the backend API for eCommerce project.  

Features
--------
1. Products API endpoint available at `/product/`.
2. Orders API endpoint available at `/orders/`.
3. Custom user authentication using JSON Web Tokens. The API is available at `/authentication/`.![Screenshot 2024-04-17 at 12.46.14 PM.png](static_files%2FScreenshot%202024-04-17%20at%2012.46.14%20PM.png) ![Screenshot 2024-04-17 at 12.46.26 PM.png](static_files%2FScreenshot%202024-04-17%20at%2012.46.26%20PM.png)
4. Swagger documentation of the API endpoints is available at `/swagger/` ![Screenshot 2024-04-17 at 11.34.53 AM.png](static_files%2FScreenshot%202024-04-17%20at%2011.34.53%20AM.png)


Main requirements
------------

1. `python` 3.7, 3.8, 3.9, 3.10
2. `Django` >=3.2,<4
3. `MySQL` 8.3.0


## How to set up





### Manual setup

Firstly, create a new directory and change to it:

`mkdir ecommerce-backend && cd ecommerce-backend`

Then, clone this repository to the current directory:

`git clone https://github.com/Abheet007/ecommerce-backend.git`

For the backend to work, one needs to setup database like MySQL or PostgreSQL on a local machine. This project uses MySQL by default (see [Django documentation](https://docs.djangoproject.com/en/3.2/ref/settings/#databases) for different setup). This process may vary from one OS to another, eg. on Arch Linux one can follow a straightforward guide [here](https://wiki.archlinux.org/index.php/PostgreSQL).

The database settings are specified in `ecommerceBackend/settings.py`. You can create your own database and update the `PASSWORD` and `NAME` fields in it.

Next, set up a virtual environment and activate it:

`python3 -m venv env && source env/bin/activate`

Install required packages:

`pip3 install -r requirements.txt`

Next, perform migration:

`python3 manage.py migrate`

At this point, one may want to create a superuser account and create some products. One can also use sample data provided in `products/fixtures.json` by running:

`python3 manage.py createsuperuser`

For the verfication email to come you need to update `EMAIL_HOST_USER ` and 
`EMAIL_HOST_PASSWORD` in `settings.py` with your email and HOST_PASSWORD.

The backend is now ready. Run a local server with

`python3 manage.py runserver`

The backend should be available at `http://127.0.0.1:8000/`.

NOTE: There might be additional packages to need to install which are not mentioned in the requirements.txt file.
