from flask import Flask # Import the web framework
app = Flask(__name__) # Initialize the application

@app.route("/like") # Define the URL address for liking a post
def like_post(): # The function called when the button is clicked
    return "Liked!" # PROBLEM: No limit, a bot can call this 1000 times a second to fake fame
