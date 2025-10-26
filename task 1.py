from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Apply Form Submission
@app.route('/apply', methods=['POST'])
def apply():
    name = request.form.get('name')
    email = request.form.get('email')
    university = request.form.get('university')

    # For now, just print the data (you can later connect to a DB)
    print(f"New Application: {name} | {email} | {university}")

    # Redirect back to home with success
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
