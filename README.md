# The Work Workouts Business Project

## Basic Site Description

Welcome to Work Workouts health and fitness site!
We specialize on giving companies and organisation the opportunity to experience
our world class workout session.
There is never a dull moment here at the state of the art gym with everything from
spinning, boxing, weight lifting gym and yoga session.

## Purpose of the Project / Business Model

The purpose of the this site is to make it easy for company owners/HR/health-organizers
working for companies or organisation to book group sessions for their employees.
It's a simple payment system ported from the stripe module, where we utilize the
once payment for X different workout sessions.
As a site/business owner we can easily access the backend to se orders and contact
constumers to book time and place.

Our business is a B2B based site where the main goal is to sell group sessions
to larger parties or businesses. Our main goal is to create lasting business relations
as this is the case our focus will be on relational selling points like togetherness,
group activities, team-building and long lasting health.
We're going to rely on the good word spreading from our first clients, and the importance
of open-for-everyone events outside of the business locals.

### **[Live Site](https://project-5-first-a9f5854c68ec.herokuapp.com/)**

---

### **[Repository](https://github.com/Rakdoslover/Project-5-first)**

---

### **[Facebook Page](https://www.facebook.com/profile.php?id=100095114092579)**
[Facebook page picture](/media/work-fb.jpg)

## Table of contents

<a name="tcontents">Back to Top</a>

