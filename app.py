from flask import Flask, render_template, request

app = Flask(__name__)

# Define the path for storing emails (you can change the path if needed)
EMAIL_FILE_PATH = "emails.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-email', methods=['POST'])
def submit_email():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Store the email data in a text file
    with open(EMAIL_FILE_PATH, 'a') as file:
        file.write(f"Name: {name}, Email: {email}, Message: {message}\n")

    # Return a success message as response
    return "Data received and stored successfully!"

if __name__ == '__main__':
    app.run(debug=True)
