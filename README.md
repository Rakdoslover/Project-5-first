# The Work Workouts project

## Basic Site Description

Welcome to Work Workouts health and fitness site!
We specialize on giving companies and organisation the opportunity to experience
our world class workout session.
There is never a dull moment here at the state of the art gym with everything from
spinning, boxing, weight lifting gym and yoga session.

## Purpose of the Project

The purpose of the this site is to make it easy for company owners/HR/health-organizers
working for companies or organisation to book group sessions for their employees.
It's a simple payment system ported from the stripe module, where we utilize the
once payment for X different workout sessions.
As a site/business owner we can easily access the backend to se orders and contact
constumers to book time and place.

### **[Live Site](https://project-5-first-a9f5854c68ec.herokuapp.com/)**

---

### **[Repository](https://github.com/Rakdoslover/Project-5-first)**

---
## Table of contents
<a name="tcontents">Back to Top</a>
 1. [ UX ](#ux)
 2. [ User Stories ](#userstories)
 3. [ Features ](#features)
 4. [ Technology Used ](#tech)  
 5. [ Testing ](#testing)   
 6. [ Screenshots ](#screenshots) 
 7. [ Future Implemetations ](#future)  
 8. [ Content ](#content)  
 9. [ Credits](#credits) 
 10. [ Acknowledgements](#acknowledgements)

## UX
<a name="ux"></a>

![Lucid Chart](/media/database-structure.jpg)

### Database Structure
#### UserProfile

| id | Field |
|--|--|
| user | OneToOneField |
| default_phone_number | Charfield |
| default_street_address1 | Charfield |
| default_street_address2 | Charfield |
| default_town_or_city | Charfield |
| default_county | Charfield |
| default_postcode | Charfield |
| default_country | CountryField |

---

#### Order Model

| id | Field |
|--|--|
| order_number | CharField |
| user_profile | Foreignkey |
| full_name | CharField |
| email | EmailField |
| phone_number | CharField |
| country | CountryField |
| postcode | CharField |
| town_or_city | CharField |
| street_address1 | CharField |
| street_address2 | CharField |
| county | CharField |
| date | DateTimeField |
| order_total | DecimalField |
| grand_total | DecimalField |
| original_bag | TextField |
| stripe_pid | CharField |

---

#### OrderLineItem Model

| id | Field |
|--|--|
| order | ForeignKey |
| workouts | ForeignKey |
| quantity | IntegerField |
| lineitem_total | DecimalField |

---

#### Event Model

| id | Field |
|--|--|
| title | CharField |
| slug | SlugField |
| featured_image | CloudinaryField |
| excerpt | TextField |
| updated_on | DateTimeField |
| content | TextField |
| created_on | DateTimeField |
| date | DateTimeField |
| time | TimeField |
| location | TextField |

---

#### Instructor Model

| id | Field |
|--|--|
| name | CharField |
| sessions | TextField |
| years_of_experience | IntegerField |
| words_from_the_instructor | TextField |
| image_url | URLField |
| image | ImageField |

---

#### Instructor Model

| id | Field |
|--|--|
| name | CharField |
| sku | CharField |
| description | TextField |
| place | DecimalField |
| instructors | TextField |
| image_url | URLField |
| image | ImageField |

---


[Back to Top of page](#tcontents)

---

## User Stories and Project
<a name="userstories"></a>

### Goal
---
The main goal for this project is to create a user friendly site with a simple
authentication login/signup and a place interactive storytelling platform.
Users are supposed to read the chapters published and dependeing on the theme of
the story post a comment with a proposed title and a featured image with connections
to the them of the text.
The comments are, if you're authorized and logged in, CRUD friendly.

### Agile Project
---
This project was started alongside a GitHub Projects Page to track issues that I had to solve further on.
The initial aim was to track steps and features needed to get the functionallity and layout as per project goal. 
I wrote epics with different themes according to what the user/admin/author wanted
to be able to do.

---
To see Kanban please click [here]()

I recognized 7 epics that would make the site work in the way I wanted and needed.
I also got 1 story I would like to have implemented but couldn't find time for.

For these 7, I made issues through the "project 4 story" Project on repository.
The plan was to make them all at first and cross them out as the project progressed,
but at times I got stuck on problems not forseen, which caused me to cross them off
a little more haphazardly.

#### User stories

Down below you can find both the fulfilled stories but also those not completed.

##### Completed

1. [USER STORY: Create Account]()
2. [USER STORY: Admin Page]()
3. [USER STORY: Site Pagination]()
4. [USER STORY: Create Comment]()
5. [USER STORY: Deploy the Site]()
6. [USER STORY: UD Comments]()
7. [USER STORY: View Comments]()

##### Uncompleted

1. [USER STORY: Rate Comments]()

[Back to Top of page](#tcontents)

---

## Features
<a name="features"></a>

#### Users can:

- **Users can** create an account (**Create**)
- **Users can** log into their account
- **Users can** log out of their account
- **Users can** create comment on chapter **(Create)**
- **Users can** read comments from other members *(**Read**)
- **Users can** view chapters from home page (**Read**)
- **Users can** edit their own comments (**Update**)
- **Users can** delete their own comments (**Delete**)
- **Users can** edit and delete others comments/chapters if they have superuser status through the adminpanel (**Update/Delete**)

#### User cannot:

- **Users cannot** post comments without an account or being logged in.
- **Users cannot** edit comments they've made previously without being logged in.
- **Users cannot** access the admin panel of the website unless they have admin status.
- **Users cannot** 

#### Website Features

##### Chapters on Home page

- Chapters are published in order of newest to oldest so that it's easy for members to find the newest chapter in the story.
- Chapters are paginated to a maximum of 6 per side to not fill up the whole screen with chapters.
- User are able to get a small excerpt of what the theme of the chapter is.

##### Chapter Detail page

- Users are able to read the published chapter on a separate page than the home screen.
- Users are able to comment, if authorized, and participate in the stories community.
- users can use CRUD to change what they already commented or delete it completely.

[Back to Top of page](#tcontents)

---


##  Technology Used
<a name="tech"></a>

---

### Html

 - Used to structure my webpages and the base templating language.

### CSS

 - Custom CSS was written on bits to make it stick out but played a background role over functionality.

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

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
- Used for to visulize the database structure


[Back to Top of page](#tcontents)

---

## Testing
<a name="testing"></a>

Tested the site on Google Chrome and Microsoft Edge, both of them worked the same
with the tests provided below.

### Main Site Testing
**TESTING** | **ACTION** | **EXPECTATION** | **RESULT**
----------|----------|----------|----------
Home Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Home Page	| Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Login form | Click "Signin" button without data in form fields | Cannot submit form | Works as expected
Logout form | Click "Signout" button | Submits form and logs out user | Works as expected
Signup form | Click "Signup" button without data in form fields | Cannot submit form | Works as expected
Nav bar - home page | Click home button | Home button takes me to the home page | Works as expected
Nav bar - register page | Click register button | Register button takes me to the signup page | Works as expected
Nav bar - login page | Click login button | Login button takes me to the signin page | Works as expected
Nav bar - logout page | Click logout button | Logout button takes me to the signout page | Works as expected
Chapter Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Chapter Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Login Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Login Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Signup Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Signup Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected
Logout Page   | Size to 320px using Chrome Dev Tools | Elements look good @ 320px | Works as expected
Logout Page   | Size to 1920px using Chrome Dev Tools | Elements look good @ 1920px | Works as expected

### Account Registration
| Test | Result |
|--|--|
| User can create account |Pass|
| User can log into account |Pass|
| User can log out of account |Pass|

---

### Chapter and Pagination 
| Test | Result |
|--|--|
| User can open each chapter paginated on the site |Pass|
| User can go back and forth between sites with Next/Prev-button |Pass|
| User can see chapters without being logged in |Pass|

---

### Nav Bar
| Test | Result |
|--|--|
| Users can engage with the nav bar on the home page | Pass |
| Users can engage with the nav bar on each of the login/logout/signup pages | Pass |
| Users can engage with the nav bar on the chapter detail page | Pass |

---

### Create Comment and Read Comments
| Test | Result |
|--|--|
| Authorized users can comment on a specific chapter | Pass |
| All users can read comments posted by authorized users | Pass |

---

### Update Comment and Delete Comment
| Test | Result |
|--|--|
| Authorized users can update a previously published comment they own | Pass |
| Authorized users can delete a previously published comment they own | Pass |

---

#### Admin Tests

| Test | Result  |
|--|--|
| Admin can add chapters from adminpanel |Pass|
| Admin can add comments from adminpanel |Pass|
| Admin can update chapters from adminpanel |Pass|
| Admin can update comments from adminpanel |Pass|
| Admin can delete chapters from adminpanel |Pass|
| Admin can delete comments from adminpanel |Pass|
| Admin can create/update/delete user profiles from adminpanel |Pass|

---

### Validators

#### HTML
- [W3C HTML Validator](https://validator.w3.org/)
    - Checked all HTML-fiels checked.
    - Had minor errors mostly called by the django templating inside the HTML.
        - Errors corrected by [commit: b15573e](https://github.com/Rakdoslover/project-4-story/commit/b15573e31dafd501b9720b6330692526b2dfd3d4)
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
Here we can see the navbar with it's few but simple options(home, login & register),
the latest chapters sorted by newest to oldest and at the bottom a small footer.
![Home Page](/media/pictures/home-page.jpg)
##### Responsiveness Home Page
---
And here we have it opened and scaled down to 320px width.
The navbar is opened to show how it looks downscaled.
![Home Page 320px](/media/pictures/home-page-320.jpg)

#### Register Page
---
The register/signup page is based on the Allauth templates with some modifications.
It should be simple and easy to use, user should be able to just register a
username and a password to get access to the comment section.
![Register Page](/media/pictures/register-page.jpg)

##### Responsiveness Register Page
---
And here we have it opened and scaled down to 320px width.
![Register Page 320px](/media/pictures/register-page-320.jpg)

#### Login page
---
This is the login page for the users.
A simple page that takes the user back to the home page after signing in.
![Login Page](/media/pictures/login-page.jpg)

#####  Responsiveness Login Page
---
And here we have it opened and scaled down to 320px width.
![Login Page 320px](/media/pictures/login-page-320.jpg)

#### Logout Page
---
This is the logout page for the users.
A simple page that takes the user back to the home page after signing out.
![Logout Page](/media/pictures/logout-page.jpg)

#####  Responsiveness Logout Page
---
And here we have it opened and scaled down to 320px width.
![Logout Page 320px](/media/pictures/logout-page-320.jpg)

#### Chapter Page (upper)
---
This is where most of the interaction happens.
The chosen chapter, published by the author, is being displayed and the user can
see the placeholder image from the author and the story down below.
![Chapter Page upper](/media/pictures/chapter-text.jpg)

#### Chapter Page (lower)
---
Further down below the users can interact by uploading a proposed new title for
this weeks chapter, and also upload an image symbolizing the story.
This is where they can make use of the CRUD functionality for real.
While logged in you can Create, Read, Update and Delete your own comments.
![Chapter Page lower](/media/pictures/chapter-comment.jpg)

##### Responsiveness Chapter Page
---
And here we have it opened and scaled down to 320px width.
![Chapter Page 320px](/media/pictures/chapter-320.jpg)

#### Update Page
---
This is the Update page where the user can change their previous entries.
After a valid new form has been submitted, the button will take them back to the site.
This fulfills the U in CRUD.
![Update Page](/media/pictures/update-page.jpg)

##### Responsiveness Update Page
---
And here we have it opened and scaled down to 320px width.
![Update Page 320px](/media/pictures/update-page-320.jpg)

#### Delete Page
---
This is the Delete page where the user can delete their own comment.
After the button is pressed, it will take them back to the site.
This fulfills the D in CRUD.
![Delete Page](/media/pictures/delete-page.jpg)

##### Responsiveness Delete Page
---
And here we have it opened and scaled down to 320px width.
![Delete Page 320px](/media/pictures/delete-page-320.jpg)

[Back to Top of page](#tcontents)

---

## Future Implementations
<a name="future"></a>

---

<strong>1. Poll:</strong>
The initial idea was to create a poll for the user to voted on 1 of 2 choices
the story would take, at the end of the week the author would pick the choice
with the most votes and for the next chapter he/she would write it accordingly.

I started implementing this idea but never got past an issue were users could
vote multiple times and also vote for both. This is something I would like to
implement in the future because I like the idea of the user pushing the story
forward together with the author.

<strong>2. Reaction instead of likes:</strong>
I would be cool if the user would be able to express more than just a like.
Lets say the theme of the chapter was happiness/success, the user could express
a happy face. the same would be true about a chapter which had a theme of
sorrow they could express a sad face.

This idea only came to the idea stage, I thought about it but never really
looked in to how I would implement it. Maybe it would be in the same manor as
the likes system we did in the walkthrough for the blog but I'm not sure.

<strong>3. Comment on comment:</strong>
Another cool thing for my users would be if they could comment each others
comment, and give likes to other peoples suggested titles and images.
This would create a deeper "community" interactivity between users.

Just like the idea number 2, this one was only just an idea. It's a cool system,
sort of like comment system found on most sites like 9gag, reddit, etc..
I might look into the further on but at the moment it would be out of the scope
for this portfolio project.

<strong>4. User costumization:</strong>
I would like the users to have a chance to customize their own profiles, lets
say we're going to add a smaller shop och subscription profile to the site, it
would be a good idea for the users to have more control over their own pages.

This one doesn't seem far off as I think I will be able to apply this soon after
the E-commerce section is done.

### Problems/Errors left

#### Disclaimer:

There are 5 error indicating lines that're too long in my settings.py file,
I've intentionally left them in because they were created when django was
installed on the system. I've tried moving them but only gotten more errors.

<strong>Problem 1: Remains</strong>
Through my whole development process I've had this issue with a class "Chapter"
that still says it contains no objects. I've tried my best can't seem to solve
this issue.

<strong>Problem 2: Resolved</strong>
For a long time I didn't understand how to get the files from allauth copied for
my workspace. This coupled with the fact that I copied them manually made it
impossible to redirect the right static to the files.
It took both help from tutors and the slack community to address the issue but
it was resolved at last.

[Back to Top of page](#tcontents)

---

## Content
<a name="content"></a>
  
##### Django Documentation
  - Read through the django documentation multiple times to get to grips with the basics regarding models.

##### Geeks for Geeks.com
  - Used their walkthroughs and tips to get the CRUD just right for the comments CRUD by user.

##### Stackoverflow
  - I've read an ocean of questions and answers on Stackoverflow, some helpful some worthless.
    But when they actually helped me it really did the job.
  
##### W3 Schools
  - Used for reference throughout for simple HTML/CSS examples.
  
##### Code Institute
  - Course content for portfolio project 4 helped greatly in being able to complete this project.
  - Initial structure **based heavily** on the CI walkthrough of the "I Think Therefore I Blog".
  - Legacy code regarding Base/index.html and accompaning CSS remains.

[Back to Top of page](#tcontents)

---

## Credits
<a name="credits"></a>

##### Code institue Django3blog
- I started the project using the blog template from https://github.com/Code-Institute-Solutions/Django3blog
- This gave me a guide how to develop the project, install all parts and deploy to Heroku.
- It also gave me the starting baseline for my inital CSS/settings/url/models/Base and Index template/admin and start view functions.
- I copied and used the Allauth templates for sign-up/-in/-out 
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
- [Stockvault.net](https://www.stockvault.net/)
- [Unsplash.com](https://unsplash.com/)

[Back to Top of page](#tcontents)

---