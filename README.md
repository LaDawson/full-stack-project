# The Coding Pen

The Coding Pen is a freelancer website that enables people to hire a full-stack web developer.
The aim is to provide a site where users can place an can set up a consultation in order to receive
infomation and guidance from a full-stack developer. This site is intended to simplify the process of
finding a developer as most of the sites I have visited in the past often give a list of different developers
that you have to contact individually. 

The users can easily contact a developer on this site through a simple yet neatly laid out form which will then
put the user in to contact with the developer either by email or phone for further discussion about the consultation.
The website is for anybody that is looking for a web developer but doesn't have much knowledge on the subject.

## User Experience

This website is intended for people that do not have much knowledge on web development and either would like advice
to point them in the right direction, or would like to book a consultation to start the development of their ideal
website.

* The website should be responsive to user actions.
* As a user I would like a navigation bar so that I can easily reach different pages of the webiste.
* As a user I would like the links and forms to respond to my click.
* As a user I would like to be notified about what I am doing on the site.
* As a user I would like to be able to easily fill out a consulation form.
* As a user I would like the option to register and log in to an account I had already created to be able to place a consultation order.
* As a user I would like feedback when I fill a form incorrectly.
* As a user I would like visual indication on which buttons/links I am about to press.
* As a user I would like to see my order history.
* As a user I would like feedback to know when my consultation was successfull.
* As a user I would like a secure payment method to know my details are safe.

## Existing Features

### Navigation:
There is a navigation bar on the desktop version and a navigation menu which expands when clicked on
mobile devices. This provides the user with links to all of the available pages to them. When clicked
the user will be taken to the corresponding page.

### Registering and loging in/out of an account:
You have the option to sign up to the website. This is provided by Allauth which enables the user to 
easily register, login and logout to the site. The user must have an account and be logged in to be able
to access and complete the consultation form. This is to ensure that the user can always see their order
history through their profile so that in the even the user loses the confirmation email they will always
have a copy of it stored on the site. Also the next time they place a consultation order, the form will autofill
with the default information of the user to make the process quicker.

### The option to fill out a consultation:
If you are logged in, you will be able to access the consultation page. Once all of the options on the
form are filled in then you can submit the consultation. You will then be redirected to a confirmation page
which will display your order and let you know that the form was submitted successfully. You will also be sent
a confirmation email with the same information so that you can keep a copy of the order if needed.

### To be notified when a form is not correctly filled in:
If an input is required on a form there will be an indication to the user if it is not filled correctly or at all.
For the registration/login forms Allauth handles all of the notifications which will appear on the form if the inputs
are not correct when the user attempts to submit the form. For the consultation form, not only will you receive notifications
for the inputs that are incorrect, the inputs will also turn red to indicate if there is an empty field on the form when the user
attempts to submit it.

### Responsive navigation bar:
The navigation bar/menu for mobile changes depending on whether you are logged in or not, and also if you are an admin. 
This is done by using if statements in the html.

If you are not logged in you will have the options of:
* "Home", which links to the home page.
* "About", which will take you to a page which has information about the web developer.
* "Consultation", which will take you to a login page if you are not logged in and then to the consultation page once logged in.
* "Account", which is a dropdown with the option to register an account or to login.

If you are logged in as a user you have the options of:
* "Home", which links to the home page.
* "About", which will take you to a page which has information about the web developer.
* "Consultation", which will take you to the consultation page.
* "Account", which is a dropdown with the option to either visit your profile, or to logout.

If you are logged in as an admin you have the options of:
* "Home", which links to the home page.
* "About", which will take you to a page which has information about the web developer.
* "Consultation", which will take you to the consultation page.
* "Admin", which will take you to the admin page.
* "Account", which is a dropdown with the option to either visit your profile, or to logout.

### Website notifications:
The website currently features notifications so that the user receives feedback about what they are doing.
The notfications let the user know whether what they tried to do was successful, for example if their login was successful,
or whether there was an error. This helps as it easily displays to the user what has happened in the form of an easily dismissible
message in the top right of the website.

### The ability to see order history:
The fact that the user has to have an account and be logged in to place an order allows the ability to store their order history.
When a consultation is placed, it is linked to the user profile. The user can then see their order history in the profile page.
The user can also click on the order number to be redirected to a copy of the order confirmation. 

