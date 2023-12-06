from app import app
from flask import render_template, request
import sqlite3
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-accident', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']

        # Process the input data (e.g., store in a database)
        # For example, printing the received data:
        print(f"name: {name}")
        print(f"Location: {location}")
        print(f"Description: {description}")
        
        conn = sqlite3.connect('accident_details.db')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Create a table to store accident details
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        
        cursor.execute('INSERT INTO accidents (name, location, description) VALUES (?, ?, ?)', (name, location, description))
        conn.commit()
        conn.close()

        # Redirect or render a confirmation page
        # return render_template('confirmation.html')
        # or
        # return redirect(url_for('confirmation'))
  
        return render_template('confirmation.html', name=name, location=location, description=description ) 