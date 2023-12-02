import os
from typing import Any, Optional

import requests

RECALL_API_KEY = os.getenv('RECALL_API_KEY')
BOT_ENDPOINT = 'https://api.recall.ai/api/v1/bot'
TIMEOUT = 30


def create_bot(url: str) -> requests.Response:
    """Creates a meeting bot and sends it to the specified meeting."""
    return _make_post_request(BOT_ENDPOINT, {"meeting_url": url, "bot_name": "Meeting Summarizer"})


def transcribe_meeting(bot_id: str) -> requests.Response:
    """Begins transcribing the audio of a meeting."""
    return _make_post_request(f"{BOT_ENDPOINT}/{bot_id}/transcribe")


def get_chat_messages(bot_id: str) -> requests.Response:
    """Retrieves all chat messages from a meeting."""
    return _make_get_request(f"{BOT_ENDPOINT}/{bot_id}/chat-messages")


def get_meeting_transcript(bot_id: str) -> requests.Response:
    """Retrieves the meeting transcript of verbal audio."""
    return _make_get_request(f"{BOT_ENDPOINT}/{bot_id}/transcript")


def _make_get_request(url: str) -> requests.Response:
    """Make a GET request to the Recall API."""
    return requests.get(
        url,
        headers=_get_headers(),
        timeout=TIMEOUT,
    )


def _make_post_request(url: str, payload: Optional[dict[str, Any]] = None) -> requests.Response:
    """Make a POST request to the Recall API."""
    return requests.post(
        url=url,
        json=payload,
        headers=_get_headers(),
        timeout=TIMEOUT,
    )


def _get_headers() -> dict[str, Any]:
    """Gets the headers used for Recall AI API calls."""
    return {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Token {RECALL_API_KEY}",
    }
