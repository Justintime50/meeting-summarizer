<div align="center">

# Meeting Summarizer

Summarize your meetings with the power of Recall AI.

[![Build Status](https://github.com/justintime50/meeting-summarizer/workflows/build/badge.svg)](https://github.com/justintime50/meeting-summarizer/actions)
[![Coverage Status](https://coveralls.io/repos/github/justintime50/meeting-summarizer/badge.svg?branch=main)](https://coveralls.io/github/justintime50/meeting-summarizer?branch=main)
[![PyPi](https://img.shields.io/pypi/v/meeting-summarizer)](https://pypi.org/project/meeting-summarizer)
[![Licence](https://img.shields.io/github/license/justintime50/meeting-summarizer)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/meeting-summarizer/showcase.png" alt="Showcase">

</div>

Have you ever missed a meeting or wanted to reference the sidebar chat but no longer can because it's concluded? With Meeting Summarizer, you'll never miss an important detail again. Get a link to the meeting, the meeting transcript, and the sidebar chat delivered directly to your Slack instance to easily reference and share.

## Install

```bash
# Install locally
just install
```

## Usage

```bash
# Create a bot and send it to a meeting by supplying the meeting URL 
venv/bin/python meeting_summarizer/cli.py --create https://us04web.zoom.us/j/123

# Summarize the meeting once it is complete (should wait a few minutes after a meeting finishes) by supplying the Bot ID output when created
venv/bin/python meeting_summarizer/cli.py --summarize "123"
```

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
