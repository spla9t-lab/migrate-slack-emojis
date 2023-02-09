# Slack Emoji Copier 📢💬🎉
A python script that grabs all the custom emojis from one Slack Workspace and uploads them to another, because who wants to manually upload emojis one by one, right? 🙄

## Prerequisites 
- A Slack API token for both the source and destination Workspaces. If you don't have one, go to https://api.slack.com/authentication/token-types#bot to generate one. 
- `requests` and `json` libraries installed. If you don't have them, run `pip install requests json`

## Usage
- Replace the `SLACK_API_TOKEN_1` and `SLACK_API_TOKEN_2` with your actual Slack API tokens for the source and destination Workspaces respectively. 
- Run the script `python emoji_copier.py`

## How does this work? 
The script uses the Slack API to grab all custom emojis from one Slack Workspace (let's call it Workspace 1) and uploads them to another Slack Workspace (let's call it Workspace 2). 

1. Imports the `requests` and `json` libraries. 
2. Sets the API tokens for Workspace 1 and Workspace 2. 
3. Makes a GET request to the Slack API to retrieve a list of all custom emojis in Workspace 1. 
4. Loops through each emoji, creates a `files` dictionary with the emoji image, and makes a POST request to the Slack API to upload the emoji to Workspace 2. 
5. Checks the status code of the response to determine if the emoji was successfully uploaded. 

## Caveats 
- The script does not check for duplicates, so if an emoji with the same name already exists in Workspace 2, it will be overwritten. 
- The script only works for custom emojis and does not transfer system emojis. 
- Make sure you have the right Slack API tokens and permissions, otherwise, this script will be as useful as a screen door on a submarine. 

## Conclusion 
With this script, you can now sit back, relax, and let the code do the work for you. No more manual emoji uploads, no more frustration, just pure emoji bliss. 🎉😎
