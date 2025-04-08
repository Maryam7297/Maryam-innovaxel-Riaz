from flask import Flask, request, jsonify, redirect
import hashlib
import sqlite3

app = Flask(__name__)

# Function to create a shortened URL (you can customize the logic as needed)
def generate_shortened_url(original_url):
    # Using a hash function to create a unique shortened URL
    return hashlib.md5(original_url.encode()).hexdigest()[:6]  # Shorten the hash to 6 characters

# Store the original URL and its shortened URL in the database
def store_url(original_url, shortened_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY,
            original_url TEXT NOT NULL,
            shortened_url TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO urls (original_url, shortened_url) 
        VALUES (?, ?)
    ''', (original_url, shortened_url))
    conn.commit()
    conn.close()

# Fetch the original URL by shortened URL
def get_url_by_shortened(shortened_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('SELECT original_url FROM urls WHERE shortened_url = ?', (shortened_url,))
    result = cursor.fetchone()
    conn.close()
    return result

# Update the original URL of a given shortened URL
def update_url(shortened_url, new_original_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE urls SET original_url = ? WHERE shortened_url = ?', (new_original_url, shortened_url))
    conn.commit()
    conn.close()

# Delete a shortened URL from the database
def delete_url(shortened_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM urls WHERE shortened_url = ?', (shortened_url,))
    conn.commit()
    conn.close()

# Route to shorten a URL (Create)
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()  # Get the JSON data
    original_url = data.get('original_url')  # Extract the URL from the request

    if original_url:
        # Generate a shortened URL
        shortened_url = generate_shortened_url(original_url)
        # Store the original URL and shortened URL in the database
        store_url(original_url, shortened_url)
        # Return the shortened URL
        return jsonify({"shortened_url": f"http://127.0.0.1:5000/{shortened_url}"}), 200
    else:
        return jsonify({"error": "No URL provided"}), 400

# Route to retrieve original URL (Read)
@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_url(shortened_url):
    result = get_url_by_shortened(shortened_url)

    if result:
        return redirect(result[0])  # Redirect to the original URL
    else:
        return jsonify({"error": "Shortened URL not found"}), 404

# Route to update a URL (Update)
@app.route('/update/<shortened_url>', methods=['PUT'])
def update_shortened_url(shortened_url):
    data = request.get_json()
    new_original_url = data.get('original_url')
    
    if new_original_url:
        update_url(shortened_url, new_original_url)
        return jsonify({"message": "URL updated successfully"}), 200
    else:
        return jsonify({"error": "No new URL provided"}), 400

# Route to delete a shortened URL (Delete)
@app.route('/delete/<shortened_url>', methods=['DELETE'])
def delete_shortened_url(shortened_url):
    delete_url(shortened_url)
    return jsonify({"message": f"Shortened URL {shortened_url} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
