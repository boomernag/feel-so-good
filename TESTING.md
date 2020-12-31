# Testing
 1. [**Manual Testing**](#manual-testing)
     - [**Responsiveness**](#responsiveness)
     - [**Navbar**](#navbar)
     - [**Footer**](#footer)
     - [**Search bar**](#search-bar)
     - [**Landing page**](#landing-page)
     - [**About page**](#about-page)
     - [**Products and product details pages**](#products-and-product-details-pages)
     - [**Cart page**](#cart-page)
     - [**Checkout and checkout success pages**](#checkout-and-checkout-success-pages)
     - [**Authentication pages**](#authentication-pages)
     - [**Profile and Order History**](#profile-and-order-history)
     - [**Admin product management functionality (admin CRUD)**](#admin-product-management-functionality-admin-crud)
 2. [**Automated Testing**](#automated-testing)
      - [**Travis**](#travis)
 3. [**Validators**](#validators)
 4. [**Compatibility and Responsiveness**](#compatibility-and-responsiveness)
 5. [**Other Testing**](#other-testing)
 6. [**Bugs**](#bugs)
## Manual Testing
Manual testing was conducted with each feature and each user story on different screen resolutions, devices and in different browsers to ensure the application is a good solution to user's needs.  
### Responsiveness
- **User story being tested**:       
*As a user, I expect to access the website from any device, so that I can use the website anytime and anywhere.*
- **Test**:
    - check each page of the website from multiple devices and multiple browsers
    - open the website in the Google Dev Tools and click on "Responsive" to check all pages for all resolutions from 320px and above
    - more detailed information about responsiveness testing can be found in [Compatibility and Responsiveness](#compatibility-and-responsiveness) section
- **Results**:
- **Verdict**:

### Navbar
- **User story being tested**:      
*As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.*
- **Test**:
    - click on all the links in the navbar, to check if they work properly pointing to the correct destination
    - check all the links on different devices (navbar looks different for mobile, tablet and desktop screens)
    - on mobile devices make sure that navbar is collapsed and the side bar shows up when the hamburger menu is clicked 
    - scroll down the page to see if the navbar is visible for a user all the time
    - on the large devices hover over the links to see if the highlighted effect (change colour to green and expand) works properly
    - on the smaller devices the search button collapses the search input box and redirects to the products page
    - test the navbar being non-logged in, logged in and as an admin user and to see if the user's status is reflected in the navbar links (login|register - for guests users, my profile, order history, logout - for all logged in users, for admin additional link - product management)
    - check when an item is added to the cart, a cart icon's colour changes to yellow and a badge with cart total appears, the total updates each time new item is added or deleted from the cart
- **Results and Verdict**:

### Footer
- **User stories being tested**:     
*As a user, I want to easily access social media links of the company, so that I can read more information about it.*     
*As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.*
- **Test**:
    - click on the social media icons to check if they lead to the corresponding pages and open in the new tabs 
    - check if GitHub and LinkedIn icons open my profiles, while Instagram and Facebook icons open the main pages (as it's an educational project and no real pages exist)
    - check different devices to test if the footer id is displayed correctly (with additional top section on large resolutions)
    - on large resolution, click on all the links in the footer (Quick links section, logo), to check if they work properly pointing to the correct destination
    - hover over the links and social media icons to test if the hover effect is working properly
- **Results and Verdict**: 

### Search bar
- **User story being tested**:     
*As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.*
- **Test**
    - enter any search word into the search box to see if it redirects to the products page with correct results displayed
    - submit an empty search query without entering anything
    - enter some search words that are not expected to be found in the website, from totally different areas (e.g. "coding", "microbiology") or just random letters/numbers
 - **Results**:       
    - when an empty form is submitted without any queries, the error message appears informing that no search word was entered
    - if the search query exists in the database, the products page renders, displaying the search word, number of the results found and all products that satisfy the query
    - if the search query does not exist in the database, the products page renders, displaying the search word, number of results equal to 0 and a paragraph telling that no results were found for the entered query
 - **Bugs found and fixed**: 
 - **Verdict**: 
 
### Landing page 
- **User story being tested**:     
*As a user, I want to get an intoduction to the company and easily find my way further into the page*
- **Test**:
    - click all the buttons accross the page
    - check all the image-carousels and reviews-carousel by clicking on chevrons
    - verify that the expected text, icons and  images are displayed 
 - **Results**:
    - all the buttons redirect to the corresponding pages (About, Blog, Products) (see **bugs** paragraph below)
    - the hover effect on buttons works as expected (expanding, changing background colour)
    - image and review carousels display correctly when chevrons are clicked
    - all the text sections, icons and all the images display correctly, changing the position, size when viewed on different screens
- **Bugs found and fixed**: The bug with the blog is found in the [Bugs](#blog-not-working) section.
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### About page
- **User story being tested**:     
*As a user, I want to find an information about the company*
- **Test**:
    - verify that the expected text is displayed correctly
- **Results**:
    - all the text sections are displayed correctly on different screens
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Products and product details pages
- **User stories being tested**:     
*As a user, I want to view product details (e.g. image, price, description), so that I can buy some of them.*    
*As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.*
- **Test**:
    - verify that the expected text and images are displayed correctly in both products and product details pages
    - login with superuser credentials and verify that the Edit/Delete buttons appear in both products and product details pages under the image
    - being a guest or logging in as a regular user, try manually enter the `/edit/` and `/delete/` urls 
    - click on the image on the product image on the all products page
    - click on the "Add to Cart" button on the product details pages
    - on the products page try to enter a negative or higher than 99 number in the quality form and click on "Add to cart" button
    - enter the quantity in the range of 1-99 and click on the "Add to cart" button
    - on the product details page click on the "Keep Shopping" button
    - on the product details page click on the product's image    
- **Results**:
    - the texts, icons and images are displaied correctly on different screens
    - Edit/Delete buttons are visible only to the superuser
    - after manually entering the `..products/edit/<prduct_id here>` and `..products/delete/<prduct_id here>` urls, the error messages were displayed as expected.
    - clicking the product image redirects to the product details page.
    - clicking the "Add to cart" button on the all products page, adds the product to the cart with quantity of 1; clicking it again increases the quantity by 1 and updates the cart
    - after submission the invalid quantity form (when a number is negative or higher than 999), the validation error messages appeared as expected
    - if the quantity form is submitted correctly, the grand total in the navbar reflects this addition. Toast success message appeared as expected
    - clicking on the "Keep Shopping" button redirects to the all products page as expected
    - clicking on the image on product details page opens an image in a new tab (if an image URL was assigned, as it's an optional field) as expected
- **Verdict**: Test passed. All the functionality works as expected, the bug was fixed.


### Cart page
- **User stories being tested**:     
*As a user, I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.*     
*As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.*
- **Test**:
    - verify that the text and images of the added items are displayed correctly 
    - try to update the item quantity with different products
    - try to manually enter invalid quantity (negative or greater that 999)
    - click on the red trash icon(remove button)
    - click on the "Checkout" button
    - remove all the items and check the empty cart, click on the "Go shopping" button
- **Results**:
    - information abour all the items is displayed correctly on different screens
    - update functionality works for products but can go over 99 (see **bugs** paragraph below)
    - clicking remove button removes item and the toast message confirms the deletion
    - subtotal changes correspondingly to reflect the update/remove
    - clicking "Checkout" button redirects to the Checkout page
    - toast messages are always displayed as expected after each update/remove action
    - if the cart is empty, the paragraph informs a user that the cart is empty; clicking "Keep shopping" button redirects to the products page
 - **Bugs found and fixed**: The bug with updating the quantity in the cart was found during testing process and it is described in details in the [Bugs](#update-quantity-in-the-cart) section.
 - **Verdict**: The bug was fixed, all the functionality works as expected. Test passed. 

### Checkout and checkout success pages
- **User stories being tested**:     
*As a user, I expect to make payments by card in a safe and secure way.*      
*As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.*      
- **Test**:
     - verify that the text (Order summary) are displayed correctly 
     - click on the "Edit cart" link
     - try to submit an empty field set (check each section- Personal details, Shipping Info and Payment)
     - try to put an incorrect information (e.g. email without @)
     - create a large number of orders as logged in and non-logged in user, ticking or not the save-info checkbox.
     - in the Payment section enter the testing **4242 4242 4242 4242** card number, any expiration date in future and any CVC, and then click on the "Proceed to payment" button (this was also checked on Stripe Dashbord to see if the order was created)
     - try to enter different and incomplete card numbers, the expiration date in the past to check the error messages
- **Results**:
    - order summary displays the order correctly
    - clicking "Edit cart" redirects back to the cart.
    - if an empty form was submitted or filled out incorrectly, the validation error messages were displayed correctly, when the "Next" button is clicked, not allowing to go to the next step before the current section is filled up with correct information.
    - when an order is created by non-authenticated user, the save-info checkbox is hidden from the view. Instead, the links to the Create account and Login pages are displayed, offering a user to login to save the information and the order to the order history 
    - if an authenticated user ticks the save-info checkbox, all the personal and shipping information is saved to their profile. There was an issue with the save-info field found during testing, that is described in the Bugs section and was successfully fixed
    - testing 4242 4242 4242 4242 card number leads to the successfull payment, that was confirmed in the Stripe Dashboard.
    - if the incorrect or incomplete card details were entered, the error messages are displayed as expected under the Payment field.
    - after the valid form was submitted, the confirmation email was recieved in the email provided with all the correct order info. As well as that, the checkout page renders showing the order summary.
    - when the order was completed by the logged in user in the checkout success page, the "View full order history" button redirects to the Order history page. "Keep shopping" button is displayed for both non-logged in and logged in users and redirects to the products page
 - **Verdict**: Test passed. 

### Authentication pages
These features are built-in components of Django allauth package were tested manually as well, as about 5-10 different accounts were created.     
Forgot/reset password, verification email, login, create account - all work as expected.
- **User stories being tested**:     
*As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.*    
*As a user, I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.*       
*As a user, I want to reset my password if I forgot it, so that I can get access to my profile again.*     
- **Test**:
     - try to register entering incorrect email, incorrect password and  username/email that already exists in the database
     - submit valid registration form
     - entering two different passwords in registration form and trying to enter old password when re-setting password
     - create an account and try to login with correct and incorrect details
     - click on logout link in the navbar and then on logout button
- **Results**:
    - if required data is missing or incorrect, form does not submit and an error messages are displayed informing user what was wrong
    - if the registration form is valid, user is informed that they need to verify their account and the email was sent to them with the verification link
    - when verification link is clicked in the email, user is redirected to the confirmation page, clicking "Confirm" button, success message is displayed and user is automatically logged in
    - on the login page, when "Forgot password" link is clicked, a user is redirected to the password reset page and asked for their email address, then an email is sent with a link to reset password. After entering new password twice, the password is reset and user can login with a new password
    - when logout link in the navbar is clicked, the login page opens asking for confirmation to logout, when it is confirmed, the user is logged out and the session is stopped
    - the login and registration page are only available to anonymous users and logged-in users are redirected out automatically.
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Profile and Order History
- **User stories being tested**:     
*As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history*        
*As a user, I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.*           
*As a user, I want to  be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.*    
*As a user, I want to  be able to change my email or add the second email,so that I can having an easier access to the website's functionality and to gain more flexibility.*
- **Test**:
    - navigate to the My Profile from the Navbar link
    - check being a logged in and non-logged in user, that it's only available to the authenticated users
    - click on the Order number on the Order History page
    - on the My Profile page fill out the shipping details form and click on the "Update information" button
    - on the My Profile page update/delete some information in the shipping details form and click on the "Update information" button
    - after submiting the form, make a purchase to see if the personal and shipping fileds in checkout form are pre-populated with that info
    - click on the "Change password" button and test Change password functionality by filling out the form
    - click on the "Manage emails" button and test Manage email functionality by adding new emails, removing them, making primary
    - check the Order History page with a freshly created account with no orders
    - click on the "View My Profile" on Order History page
- **Results**:
    - My Profile is available only to the logged-in users
    - clicking the Order number on the order history page opens the past confirmation (checkout success) page with the corresponding toast info message as expected
    - Profile page displays all the personal info (email and username), clicking on the "Change password" and "Manage emails" buttons leads to the correct destinations (that's built-in Django functionality). Everything works as expected.
    - if all the shipping information on the profile page was deleted, then on the checkout page all the fields were empty. At the same time if there are shipping details saved on the profile page, the checkout form fields were pre-filled, confirming that the shipping info was saved into the Profile model.
    - "View My Profile" link lead to the correct destinations
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.
 
### Admin product management functionality (admin CRUD)
- **User stories being tested**:     
*As a user, I want to have convenient and secure admin interface avalable only for website admin, so that I can add, edit and remove products.*
- **Test**:
    - navigate to the Product Management page from the navbar
    - click on the "Add a New Product" to open the corresponding form
    - try to submit form being empty in required fields or with invalid information to see if the error messages will appear
    - submit "Add a New Product" form with all valid information multiple times creating different products (providing/not providing an image, filling all/only required fields)
    - after adding a product with an image, go to the AWS S3 website and check the basket to see if the image was saved there
    - after clicking "Edit" button on the product pages, fill out the edit form (change something, remove some fields' values)
    - create few testing products with dummy data for testing the delete functionality
    - being a guest or logged in as a regular user(not admin), manually enter the edit/delete/add URLS to reach the corresponding pages trying to access admin functionality and manipulate the database
- **Results**:
    - Add product forms work as expected: validation error messages appear if the form is invalid. After successfull addition it redirects to the new created product page with all correct information displayed.
    - if image wasn't provided, no-image placeholder is assignmed and displayed. In production all images are stored in the AWS S3, so the new images were successfully saved into the Basket as expected.
    - Edit functionality works as expected: validation error messages appear if the form is invalid. After successfull addition it redirects to the product/service page and all the changes straight away can be seen in that page and in the database (admin panel can be checked as well).
    - Delete functionality works as expected: after clciking "Delete" button on the product the product is removed.
    - The defensive design worked well, allowing only superuser to have an access to this functionality. If non-admin users try to access the pages, they are redirected to the home page with corresponding error messages displayed.
 - **Verdict**: The bug was fixed, all the functionality works as expected. Test passed. 
 
 <div align="right">
    <b><a href="#testing">↥ Back To Top</a></b>
</div>


## Validators
### HTML
All the HTML files were tested through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Since it does not recognize Jinja2 templating language, it showed a number of errors. There were also few minor errors and warning that can be safely ignored. Apart from that, no other errors were found across the html pages.   
### CSS
All the CSS files were tested through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). Since it does not recognize CSS variables (colours and fonts variables were used), there were several Parse Errors found. These errors can be safely ignored as they are not errors in fact. The rest of the CSS files was completely valid.   
### JavaScript
All the JS files were tested through and [JSHint](https://jshint.com/) validators, code was syntactically valid.  
### Python
All the Python files were tested through [PEP8 Online](http://pep8online.com/) validator and further changes were made to make the code PEP8 compliant where possible.

 <div align="right">
    <b><a href="#testing">↥ Back To Top</a></b>
</div>

## Compatibility and Responsiveness
This website is tested on **Chrome** and on **MacBook Pro 13'**           
Also, the following tools were used to constantly test the project:
- **Google Chrome's developer tools** to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.       
-  [Am I Responsive](http://ami.responsivedesign.is/) and [Responsinator](http://www.responsinator.com/) online tools for checking responsiveness on different devices (used the local GitPod link as the Heroku has security restrictions).

<div align="right">
    <b><a href="#testing">↥ Back To Top</a></b>
</div>

## Other Testing 
- The app was constantly testing with **debugger** locally: `debug=True` throughout all the development process. Every time when there was an error (when app crashed), the debugger displayed an error message to the view, that allowed me to find the location of the error and fix it.

<div align="right">
    <b><a href="#testing">↥ Back To Top</a></b>
</div>

## Bugs 
### Blog not working
- The time is running up and I don't have anymore time to try to fix this. The blog homepage is working in gitpod but not on deployed site.
- Admin cannot add blog post but is redirected to 500 page.

### Type number over 99 in quantity box
- User can type a value higher than 99 then click update.
### Example
#### Bug

#### Verdict
- Time is running out so these bugs will be fixed after submission.

 <div align="right">
    <b><a href="#testing">↥ Back To Top</a></b>
</div>

[Back to README](https://github.com/boomernag/feel-so-good/blob/master/README.md#testing)
