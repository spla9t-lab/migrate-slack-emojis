import requests
import json

# Replace with your Slack Workspace 1 API Token
SLACK_API_TOKEN_1 = "xoxb-your-workspace-1-token"

# Replace with your Slack Workspace 2 API Token
SLACK_API_TOKEN_2 = "xoxb-your-workspace-2-token"

# URL for Slack API to list all custom emojis
emoji_list_url = "https://slack.com/api/emoji.list"

# URL for Slack API to add custom emoji
add_emoji_url = "https://slack.com/api/emoji.add"

# Get all custom emojis from Workspace 1
response = requests.get(
    emoji_list_url,
    headers={
        "Authorization": "Bearer " + SLACK_API_TOKEN_1
    }
)

# Extract the emojis from the response
emojis = response.json()["emoji"]

# Loop through each emoji and upload it to Workspace 2
for emoji_name, emoji_url in emojis.items():
    files = {
        "image": (emoji_name + ".png", requests.get(emoji_url).content)
    }
    response = requests.post(
        add_emoji_url,
        headers={
            "Authorization": "Bearer " + SLACK_API_TOKEN_2
        },
        data={
            "mode": "data",
            "name": emoji_name
        },
        files=files
    )
    if response.status_code == 200:
        print(f"Successfully added {emoji_name} to Workspace 2")
    else:
        print(f"Failed to add {emoji_name} to Workspace 2")
