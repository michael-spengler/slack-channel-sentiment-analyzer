import os
from slack_sdk.web import WebClient
from dotenv import load_dotenv

load_dotenv()

slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def _get_all_channels(cursor=''):
  conversations = slack_web_client.conversations_list(exclude_archived=True, cursor=cursor)
  channels = conversations['channels']
  next_cursor = conversations['response_metadata']['next_cursor']
  if next_cursor:
    channels = channels + _get_all_channels(next_cursor)

  return channels

def get_channels():
  # TODO: Cache response to limit number of API calls to Slack
  channels = [channel for channel in _get_all_channels() if channel['is_member'] is True]
  return channels

def get_messages(channel_id):
  history = slack_web_client.conversations_history(channel=channel_id)
  messages = [message for message in history['messages'] if 'subtype' not in message]
  return messages
