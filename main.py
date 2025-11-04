import os
from dotenv import load_dotenv

def main():
    print("Hello from ai-agent!")

load_dotenv()
api_key = os.environ.get("AIzaSyD4W94XWwHrt8GZQFeHYoJvzSPVOOYrIaU")

if __name__ == "__main__":
    main()
