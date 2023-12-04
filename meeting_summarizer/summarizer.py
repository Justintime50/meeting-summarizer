import json
from typing import Any

from meeting_summarizer.messages import send_slack_message
from meeting_summarizer.recall import (
    create_bot,
    get_chat_messages,
    get_meeting_transcript,
    transcribe_meeting,
)


class MeetingSummarizer:
    def __init__(
        self,
        create=None,
        summarize=None,
        slack=False,
    ):
        self.create = create
        self.summarize = summarize
        self.slack = slack

    def run(self):
        """Run the command-line tool to summarize meetings."""
        if self.create:
            output = self.send_bot_to_meeting()
            print(output)
        elif self.summarize:
            title, summary = self.summarize_meeting()

            if self.slack:
                send_slack_message(title, summary)

    def send_bot_to_meeting(self) -> str:
        """Sends a Recall AI bot to a meeting."""
        response = create_bot(self.create)

        if response.status_code == 201:
            output = f"Bot ID: {response.json()['id']}"
        else:
            output = json.dumps(response.json(), indent=4)

        return output

    def summarize_meeting(self) -> tuple[str, str]:
        """Summarize a Zoom, Google Meet, etc meeting with Recall AI. We do this by doing the following:
        1. Kick off a transcription job (can use same response to grab participant list)
        2. Get the list of chat messages
        3. Get the meeting transcript
        4. Build the summary string and save it to a file
        """
        transcribe_response = transcribe_meeting(self.summarize)
        if transcribe_response.status_code != 200:
            raise Exception(f"Could not transcribe meeting: {transcribe_response.text}")
        meeting_json = transcribe_response.json()
        participant_list = sorted([
            participant.get('name') for participant in meeting_json.get('meeting_participants', [])
        ])
        meeting_title: str = meeting_json['meeting_metadata'].get('title')
        video_url = meeting_json.get('video_url')

        chat_message_response = get_chat_messages(self.summarize)
        if chat_message_response.status_code != 200:
            raise Exception(f"Could not retrieve chat messages: {chat_message_response.text}")
        # TODO: Need to account for pagination?
        chat_messages = chat_message_response.json().get('results', [])

        # TODO: Need to account for a transcript not being complete yet and retry/wait here
        transcript_response = get_meeting_transcript(self.summarize)
        if chat_message_response.status_code != 200:
            raise Exception(f"Could not retrieve meeting transcript: {transcript_response.text}")
        transcript = transcript_response.json()

        summary = build_summary(meeting_title, video_url, participant_list, transcript, chat_messages)
        save_file(meeting_title, summary)

        return meeting_title, summary


def build_summary(
    meeting_title: str,
    video_url: str,
    participant_list: list[str],
    transcript: list[dict[str, Any]],
    chat_messages: list[dict[str, Any]],
) -> str:
    """Builds a string containing all the details of the meeting summary. This string summary can then
    be used to populate a file and send off to Slack.
    """
    summary = f'{meeting_title} Summary'
    summary += f'\n\nMeeting Video: {video_url}'
    participants_string = "\n- ".join(participant for participant in participant_list)
    summary += f'\n\nParticipants:\n- {participants_string}'
    summary += '\n\nAudio Transcript:'
    # TODO: Calculate timestamps for speaking transcript entries (they are in seconds since start of meeting)
    for speaker in transcript:
        summary += f'\n- {speaker.get("speaker")}: '
        words = speaker.get('words', [])
        for word in words:
            summary += f'{word.get("text")} '

    summary += '\n\nChat Messages:'
    for message in chat_messages:
        sender = message.get('sender', {})
        summary += f'\n- ({message.get("created_at")}) {sender.get("name", {})}: {message.get("text")}'

    return summary


def save_file(filename: str, content: str) -> None:
    """Saves a string to a text file."""
    with open(f'{filename.lower().replace(" ", "_")}.txt', 'w') as filepath:
        filepath.write(content)
