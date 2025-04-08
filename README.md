# URL Shortener Project

This project implements a simple URL shortening service using Flask and SQLite. It provides CRUD (Create, Read, Update, Delete) operations for managing shortened URLs. The URLs are stored in a local SQLite database (`urls.db`).

## Features
- **POST**: Create URL, Shorten a URL.
- **GET**:  Read URL, Retrieve the original URL from a shortened URL.
- **PUT**: Update URL, Update an existing shortened URL.
- **DELETE**: Delete URL, Delete a shortened URL.

## Requirements

To run this project, you need the following installed on your local machine:

- Python 3.8 or higher
- Flask
- SQLite

### Installing Dependencies

You can install the necessary Python packages using the following command:

```bash
pip install -r requirements.txt

```
## FILE STRUCTURE
- app.py              # Main application logic
- db.py               # Database setup and operations
- view_db.py          # View database contents
- .gitignore          # Files and directories to ignore by Git
- README.md           # Project documentation
- urls.db             # SQLite database storing the URLs (ignored by Git)
- __pycache__/        # Python bytecode files (ignored by Git)

## USAGE
### RUNNING THE APPLICATION

To run the Flask app locally, execute the following command:
```bash
python app.py
```
The application will start and be accessible at http://127.0.0.1:5000.

## API Endpoints

### POST /shorten:
Accepts a JSON object containing the original_url and returns the shortened URL. Example Request:
{
  "original_url": "http://google.com"
}
Example Response:
{
  "shortened_url": "http://127.0.0.1:5000/c7b920"
}

### GET /<shortened_url>:
Redirects to the original URL for the given shortened URL. Example Request: GET http://127.0.0.1:5000/c7b920

### PUT /shorten:
Updates an existing shortened URL with a new original URL. Example Request:
{
  "shortened_url": "http://127.0.0.1:5000/c7b920",
  "original_url": "http://example.com"
}

### DELETE /shorten:
Deletes the specified shortened URL from the database. Example Request:
{
  "shortened_url": "http://127.0.0.1:5000/c7b920"
}

## Testing with Postman
To test the API, you can use Postman with the following steps:

- POST /shorten: Create a shortened URL by sending a JSON payload with the original URL.

- GET /c7b920: Retrieve the original URL using the shortened URL.

- PUT /shorten: Update an existing shortened URL.

- DELETE /shorten: Delete a shortened URL.

# DATABASE
The application uses SQLite (urls.db) to store the mappings between original URLs and shortened URLs. The database file is included in the .gitignore file to prevent it from being pushed to the repository.

#LICENCE
This project is licensed under the MIT License - see the LICENSE file for details.

# Future Improvements
- Add validation for URL format and error handling.
- Implement user authentication for managing URLs.
- Provide more detailed error responses.

# Clone the Repository
To clone this project to your local machine, run the following command:
```bash
git clone https://github.com/Maryam7297/Maryam-innovaxel-Riaz.git
```
After cloning, navigate into the project directory:
```bash
cd Maryam-innovaxel-Riaz
```