1.  [ UX ](#ux)
2.  [ User Stories ](#userstories)
3.  [ Features ](#features)
4.  [ Technology Used ](#tech)
5.  [ Testing ](#testing)
6.  [ Screenshots ](#screenshots)
7.  [ Facebook Profile ](#fbprofile)
8.  [ Future Implemetations ](#future)
9.  [ Content ](#content)
10. [ Credits](#credits)
11. [ Acknowledgements](#acknowledgements)

## UX

<a name="ux"></a>

![Lucid Chart](/media/database-structure.jpg)

### Database Structure

#### UserProfile

| id                      | Field         |
| ----------------------- | ------------- |
| user                    | OneToOneField |
| default_phone_number    | Charfield     |
| default_street_address1 | Charfield     |
| default_street_address2 | Charfield     |
| default_town_or_city    | Charfield     |
| default_county          | Charfield     |
| default_postcode        | Charfield     |
| default_country         | CountryField  |

---

#### Order Model

| id              | Field         |
| --------------- | ------------- |
| order_number    | CharField     |
| user_profile    | Foreignkey    |
| full_name       | CharField     |
| email           | EmailField    |
| phone_number    | CharField     |
| country         | CountryField  |
| postcode        | CharField     |
| town_or_city    | CharField     |
| street_address1 | CharField     |
| street_address2 | CharField     |
| county          | CharField     |
| date            | DateTimeField |
| order_total     | DecimalField  |
| grand_total     | DecimalField  |
| original_bag    | TextField     |
| stripe_pid      | CharField     |

---

#### OrderLineItem Model

| id             | Field        |
| -------------- | ------------ |
| order          | ForeignKey   |
| workouts       | ForeignKey   |
| quantity       | IntegerField |
| lineitem_total | DecimalField |

---

#### Event Model

| id             | Field           |
| -------------- | --------------- |
| title          | CharField       |
| slug           | SlugField       |
| featured_image | CloudinaryField |
| excerpt        | TextField       |
| updated_on     | DateTimeField   |
| content        | TextField       |
| created_on     | DateTimeField   |
| date           | DateTimeField   |
| time           | TimeField       |
| location       | TextField       |

---

#### Instructor Model

| id                        | Field        |
| ------------------------- | ------------ |
| name                      | CharField    |
| sessions                  | TextField    |
| years_of_experience       | IntegerField |
| words_from_the_instructor | TextField    |
| image_url                 | URLField     |
| image                     | ImageField   |

---

#### Instructor Model

| id          | Field        |
| ----------- | ------------ |
| name        | CharField    |
| sku         | CharField    |
| description | TextField    |
| place       | DecimalField |
| instructors | TextField    |
| image_url   | URLField     |
| image       | ImageField   |

---

[Back to Top of page](#tcontents)

---

## User Stories and Project

<a name="userstories"></a>

### Goal

---

The main goal for this project is to create a user friendly site with simple navbar
and a place for businesses to purchase workout sessions.
The users/customers are browsing the different types of sessions, our instructors
and upcoming events hosted by Work Workouts.
Users can choose a product/session, take it through to the bag and from there to
the checkout. If the user has a registered account they can then see their order
on their profile site.

### Agile Project

---

This project was started alongside a GitHub Projects Page to track issues that I had to solve further on.
The initial aim was to track steps and features needed to get the functionallity and layout as per project goal.
I wrote epics with different themes according to what the user/admin wanted
to be able to do.

---

To see Kanban please click [here](https://github.com/users/Rakdoslover/projects/6)

### Deployment to Heroku
---
After the repository, Kanban board and workspace was up and running I started to connect it to Heroku.
Steps to deploy:
- Created a new app with the name of project-5-first.
- Connected my postgres database, Cloudinary, AWS keys, Stripe keys and secret key to the config vars.
- Added the Email host as a var for confirmation purposes.
- Put the DISABLE_COLLECTSTATIC to 1 until final depolyment.
- Assigned the port = 8000.
- Connected the repo to automatically deploy when commited to main branch.
- Set the debug to "DEBUG = 'DEVELOPMENT' in os.environ" and added correct code to my env.py to make sure the code when to debug and not.
- Updated the allowed hosts in settings to show both sites (live and in workspace).
- Started commiting to the repo and checking the live site with after each major update.
- At the end when i was happy with the finished product, I made sure to remove DISABLE_COLLECTSTATIC and published the site.

At some points I had to take a step back to redo certain bits and pieces, but I followed these steps to get the final version.

#### User stories

Down below you can find both the fulfilled stories but also those not completed.

##### Completed

1. [USER STORY: View and Bag Sessions (Must-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34566714)
2. [USER STORY: Admin Page (Must-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34561980)
3. [USER STORY: View Instructors (Should-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34566881)
4. [USER STORY: Upcoming Events (Should-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34567113)
5. [USER STORY: CRUD Sessions and Events (Must-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34567578)
6. [USER STORY: Admin Login Frontend (Must-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34568010)
7. [USER STORY: Create Account (Should-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34568128)
8. [USER STORY: Purchase Session (Must-Have)](https://github.com/users/Rakdoslover/projects/6/views/1?pane=issue&itemId=34568300)
9. [USER STORY: View Comments]()

##### Uncompleted

1. [USER STORY: Booking system for events]()

[Back to Top of page](#tcontents)

---

## Features

<a name="features"></a>

#### Users can:

- **Users can** create an account (**Create**)
- **Users can** log into their account
- **Users can** log out of their account
- **Users can** browse our sessions, instructors and events **(Read)**
- **Users can** view specific sessions and events **(Read)**
- **Users can** pick sessions and put in their bag 
- **Users can** edit their bag contents (**Update**)
- **Users can** delete their own bag contents (**Delete**)
- **Users can** take the bag contents through to the checkout app
- **Users can** fill out a contactform and preview the sub/grand total of the items
- **Users can** go back and not finish the purchase
- **Users can** take the purchase through and get a confirmation email/order update on their profile page
- **Users can** view and update their profile page (**Read and Update**)

#### User cannot:

- **Users cannot** create, update and delete sessions/instructors/events they didn't create.
- **Users cannot** access the admin panel of the website unless they have admin status.

#### Website Features

##### Our Sessions page

- Sessions are published on the page and can be accessed both from the home page and from the navbar.
- Sessions are detailed on both the outer layer and the inner layer.
- User are able to click the session in question to get a detailed page.

##### Session Detail page

- Users are able to read the information published for the session.
- Users are able to choose an amount of sessions they would like and put them in their bag.

##### Instructors page

- Users are able to read information about our instructors.

##### Events page

- Events are ordered in the newest to oldest.
- Users can see basic information about each event up front.
- Users can click the event they're interested in and get to the detailed page.

##### Event Detail page

- Users can read the full information about the event.
- There is no signup/book section as of yet.

[Back to Top of page](#tcontents)

---

## Technology Used

<a name="tech"></a>

---

### Html

- Used to structure my webpages and the base templating language.

### CSS

- Custom CSS was written on bits to make it stick out but played a background role over functionality.

### Python

- Used for the logic in this project.

### Django

- Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Bootstrap 5

- Used as the base front end framework to work alongside Django.

### Allauth

- To implement quick and easy user registration and login, modified after implemetations

### GitHub

- Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku

- Used to host and deploy this project.

### ElephanSQL

- Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary

- Used to host the static files for this project including users featured images.

### Git

- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

### Lucidcharts

- Used for to visulize the database structure.

### AWS

- Used to store the staicfiles and media.

[Back to Top of page](#tcontents)

---

## Testing

<a name="testing"></a>

Tested the site on Google Chrome and Microsoft Edge, both of them worked the same
with the tests provided below.

### Main Site Testing

| **TESTING**             | **ACTION**                                        | **EXPECTATION**                             | **RESULT**        |
| ----------------------- | ------------------------------------------------- | ------------------------------------------- | ----------------- |
| Home Page               | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Home Page               | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Login form              | Click "Signin" button without data in form fields | Cannot submit form                          | Works as expected |
| Logout form             | Click "Signout" button                            | Submits form and logs out user              | Works as expected |
| Signup form             | Click "Signup" button without data in form fields | Cannot submit form                          | Works as expected |
| Nav bar - home page     | Click home button                                 | Home button takes me to the home page       | Works as expected |
| Nav bar - register page | Click register button                             | Register button takes me to the signup page | Works as expected |
| Nav bar - login page    | Click login button                                | Login button takes me to the signin page    | Works as expected |
| Nav bar - logout page   | Click logout button                               | Logout button takes me to the signout page  | Works as expected |
| Our Sessions Page       | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Our Sessions Page       | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Session Detail Page     | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Session Detail Page     | Size to 1920px using Chrome Dev Tools             | Elements look good @ 320px                  | Works as expected |
| Instructors Page        | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Instructors Page        | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Events Page             | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Events Page             | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Event Detail Page       | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Event Detail Page       | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Bag Page                | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Bag Page                | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Checkout Page           | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Checkout Page           | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Profile Page            | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Profile Page            | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Login Page              | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Login Page              | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Signup Page             | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Signup Page             | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |
| Logout Page             | Size to 320px using Chrome Dev Tools              | Elements look good @ 320px                  | Works as expected |
| Logout Page             | Size to 1920px using Chrome Dev Tools             | Elements look good @ 1920px                 | Works as expected |

### Account Registration

| Test                        | Result |
| --------------------------- | ------ |
| User can create account     | Pass   |
| User can log into account   | Pass   |
| User can log out of account | Pass   |

---

### Sessions

| Test                                                           | Result |
| -------------------------------------------------------------- | ------ |
| User can read all session available on the site                | Pass   |
| User can click the session to get into the session details     | Pass   |
| User can choose an amount and put in their bag                 | Pass   |

---

### Nav Bar

| Test                                                                       | Result |
| -------------------------------------------------------------------------- | ------ |
| Users can engage with the nav bar on the home page                         | Pass   |
| Users can engage with the nav bar on each of the login/logout/signup pages | Pass   |
| Users can engage with the nav bar on the Our Sessions pages                | Pass   |
| Users can engage with the nav bar on the Instructors page                  | Pass   |
| Users can engage with the nav bar on the Events pages                      | Pass   |
| Users can engage with the nav bar on the Bag page                          | Pass   |
| Users can engage with the nav bar on the Checkout page                     | Pass   |

---

### View/Update Bag Contents

| Test                                                   | Result |
| ------------------------------------------------------ | ------ |
| Users can click on the bag icon to see their bag       | Pass   |
| Users can see each item row by row                     | Pass   |
| Users can update and remove items from the bag         | Pass   |

---

### Checkout

| Test                                                                  | Result |
| --------------------------------------------------------------------- | ------ |
| Users can take their bag through to the checkout app                  | Pass   |
| Users can fill out a contact form and see their sub/grand total       | Pass   |
| Users can fulfill the payment and get a confirmation email/order      | Pass   |
| If logged in, the user gets the order info assigned to their profile  | Pass   |

---

#### Admin Tests

| Test                                                         | Result |
| --------------------------------------------------------------- | ------ |
| Admin can add sessions from adminpanel                          | Pass   |
| Admin can add instructors from adminpanel                       | Pass   |
| Admin can add events from adminpanel                            | Pass   |
| Admin can update sessions from adminpanel                       | Pass   |
| Admin can update instructors from adminpanel                    | Pass   |
| Admin can update events from adminpanel                         | Pass   |
| Admin can delete sessions from adminpanel                       | Pass   |
| Admin can delete instructors from adminpanel                    | Pass   |
| Admin can delete events from adminpanel                         | Pass   |
| Admin can create/update/delete user profiles from adminpanel    | Pass   |
| Admin can create/update/delete user purchases from adminpanel   | Pass   |
| Admin can create/update/delete sessions from Frontend           | Pass   |
| Admin can create/update/delete events from Frontend             | Pass   |

---

### Validators

#### HTML

- [W3C HTML Validator](https://validator.w3.org/)
  - Checked all HTML-fiels checked.
  - Had minor errors mostly called by the django templating inside the HTML.
    - The remaining validation issues are all attributed to Django Templating not being recognized by W3C:
      - **Warning**: Consider adding a `lang` attribute to the `html` start tag to declare the language of this document
      - **Error**: Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
      - **Warning**: This document appears to be written in English. Consider adding `lang="en"` (or variant) to the `html` start tag
      - **Error**: Element `head` is missing a required instance of child element `title`

#### CSS

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri)
  - No errors found.

#### Pip8 Validation

- [CI Python Linter](https://pep8ci.herokuapp.com/)

##### Project Five App

- [settings.py](/media/settings.jpg)
- [urls.py](/media/main-urls.jpg)
- The settings still shows 4 lines that're too long. These will not be correct due to them being installed/written by DJango.

##### Bag App

- [context.py](/media/bag-contexts.jpg)
- [urls.py](/media/bag-urls.jpg)
- [views.py](/media/bag-views.jpg)
- No errors found

##### Checkout App

- [forms.py](/media/checkout-forms.jpg)
- [models.py](/media/checkout-models.jpg)
- [urls.py](/media/checkout-urls.jpg)
- [views.py](/media/checkout-views.jpg)

##### Events App

- [forms.py](/media/events-forms.jpg)
- [models.py](/media/events-models.jpg)
- [urls.py](/media/events-urls.jpg)
- [views.py](/media/events-views.jpg)

##### Home App

- [urls.py](/media/home-urls.jpg)
- [views.py]()

##### Instructors App

- [models.py](/media/instructors-models.jpg)
- [urls.py](/media/instructors-urls.jpg)
- [views.py](/media/instructors-views.jpg)

##### Profiles App

- [forms.py](/media/profiles-forms.jpg)
- [models.py](/media/profiles-models.jpg)
- [urls.py](/media/profiles-urls.jpg)
- [views.py](/media/profiles-views.jpg)

##### Workouts App

- [forms.py](/media/workouts-forms.jpg)
- [models.py](/media/workouts-models.jpg)
- [urls.py](/media/workouts-urls.jpg)
- [views.py](/media/workouts-views.jpg)
- No errors in code except settings.

[Back to Top of page](#tcontents)

---

## Screenshots

<a name="screenshots"></a>

---

#### Home Page

---

Main page of my site, this is where we draw our users attention.
Here we can see the navbar with it's few but simple options(our sessions, instructors & events).
A large hero-image takes up the rest of the page.
![Home Page](/media/main-page.jpg)

##### Responsiveness Home Page

---

And here we have it opened and scaled down to 320px width.
The navbar is opened to show how it looks downscaled.
![Home Page 320px](/media/main-page-320.jpg)

#### Our Sessions page

---

The our sessions page is the equivalent of the "products" page in the walkthrough
we did for Boutique Ado. It showcases the different sessions the customer can 
choose from.
![Our Sessions](/media/our-sessions.jpg)

##### Responsiveness Our Sessions Page

---

And here we have it opened and scaled down to 320px width.
![Our Sessions 320px](/media/our-sessions-320.jpg)

#### Session Detail page

---

Here we have the details page, where the customer can choose the amount of sessions
he/she wants to buy. 
![Session Detail Page](/media/session-detail.jpg)

##### Responsiveness Session Detail Page

---

And here we have it opened and scaled down to 320px width.
![Session Detail Page 320px](/media/session-detail-320.jpg)

#### Instructors Page

---

This is the instructors page showcasing our instructors.
An info page, describing every instructors skillset and a word of encouragement.
![Instructors Page](/media/instructors.jpg)

##### Responsiveness Instructors Page

---

And here we have it opened and scaled down to 320px width.
![Instructors Page 320px](/media/instructors-320.jpg)

#### Events Page

---

On the events page the customers can see our future events.
By pressing the event the can get to a more detailed page.
![Events Page](/media/events.jpg)

#### Responsiveness Events Page

---

And here we have it opened and scaled down to 320px width.
![Events Page 320px](/media/events-320.jpg)

##### Event Detail Page

---

This is the page where the customer/site-visitors can see more information on the chosen event.
![Event Detail Page](/media/event-detail.jpg)

##### Event Detail Page

---

And here we have it opened and scaled down to 320px width.
![Event Detail Page 320px](/media/event-detail-320.jpg)

#### Bag Page

---

This is the Bag page where the user can see their chosen items.
They can see a subtotal of each item, they can see a grand total, the can update
and remove items and take the bag through a purchase.
![Bag Page](/media/bag.jpg)

##### Responsiveness Bag Page

---

And here we have it opened and scaled down to 320px width.
![Bag Page 320px](/media/bag-320.jpg)

#### Checkout Page

---

This is the Checkout page, the last step the user takes before getting their sessions.
I've provided an upper and lower picture to get the whole thing.
![Checkout Page Upper](/media/checkout-upper.jpg)
![Checkout Page Lower](/media/checkout-lower.jpg)

##### Responsiveness Checkout Page

---

And here we have it opened and scaled down to 320px width.
![Checkout Page 320px](/media/checkout-320.jpg)

[Back to Top of page](#tcontents)

---

## Facebook Profile

<a name="fbprofile"></a>

Here we have the Facebook page for the Work Workouts.
On this page customer/visitors/fellow enthusiasts can see the basic info of from our main
site, like different sessions provided, some info on our gym and future events.
![Facebook Profile]()

[Back to Top of page](#tcontents)

---

## Future Implementations

<a name="future"></a>

---

<strong>1. Booking System for events:</strong>
We would like to implement a booking system where you can book your group/
colleagues directly onto the event you guys want to partake in.

This can be done with a similar purchase system as on the sessions page but when
you fill in the number of attendees you can see how many spots are left.

<strong>2. Customer Interaction</strong>
Another thing we're looking into is getting an interaction wall, like a bulletin board
where our customers can post their experiences and pictures from their own sessions.

This can be done with a comment system like a flow or review cards popping up randomly
from time to time.
This can also be done under each kind of session, like a rating system. Although,
if you're posting under an individual session you need to first press each session
to access peoples general thoughts.
We'll have to think a little more on this one.

<strong>3. Chat/Contact Function</strong>
This is the next step after the bulletin board to integrate some sort of chat function,
either we us as instructor/admins or with customer service.

Which direction we're going here depends on how the first interaction goes.


### Problems/Errors left

#### Disclaimer:

There are 4 errors indicating lines that're too long in my settings.py file,
I've intentionally left them in because they were created when django was
installed on the system. I've tried moving them but only gotten more errors.

<strong>Problem 1: Static Files on deployed site Remains</strong>

In the eleventh hour something happened to the files on the site and I lost all contact with them.
On the deployed stie it only show the bare minimals right now, I'm working with this one up until the submission moment.


[Back to Top of page](#tcontents)

---

## Content

<a name="content"></a>

##### Django Documentation

- Read through the django documentation multiple times to get to grips with the basics regarding models.

##### Geeks for Geeks.com

- Used their walkthroughs and tips to get the CRUD just right for the sessions/events CRUD by admin.

##### Stackoverflow

- I've read an ocean of questions and answers on Stackoverflow, some helpful some worthless.
  But when they actually helped me it really did the job.

##### W3 Schools

- Used for reference throughout for simple HTML/CSS examples.

##### Code Institute

- Course content for portfolio project 4 helped greatly in being able to complete this project.
- Initial structure **based heavily** on the CI walkthrough of the "Boutique Ado".
- Legacy code regarding Base/index.html and accompaning CSS remains.

[Back to Top of page](#tcontents)

---

## Credits

<a name="credits"></a>

##### Code institue Boutique Ado

- I started the project using the boutique template from https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/c82c677a83756a84c24181ed124e50ad38de67cf
- This gave me a guide how to develop the project, install all parts and deploy to Heroku.
- It also gave me the starting baseline for my inital CSS/settings/url/models/Base and Index template/admin and start view functions.
- I copied and used the Allauth templates for sign-up/-in/-out, these were not the main focus of my site this time around.
- This allowed me to test with trial and error (with django documentations and stackoverflow as my handbook).

##### Mentoring

- I had a couple of down periods during this project and had a really hard time grasping exactly what I need, but my mentor allways pushed onwards.
- She had some really cool ideas, tip and tricks for me to test, that includes documentation to read or videos to watch.

##### Tutor sessions

- Those hard hours were made so much easier by the giant help of the tutors.
- They've giving me alot of different ways to look at an issue and maybe getting it to work another way.

##### Various old students README-files

- I've gotten some great tips from former students/lecturers on how to write the README.
- They gave both tips on the structure but also the contents.

[Back to Top of page](#tcontents)

## Acknowledgements

<a name="acknowledgements"></a>

### My family

- I haven't been very chearful the last couple of weeks but my family has allways managed to put a smile on my face during the hardest hours.

[Back to Top of page](#tcontents)

## Resources

<a name="resources"></a>

#### Django documentation

So for this project I've leaned on the documentation quite heavliy, I've tried to go a little more "solo" from the the walkthroughs we've done so far, so to lean on the documentation have been a savior.

#### Free Stock images

Used to following sites to get some stock images for my pages:

- [Stockvault.net](https://www.stockvault.net/)
- [Unsplash.com](https://unsplash.com/)

[Back to Top of page](#tcontents)

---
