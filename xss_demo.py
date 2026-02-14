from flask import Flask, render_template_string, request # Import web tools
app = Flask(__name__) # Initialize app

@app.route("/profile") # Define the profile page URL
def view_profile(): # Function to show the bio
    bio_text = request.args.get("bio", "") # Take whatever is typed in the URL search bar
    # PROBLEM: '|safe' tells the browser NOT to clean the text, but to run it as code
    return render_template_string("<h1>User Bio: {{ bio | safe }}</h1>", bio=bio_text)
