from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_database"]
collection = db["todo_items"]

@app.route('/')
def home():
    return "Home Page"

# Route to render the frontend To-Do page created in master_1
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Backend route for accepting POST requests
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    # Retrieve data from the HTML form POST request
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    # Store the details in the MongoDB collection
    todo_document = {
        "itemName": item_name,
        "itemDescription": item_description
    }
    collection.insert_one(todo_document)
    
    return jsonify({
        "status": "success",
        "message": "To-Do item successfully saved to MongoDB!"
    }), 201

if __name__ == '__main__':
    app.run(debug=True)