<div align="center">

# Meeting Summarizer

Summarize your meetings with the power of Recall AI.

[![Build Status](https://github.com/justintime50/meeting-summarizer/workflows/build/badge.svg)](https://github.com/justintime50/meeting-summarizer/actions)
[![Licence](https://img.shields.io/github/license/justintime50/meeting-summarizer)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/meeting-summarizer/showcase.png" alt="Showcase">

</div>

Have you ever missed a meeting or wanted to reference the sidebar chat but no longer can because the meeting has concluded? With Meeting Summarizer, you'll never miss an important detail again. Get a link to the meeting, the meeting audio transcript, the sidebar chat, and the list of participants nicely packaged into a text file and delivered directly to your Slack instance to easily reference and share.

Meeting Summarizer will produce output that looks like the following:

```text
Justin's Personal Meeting Room Summary

Meeting Video: https://recallai-prod-bot-data.s3.amazonaws.com/123...

Participants:
- Chris’ iPhone 15 Pro
- Justin
- Mark

Audio Transcript:
- Justin: We're basically just waiting for everybody to join at this point. Hello? Hello? 
- Mark: My phone wouldn't do it, so I came over to the computer. 
- Justin: Sorry. 
- Mark: No problem.
- Justin: That's lame.
- Mark: Yeah.
- Justin: Chris's iPhone, admit. Hello? Chris? 
- Justin: everybody's got to leave the meeting so that the bot leaves the meeting, too. Otherwise, it'll just stay put. 
- Mark: All right, toodles. Thanks, 
- Justin: Yeah. Bye. 

Chat Messages:
- (2023-12-02T02:04:23.199060Z) Justin: Here is the first message
- (2023-12-02T02:07:15.101570Z) Chris’ iPhone 15 Pro: Give me money
- (2023-12-02T02:07:23.490492Z) Justin: I don’t have any
- (2023-12-02T02:07:32.679688Z) Chris’ iPhone 15 Pro: I want chicken nuggets and an Oreo McFlurry
- (2023-12-02T02:07:32.940949Z) Mark: I hope everyone remembers to meet up tomorrow at 8am.
- (2023-12-02T02:07:49.105166Z) Chris’ iPhone 15 Pro: I can meet at 8:01 not at 8pm
```

## Install

```bash
# Install locally
just install
```

## Usage

### Env Vars

You will need a few environment variables to get started:

```text
RECALL_API_KEY=123
SLACKBOT_TOKEN=123
SLACK_CHANNEL=my_channel
```

You'll need to [grab your Recall API key](https://api.recall.ai/dashboard/apikeys/) to authenticate with their API.

If using Slack, you will need to follow their [Quickstart Guide](https://api.slack.com/start/quickstart) on setting up a Slackbot integration if you haven't already.

### CLI Args

```text
  -h, --help            show this help message and exit
  -c CREATE, --create CREATE
                        Create a bot, supplying a meeting URL (Zoom, Google Meet, etc).
  -s SUMMARIZE, --summarize SUMMARIZE
                        Summarize a meeting, supplying a bot ID.
  --slack               Use to send the meeting summary to Slack.
```

### Examples

```bash
# Create a bot and send it to a meeting by supplying the meeting URL 
venv/bin/python meeting_summarizer/cli.py --create "https://us04web.zoom.us/j/123"

# Summarize the meeting once it is complete by supplying the bot ID output when the meeting was created
venv/bin/python meeting_summarizer/cli.py --summarize "123"
```

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
