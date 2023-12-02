import os
from typing import Any

import slack_sdk

SLACKBOT_TOKEN = os.getenv('SLACKBOT_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')


def send_slack_message(message: str):
    """Send the meeting summary as a Slack message via a Slackbot."""
    slack_client = slack_sdk.WebClient(SLACKBOT_TOKEN)

    summary_file = slack_client.files_upload_v2(
        title="Meeting Summary",
        filename="meeting_summary.txt",
        content=message,
    )
    file_object: dict[str, Any] = summary_file.get("file", {})
    file_url = file_object.get("permalink")

    slack_client.chat_postMessage(
        channel=SLACK_CHANNEL,  # type:ignore
        text=f"A meeting happened! Check out the summary: {file_url}",
    )
