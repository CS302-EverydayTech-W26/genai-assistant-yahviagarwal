from gemini_client import *
from flask import Flask, request, render_template

app = Flask(__name__)
client = GeminiClient() 

@app.route("/", methods=["GET", "POST"])
def main():
    response_text = ""
    user_input = ""

    if request.method == "POST":
        # Get user input from the form
        user_input = request.form.get("prompt", "")
        if user_input:
            response_text = client.generate_response(user_input)
  
    return render_template("index.html", response_text=response_text, user_input=user_input)

if __name__ == "__main__":
  app.run(debug=True)