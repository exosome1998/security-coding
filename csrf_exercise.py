from flask import Flask # Import web framework
from flask_wtf.csrf import CSRFProtect # Import CSRF protection library

app = Flask(__name__) # Initialize app

# STEP 1: Set a secret key to sign the security tokens
app.secret_key = "hsc-secure-2026" # TODO: Set to a random string

# STEP 2: Turn on CSRF protection globally
# TODO: Add csrf = CSRFProtect(app)
pass # Placeholder
