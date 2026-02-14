from flask import Flask # Import the web framework
app = Flask(__name__) # Initialize app

@app.route("/privacy", methods=["POST"]) # Route for privacy changes using a form
def update_privacy(): # Function to execute the change
    return "Account set to PRIVATE." # PROBLEM: No token check, any malicious site can trigger this
