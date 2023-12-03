from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key'

# Username and password for entering the login
valid_username = "Yogender"
valid_password = "Yogender"

# Initialize an empty dictionary for flashcards
flashcards = {}

# Function to get the current flashcard index from the session
def get_current_flashcard_index():
    return session.get('current_flashcard_index', 0)

# Function to update the current flashcard index in the session
def update_current_flashcard_index(index):
    session['current_flashcard_index'] = index

# Login
@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the entered username and password match the valid credentials
        if username == valid_username and password == valid_password:
            # Set session variable to indicate the user is logged in
            session['logged_in'] = True
            return redirect(url_for('flashcard'))
        else:
            error_message = 'Incorrect username or password. Please try again.'

    return render_template('login.html', error_message=error_message)

# Displaying flashcards
@app.route('/flashcard')
def flashcard():
    # Check if the user is logged in
    if 'logged_in' in session and session['logged_in']:
        # Get the current flashcard index
        current_flashcard_index = get_current_flashcard_index()

        # Current flashcard index, total number of flashcards, and flashcards
        return render_template(
            'index.html',
            flashcards=flashcards,
            current_flashcard_index=current_flashcard_index,
            total_flashcards=len(flashcards)
        )
    else:
        return redirect(url_for('login'))

# Navigating to the next flashcard
@app.route('/next_flashcard', methods=['POST'])
def next_flashcard():
    if 'logged_in' in session and session['logged_in']:
        current_index = get_current_flashcard_index()
        current_index = (current_index + 1) % len(flashcards)
        update_current_flashcard_index(current_index)
        return redirect(url_for('flashcard'))
    else:
        return redirect(url_for('login'))

# Navigating to the previous flashcard
@app.route('/prev_flashcard', methods=['POST'])
def prev_flashcard():
    if 'logged_in' in session and session['logged_in']:
        current_index = get_current_flashcard_index()
        current_index = (current_index - 1 + len(flashcards)) % len(flashcards)
        update_current_flashcard_index(current_index)
        return redirect(url_for('flashcard'))
    else:
        return redirect(url_for('login'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # Check if the user is logged in
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            # Check if the flashcard key exists for editing
            if 'flashcard_key' in request.form:
                flashcard_key = request.form['flashcard_key']
                flashcards[flashcard_key]['question'] = request.form['question']
                flashcards[flashcard_key]['answer'] = request.form['answer']
                flash('Flashcard updated successfully', 'success')
            else:
                # Add a new flashcard
                question = request.form['question']
                answer = request.form['answer']
                flashcards[question] = {'question': question, 'answer': answer}
                flash('Flashcard added successfully', 'success')

        # After editing or adding a flashcard, reset the current_flashcard_index to the last index
        update_current_flashcard_index(len(flashcards) - 1)

        return render_template('edit.html', flashcards=flashcards)
    else:
        return redirect(url_for('login'))

@app.route('/remove_flashcard', methods=['POST'])
def remove_flashcard():
    # Check if the user is logged in
    if 'logged_in' in session and session['logged_in']:
        if 'flashcard_key' in request.form:
            flashcard_key = request.form['flashcard_key']

            # Remove the specified flashcard
            if flashcard_key in flashcards:
                del flashcards[flashcard_key]
                flash('Flashcard removed successfully', 'success')

        return redirect(url_for('edit'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the session variable to log out the user
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)