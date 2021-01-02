# Feel So Good

[![Build Status](https://www.travis-ci.com/boomernag/feel-so-good.svg?branch=master)](https://www.travis-ci.com/github/boomernag/feel-so-good)      


![Landing Page](/static/img/landing_page.png)

#### You can access the platform [Here]('https://boomernag-feel-so-good.herokuapp.com/')

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content and Media**](#content-and-media)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)

---

## UX

### Project Goals
#### Target Audience
- People who wants to feel good
- People who wants to buy products regarding feeling good
- People who wants to be inspired to feeling good

#### Visitor/user goals:
- Purchase products shown on the website in a safe and secure way
- Get inspiration about feeling good

#### Business goals(site owner's goals):
- Provide users with a secure professional e-commerce online shop.
- Make profit from selling products.
- Inspire people who are striving to feel good.
### User Stories    
#### Common user stories (guests, new users and authenticated users)
- As a user, I expect to access the website from any device, so that I can use the website anytime and anywhere.
- As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.
- As a user, I want to easily access social media links of the company, so that I can read more information about it.
- As a user, I want to read an about section of the company, so that I can quickly decide if it satisfies my needs.
- As a user, I want to find an information about the company, to know what they do, what their main principles and ideas
- As a user, I want to view product details (e.g. image, price, description), so that I can buy some of them.
- As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
- As a user, I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment. 
- As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
- As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
- As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successful.
#### New Users
- As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.
#### Returning users
- As a user, I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
- As a user, I want to reset my password if I forgot it, so that I can get access to my profile again. 
- As a user, I want to  be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.    
- As a user, I want to  be able to change my email or add the second email, so that I can have an easier access to the website's functionality and to gain more flexibility.
#### Website Owner(admin)
- As a user, I want to have convenient and secure admin interface avalable only for website admin, so that I can add, edit and remove products.
- As a user, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries.
### Design
#### Framework
- [Bootstrap](https://www.bootstrapcdn.com/), front-end framework is chosen for this project for its modern interface, ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, modals, as well as for the layout.
- [JQuery](https://jquery.com/) is used for initializing some Bootstrap components, as well as for custom functions, DOM manipulation.
#### Colour Scheme
**Green** and **Black** and **White** are the colors used throughout the site. **Green** is the nature color and we unconsiously feel good seeing it.
#### Typography
There is one font used across the project: 
- [Lato](https://fonts.google.com/specimen/Lato) used as the main body font, popular modern sans-serif typeface providing good readability.
#### Icons
Icons are used widely, as they are good attention grabbers.
- I used [FontAwesome](https://fontawesome.com/) as the main icon library across the project (e.g. for social media links, forms, cart, search and user icons in navigation).

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) tool was used to create all wireframes for the project.   


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Features
Feel So Good website is composed by seven applications: `home`, `about`, `blog`, `products`, `bag`, `checkout`, `profiles`.
### Existing Features     
#### Navbar
The navbar is fixed at the top of the page all the time, this allows a user to easily navigate throughout the website.
 The **logo** is located in the top left corner on a desktop and in the center on the smaller devices. 
 It redirects a user to the home/landing page when clicked. On smaller resolutions (tablet, mobile) 
 the navbar is collapsed into a burger icon. Menu links appear when the burger icon is clicked and collapse back, when clicked again.    
 
Navbar also contains a **search box**, where a user can search for product. It is collapsed into a search icon on the mobile and tablet, and slides down when the icon is clicked.     
Also, navbar contains a **cart icon** along with a grand total displayed if there are items in the cart added. It changes the colour to yellow when there's something
in the cart to catch user's attention, and remains white (as other navbar elements) when the cart is empty. Clicking the cart icon redirects a user to the cart page.   

On the large screens an active page is highlighted (colour changes to green) depending on which page a user is currently on.      
The difference in navbar for logged in, non-logged in users and admin:   
For **non-logged in** users or guests navbar contains the following links: Login, Register.   
For **logged in** users it contains the **"My Account"** nav-item which toggles down the following links that redirect user to the corresponding pages: My Profile, Order History, Logout.   
- For **admin** apart from all the links available for logged-in users mentioned above, there is also a link to the **Product Management page**, where admin can add new products. This is avaliable only for superusers. Defensive design with corresponding error messages is in place to protect this page from manual entering the url in the browser.
#### Footer 
Main footer section is stuck to the bottom of the page and displayed across all the screens. It contains the **social media icon-links** which redirect a user to the corresponding page, opening in a new tab. Icons open the main pages, as it is not the real company.   
- **logo**, that is clickable and redirects to the landing page and also a small paragraph about the company
- **quick links** to the main pages
- **contact information** that contains address, phone number and email

#### Landing (home) page
The landing page serves to attract new users to the business, to give a clear understanding about that and to attract users to use the website's functionality (book ceremony/buy products). Smooth animation on scroll is apllied to almost all sections of the page(mostly to images and icons). Tha landing page consists of 9 sections:
- **Hero image** section contains a full-screen image, main heading with a subheading and 1 button "See products" that redirect a user to the products pages. The purpose of this section is to attract new users, to make the first impression and to call to action.
- **Quote**  section  contains heading and Virgil's quote about health.
- **Products** section also displays an image-carousel (3 images) and a paragraph about the products, along with a button "View our products" that redirects to the Products page. 
- **Reviews** sections contains the customers' reviews carousel with the user's avatars, review and usernames.

#### About page
The page provides a user information about the main focus of the website.    

#### Products page
- The "All products" page displays product cards, including the following information: category, name, price. All product cards are clickable and redirect a user to the individual product page with detailed information (by clicking on the image or the "View details" button).   
- Clicking on **Add to cart** button will add the product to the cart with quantity equal to 1, clicking again will simply updates the quantity by 1. This functionality was added to enhance user experiance, to allow users straight away add an item to the cart without viewing products details and giving more flexibility to use the website.
- If the user is **admin**, there are also 2 buttons displayed in the cards: **Edit** and **Delete**. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as **discontinued** and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
- User can filter the products by **category** to see the specific items. When the category is clicked, only products of the selected category are displayed, as well as the  Category Name and a number of the items satisfying the query.

#### Product details page
- The product details page displays information about the selected product: category, name, description, rating, price and product image (or placeholder if no image was added). Clicking the image will open it in the new tab, if the image_url is assigned.
- The item quantity can be assigned filling the quantity form, the validation is in place restricting the quantity to the range of 1-999. The validation errors will be displayed, if the user tries to input the numbers outside of that range.
- Product can be added to the cart by clicking **Add to cart** button, that will be reflected in the cart icon in the navbar (grand total will be increased there). As well as that, the **toast success message** will be displayed when the product is added to the cart.
- If the user is **admin**, there are also 2 buttons displayed below the product name: **Edit** and **Delete**. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as **discontinued** and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by a superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
- **Products** button redirects user back to the All Products page.

#### Cart page
- The link at the top of the page **Continue shopping"** navigates  a user back to the products page, if a user wants to add something else to the cart.
- Cart page is available for both logged in and non-logged in users, so that it is possible to make purchase being a guest.
- The page contains a summary of the user's order: the item's **name**, **image**, **price**, **sub-total** and **sku**.
- A user can **update** item's quantity and **remove** items from their order completely. If a user tries to enter invalid quantity, error message will be displayed when "Update" button is clicked and will prevent the invalid form submission. The error message will inform about the possible range: 1-99 for product's quantity fields.
- **Toast messages** will be displayed when a user updates/removes items in the cart.
- At the bottom of the page the **cart subtotal**, **delivery coast** and **grand total** are displayed.
- There is a **Checkout button** that takes a user to the checkout page to proceed with the payment.

#### Checkout page
Checkout page contains checkout 3-steps form and order summary.
- **Order summary** includes short information about items in the order (image, name, quantity, subtotal, date-time), the link to **Edit cart** ( that redirects a user to the Cart page), delivery cost and also **Total to pay**.
- **Checkout form** is represented as 3 tabs with the **Next** and **Go back** buttons to navigate between the tabs. The form sections are the following: **Personal Details**, **Billing/Shipping info** and **Payment**.
- If a user already has a profile with the shipping information saved, the form will be pre-populated with this information.
- The **validation** messages will be displayed on click **Next** button, so a user can move on the next tab only if the current form-section is filled with valid information.
- The **save info** checkbox allows the form information to be saved to the user's profile for the **logged in** users.
- If it's a new or **non-logged** user there are links to register or login pages, in case a user wants to save the information to their profile.
- Before proceeding the payment, user can review and check all the information in the table (**Form Summary**).
- A user is informed how much the card will be charged in the paragraph below the **Proceed to payment** button.
- Since the website is made for educational purposes only and the Stripe functionality is only for testing, only **4242 4242 4242 4242** card number will lead to the successfull payment. A user is asked to provide card number, expiration date (any date in future) and CVC (any numbers). 
- A webhook is used to make sure that the order is processed even in the cases when the payment process is interrupted (e.g. if a user accidentally closes the page or browser after clicking "Proceed to payment" button).
- Once the form is submitted and the payment is successfully proceeded, the **Checkout sucesss** page is loaded and a confirmation email is sent to the user's email. Also, a toast message appears to ensure the user that the order was processed successfully.

#### Checkout Success page
- The paragraph with a Thank you message is displayed on the top of the page to inform a user that the payment was processed and the email was sent to the user's email.
- The **Order details** section contains all the information about the completed order. 
- **Keep shopping** button redirects user to the Products page.

#### Profile page
Profle feature is available only for **authenticated** users.
- Profile page contains **Personal info** section (username and email displayed). Also it contains 2 buttons **Change password** and **Manage emails** (changing the current or adding a new email) that take a user to the corresponding pages (that's a part of Django allauth functionality with a customized templates).
- **Shipping details** section allows to save the shipping information, so for the next purchase the fields in the checkout form will be pre-filled with this info. User can update this information anytime.
- **Order history** section that displays Order History for account.

#### Order History
Order history feature is available only for **authenticated** users.
- If a user has not made any purchases, the paragraph will inform that the order history is empty with a link to the Product page.
- If there are completed orders, the table with the following fields: **Order Number**, **Date**, **Items**, **Total** is in place.
- Clicking the link on the Order number will redirect a user to the **checkout success** page with all the order information. The Toast info message will tell the user that it's a past confirmation for the order number.
- **Back To Profile** link will redirect a user to the Profile page.

#### Admin product managment
- Product managment feature is available only for **authenticated superuser**.
- Admin page allows an owner of the website to add new products by filling out forms - **Add New Product** on the Product Management page. 
- If the form is valid, the product is added to the database and the user is redirected to the new created product details page.
- The defensive design is implemented to restrict other than admin users to manually enter the url to get access to the page. User will be redirected to the home page with the toast error messages appeared.
- **Edit** and **Delete** product functionality allows an admin to make the corresponding manipulations.
#### Django-allauth features
##### Sign Up
- The sign up page allows a user to create a new account. The user is asked to fill the fields "email", "username", "password" and "password (again)". When adding a username, the code compares it against existing email to ensure that it is unique. If user's input does not meet requirements, flash messages will inform a user about the error. When the form is submitted, a **verification email** is sent to the user's email to verify the email and finish registration process.   
- There is also a link to the login page for existing users at the bottom of the form.    
- The Registration page is only available to anonymous users and logged-in users are redirected out automatically.
##### Login
- The login page features the form with "username" and "password" fields, allowing registered users to log into their account. If the login was successfull, a user is redirected to the home page and the toast success message appears informing that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.   
- There is also a link to the sign up page for new users at the bottom of the form.
- As well as that, there's a link to the **forgot password** functionality, using which a user can reset their password.
- The login page is only available to anonymous users and logged-in users are redirected out automatically.
##### Forgot password
- A user can reset their password to be able to login by entering the email. Then the link for reseting password will be sent to the email provided. The user can create a new password and then login with a new password.
##### Logout
- Clicking "logout" button renders logout page, asking to confirm if a user wants to logout. It will end their session and redirects to the homepage with a toast success message appeared.
#### 404 and 500 error pages
- Custom 404 and 500 pages contain heading, short information about the error and a button "Back Home". As well as that, they display navbar that allows users to come back easily to any page if they got lost.

### Features Left to Implement

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>


---
## Information Architecture
### Database choice
During the development phase I worked with **sqlite3** database which is installed with Django.   
For deployment(production), a **PostgreSQL** database is provided by Heroku as an add-on.
- The **User model** used in this project is provided by Django as a part of defaults `django.contrib.auth.models`. More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

### Data Modelling
#### Profile App
##### Profile
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Full Name | profile_full_name | CharField | max_length=70, null=True, blank=True
 Phone number | profile_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | profile_address_line1 | CharField | max_length=60, null=True, blank=True
 Address Line2 | profile_address_line2 | CharField | max_length=60, null=True, blank=True
 Town/City | profile_town_or_city | CharField | max_length=50, null=True, blank=True
 County | profile_county | CharField | max_length=50, null=True, blank=True
 Postcode | profile_postcode | CharField | max_length=20, null=True, blank=True
 Country | profile_country | CountryField | blank_label='Country', null=True, blank=True

#### Products App
##### Product
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Name | name | CharField
 Description | description | TextField | max_length=800 
 Price | price | DecimalField |max_digits=6, decimal_places=2 
 Rating | rating | DecimalField | max_digits=2, decimal_places=1, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)]
 Image | image| ImageField | null=True, blank=True
 Image Url | image_url | URLField | max_length=1024, null=True, blank=True
 Sku | sku | CharField | max_length=254, null=True, blank=True
 
##### Category
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
Programmatic Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

#### Checkout App
##### Order
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=70, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone number | phone_number | CharField | max_length=20, null=False, blank=False
Address Line1 | address_line1 | CharField | max_length=60, null=False, blank=False
Address Line2 | address_line2 | CharField | max_length=60, null=False, blank=False
Town/City | town_or_city | CharField | max_length=50, null=False, blank=False
County | county | CharField | max_length=50, null=True, blank=True
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Country | country | CountryField | blank_label='Country*', null=False, blank=False
Purchase Date | purchase_date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Cart | original_cart | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

##### Order LineItem Details 
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.PROTECT
Quantity | quantity | IntegerField | null=False, blank=False, default=0
Item Total | item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

Note: I wont include the "blog app" here as it is not functioning at the moment.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Heroku](https://heroku.com/) - to host the project.
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in prodcution.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS.
- [Travis](https://travis-ci.org/) - for integration testing.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [Coolors.co](https://coolors.co/) - to create colour palette used in the README.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---
## Testing
Testing information can be found in a separate [TESTING.md](https://github.com/boomernag/Feel-So-Good/blob/master/TESTING.md) file

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Deployment
The Feel So Good project was developed using the [GitPod](https://www.gitpod.io/) online IDE and
using Git & GitHub for version control. It is hosted on the [Heroku](https://heroku.com/) platform and user-uploaded images being hosted in [AWSS3Basket] (https://aws.amazon.com/)
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/download/releases/3.0/)    

Apart from that, you also need to create accounts with the following services:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://mail.google.com/)

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/boomernag/feel-so-good`    
Alternatively, you can save a copy of this repository by clicking the green button **Clone or download** , then **Download Zip** button, and after extract the Zip file to your folder.      
In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).       

Note: You can read more information about the cloning process on the [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).   

2. Set up environment variables.     
Note, that this process will be different depending on IDE you use.   
In this it was done using Heroku but it can also be done the following way:      
    - Create `.env` file in the root directory.
    - Add `.env` to the `.gitignore` file in your project's root directory
    - In `.env` file set environment variables with the following syntax:     
    ```bash 
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
     ```
       
Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)
    
3. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`
4. In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`
`python3 manage.py migrate`    
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`
7. You will now be able to run the application using the following command:     
`python3 manage.py runserver`
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
*To start Heroku Deployment process, you need to clone the project as described in the [Local deployment](#local-deployment) section above.*     
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:    
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:    
`pip3 freeze > requirements.txt`    
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:      
`web: gunicorn feel_so_good.wsgi:application`    
3. `git add`, `git commit` and `git push` these files to GitHub repository.     
NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illistrated here as they are required for the successfull deployment to Heroku.        
As well as that, other things that are required for the Heroku deployment and have to be installed: **gunicorn** (WSGI HTTP Server), **dj-database-url** for database connection and **Psycopg** (PostgreSQL driver for Python). All of the mentioned above are *already installed* in this project in the requirements.txt file.     
4. On the [Heroku](https://heroku.com/) website you need to create a **new app**, assigne a name (must be unique),set a region to the closest to you(for my project I set Europe) and click **Create app**.   
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type `postgres`), select **Hobby Dev — Free** and click **Provision** button to add it to your project.     
6. In Heroku **Settings** click on **Reveal Config Vars**.   
7. Set the following config variables there:     

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |
     
8. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in **settings.py**.     
You can temporary comment out the current database settings code and just paste the following in the settings.py:   
```bash 
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
  ```
Important Note: that's just temporary set up, this URL **should not be committed and published to GitHub** for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.     
9. Migrate the database models to the Postgres database using the following commands in the terminal:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`
11. Create a **superuser** for the Postgres database by running the following command(*you need to follow the instructions and inserting username,email and password*):      
`python3 manage.py createsuperuser`     
12. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.    
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.     
13. Add your Heroku app URL to **ALLOWED_HOSTS** in the settings.py file.
14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.    
To do so, from the Heroku dashboard follow the steps:
-  **Deploy** section -> **Deployment method** -> select **GitHub**
-  link the Heroku app to your GitHub repository for this project
- click **Enable Automatic Deploys** in the Automatic Deployment section
- Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.     

Alternatively, in the terminal you can run:    
- `heroku login`    
-  after adding and comitting to Git, run the following command:     
`git push heroku master`
15. After successful deployment, you can view your app bu clicking **Open App** on Heroku platform.
16. You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!    
##### Hosting media files with AWS
The **static files** and **media files** (that will be uploaded by superuser - product images) are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). To host them, you need to create an account in AWS and create your S3 basket with *public access*. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) and [this tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).
##### Sending email via Gmail
In order to send real emails from the application, you need to connect it to your **Gmail account**, setting up your **email address** in EMAIL_HOST_USER variable and your **app password** generated by your email provider in EMAIL_HOST_PASS variable.


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Credits
### Code
- The main code for the project is retraced through [Code Institute](https://codeinstitute.net/) video lessons on the last project in the course -Boutique Ado Django Mini-Project. It is customized to some parts, modified and enhanced to fit the project purposes.
- [Stack Overflow](https://stackoverflow.com/) was helpful in countless number of times for giving answers to questions of how to proceed.
- For the blog the code was taken from [DjangoCentral] (https://djangocentral.com/building-a-blog-application-with-django/)
### Content and Media
- The images are bought images since earlier from [Unsplash](https://unsplash.com).

### Acknowledgements

- I have had a really ruff time finding the time to give to this project that I wanted to. I changed the idea half-way through as I realised I didn't have the knowledge yet for completing it.
- As it has been over holidays the schools support has been closed for some time, especially when I needed it the most.
- I didn't make it to scheduele the last call with my mentor Rohit.
- I have been highly inspired by the MS4 project of fellow student [Irinatu17](https://github.com/irinatu17/Art-of-Tea). A fantastic project in my opinion and it has been a guiding star for me. I am not sure if I have taken code from that project without giving acknowledgements, if that is the case I want to do that here.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Disclaimer
This site is made for **educational purposes** only.        


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

