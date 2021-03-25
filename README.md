#### Adding buttons to the django-bot-server application
- At initial, few users have been populated to the postgres database through migration file.
- The user needs to select a name and proceed with the bot.
- The user is permitted to enter the first welcome message, then three buttons pop up displaying fat,stupid and dumb buttons.
- The user can continue the chat, just by selecting the buttons.
- For each user selected, every time the button is clicked, the counts for each button and user is counted and saved in django model.
- The table showing each user total calls can be view using the below link.
    127.0.0.1:8001/mocker/clicks/
    
Corrections.
The input text field was used with a div element, which is been changed to input field.
Javascript file have been modified according to the change.

Notes :
- A total of 4 users have been added through the migration file.
- A new django app has been created. 

# django-bot-server-tutorial

Accompanying repository for a seminar on creating a django based bot server that uses django-channels for  WebSockets connection. This borrows heavily from the code at https://github.com/andrewgodwin/channels-examples 

# What is this useful for?

- Get an idea how to get django-channels working
- Get some sample code for a simple working front end that uses web sockets for a connection

# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot

