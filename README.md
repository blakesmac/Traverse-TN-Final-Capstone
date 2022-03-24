# Traverse-TN-Final-Capstone

Link to Client Repo => https://github.com/blakesmac/Traverse-TN-Client
<!-- Introduction -->
Welcome to Traverse TN!

This application is designed to help users and any interested parties browse local rivers and places to visit in beautiful Tennessee.
Get out there and explore the unbelievably beautiful natural landscapes and locations of Tennessee!

<!-- Purpose -->
Tennessee has been a fast growing state for many years, due to it's natural beauty and stunning locations. Many individuals from all over the country,
and the world come here to visit, and end up making this wonderful place their home. Most people probably do not think about going to explore the wilder
parts of the state, and miss out on gorgeous hidden locations around the state. This application aims to change that. Members can sign up to browse lovely
rivers, and scenic places to visit. Once they have looked over the places, they will be able to see which other members have planned trips to these locations.
Members can plan their own trip to visit anywhere they would like! I wanted to create an all in one experience for members to be able to 

<!-- Walkthrough of App -->
https://user-images.githubusercontent.com/81835278/159962881-a39a6644-17f9-4354-98ef-9fd01bad4ffb.mp4

[TraverseTN App p.2.mp4.zip](https://github.com/blakesmac/Traverse-TN-Final-Capstone/files/8343517/TraverseTN.App.p.2.mp4.zip)

<!-- Install and Run -->
First things first
1. Clone the Repository
2. Create directory inside your terminal and set the target at the directory desired.
3. Install pip
4. This will create the ability to enter a shell environment/ pipenv shell
5. Once inside the shell install django

<!-- Difficulties -->

Stumbling blocks while building the application included more React based issues. Displaying the correct data within React coming from Django.
An example would be the many to many relationship between Members and rivers/places. Listing the username of the member who planned a trip to these spots is captured
and added to the array inside of rivers and places, listing the username. Once I fixed the serializers to produce the data with foreign keys about the members,
it was then straight forward to grab the key of username from inside of members, and access the django user model data. 
Other challenges included managing my time correctly and getting as much as I could done. This was an amazing experience to work on this project.
It was a lot of hard work and time spent to complete the requirements I needed to meet. 






