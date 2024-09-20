from flask import Flask, render_template, request, jsonify
from src.languages import get_languages  # Import the function
import google.generativeai as gen_ai

app = Flask(__name__)
api_key = "AIzaSyCu4O8kGxwU1BqGhlbiEnB-QQpEPzuEKfM"
gen_ai.configure(api_key=api_key)
model = gen_ai.GenerativeModel('gemini-1.5-flash')
# Function to generate the translation using Gemini
def generate_translation(source_text, target_language):
    full_prompt = f"Translate the following '{source_text}' into {target_language}. Keep concise to the length of the prompt, don't add any characters that are not required, and keep the response contextual."
    # Assuming model.generate_content exists and works
    response = model.generate_content(full_prompt)
    return response.text

@app.route("/", methods=["GET"])
def index(): 
    languages = get_languages()  # Get the list of languages from languages.py
    return render_template("index.html", languages=languages)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    source_text = data.get("source_text")
    target_language = data.get("target_language")

    # Call the generate_translation function
    translated_text = generate_translation(source_text, target_language)
    
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
