# Welcome to **[Little Learner's Lab Logs](https://little-learners-lab-logs.herokuapp.com/)**

## PERSPECTIVE
The main inspiration behind creating this website is a little curious learner, my little boy. When he started missing his normal visits to playgrounds during the winter break, he was on a constant lookout for activities around the house. Being among the large percentage of parents who wish to keep their kids engaged throughout the day, I started the quest of finding simple small fun activities that can be performed with the items available in the house. To find those activities, the best source is kids websites. Then followed a thought, what if one can perform the fun experiments and also can log the observations for others to read and repeat.. <br>
With this idea, I created "Little Learner's Lab Logs" which started for a little learner and after its creation, I see that it appeals to all the little scientists hidden within us. The user of this website could be a little kid referring to these logs for fun or a student who wishes to learn and create logs of their own. Not to mention it's a great place for parents, who can help their kids learn new concepts along with having fun. And for teachers, this could be a site where their students can enter their observations and understand the scientific methodology better. <br>
The aim is to collect simple fun-filled small experiments for the Learners created by the Learners. 

## Contents
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
		- [Automated Testing](<#automated-testing>)
		- [Manual Testing](<#manual-testing>)
			- [Validation](<#validation>)
- [Bugs and Issues](<#bugs-and-issues>)
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

## Scope

- An attractive and intuitive UX experience: 
	1. Website title focus kids as primany users
	2. Hero-image with information on the site's purpose
	3. Responsve design
	4. A clear and straightforward layout
	5. Footer fixed at the bottom with links to social media

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


## Production
### Django Installation and Set Up
This website is built on the Django framework.To set up a Django project and install the necessary dependencies, these steps were followed:

Within your development environment, 
1. install Django using the command:
~~~
pip3 install django gunicorn
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
django-admin startproject <your-project-name> .
~~~
(don't leave off the dot at the end as this determines where the project is created).

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
