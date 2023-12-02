# Flashcard
## Milestones Achieved 
###### *(Note: Its and individual piece of work)*
##### Login Page
##### Universal Username & Password
##### Flashcard itself (interactive Flashcard)
##### Number below flashcard which shows what flashcard its on.
##### Previous and Next buttons which allows to switch between flashcards
##### Edit Flashcard place where you are able to add flashcards and preview how they would look and save them. 

## Description: 
#####

## Summary of the program's functionality
### login.html: 
##### Users are prompted to enter a username and password.
##### Upon successful login, users are redirected to the flashcard page.
##### Uses simple in-memory authentication with a hardcoded username and password.

### index.html:
##### Displays flashcards with questions and answers.
##### Users can navigate between flashcards using "Next" and "Previous" buttons.
##### Implemented with AJAX to dynamically load the next and previous flashcards without refreshing the entire page.
##### Provides a logout button to log out the user.

### edit.html:
##### Allows users to edit existing flashcards or add new ones.
##### Displays existing flashcards with the ability to flip them to view both the question and answer.
##### Users can navigate to the flashcard page or log out from this page.

### app.py:
##### Uses Flask to handle routing, sessions, and rendering HTML templates.
##### Manages user authentication with a simple username and password.
##### Stores flashcards in-memory and provides functionality to add, edit, remove, and navigate through flashcards.
##### Implements server-side logic for handling user actions, such as logging in, navigating flashcards, and editing flashcards.


