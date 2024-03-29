# Project 4 - Movie-App
The Movie-App Finder does exactly what it says on the app. It's a place where users can create and view Movies. The live Website can be found here.

A live preview of the website can be found [Here](https://https://aquesidilly.herokuapp.com/) 


# Table of Contents
 - User Experience Design (UX)
  * The Strategy Plane
   * Site Goals
   * User stories
 - The Scope Plane
 - The Structure Plane
 - The Skeleton Plane
   * Database Design
   * Security
 - The Surface Plane
  * Design
   * Colour Scheme
   * Typography
   * Imagery
  * Differences to Design
 - Features
  * Existing Features
  * Future Features
 - Technologies
  * Testing
   * Test Strategy
   * Test Results
   * Issues and Resolutions
 - Deployment
  * Project Creation
  * GitHub Pages
  * Run Locally
  * Fork Project
 - Credits
  * Content
  * Acknowledgements
# User Experience Design
 # The Strategy Plane
 There are so many Movie-App been advertised on social media, it can be difficult to get an app which can help you create add and display movies. As a movie pundit, many clients have  requested for a  website for a majority people who love movies  to use in thier various homes and work place  to have easy accessible information about the movie-app.

 This movie-app was created for the mass people to choose from selected movies on the app for movie lovers. The aim is to provide users with a simple website that allows them to quickly find,search,edit and delete movies that can be watched by movie lovers. All movies created can be delete and can also create new ones to be watched, although they do not have to be displayed as this data will not be needed enhancements of the website.

 # Site Goals
 To know the number of people who watch movies from the movie-app by providing a simple, easy to use website that contains updates of movies or movies available.
 This site displays movies to be watched by people from all walks of life.
 # User stories
 As a user, I want the main purpose of the Movie-App to be clear so that public immediately know what the app is intended for upon entering.
 As a user, I want to easily navigate the site so that I can find content quickly with ease.
 As a user, I want the website to be responsive so that I can clearly view the webpages from my mobile, tablet or desktop.
 As a user, Anybody should be able to register to the movie-app so that they can create and manage movies of interest.
 As a user, Should be able to search or filter movies based on custom criteria so that I can find movies that suits the interest of the public or users.
 As a user, will like a way to delete movies that is not interest again.
 As a user, I want to be able to return to the main site without having to use the browser buttons so that I can easily return to the website if I navigate to a page that doesn't exist.
 # The Scope Plane
  # Features planned:

  * Responsive design.
  * Movie-App and information on the site purpose.
  * Navigation Menu 
  * MongoDB databases to store event information and user login/profile information.
  * CRUD Functionality
  * Login functionality.
  * Logout functionality.
  * Home Page
  * Search for movies for users.
  * Registered user .
  * Importance and Difficulty

# The Structure Plane
 User Story:

As a user, I would like to know the main purpose of the app to be clear so that a user can immediately know what the site is intended for.

Acceptance Criteria:

  * Site Login to be displayed on the main navigation bar on all pages.
  * Home Page to display Website Title and information to the user on the purpose of the site.
Implementation:

A site logo will be displayed on the main navigation menu. This should be displayed on all webpages.

The Movie-App title be displated as a h1 element on the home page and a detailed description of the site will be displayed on the Home page so that is evident of the movie-app's purpose as soon as the user visits the app.

User Story:

As a user, I want to easily navigate the site so that I can find movies quickly with ease.

Acceptance Criteria:

  * Navigation menu to be displayed on all pages.
  * All navigation links redirect to the correct pages.
Implementation:

A navigation menu will be displayed on all movie-app. This will redirect users to the approriate page when clicked. On smaller devices, the menu will collapse into a hamburger menu to make efficient use to screen space. When clicked, the menu will expand out from the right side of the screen displaying all nav items.

The following navigation items will be implemented:

Home - index.html
* Register - register.html
* Sign In - login.html
* Base - base.html
* Create - create_movie.html
* Delete - delete.html
* Movies - movies.html
* Edit - edit_movies.html
* Search- search.html
* Sign Out - (redirects to home page)
User Story:

As a user, I would want the Movie-App to be responsive so that I can clearly view the movies from my mobile, tablet or desktop.

Acceptance Criteria:

* Content should be responsive and display clearly on all devices with no horizontal scroll.
Implementation:

User Story:

As a user, I want to be able to register to the website so that I can create and watch movies from the app by myself.

Acceptance Criteria:

 * Sign up - Login and Logout functionality to be added.
 * User must have the ability to create, edit and delete movies from the app.
 * User must have movies  displaying their details and movies they have created and watched.
 * Only the creator of the movies can have the ability to edit or delete the movies created .
Implementation:

A Sign Up page will be implemented that allows users to register their account for the movie-app. The username and password along with basic details for the users account will be stored in a MongoDB database collection called users. In order to create or modify , a user will have to register and login to the app. Only the creator of the app will have the ability to edit or delete movies, this is to prevent unwanted modification or deletion of movies by other users. A flash message will be shown to the user to alert them whether the edit or delete their movies was successful or failed.

A Sign In page will be implemented to allow registered users the ability to login in to their account.

Once a user has successfully logged in, they will be redirected to their home page. The users basic details will be displayed on their home page, along with any movies they have created. The user will be able to edit or delete their movies from the home page. This page will only be available to logged in users, this includes the visibility of the navigation menu item.

A Sign Out button will be displayed to users who are logged in. When clicked this will sign the user out of the website and redirect them to the home page.

A Create movie page will be implemented that will be acessible and visible on the navigation menu to logged in users. The user will be able to create movies from this page. The movie information will be stored in a MongoDB database collection called user and the user categories will be stored in a MongoDB collection called categories.

User Story:

As a user, I want to be able to search or filter through the movies based on custom criteria so that I can find movies suitable to the user.

Acceptance Criteria:

 * Movies must be displayed to all users regardless of being logged in.
 * Users should be able to search for movies.
Implementation:

A Movie-App will be implemented that is displayed to all users that is accessible to logged in or guests. This page will display the movies available to watch . In order to make use of space, this app will be collapsable and can be expanded to view details on click.

A search box will be displayed on screen which will allow users to search for movies. This will return a filtered, full list movies for the current search criteria. This will be implemented by using a database index that will be created on the MongoDB collection users.

Implementation:

A login page will allow users to get access to the app. The EmailJS API will be used in order to implement this feature and a flash message will be displayed to alert the user if the contact form submitted successfully or unsuccessfully.

Validation will be performed on the form to ensure valid data input. The form will not submit if any field is blank.

Form Fields:

 * Name - Type: Text, required.
 * Email - Type: Email, required.
 * Password- Type: Text, required
User Story:

As a user, I want to be able to return to the main site without having to use the browser buttons so that I can easily return to the website if I navigate to a page that doesn't exist.

Acceptance Criteria:

  * If a user redirects to the wrong page, an error will display that contains a link to go back to the main website.
Implementation:

A custom 404 page will be created so that if a user attempts to navigate to a page that it not found, an error will be displayed. This page will contain a clickable anchor link to allow the user to redirect to the main website without needing to use the browser navigation buttons.

Collection: movies
{
    id:
title:""
user:"crownie"
short_description:"test2"
collections:"test2"
method:"test2"
tags:"test2"image
:"test2"
views:1

}

Collection: 
{
    _id: unique-value,
    event_type: "Rally",
    location : "Wexford",
    date : "09 February, 2021",
    description : "This Rally is hosted by Unicorn MCC.",
    organiser : "Daisy McGirr"
    created_by : session[user]
}

Collection: users
{
    _id: unique-value,
    username: "Admin",
    password : "12a6yt&jddn",
    name : "Jane Doe",
}

* Security
Database connection details are set up in an env.py for development, for security reasons this is not uploaded to GitHub so that database and connection details are not visible to users. In production these are stored in Heroku.

#The Surface Plane
#Design
*Colour Scheme
The main background colour is a cream #d2d2af for the header, footer and form button backgrounds.

The main website text is black #000000

All custom heading text is a deep shade of red #831717

*Typography
The main heading on all pages and in the expanded materialize collapsible element headings use the 'PT Serif' font while the rest of the websites content uses the 'Play' font.

* Imagery
A background image will be used on all pages displaying vegetation, this image was taken from goggle .

A live preview of the website can be found [Here](https://kenan-cookbook-ms3.herokuapp.com/) 

# Features
 # Existing Features
  * Home page displaying images and information on the sites purpose.
  * Register functionality.
  * Sign in / Sign out functionality.
  * Search that displays the movies from the Movie-App that allows users to search for movies.
  * Create Movie page allowing signed in users to create movies.
  *  Delete Movie showing basic user information and MOVIES created by the user with modification ability.
  * Edit Movies with .
  * Mobile responsive design.
  * Site wide footer containing contact information, Copyright info and Site Links.
# Features Left to Implement
 A feature to be included in the next release will allow users the ability to edit and create their own movies.

Admin login will be implemented in the next release to allow admin users to delete any movies that may be inappropriate.

# Technologies
* HTML
This project uses HTML as the main language used to complete the structure of the Website.
* CSS
This project uses custom written CSS to style the Website.
* JavaScript
   * JavaScript is used along with emailjs for the contact form. This sends an email to the owner on form submit.
   * jQuery is used for the following:
     * Mobile side nav
     * Displaying Success/Fail message verifying contact form status.
     * To populate downdrops on select elements.
* Python
 * This projects core was created using Python, the back-end logic and the means to run/view the Website.
 * Python Modules used (These can be found in the requirements.txt project file):
  * dnspython==2.0.0
  * Flask==1.1.2
  * Flask-PyMongo==2.3.0
  * Flask-WTF==0.14.3
  * itsdangerous==1.1.0
  * pymongo==3.11.2
  * Werkzeug==1.0.1
  * WTForms==2.3.3
* MongoDB
 * MongoDB was used to create the document based databases(collections) used as data storage for this project.
* GitHub
 * GithHub is the hosting site used to store the source code of the Movie-App.
* VSCode
 * VSCode is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* Heroku
 * Heroku was used to deploy the live website.
* Google Chrome Developer Tools
 * Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* Font Awesome
 * All the Icons displayed throughout the website are Font Awesome icons.
* Favicon
 * Favicon.io was used to make the site favicon
* Techsini
 * Multi Device Website Mockup Generator was used to create the Mock up image in this README
# Testing
 # Test Strategy
  # Summary
Testing is required on all features and user stories documented in this README. All clickable links must redirect to the correct pages. All forms linked to MongoDB must be tested to ensure they insert all given fields into the correct collections.

HTML Code must pass through the W3C HTML Validator.

CSS Code must pass through the W3C CSS Validator.

JavaScript code must pass through the JSHint Validator.

Python Code must pass through PEP8 Validator

* Access Requirements
Tester must have access to MongoDB in order to manually verify the insertion of records to users and events collections.

* Regression Testing
All features previous tested during development in a local environment must be regression tested in production on the live website.

* Assumptions and Dependencies
Testing is dependent on the website being deployed live on Heroku.

* Out of Scope
Only test cases listed under High Level Test Cases will be performed as part of this testing effort.

# Test Results

# Deployment
 # Project Creation
To create this project I used the CI Gitpod Full Template by navigating here and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

 * git add filename - This command was used to add files to the staging area before committing.

 * git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

 * git push - This command is used to push all committed changes to the GitHub repository.

#Deployment to Heroku
 # Create application:

 1. Navigate to Heroku.com and login.
 2. Click on the new button.
 3. Select create new app.
 4. Enter the app name.
 5. Select region.
 # Set up connection to Github Repository:

 1. Click the deploy tab and select GitHub - Connect to GitHub.
 2. A prompt to find a github repository to connect to will then be displayed.
 3. Enter the repository name for the project and click search.
 4. Once the repo has been found, click the connect button.
 # Set environment variables:

Click the settings tab and then click the Reveal Config Vars button and add the following:

 1. key: IP, value: 0.0.0.0
 2. key: PORT, value: 5000
 3. key: MONGO_DBNAME, value: (database name you want to connect to)
 4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and dbname that you set up in the link).
 5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).
 # Enable automatic deployment:

 1. Click the Deploy tab
 2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.
