# :custard:  Cuisine Quest

## Description:

Dive into a world full of delicious food choices with Cuisine Quest! Unleash your taste buds by discovering a wide array of delicious dishes from around the globe. CQ curates random dishes, letting you uncover the intricate flavors and origins of diverse cultures. Find a dish that catches your eye but you're too busy to try it right now? Save it to your favorite dishes' list and try it later! Want to tell others how amazing the food was at your local restaurant? No worries, share your experience with the community by leaving comments, along with the city and restaurant where you enjoyed the dish. And why stop at words? Capture the essence of your dining adventure by uploading mouthwatering photos of the dishes. Embark on a flavorful expedition today with Cuisine Quest, where every bite tells a story!


## Screenshots of the App

#### Home Page
![Home Page](/main_app/static/assets/CQHome.png)

#### All Dishes Page
![Dashboard Page](/main_app/static/assets/allDishes.png)

#### User's Favorite Page
![Fav List Page](/main_app/static/assets/favorites.png)


## Technologies Used:

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white) ![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![VScode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

## Getting Started

then run python3 manage.py makemigrations

then run the comment python3 manage.py migrate

finally, run the program locally
python3 manage.py runserver

Here's a live link to check out the app! [Live Link](https://cuisine-quest-app-72c4b2078ce8.herokuapp.com/)

Here's a link to our Trello Board: [Trello Board](https://trello.com/invite/b/H5CgLobg/ATTI12e846a40b7c81b7aac01714fbbedf358BA56E74/project-x)

And a link to our Presentation: [CQ Presentation](https://docs.google.com/presentation/d/1WfC8VgTBY0pQOlEFjcsf_ahRLroUgU2QxTImZARp6ww/edit?usp=sharing)

Want to deploy it locally? No problem! Here's a guide:

Clone the repository: Start by cloning this GitHub repository to your local machine using the following command:

```
git clone https://github.com/andrewsegovia00/CuisineQuest.git
```

Install Dependencies: Navigate to the project directory and install the required dependencies by running the following command:

```
pip3 install
```
Set up Environment Variables: Create a .env file in the root directory of the project and set the following environment variables: 
Hint: You'll have to create an S3, IAM account with AWS

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
S3_BUCKET
S3_BASE_URL
SECRET_KEY
MODE
DB_PASSWORD
```

Start the Server: Once the dependencies and environment variables are set up, start the server with the following command:

```
python3 manage.py runserver
```
Access the Application: Cuisine Quest should now be running on http://localhost:8000/. Open your web browser and visit this URL to access the application.

Explore and Enjoy: Now you're all set to explore Cuisine Quest's features and enjoy a delicious adventure!

## Future Features / Icebox:
- [ ] Add a questionaire that curates the dishes shown to the user
- [ ] Add a searchbar to search for dishes
- [ ] Add tags to filter dishes by their primary protein, whether it's fried or spicy!

## Below: The Wireframe of the App

#### Home Page
![Home Page](/main_app/static/assets/Home.png)

#### Try a Random Dish
![Random Dish](/main_app/static/assets/RandDish.png)

#### Display All Dishes
![All Dishes](/main_app/static/assets/AllDishes.png)

#### View a Specific Dish
![View Dish](/main_app/static/assets/ViewDish.png)

#### Favorited Dishes
![Favorite Dishes](/main_app/static/assets/FavoritedDishes.png)

#### Create a Dish
![Create Dish](/main_app/static/assets/CreateDish.png)

#### Login
![Login Page](/main_app/static/assets/LogIn.png)

#### Sign Up
![Sign Page](/main_app/static/assets/SignUp.png)