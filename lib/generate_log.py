from datetime import datetime
import requests

def fetch_data():
    """Fetch a sample post from the JSONPlaceholder API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log(data):
    """Write a list of log entries to a timestamped .txt file."""
    if not isinstance(data, list):
        raise ValueError("Log data must be a list")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    generate_log(["User logged in", "User updated profile", "Report exported"])