### To see if the consultation was successful:
Once the consultation form is submitted, the user will know if it is successfull or not by whether they are taken to the confirmation page.
If it is successful, not only will the user be taken to the confirmation page, a notification will pop up to inform them that it was successful.
If the payment failed, the user will receive an error message to let them know that it was not successful.

### A secure payment method:
The payment system used is Stripe. Stripe is a payment platform, like Paypal, which allows secure transactions to occur.
None of the users card details are stored on the site so that none of their data is at risk.

### Emails:
Currently the website is using django mail to send confirmation/verification emails to the user and the admin. 
This is to aid in the registration of the users and also to make sure that they have a copy of their order as proof of purchase.

### Mobile device styles:
The desktop and mobile devices have different layouts.
The nav bar on mobile devices with small screens is a collapsable navigation bar, which once the dropdown is pressed will reveal the same
options as the usual navigation bar.
On smaller screens the background is faded to make the text more visible on the home screen.
On smaller screens the about page is organised differently so that all of the information is easily displayed.
On smaller screens, the forms that are provided are altered so that the information is always readable and so that the forms are not squashed.

## Features to implement in the future:

### A contact form:
Currently the only way to contact me if there are any issues is by using the email address provided in the about page. I would like
to add an email app which will consist of a form which the user can fill in similarly to the consultation form. This form will not 
come with a charge so that the user can easily contact me for free. I could then either have this form either send an email to myself
or have a section on the admin page so that I can see all of the forms that are submitted through this method.

### A search bar:
If a user places a lot of orders through my site then the order history will fill up. Currently there is a scroll bar which appears
when the order history reaches a certain size, which allows the user to scroll through all of their orders. I would like to implement
a search bar so the user can filter the orders by order number or date so they can find specific orders faster.

### A better admin interface:
Currently the admin interface is very simple, it just lists all of the consultations that have been submitted in a similar fashion to
the user profile order history section. This just allows the admin to safely store all confirmations in case the initial emails are lost.
I would like to implement features that will allow the admin to mark whether the consultations are in progress or whether they are already complete.
This will allow the admin to quickly filter through the new orders and old orders.

## References/Technologies used:

### Django
I used Django to help develop the entire site and cut down the development time.

### Bootstrap: https://getbootstrap.com/
I used Bootstrap as the main framework for my website, it provided the website structure and layout. Also, it was used
it was used to help the styling of the forms, nav bar and footer. I also used a base template provided by bootstrap to 
quickly set up the base.html template, which I then customized. I used bootstrap for the basic tables, buttons and the progress
bars also.

### Google Fonts: https://fonts.google.com/ 
This was used for the font of the text and titles.

### jQuery: jQuery: https://jquery.com/
To help with manipulation of the DOM and Materialize requiered jQuery for some of the html elements to work.

### Google Developer Tools: 
This was used to test the website and find bugs.

### W3Schools: https://www.w3schools.com/cssref/css_colors.asp
This helped to choose the colors for my css.

### Stripe: https://stripe.com/en-gb
This is the payment system that I use within my website. A lot of the code for the Stripe system came from
their website, the rest was written with the help of the Code Institute.

### Allauth:
Allauth is provided by django, which deals with the registration, logins and logout functions for the user.

### Home page background image
https://pixabay.com/photos/desktop-desk-iphone-workplace-1155613/


I also used parts of the Code Institutes lessons in my work where I struggled to make my versions work correctly, such as the backend for the stripe
payment system and user profiles.


## Testing:

### Navigation Bar Sizing:
1. Change the screen size, when on smaller screens it should become a collapsable navigation bar.

### Admin Login:
1. If logged in, verify that you have the option to fill out the consultation form, logout and to visit the admin and profile pages.
2. If logged in, verify that the sign up and login links disappear.

### User Login:
1. If logged in, verify that you have the option to fill out the consultation form, logout and to visit the profile page.
2. If logged in, verify that the sign up and login links disappear.

### Navigation Bar Desktop:
1. Click the "home" link, it should take you to the home page.
2. Click the "consultation" link, if logged in it should take you to the consultation page, if not logged in it should take you to a login page, and then to the consultation page once logged in.
3. click the "login" link, it should take you to the login page.
4. click the "logout" link (if logged in), it should log you out and take you to the home page.
5. click the "admin" link (if admin), it should take you to the admin page.
6. click the "sign up" link, it should take you to the sign up page.
8. Click the "The Coding Pen" title or the logo, it should link to the home page.

