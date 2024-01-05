# Flashcard
## Milestones Achieved 
###### *(Note: Its and individual piece of work)*
##### Login Page
##### Universal Username & Password
##### Flashcard itself (interactive Flashcard)
##### Number below flashcard which shows what flashcard its on.
##### Previous and Next buttons which allows to switch between flashcards
##### Edit Flashcard place where you are able to add flashcards and preview how they would look and save them. 
##### Remove Flashcard button which allows you to select multiple flashcards and remove them with one button.  
##### Star Flashcard which you can press to highlight a flashcard which is hard for you to understand, and thus later pay more attention to it. 

## Description: 
##### The purpose of this program is to provide a simple web-based flashcard application. It is designed for users who want an interactive and digital way to study and review information using flashcards. The program caters to individuals who may be preparing for exams, learning new topics, or engaging in self-directed learning.



## Summary of the program's functionality
### login.html: 
##### Users are prompted to enter a username and password.
##### Upon successful login, users are redirected to the flashcard page.
##### Uses simple in-memory authentication with a hardcoded username and password.

### index.html:
##### Displays flashcards with questions and answers.
##### Users can navigate between flashcards using "Next" and "Previous" buttons.
##### Implemented with AJAX to dynamically load the next and previous flashcards without refreshing the entire page.
##### Provides a function which shows what flashcard you are on currently. 
##### Star flashcard which allows you to star flashcards which are hard for you to understand. 
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

## Breakthrough Moment
##### I had multiple breakthrough moments but one of the most important ones that I believe was about when I fixed the edit.html so that I am able to add more flashcards directly from the website and not have to go back to the code to do it. I believe that I had to learn multiple things for this because it was not working for me. flashcards[question] = {'question': question, 'answer': answer} for example this if i have a question and an answer this takes that input and adds it in the flashcard and the line after this one: flash('Flashcard added successfully', 'success') shows that it has been added and refreshes the page. 


