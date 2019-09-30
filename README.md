# Pizza ordering app using Django

This app is live [here](https://django-pizza-order-hkamboj.herokuapp.com) <br>
It runs a bit slow since it is deployed on Heroku free tier account.

This project is based on an assignment of 
[CS50 Web Development with python and javascript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript)



## Milestones achieved

The assignment had to be completed with meeting following requirements:

- Complete the Menu, Adding Items, and Registration/Login/Logout steps.
- Complete the Shopping Cart and Placing an Order steps.
- Complete the Viewing Orders and Personal Touch steps.

## Installation

1. Open terminal using Ctrl+T. Run the following command <br>
`git clone https://github.com/HemabhKamboj/Pizza-ordering-app.git`

2. Create and active virtual environment using  <br>
` virtualenv -p python3 venv` <br>
` cd venv` <br>
`source bin/activate` <br>
3. Change the directory using <br>
`cd ..` <br>
` cd Pizza-ordering-app master`
4. Now you need to install python packages to run the app <br>
`pip3 install -r requiements.txt`
5. Create superuser <br>
 `python manage.py createsuper`
6. Run Django app <br>
`python manage.py runserver`

## Tech Stack

- **Django**  Django is a Python-based free and open-source web framework,
 which follows the model-view-template architectural pattern. It is maintained by the Django Software
 Foundation, an independent organization established as a 501 non-profit. 
Django's primary goal is to ease the creation of complex, database-driven websites. [Django Project](https://www.djangoproject.com/) <br>
It is used in this project, to handle all routes, rendering pages, managing databases, 
user authentication and almost all the stuff of which the application is capable of.
- **SQLite** SQLite is a relational database management system contained in a C programming library. In contrast to many other database management systems, 
SQLite is not a client–server database engine. Rather, it is embedded into the end program<br>
It comes with Django with itself, no setup required, hence easy to use, but is not recommended for large scale
production application.
- **Bootstrap** Bootstrap is a free and open-source front-end Web framework. It contains HTML and CSS-based design templates for typography, forms, buttons, navigation and other
 interface components as well as optional JavaScript extensions. [Get Bootstrap](getbootstrap.com) <br>
Used for stylising frontend. 


## To do list 
1. Integrate Payment gateway 
2. Authenticate user using Google and Facebook
3. Integrating automatic mailing system to send conformation of order.
4. Improving frontend with better CSS and Javascript implementation 



