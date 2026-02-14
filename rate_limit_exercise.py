from flask import Flask # Import framework
from flask_limiter import Limiter # Import the rate limiting extension
from flask_limiter.util import get_remote_address # Identification tool

app = Flask(__name__) # Initialize app
limiter = Limiter(get_remote_address, app=app) # STEP 1: Setup the limiter for the app

# STEP 2: Add the limit decorator below
# TODO: Add @limiter.limit("3 per minute") right above the @app.route line
@app.route("/secure_like") # Define the web address
def secure_like(): # Secure function
    return "Like recorded safely!" # Return success