### Navigation Mobile Menu:
1. Click the menu icon, it should bring out the overlay with the same links as the desktop view.
2. On small screen sizes the title should move to the center of the navigation bar.
3. On extra small screens the logo should be no longer visible and the title should move back to the left.

### Footer:
1. Click the "The Coding Pen" text, it should take you to the home page.

### Home Page:
1. On smaller screens the background overlay should become visible which will add a white overlay to the image.
2. Click the learn more button, it should take you to the about page.

### Login Page:
1. Try submitting without username, it should notify that it needs to be filled.
2. Try submitting without password, it should notify that it needs to be filled.
3. Use and incorrect username or password, it should notify that the combination doesnt match.
4. Submit with the correct information, it should take you to the home page and create your session.

### Sign Up Page:
1. Try submitting without username, it should notify that it needs to be filled.
2. Try submitting without email, it should notify that it needs to be filled.
3. Try submitting without password, it should notify that it needs to be filled.
4. Try submitting without repeat password, it should notify that it needs to be filled.
5. Try submitting with a username already in use, it should notify that the username already exists.
6. Try submitted with an invalid email format, it should notify that it is invalid.
7. Try submitting when the 2 password fields are different, it should notify that they do not match.
8. Submit with the correct information, it should create your account then ask you to verify your account.
9. Once verified it should take you to the login page.

### Forgotten Password Page:
1. Enter your email and verify that it sends you an email.
2. Use the verification email and verify it takes you to a page to reset your password.
3. The passwords must match for the form to submit.
4. Once submitted, login with the new password to verify that it has successfully updated the password.

### Logout Page:
1. Try to logout, it should ask for confirmation.
2. If successful it should return you to the home page and you will no longer be able to access your profile.

### Admin Page:
1. Submit consultations from multiple test accounts and verify they all appear in the table on the admin page.
2. Click the order number and verify that you are taking to a confirmation page with the form filled out with the details submitted by the user.
3. Try to access the admin page whilst not logged in and verify that it takes you to the login page first.

### My Profile Page:
1. Submit a few test consultations and verify they appear in the order history table.
2. Click the order number and verify that you are taking to a confirmation page with the form filled out with the details submitted by the user.
3. Update the form data for default details and verify that when you visit the consultation page the form is filled with the same details.

### Consultation Page:
1. Try to submit the form with any of the fields empty, the fields should turn red and notify you that they are required.
2. Try to submit with no card details/incorrect details and you should get notified of the issue.
3. Verify that on smaller screens the input fields change to fill a larger width of the screen and no longer share a row.

### Notifications:
1. Login/register/logout and verify a notification pops up to tell you that it was successful.
2. Submit a consultation and verify a notification pops up to tell you that it was successful, if the form/payment fails then it will notify you of the failure.
3. Go to a past order from your profile and verify that it notifies you that it is a past order confirmation.

### Emails:
1. Register for an account and you should receive an email for verification.
2. Place a test order and verify both the admin and user receive confirmation emails.

### Progress Bars:
1. When the screen width is above 1000px, hover over the bars and they should change color to black.
This was not implemented in the mobile view as the padding/margin of other elements overlapped the progress bars so the hover function did not work.


## Bugs I Encountered:
Most of the small bugs I encountered were simple fixes to do with typos such as spelling mistakes or referencing wrong.
If I could not solve a bug by reading through my code I would try to use the google developer tools and the console to figure out where
an error was coming from. Most of the larger bugs I encountered were coming from the stripe payment system. I had a difficult time setting up
Stripe and the webhooks correctly so that not only a payment would be successful but the data would be saved from the form. These errors normally
occured in the views.py or my stripe javascript file due to me using the incorrect code for the most part. These issues were solved with the help 
of the tutors provided by the Code Institute and also by looking back on lessons to help understand the code needed for these areas and to walk me through
the process a couple more times.

A particular bug I encountered was that Stripe webhooks would return an error when submitting the form. This was because I was trying
to pass the user idea from the form as metadata. The idea was that the webhook would send this field as metadata so that the idea wouldn't
be lost if the confirmation email was lost. After a long chat with a tutor, it was decided upon removing this meta data as it was 
an unknown variable to stripe which was throwing an error. Instead I just kept the billing information within the stripe billing details.
The consultation idea is instead now sent through an email to the admin similarly to the way a confirmation email is sent to the user.

