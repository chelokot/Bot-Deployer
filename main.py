# read .env
from dotenv import load_dotenv
load_dotenv()

import os
repo_url = os.getenv("REPO_URL")
bot_token = os.getenv("BOT_TOKEN")
branch = os.getenv("BRANCH")
chat_id = os.getenv("CHAT_ID")

github_username = os.getenv("GITHUB_USERNAME")
github_repository = os.getenv("GITHUB_REPOSITORY")

user_name = os.getenv("OS_USERNAME")

def get_tag_name():
    import requests

    # Replace with your GitHub username, repository name, and access token (if needed)
    username = 'chelokot'
    repository = 'Bot'

    # Construct the API URL for tags
    api_url = f'https://api.github.com/repos/{username}/{repository}/tags'

    # Make a GET request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        tags = response.json()
        
        # Get the newest tag name (assuming tags are sorted by creation date)
        newest_tag = tags[0]['name']
        
        return newest_tag
    else:
        return None


# execute tbd -u <repo_url> -bot_token <bot_token> -b <branch>
import subprocess, time, os

command = [f"/home/{user_name}/.local/bin/tbd", "-u", repo_url, "--chat_id", chat_id, "--bot_token", bot_token, "-b", branch, "-F", "-c", "-t", "--virtualenv_path=venv", "--create_virtualenv", f"/home/{user_name}/.local/bin/virtualenv venv"]
process = subprocess.Popen(command)
pid = process.pid
old_tag_name = get_tag_name()
while True:
    time.sleep(60)
    new_tag_name = get_tag_name()
    if old_tag_name != new_tag_name and new_tag_name != None:
        # Terminate the process
        os.kill(pid, 15)
        print(1/0)
