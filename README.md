# Microservices_demo
A demo on how to get started with micro services using python flask

## Get Started
### Requirements
Flask


Simplejson

git clone `https://github.com/NeostreamTechnology/Microservices`

### Installation 

Do  `pip install -r requirements.txt `

### Running
`python user.py`
`python todo.py`

### Navigation
`127.0.0.1:5000/users`-To view all the users
`127.0.0.1:5000/user/<username>` -To view a specific user
`127.0.0.1:5000/user/<username>/lists` -To view the lists of a specific user

`127.0.0.1:5001/lists` -To view all the to do list
`127.0.0.1:5001/lists/<username>`-To view the to do list of a specific user

