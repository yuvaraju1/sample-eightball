import requests

# Secret API key (DO NOT expose this in your code)
API_KEY = "12345abcde67890fghij"

# Example of using the API key to make a request to a public API
response = requests.get(f"https://api.example.com/data?apikey={API_KEY}")

if response.status_code == 200:
    print("Data retrieved successfully!")
else:
    print("Failed to retrieve data.")

# Secret database password (DO NOT expose this in your code)
DB_PASSWORD = "supersecretpassword"

# Simulated database connection using the password
def connect_to_database():
    print(f"Connecting to the database with password: {DB_PASSWORD}")
    # Imagine connecting to a real database here
    # db.connect(user="username", password=DB_PASSWORD)

connect_to_database()
