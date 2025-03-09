from flask import Flask, jsonify, request
import random
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # Adjust this if using a different host
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # Your MySQL password
app.config['MYSQL_DB'] = 'university_chatbot'  # Database name

mysql = MySQL(app)

# Sample funny responses
funny_responses = [
    "Are you sure you're not a robot?",
    "I think I need a vacation...",
    "Did you say something? I'm busy thinking.",
    "Error 404: Sense of humor not found!",
    "Haha, that's a good one! 😄"
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()

    # Query the database for a response
    cur = mysql.connection.cursor()
    cur.execute("SELECT response FROM responses WHERE keyword = %s", (user_input,))
    result = cur.fetchone()

    if result:
        return jsonify({"response": result[0]})
    else:
        # If no match, return a random funny response
        return jsonify({"response": random.choice(funny_responses)})

if __name__ == '__main__':
    app.run(debug=True)
