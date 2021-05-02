# Area_master Application

## Author
Vincent Juma

## Description
This a django web application that allows registered users to know about everything happening in their current residential sites.
| The program navigates to the authentication page                                                                            | Load the application                                                   | Navigate to the login/register page                                                            |
| Navigate to the Registration Page                                                                                           | Click on Register link                                                 | A registration form is displayed                                                               |
| If registration is successful navigate to login page                                                                        | Click on Login Link                                                    | Application navigates to the homepage where posts are displayed                                |
| A post creation form is displayed with the empty fields. After saving the user is redirected to homepage to view the posts. | Click on create post button and submit button                          | A form with post picture,name,description is displayed.                                        |
| Application navigates to the activity creation form . After saving user is redirected to all activity page.               | Click on create activity button                                        | A form with activity name,email and area name is displayed.A submit button is also displayed.  |
| All user details including the name, posts and activity created by the user are displayed                                 | User clicks on the Profile link                                        | A User profile with all info pertaining the user is displayed.                                 |
| An Edit Form is displayed to update user info.                                                                              | Use clicks the edit profile button, makes changes and submits the form | A user edit form with update fields is shown to the user to enable them update necessary info. |
|A list of all activities in that area is displayed with all the information| User clicks on View activities link on the navbar |All activities are displayed in that particular locations |
|User is logged out of the application |User clicks on the Logout dropdown |User logged out and redirected to the register/login page.|

### Project Setup instructions
Use the following commands to use this project.
- git clone `https://github.com/Vincent-Juma/area_master.git`
- install `python 3.6`
- Install [Postgresql](https://www.postgresql.org/download/)
- cd my_area
- Navigate to the virtual environment using `source virtual/bin/activate`
- `atom .`  //For those using atom text editor.
- `code .`  //For those using Visual Studio editor.

### Install dependancies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`

### Create the Database
```
psql
CREATE DATABASE <preferred name>;
```
- Run `python3 manage.py runserver`
- Access the application on this localhost address `http://127.0.0.1:8000`

### Technologies used
The different technologies that were used to develop this program include:
```
1. Python 3.9
2. Bootstrap
3. HTML
4. CSS
5. Postgresql
6. MDBootstrap
7. Django Framework
```

### Link to live site
Here is a link to the live site https://myareaproject.herokuapp.com/ 
### Contact Me
Contact me on my email for any suggestions or changes vincentjuma64@gmail.com
### License  & Copyright information
Copyright (c) 2021 Vincent Juma

[MIT License](./LICENSE)