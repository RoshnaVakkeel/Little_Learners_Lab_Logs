# Welcome to **[Little Learner's Lab Logs](https://little-learners-lab-logs.herokuapp.com/)**

## PERSPECTIVE
The main inspiration behind creating this website is a little curious learner, my little boy. When he started missing his normal visits to playgrounds during the winter break, he was on a constant lookout for activities around the house. Being among the large percentage of parents who wish to keep their kids engaged throughout the day, I started the quest of finding simple small fun activities that can be performed with the items available in the house. To find those activities, the best source is kids websites. Then followed a thought, what if one can perform the fun experiments and also can log the observations for others to read and repeat.. <br>
With this idea, I created "Little Learner's Lab Logs" which started for a little learner and after its creation, I see that it appeals to all the little scientists hidden within us. The user of this website could be a little kid referring to these logs for fun or a student who wishes to learn and create logs of their own. Not to mention it's a great place for parents, who can help their kids learn new concepts along with having fun. And for teachers, this could be a site where their students can enter their observations and understand the scientific methodology better. <br>
The aim is to collect simple fun-filled small experiments for the Learners created by the Learners. 

## [Contents](#contents)
- [User Experience (UX)](#user-experience-ux)
	- [Site Goals](#site-goals)
	- [User Personas](#user-personas)
	- [Scope](#scope)
- [Agile Methodology](<#agile-methodology>)
    - [Epics and User Stories](<#epics-and-user-stories>)
        - [Website UI](<#website-ui>)
        - [Registration and Account Management](<#registration-and-account-management>)
		- [Lab Log Post Management](<#lab-log-post-management>)
		- [Comment and Like Management](<#comment-and-like-management>)
    - [Acceptance Criteria](<#acceptance-criteria>)
	- [Tasks](<#tasks>)
	- [User Story Management](<#user-story-management>)
- [Features](<#features>)
	- [Home Page](<#home-page>)
        - [Search Button](<#search-button>)
		- [Navbar](<#navbar>)
		- [Hero-image](<#hero-image>)
		- [About](<#about>)
		- [Getting Started](<#getting-started>)
		- [Latest Entries](<#latest-entries>)
		- [Footer](<#footer>)
	- [Lab Logs](<#lab-logs>)
		- [All Collections](<#all-collections>)
		- [Post Details](<#post-details>)
	- [My Page](<#my-page>)
		- [Add Logs](<#add-logs>)
		- [Edit Logs](<#edit-logs>)
		- [Delete Logs](<#edit-logs>)
	- [Sign Up](<#sign-out>)
	- [Sign In](<#sign-in>)
	- [Sign Out](<#sign-out>)
	- [Admin](<#admin>)
	- [General](<#general>)
		- [Security](<#security>)
		- [User Experience](<#user-experience>)
- [Design](<#design>)
	- [Colours](<#colours>)
	- [Typography](<#typography>)
	- [Imagery](<#imagery>)
	- [Wireframes](<#wireframes>)
    - [Database Schema](<#database-schema>)
- [Technologies](<#technologies>)
	- [Languages Used](<#languages-used>)
	- [Frameworks, Libraries and Programs](<#frameworks-libraries-and-programs>)
- [Production](#production)
	- [Django](<#django>)
- [Testing](<#testing>)
	- [Testing Technologies](<#testing-technologies>)
		- [Manual Testing](<#manual-testing>)
			- [Validation](<#validation>)
- [Issues and Fixes](<#issues-and-fixes>)
- [Deployment](<#deployment>)
	- [Heroku](<#heroku>)
- [Credits and Resources](<#credits-and-resources>)
	- [Code](<#code>)
	- [Learning Resources](<#learning-resources>)
	- [Content](<#content>)
	- [Media](<#media>)
- [Acknowledgements](<#acknowledgements>)

# User Experience (UX)

## Site Goals
- Little Learner's Lab Logs is a website mainly meant for curious kids of all ages, where they can explore, create activity logs and also post fun science experiments that could even be performed at home. 
- It is also an useful site for busy parents, who wish that their children to learn new scientific concepts through simple fun experiments. 
- It is also a place for those passionate teachers who want to encourage their students to be motivated to learn science and be intuitive about the scientific concepts around them. 
- All users who sign up and sign in, can access all the features of the website and can create, edit, and delete their posts.

## User Personas 
As mentioned in Site Goals, the users expected to be visiting this website regularly are going to be kids, students, parents and teachers. I created 4 fictional characters which represents the target users. The user personas with their needs, goals and frustrations are enlisted, which helped me design this website with a point of view of distinct users.
The link to User Personas can be found [here](docs/agile/user_personas.pdf).

## Scope
- An attractive and intuitive UX experience: 
	1. Website title focus kids as primany users
	2. Hero-image with information on the site's purpose
	3. Responsve design
	4. A clear and straightforward layout
	5. Footer fixed at the bottom with links to social media
	6. The user knows which page they are on by the name that appears on the head of each webpage.

- An easy navigation for the user through all the pages and features
	1. Navigation Menu with easy access to all links.
	2. Easy Sign Up/ Sign In/ Sign Out functionality visible.
	3. Content guiding users how to start using the websites features
	4. Description of features that would suite different users' needs 
	5. Hero image guidance to sign up/sign in

- Lab Log posts features
	1. Latest entries feature on the landing page
	2. Exclusive page for all the posts
	3. On a click they can view post details
	4. Ability to be able to search for posts
	5. Ability to comment on/like posts
	6. Create, Edit and Delete Posts
	7. Ability to add/edit and remove posts in user's personal page

## Agile Methodology
Throughout this project, an agile approach was taken in order to develop the website  Each activity was broken down into  manageable actions from initially creating 4 Epics, which were then broken down into smaller User Stories. Each of the user stories then had different acceptance criteria. The status, comments and details of each Epic along with the associated User Stories can be found in the kanban board linked [here](https://github.com/users/RoshnaVakkeel/projects/2/views/1). This made the overall project much more manageable to build. 

## Epics and User Stories
4 Epics were created which were further developed into 15 User Stories. The initial conception was done using google sheets. The link can be found [here](docs/agile/epics_and_user_stories.xlsx).

### Website UI
[Epic 01: Little_Learner's_Lab_Logs website UI #1](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/1)
Epic Goals for End User:
1. An intuitive User Interface with easy to use navigation
2. A means of viewing the full list o blogs including likes
3. functionality to allow users to register, sign in and sign out
4. Upon signing in, the user should be able to like, comment on the blog posts

Related User Stories:
1. [USER STORY US01: Intuitive User Interface #2](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/2):
	As a Site user I can see a well defined landing page so that I can easily understand the purpose and main features of the website.
2. [USER STORY US02: Site pagination#3](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/3):
	As a Site user I can view a well paginated website so that navigate easily to different features offered.
3. [USER STORY US03: Log Posts Display#4](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/4):
	As a Site user I can see the collection of log posts at a glance so that I can find the lab log posts of my choice.
4. [USER STORY US04: User Registration/Sign Up Link#5](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/5):
	As a Site user I can easily see a registration button and sign up option so that I can register to access all create, edit and delete functions offered by the website.

### Registration and Account Management
[EPIC 02: Registration and Account Management #6](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/6)
Epic Goals for End User:

1. Easy registration of an account
2. Easy Sign Up, Sign in and Sign Out
3. Confirmation upon signing in 
4. Upon signing in, the user should be able to like, comment on the lab log post posts
5. Easy access to Create, Read, Update and Delete (CRUD) features upon signing in
6. Visibility of personalized lab log post posts and comments

Related User Stories:
1. [USER STORY US05: Account Creation#7](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/7):
As a Site user I can create an account by registering my details so that I can comment, like, create and edit lab log posts
2. [USER STORY US06: Account Confirmation #8](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/8):
As a Site user I can I get a message upon signing up so that I can know that my account registration was successful.
3. [USER STORY US07: Sign In and Sign Out Features #9](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/9): As a registered Site user I can easily Sign in or Sign Out so that I can access my personal posts and comments.
4. [USER STORY US 08: User Personal Page Features#10](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/10):
As a registered Site user I can see my personal page so that I can create my own lab log post posts and edit or delete them.


### Lab Log Post Management
[EPIC 03: Lab Log Post Management#11](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/11)

Epic Goals for End User:

1. Create lab log posts. 
2. View their created lab log posts
3. Update/Edit personalized lab log posts
4. Delete lab log posts

Related User Stories:
1. [USER STORY US09: Add Lab Log Posts#12](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/12): As a signed-in Site user I can create a lab log post so that I can share my ideas and experiments
2. [USER STORY US 10: View/Read Lab Log Posts #13](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/13): As a signed-in Site user who created a lab log post I can read my post with my name among other posts on homepage so that I can share my posts with others.
3. [USER STORY US 11: Edit Lab Log Posts #14](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/14):As a signed-in site user I can edit and update a lab log post I created so that I can make additions, edit, correct the entries I made in the post.
4. [USER STORY US 12: Delete Lab Log Posts#15](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/15): As a signed-in site user I can choose to delete a lab log post I created so that I publish only the posts of my choice.


### Comments and Like Management
[EPIC 04: Comments/Likes Management #16](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/16)

Epic Goals for End User:
1. Add and see Comments 
2. Add/remove Likes

Related User Stories:
1. [USER STORY US 13: Post Comments #17 ](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/17): As a signed-in site user I can add a comment on any lab log posts so that I can express my opinion about a topic of my choice.
2. [USER STORY US 14: Site Owners Approval of Comments #18](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/18): As a site owner and admin I can review and then approve or disapprove comments so that unsuitable comment can be filtered out as children also would be site users.
3. [USER STORY US 15: Add or Remove Likes on a Post#19](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs/issues/19): As a signed-in site user I can add like to the lab log posts I liked so that I can guide other users to select simple experiments that may be more interesting.

## Acceptance Criteria
For all the User Stories, Acceptance Criteria was also mentioned. The purpose of this was to provide a reference point for the developmental steps. I made sure to cross-check that all the required steps intended was implemented. It also helped with Testing to make sure that all the necessary aspects and features were covered. The acceptance criteria is described on the column next to the user stories (column H) [here](docs/agile/epics_and_user_stories.xlsx).

## Tasks
The tasks for the website development process was closely followed as mentioned in CI's Django module "I Think Therefore I Blog" walkthrough project.
The tasks during the development phase were carried out in this order.

[Back to top ⇧](#contents)

## Features

### Home Page
Homepage provides the user with some quick information on how to start using the site and make use of all its features.  It helps them decide if they would like to continue to read the posts or create them. Users do not need to be registered to view a post. 

Homepage or the Landing page has these key features: 

Visible at first glimpse:
1. Search input field and button
2. Navigation Menu
3. Hero-image

![Homepage](docs/features/home_landing.png)

Upon scrolling down:
1. About Section
2. Getting Started
3. Latest Entries
4. Footer

Details to each section has been provided below in detail.

#### Search Button 
On the top right corner, a search input field is provided along with a button to submit. User can search any query using keywords and a new search page will appear containing Search Results. Click [here](docs/features/search_result.png) to see it.

#### Navbar
The responsive navigation bar is featured on all pages. The purpose of this feature is to allow users to navigate all pages easily across all devices without having to use a back button to get to the next page. It has active links to different pages. For mobile view, the navbar transforms to a burger menu. 

Navbar features two types of views/ navigation menu items depending on if the user is logged in or logged out. 

If the user is not signed in or is signed out. The navbar will prompt to Sign Up, Sign In or log in as Admin. The navigation menu will appear as shown below. 

![here](docs/features/navbar_signed_out.png)
<br>
If the user is signed in (username Rose is provided as an example here). The navigation menu will appear as shown below. The navbar will in this case feature "User's" Page and Sign Out options.

![here](docs/features/navbar_signed_in.png)

This feature is introduced for better user guidance. 

### Hero-image
The Hero-image is introduced in a Carousel that enables a slideshow for cycling through elements. As the theme cannot be depicted in just a picture, my idea was to give three pictures with three captions. Th captions would also prompt the user to sign in or sign up. Besides that, it will also contain links to different sections within th homepage such as About and Getting Started for user guidance, and to Latest Entries section to draw user's attention to the different posts. The pictures with different links can be found [here](docs/features/hero_image.png). 

Upon clicking on "Learn More" link: The "About" section of Homepage will be loaded.
Upon clicking on "Get Started" link: The "Getting Started.. Your Guide" section of Homepage will be loaded.
Upon clicking on "Latest Entries" link: The "Latest Entries" section of Homepage will be loaded.

### About
About section asks the users questions about which kind of user persona they associate with and helps them understand the ways they can make use of the different features of the website. It also presents a welcome note for the users. Check it out [here](docs/features/about.png).

### Getting Started
This section describes how each user can use the functionalities available in the website. The user esp. a student or a kid would need guidance on how website features can be accessed. The links are provided at each step, which can directly open the links as the respective pages. The section can be seen [here](docs/features/getting_started.png).

### Latest Entries
The lab log posts is paginated in a way that only the latest 3 posts are displayed on Home page. This has been implemented to improve the user experience and not overwhelm the user with the whole list.
I wanted that the user gets to see the glimpse of the lab logs posts that exist in the website, which have been posted and approved the most recently. It is set in descending order by the date of creation, meaning the latest will be the first post visible. It shows the lab log post title (clicking on which, the post details can be seen), image uploaded by the user, author name, two lines of description followed by the date and time of creation along with the number of like the post received. The section can be seen [here](docs/features/getting_started.png).

### Footer
Each page has the same footer at the bottom containing Copyright information, link to homepage and a note that this website is meant for Educational purposes only.
The footer section includes links to my social media site [Linkedin](https://www.linkedin.com/in/roshna-vakkeel/) and my [GitHub](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs) page which opens up in a new tab to allow easy navigation for the user. 

![Footer](docs/features/footer.png)

[Back to top ⇧](#contents)

	- [Lab Logs](<#lab-logs>)
		- [All Collections](<#all-collections>)
		- [Post Details](<#post-details>)
	- [My Page](<#my-page>)
		- [Add Logs](<#add-logs>)
		- [Edit Logs](<#edit-logs>)
		- [Delete Logs](<#edit-logs>)
	- [Sign Up](<#sign-out>)
	- [Sign In](<#sign-in>)
	- [Sign Out](<#sign-out>)
	- [Admin](<#admin>)
	- [General](<#general>)
		- [Security](<#security>)
		- [User Experience](<#user-experience>)

[Back to top ⇧](#contents)

## Design
### Colours
- The colour scheme has considered based on easy accessibility for all. 
- Complimentarity was key feature in color selection, to give it a pleasant feel for all age groups.
- The colors have been consistently maintained throughout the website.

The palette was generated with inspiration from palettes provided by [Lilybug Graphic Design -Colour Wall](https://www.lilybugdesign.co.nz/colour-wall). The chosen palette of colors was generated from the graphic: [Tropical palette](docs/features/tropical-palette.jpg). The colours were modified using [Colorswall](https://colorswall.com/palette/227413). 
The colors were generated referring to the Tropical palette in colorswall palette Generator. The generated palette was:![Color Palette](docs/features/color_palette.png)
<br>
These were the colors for the body (scented frill - #c9adb6) and (variant of deep pink - #851050) was chosen for navbar and footer.


### Typography
- Fonts were imported using Google Fonts. Roboto was used throughout with a backup of sans-serif. It was chosen for easy readability for users. 
- UTF-8 Symbols 

### Imagery
The imagery on the website has been seleced according to young users. The images chosen depict children engaged in different activities. The pictures selected are with range of colors. Usually experiments are meant to be colorful. The carousel was chosen to show hero-image because one picture cannot represent the whole theme of the website.
All images were taken from [Pexels](https://www.pexels.com/).

### Wireframes
The wireframes were generated at the start of the project suing Balsamiq. After referring to different bootstrap templates, pages were divided into the different relevant sections. 
The finished website closely fololows wireframes as the designs were adapted during development but overall structure was kept constant. For eg. an additional 'About' section was introduced in order to guide the user. A search field and button was also introduced. 

The wireframes can be found in these links:<br>
[Wieframes for Desktop](docs/wireframes/PP4_project_wireframe_desktop.pdf)<br>
[Wieframes for Tablet](docs/wireframes/PP4_project_wireframe_tablet.pdf)<br>
[Wieframes for Mobile](docs/wireframes/PP4_project_wireframe_mobile.pdf)

### Database Schema
Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities User, Post and Comment are shown here. 
![Entity Relationship Diagram](docs/wireframes/database_schema.png)

[Back to top ⇧](#contents)

## Technologies
### Languages Used]
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs

**Frameworks**
-   [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
-   [Bootstrap](https://getbootstrap.com/) was used to render layout and responsiveness of the website.

**Programs**
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-	[Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.
-   [Smartdraw](https://cloud.smartdraw.com/) was used to create the Entity Relationship diagrams for the data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Google Fonts:](https://fonts.google.com/) used for the Roboto font
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db
-   [Cloudinary](https://cloudinary.com/) used to store the images used by the application
-   [Summernote](https://pypi.org/project/django-summernote/) used to provide WYSIWYG editing on the "Add Logs" page in order to add items_required and steps_to_perform input fields in the form.
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering

**Libraries**
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html)  - was used to implement account authorisation and providing associated templates
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db
-   [jquery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js) used to fade out alert messages

## Production
### Django 
**Installation and Set Up**
This website is built on the Django framework. To set up a Django project, the necessary dependencies were installed. This project uses the old versions as mentioned in CI's Django wakthrough project "I think therefore I blog"
This needs these steps to be followed:

Within the development environment, 
1. install Django using the command:
~~~
pip3 install 'django<4' gunicorn
~~~
This installs Django (the framework) and gunicorn (which is a WSGI HTTP server that will be used by the site).

2. Then install the libraries `psycopg2` and `dj_database_url==0.5.0 psycopg2` using the command line:
~~~
pip3 install dj_database_url==0.5.0 psycopg2
~~~
These libraries are needed for connecting to the database.

3. As this site uses Cloudinary to store files, this needs to be installed with:
~~~
pip3 install dj3-cloudinary-storage
~~~
This allows the site to use Cloudinary for storing and serving files

4. Once all the dependencies are installed, generate a requirements.txt document for them by using:
~~~
pip3 freeze --local > requirements.txt
~~~
This will store the dependencies of the project in a file called requirements.txt

5. Next, start a new Django project using the command:
~~~
django-admin startproject <project-name> .
~~~
(don't leave off the dot at the end as this determines where the project is created).

In my case, it was:
~~~
django-admin startproject little-learners-lab-logs .
~~~

6. Migrations need to be run to set the database up, this can be done with:
~~~
python3 manage.py migrate
~~~

7. Finally, you can commit and push your changes to GitHub using :
~~~
git add .
git commit -m "initial commit
git push
~~~


****
[Back to top ⇧](#contents)

## Testing
The testing is broken into categories: manual and validation. Details can be found below.

### Testing Technologies 
The website was manually tested the website on 3 different browsers: Chrome, Firefox and Edge. In all the browsers the website unctions very well. Only exception is Firefox Mozilla, where the Corousel wasn't functioning properly. It is addressed in the Issues section.
In addition, I also tested it on my own mobile with Safari search engine, and had a number of friends and family test it on their own devices. There are a number of accounts and lab log entries that already exist in the database which were created by diferent users. Their feedbacks were taken into account and improvements were made in the website.

This testing consisted of checking:

- The website functioned as expected
- Working of all the links
- Submission of forms
- JavaScript functioning
- Comments and posts addition
- Editing and delete functions

#### Manual Testing

#### Validation
I used the following validation tools

- HTML using [W3C HTML validator](https://validator.w3.org/)
- CSS using [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
- Site performance via [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- Accessibility via [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- Python via [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)

Results obtained are as follows:

##### HTML Validation 
All the Django templates html files hava been validated by manually copying the source of the rendered pages and then validating using the W3C Validator (link shown above). Each test result shows the source url. The results can be seen [here](docs/validation/w3c_validation_results_html.pdf).

##### CSS Validation 
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. CSS file was tested by manually copying the CSS codes into the manual input option. The result can be seen [here](docs/validation/w3c_validation_CSS.png).

##### Lighthouse Test
[Lighthouse](https://developers.google.com/web/tools/lighthouse) tool was used for analysing the performance, accessibility, best practices and SEO of the website. The results are summarised [here](docs/validation/lighthouse_report.pdf).

##### WAVE Accessibility Test
[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to check web accessibility. Only the certain contrast errors were reported. It was due to link contrast with the background. I used primary link color blue in hero-image caption for better guidance for the user, so that they identify that it is a link rather than using black color as suggested by the tool. This error was deliberately ignored. No other errors were reported. The results can be found [here](docs/validation/wave_accessibility_test.pdf). 

##### PEP8 Python Linter Test
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check that the Python code meets PEP8 standards. All the errors were also checked periodically before git push to the repository. The tests results can be seen [here](docs/validation/pep8_validation.pdf). 

[Back to top ⇧](#contents)

- [Issues and Fixes](<#issues-and-fixes>)


[Back to top ⇧](#contents)


## Deployment
### Heroku
(copied from [John-breedon-bass-tuition-pp4 project](https://github.com/adamhatton/john-breedon-bass-tuition-pp4/blob/main/README.md))

Once a Django project has been set up and developed, it can be deployed to Heroku using the following steps (this is how this project was deployed):

1.	Ensure that all dependencies are in the requirements.txt file within the project using the python command “pip3 freeze > requirements.txt”:
2.	Navigate to https://www.heroku.com/ and login
3.	In the top right corner, select ‘New’ then ‘Create new app’
4.	From the ‘Create New App’ screen, enter a unique App name and select Europe, then select ‘Create app’
5.	An app is created and the dashboard is shown, from here navigate to the 'Resources tab'
6.	The Postgres database needs to be connected to the app using an add-on. Search the 'Add-ons' in the Resources tab for 'Heroku Postgres' and select this add-on
7.	On the pop-up for Heroku Postgres select a plan type (for this site 'Hobby Dev - Free' was selected)
8.	Navigate to the 'Settings' tab for the app and select to 'Reveal Config Vars', a variable called `DATABASE_URL` will have been created by connecting the database add-on. Copy the **value** of this variable
9.	Within the development environment, create a file called `env.py` at the top level
	- Ensure that this file is added to the .gitignore file. If your project does not have a .gitignore file then create one and add the `env.py` file to it
10.	In the `env.py` file, import the `os` library and create a database variable using the value taken from Heroku:
~~~
os.environ ["DATABASE_URL"] = "<heroku database variable goes here>"
~~~

11.	Whilst in the `env.py` file, create a `SECRET_KEY` variable which will be used later. To generate a new Django secret key, do a google search for a Django secret key generator and use one of the results to create a key. The variable can be created using:
~~~
os.environ ["SECRET_KEY"] = "<secret key goes here>"
~~~

12.	Back in Heroku, add your secret key variable to the Config Vars by selecting 'Add' and entering 'SECRET_KEY' as the Key and your secret key value as the Value
13.	Return to the development environment, and navigate to the `settings.py` file. Within this file, import the following:
~~~
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
	import env
~~~

These imports will enable you to access the variables in your `env.py`

14. Find the `SECRET_KEY` variable and replace the assignment as follows:
~~~
SECRET_KEY = os.environ.get('SECRET_KEY')
~~~

15. Find the `DATABASES` variable and comment out the existing code (this will be used in a later step), add in the following code:
~~~
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
~~~

This will enable Heroku to connect to the database

16.	As a new database is now being used, migrations need to be run again by using 
~~~
python3 manage.py migrate
~~~

17.	As this project uses Cloudinary for file storage, additional steps are needed to configure this. Start by creating another variable in the `env.py` file for your personal Cloudinary (which can be obtained from the Cloudinary dashboard):
~~~
os.environ["CLOUDINARY_URL"] = "<your cloudinary url>"
~~~

18.	Next, go back to Heroku and add another Config Var for your cloudinary url using `CLOUDINARY_URL` for the Key and your cloudinary url as the Value
19.	If your project does not have any static files then add another Config Var to Heroku using `DISABLE_COLLECTSTATIC` as the Key and '1' as the Value. This will prevent the deployment from failing if there are no static files. This variable has been removed for this project as there are static files.
20.	Return to the development environment, and in the `settings.py` file find the `INSTALLED_APPS` variable add in 'cloudinary_storage' before 'django.contrib.staticfiles' and then add 'cloudinary' underneath 'django.contrib.staticfiles'.
21.	To configure Django to use Cloudinary, find the static files section towards the bottom of the `settings.py` file and add the following code:
~~~
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
~~~

22.	Next, create a `TEMPLATES_DIR` variable in `settings.py` and set it to:
~~~
os.path.join(BASE_DIR, 'templates')
~~~
so that Django knows where to find templates

23.	Find the `TEMPLATES` variable and for the `DIRS` key, set the value to be the `TEMPLATES_DIR` we have just created:
~~~
'DIRS': [TEMPLATES_DIR],
~~~

24.	Find the `ALLOWED_HOSTS` variable in `settings.py` and add in the urls that should be able to access the project:
~~~
ALLOWED_HOSTS = ['<heroku-project-name>.herokuapp.com', 'localhost']
~~~

25.	Within your project folder structure, create three directories at the top level for storing files: media, static, and templates
26.	At the top level of your project structure, create a file called Procfile and add the following code to it:
~~~
web: gunicorn codestar.wsgi
~~~

Heroku uses this file to determine how to run the app

27.	To prevent sensitive information being revealed when running the app on Heroku, the `DEBUG` variable should be set to False, however this can be set conditionally depending on whether you are in the development environment or not. To do this, create an environment variable within your development environment called `DEVELOPMENT` and set its value to True (for this project this was done in GitPod > Settings > Variables)
28.	Next, in the `settings.py` file, add the following variable and assignment:
~~~
development = os.environ.get('DEVELOPMENT', False)
~~~

29.	Set the `DEBUG` variable to be equal to development:
~~~
DEBUG = development
~~~

30.	Find the `DATABASES` variable that was previously commented out and amend the databases section to be conditional on whether you are in the development environment or not. It should look like this:
~~~
if development:
    DATABASES = {
	    'default': {
		    'ENGINE': 'django.db.backends.sqlite3',
		    'NAME': BASE_DIR / 'db.sqlite3',
        }
	}
else:
	DATABASES = {
		'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
	}
~~~
These steps will mean that `DEBUG` will be set to True whilst in the development environment, but False when running the Heroku app. It will also mean that Heroku will use the Heroku Postgres database, whereas the development environment will use the SQLite database. Note that any changes to the database will need to be migrated to both if both are to be used.

31.	Commit your changes and push these to GitHub
32.	Back in Heroku add another Config Var using `PORT` as the Key and '8000' as the Value.
33.	Navigate to the Deploy tab and from the ‘Deployment Method’ section, select ‘GitHub’
34.	Allow Heroku to connect to GitHub by selecting ‘Connect to GitHub’
35.	Search for the repository by entering the name of the GitHub repository to deploy and selecting search
36.	From the results, choose the relevant repository and select ‘Connect’
37.	To enable automatic deployment of the repository (which will automatically redeploy the project after every push to GitHub), select the ‘Enable Automatic Deploys’ option
38.	To manually deploy the project, select ‘Deploy Branch’ from the Manual Deploy section
39.	When the branch is manually deployed, Heroku will build and deploy the branch. Upon completion, a link to the deployed project will be generated

[Back to top ⇧](#contents)


## Credits and Resources
### Code
- The basic set up of the website was done by strictly following the steps as described in Code Institue Full Stack Frameworks module - Django walkthrough project "I Think Therefore I Blog".
- Search Button function - [Django Search Using QuerySet and Q() objects](https://python.plainenglish.io/django-search-using-queryset-and-q-objects-299d8e4a7f3b)
- Adding Database forms to "Add Logs" page was learnt from [How To Add Database Forms To A Web Page](https://www.youtube.com/watch?v=CVEKe39VFu8)
- 

### Learning Resources
- Creation of GitHub projects to track issues - [Creating a project Resource](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project)
- How Django slugs work?- [Learn Django](https://learndjango.com/tutorials/django-slug-tutorial) 
- Creation of Django commenting system - [Commenting system for a Django 2.X app](https://djangocentral.com/creating-comments-system-with-django/)
- Setting up 404 page - [Django 404 page setting](https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317)
- Different Projects of Code Institute student projects being referred: 
1. [John Breedon Bass Tuition](https://github.com/adamhatton/john-breedon-bass-tuition-pp4)
2. [The Newsbox](https://github.com/rashdogg74/newsbox86)
3. [Fungi News](https://github.com/Maya-Claveau/pp4-fungi-news)
4. [The Unconventional Programmer](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer)
5. [BANFF National Park Hike Booker](https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes)

	- [Content](<#content>)

	- [Media](<#media>)

[Back to top ⇧](#contents)

## Acknowledgements
I would like to acknowledge the following people who have helped me along the way in completing my fourth milestone project:
- My Mentor Elaine B Roche for her guidance, advice and constant encouragement. Her suggestions helped me improve my website well. 
- My fellow students for their company and encouragement. Special thanks to Kristyna Maulerova, Tony Albania, Jtoyi Yadav for their encouragement, support and for testing my website, adding posts and comments.
- My friends and family who tested the website and gave valuable feedback.
- My tutors who helped me solve issues when I had them.

[Back to top ⇧](#contents)
