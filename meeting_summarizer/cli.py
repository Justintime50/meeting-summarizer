import argparse

from meeting_summarizer.summarizer import MeetingSummarizer


class MeetingSummarizerCli:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Summarize your meetings with the power of Recall AI.')
        parser.add_argument(
            '-c',
            '--create',
            type=str,
            required=False,
            help='Create a bot, supplying a meeting URL (Zoom, Google Meet, etc).',
        )
        parser.add_argument(
            '-s',
            '--summarize',
            type=str,
            required=False,
            help='Summarize a meeting, supplying a bot ID.',
        )
        parser.add_argument(
            '--slack',
            action='store_true',
            required=False,
            help='Use to send the meeting summary to Slack.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        self._validate_params()
        meeting_summarizer = MeetingSummarizer(
            create=self.create,
            summarize=self.summarize,
            slack=self.slack,
        )
        meeting_summarizer.run()

    def _validate_params(self):
        """Validates all CLI params."""
        if not self.create and not self.summarize:
            raise ValueError('A CLI flag must be passed to use this tool!')
        if self.create and self.slack:
            raise ValueError('Cannot use Slack flag when creating a bot!')


def main():
    MeetingSummarizerCli().run()


if __name__ == '__main__':
    main()
