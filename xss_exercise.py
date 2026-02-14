from flask import Flask, render_template_string # Import web tools

app = Flask(__name__) # Initialize app

@app.route("/show_comment") # Define the comment display URL
def show_comment(comment_text): # Secure function
    # STEP 1: Remove the '| safe' filter so scripts show as text
    # TODO: Change the string below to render comment_text WITHOUT the safe filter
    return render_template_string("<h3>Comment: {{ comment }}</h3>", comment=comment_text)