Another issue I had was that after I had deployed my site, I could not get the webhook to send the email confirmation. I spent hours looking through
my code and having talks with tutors about the different possible causes. Although there were a few errors with variable names within my settings and
webhooks this was not the cause. I had forgotten to create an endpoint on stripe for my deployed version of the site. Not only this but the config
variable on heroku was incorrect, which took me a while to figure out, but once these were corrected the emails were being sent fine.

The lessons in particular were a great reference point to help as this was the first time taking on a Django project of this scale on my own, which lead to me
getting confused and lost at particular parts that were new to me. Although I struggled through some parts, now that I have a better understanding of Django, and 
how to use it properly, it is easy to see how much more efficient it is to use Django for projects of this size rather than to write all of the code yourself.

## Directory Structure and File Naming:
All of the HTML pages are within a folder named "templates" and are named according to their function. The CSS files are put into
folders called "static" and then "css" folder, similarly javascript files are inside the "static" folder, but a "js" folder rather than "css".
This is because Django needs files in specific file locations in order to find them. It also helps with the organisation and keeping the directory 
neat so that it is easy to find files.

## Version Control:
I used Github to control versions of the code. I would push the code to the repository every time I made a significant change or fixed a bug.
This allowed me to have back ups of earlier code just incase I deleted a file in the local repository or made an error in new code I was writing.
I could go back to earlier versions if needed.

## Difference in deployed version and development version:
In the development version, DEBUG is set to true so that I could easily find errors in my code while developing. When I deployed the project I 
turned DEBUG off so that no information is leaked.
All of the environment variables such as secret keys are removed from the code, then changed and instead stored as a variable on Heroku. This is so
that people cannot see the keys and values for objects that might compromise security within the site/payment systems.
The development and deployed versions also have different locations for the static and media files. In development they are all stored by sqlite3
where as the deployed version has to retrieve the files from an AWS bucket which hosts the files.

## Deployment Process (GitHub):

First, create a repository in GitHub, then launch Gitpod through GitHub. 
This will make sure that the remote origin for the push to GitHub is already added – 
allowing you to push your files to your repository without having to add the remote origin manually. 
When the project is first started you need to create a local repository, this is where changes that are made locally are saved to. 
From this you push them to the repository that was created earlier, this is where all the versions that have been uploaded in the past 
and where the final webpage is saved. You can then access the code for each time you have pushed to this repository. To do this 
you have to use commands in the terminal of Gitpod.

1. Git init (to create the local repository).
2. Git status (to check which files are not tracked/have been changed or removed).
3. Git add “example.html” (to add the file to the repository).
4. Git commit -m “version name” (to save your changes to the local repository).
5. Git push (to upload the local repository to the remote repository on GitHub).

To run my code locally you can visit the website "https://github.com/LaDawson/full-stack-project" which takes you to the repository 
for my project. Here you will be able to see the latest version I have uploaded. The most recent version will be the first few files 
you can see, you can open these to see my code. There is also an option to download or clone my code. You can clone the repository
to GitHub Desktop by clicking the "Open in Desktop" button after clicking the "Clone or Download" button.

If you copy the link provided when you click the clone/download button, then follow these steps to run it locally:

Open Git Bash
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied.
Press enter and your local clone will be created.

## Deployment Process (Heroku):
To deploy to heroku you need the following files:
* requirements.txt - get this by typing "pip3 freeze --local > requirements.txt" into the terminal.
This is so that heroku can install the needed addons such as stripe in order to run the site.
* Procfile - This tells heroku to run a gunicorn server and then 
You will also need to add all of your config variables such as secret keys to the heroku app through the settings.

1. Create an app on Heroku
2. Type "heroku login -i" into the terminal
3. Enter your account details
4. Type "git init" into the terminal
5. Type "git remote add heroku "your Heroku git URL" (which you find in the heroku app settings) into the terminal
6. Type "git add ." into the terminal
7. Type "git commit -m "Version Name"" into the terminal
8. Type "git push heroku master" to push the commit to heroku so it can start building the app.

Currently I am using AWS to host my static files and media files in a bucket. This is because Heroku cannot
store media files so you have to use an external site to host them.