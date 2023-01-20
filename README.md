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
- [Testing](<#testing>)
	- [Testing Technologies](<#testing-technologies>)
		- [Automated Testing](<#automated-testing>)
		- [Manual Testing](<#manual-testing>)
			- [Validation](<#validation>)
- [Bugs and Issues](<#bugs-and-issues>)
- [Deployment](<#deployment>)
	- [Django](<#django>)
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

## Website UI

## Agile Methodology
All functionality and development of this project will be managed through GitHub issues and projects. The initial conception was done using google sheets. 
The link can be found [here](docs/agile/epics_and_user_stories.xlsx).

## Epics and User Stories
4 Epics were created which were further developed into 15 User Stories. The details of each Epic along with the associated User Stories can be found in the kanban board linked [here](https://github.com/users/RoshnaVakkeel/projects/2/views/1).

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

