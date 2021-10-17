# **Tipsy Mac Staggers - Testing** #

![Image of site on several devices](assets/images/readme_images/readme_header_image.png)

<hr>

## **Table of contents** ##

### **1. Automated Testing** ###

* 1.1 HTML Code Validating
* 1.2 CSS Code Validating 
* 1.3 JavaScript Validating
* 1.4 Python Validating
* 1.5 Django Tests

### **2. Manual Testing** ###

* 2.1 Manual testing desktop
* 2.2 Manual testing mobile

### **3. Responsiveness** ###

* 3.1 Chrome Dev Tools
* 3.2 Responsive Design Checker

### **4. Console Testing** ###

* 4.1 Console test results

<hr>

<details>
<summary><strong>
1. Automated Testing
</strong></summary>
<br>

#### **1.1 HTML Code Validating** ####

* All of the HTML files were tested on the [W3C HTML Markup Validation website](https://validator.w3.org/)<br>
* NEED TO DETAIL TEST RESULTS HERE
<hr>

#### **1.2 CSS Code Validating** ####
* The main CSS files were tested on the [W3C CSS  Validation website](https://jigsaw.w3.org/css-validator/)<br>
* NEED TO DETAIL TEST RESULTS HERE
<hr>

#### **1.3 JavaScript Code Validating** ####
* The testing for the script.js file was carried out on [JShint.com](https://jshint.com/) The results from the test were as follows:<br>
* NEED TO DETAIL TEST RESULTS HERE
<hr>

#### **1.4 Python Code Validating** ####
* The testing for the python files were carried out on [pep 8 online](http://pep8online.com/) The results from the test were as follows:<br>
* NEED TO DETAIL TEST RESULTS HERE
<hr>

#### **1.5 Django Tests** ####

* I have created automated Django tests in each django app in this project. The tests can be found in the tests.py file in each app. There 
</details>
<hr>

<details>
<summary><strong>
2. Manual Testing
</strong></summary>
<br>

#### **2.1 Manual testing desktop** ####

All desktop testing was carried out on Chrome, FireFox, Opera and Safari. Results listed below will apply to all browsers unless highlighted as otherwise. 

**1. The Home Page**

* The homepage is rendering correctly on all of the browsers as intended.
* Clicking the In Safe Hands name in the top left brings the user back to the home page
* Clicking the search bar without entering an item to search for brings the user to the all products page and the correct toast displays the message in the top right of the screen. 
* The dropdown menus are all expanding when clicked and showing the correct sub menu options
* I have clicked on every option in the 4x dropdown menus and all the links bring the user to the correctly specified page
* The reviews carousel on the bottom of the page is rendering and cycling through the reviews as is intended. 

**2. The My Account, Profile & Cart**

* When a user clicks on the My Account icon and clicks on the sign up option the correct sign up page is rendering
* I have clicked on sign up and followed the steps to create a new registered user on each browser. All of the accounts were able to be set up correctly as expected on all browsers.  
* When a user clicks on the My Account icon and clicks on the Log in option the correct Log in page rendering
* If a user enterers the incorrect username and/or password the page will reload with a warning message saying <strong>"The username and/or password you specified are not correct"</strong>
* If a user tries to enter just the username or just the password the the login form validation will notify them that all fields are required and they must complete all fields. 
* If a user tries to create an account with an email address that is already in use they will see an error message displayed saying that email address is already associated with another account. 
* Users can click on the forgot my password link and enter their email address to be sent the password reset link. In testing the email with the password reset link and username is sent as expected. This works on all browsers.
* I have been able to log in with the created username and password on all browsers and have been able to log out on every browser. The correct toast confirming login and logout in the top right is also generated.
* After logging in i am able to see the users profile page and order history as expected on all browsers. 

Note!
* On safari the dropdown menu for Country is displaying slightly different than on the other browsers. I have checked the functionality and it is working as normal. The difference is purely aesthetic so i am noting here that i am aware of it

![Image of country dropdown safari](media/readme_images/country_dropdown_safari.png)

* When i click on a past order number on the profile page the order details open and are all displaying correctly. 
* If i click on the cart button when the cart is empty then the correct message saying the shopping cart is empty and the link to go to the store is displaying correctly. 
* If i try and bypass this by typing checkout in the url i correctly get redirected to he products page with the warning toast saying there is nothing in your cart. 

**3. The Products Page**

* The products page is displaying all of the products for sale in the store correctly. As the user adjusts the screen size the layout is adjusting on each browser as expected.  

**4. The Product Details Page**

* All of the product details are displaying correctly as intended on all browsers. 
* When the user clicks the Read Product Reviews the collapsible expands correctly and shows the reviews on each browser. 
* If a user tries to set the quantity to 0 and add it to the cart they will see the validation error informing them the minimum number allowed is 1.
* Users can add items to the cart as expected by selecting the quantity and pressing the add to cart button. 

**5. The Cart Page**

* A user who tries to access the cart with nothing in it will get the message there is nothing in your cart and be given the option to click and be redirected back to the store
* Once the user has an item in the cart they can adjust the quantity and update the cart. The cart on all browsers reflects the update correctly
* If a user presses the remove button the item is removed from the cart
* If the user clicks on the secure checkout button the user will be brought to the checkout page 

**6. The Checkout Page**

* The checkout page is rendering correctly and the logged in users delivery address is automatically populating on all browsers.<br>

Note!

* Again on safari the dropdown menu for Country is displaying slightly different than on the other browsers. I have checked the functionality and it is working as normal. The difference is purely aesthetic so i am noting here that i am aware of it

![Image of country dropdown safari](media/readme_images/country_dropdown_safari_2.png)

* I have placed an order on each browser and the order has gone through successfully using the Stripe test card details. 

**7. The Order Confirmation Page**

* After placing an order the order confirmation page is generated and rendered correctly with all of the order details displayed as they should. 

**8. About Us Page**

* The about us page is rendering as expected on all browsers with no issues or errors. It adjusts it structure as the page size is adjusted on smaller devices. 

**9. Covid Data Page**
* When a none logged in user comes to this page they will see the message informing them the data is only available to registered users. 
* Once logged in the covid data that was behind a registered users wall is now rendering correctly on each browser. I have used this feature to drill down into the various types of information available and it is all working as intended. 

**10. Contact Us Page**
* When a none logged in user goes to the contact us page the page is displaying as it should for a none logged in user. The message about the priority message service being only available to logged in users is displaying correctly. 
* When a logged in user goes to the contact us page the contact us form is rendering as expected on all browsers. 

Error Detected!
* When a logged in user goes to the contact us page on Firefox, the username field that automatically generates the username has a grey background, this is only happening on Firefox and not on the other browsers (Screenshot below:)   

![Image of contact us form greyed out](media/readme_images/firefox_contact_us_field.png)

I have resolved this with the following css:<br><br>
`.user-input-display {`<br>
  `background: transparent;`<br>
`}`

* The user input field now has a white background like the rest of the browsers. 

* I have tested sending a message via the priority email messaging service on the contact us page and the message successfully goes through and is appearing in the Django admin panel as expected. 

<hr>

#### **2.1 Manual testing mobile** ####
<br>

To reduce repetition of the desktop results, for the mobile testing i have just highlighted the different functionalities that mobile users may experience while using the site on a mobile device. I have carried out all of the exact same manual tests on mobile devices as i did on the desktop however unless highlighted below, readers of this document can know i experienced the exact same outcomes on mobile devices as i did on desktop.  

Mobile testing was carried out on the following devices:<br>
1. iPhone 6/7/8 (Via Chrome Dev Tools)
2. iPad (Via Chrome Dev Tools)
3. Huawei P20 lite
4. Huawei P smart
5. Chuwi h9 pro tablet 

All mobile testing was carried out on Chrome, FireFox, Opera and Brave browsers.

Error Found - Several Pages:
* On some of the pages on the site (Login, Sign up, Products, About us page image) the content of that page was sitting right at the very bottom of the screen on tablet devices when the tablet was held horizontally. Items such as buttons, text and images were touching the very bottom of the tablet screen which doesn't give a good user experience and it made the pages look poor.  

Solution:
On pages where i have encountered this issue i have added a `<br>` element at the very bottom of the code on each of the pages. Now when i reload the page there is an extra row of whitespace at he bottom which has rectified the issue. 

**1. The Home Page**

* Apart from the issue highlighted above all tests on mobile devices returned the same results as the desktop results listed above. The page is functioning normally and as intended on mobile devices. 

**2. The My Account, Profile & Cart**

* Apart from the issue highlighted above all tests on mobile devices returned the same results as the desktop results listed above. The page is functioning normally and as intended on mobile devices. 

**3. The Products Page**

* Apart from the issue highlighted above all tests on mobile devices returned the same results as the desktop results listed above. The page is functioning normally and as intended on mobile devices. 

**4. The Product Details Page**

* The page is functioning normally and as intended on mobile devices. 

**5. The Cart Page**

* The page is functioning normally and as intended on mobile devices. 

**6. The Checkout Page**

* The page is functioning normally and as intended on mobile devices. 
* One thing to note is on Google Chrome when the user clicks on the credit card details input field to enter their card number, the browser will automatically zoom into that field to help make entering the card details easier. When the user presses the button to complete the purchase they wont see the payment processing spinner. The processing spinner is still there and is still being generated correctly, whats happening is if the user doesn't zoom back out after entering their credit card details when they press the button to complete the transaction the screen will stay zoomed in on the bottom corner. 

**7. The Order Confirmation Page**

* The page is functioning normally and as intended on mobile devices. 

**8. About Us Page**

* Apart from the issue highlighted above all tests on mobile devices returned the same results as the desktop results listed above. The page is functioning normally and as intended on mobile devices. 

**9. Covid Numbers Page**

* The page is functioning normally and as intended on mobile devices. 

**10. Contact Us Page**

* The page is functioning normally and as intended on mobile devices. 

</details>
<hr>

<details>
<summary><strong>
3. Responsiveness
</strong></summary>
<br>

* 3.1 Chrome Dev Tools
* 3.2 Responsive Design Checker
</details>
<hr>

<details>
<summary><strong>
4. Console Testing
</details>
<hr>