# Run Locally
# Note: The project will not run locally with database connections unless the user sets up an env.py file configuring IP, PORT, MONGO_URI, MONGO_DBNAME and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository for security purposes.

 1. Navigate to the GitHub Repository.
 2. Click the Code drop down menu.
 3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
 4. Open your developement editor of choice and open a terminal window in a directory of your choice.
 5. Use the 'git clone' command in terminal followed by the copied git URL.
 6. A clone of the project will be created locally on your machine.
Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:

pip install -r requirements.txt

# Fork Project
Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea. - Definition from Github Docs.

 1. Navigate to the GitHub Repository you want to fork.

 2. On the top right of the page under the header, click the fork button.

Fork

 3. This will create a duplicate of the full project in your GitHub Repository.

# Credits
Background image - google images.

Website Logo - 

# Code
Stack Overflow - The code used to navigate to a specific section of a page using Flask templates was taken from here.

Stack overflow - The code used to create custom error messages on invalid form inputs was copied and modified from this stack overflow post.

Stack overflow - The CSS used to center the nav bar was gotten from this stack overflow post.

W3Schools - The figure and caption code on the home page images was done by following a W3Schools tutorial.

JavaScript Validation function in scripts.js was code from course material for Task Manager App on the LMS.

# Acknowledgements
I'd like to give special thanks to the the following people for their help with my project:

* Two friends who helped in making this project successful (names with held) 
* My mentor Spencer Baribell for his guidance throughout the project.