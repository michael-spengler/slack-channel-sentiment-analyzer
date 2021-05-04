# slack-channel-sentiment-analyzer

## Execute SA Server Locally
### Prerequisites
```sh
brew install python3
```

```sh
pip3 install -r requirements.txt
```

```sh
export SLACK_BOT_TOKEN=your-token
cd server  
uvicorn main:app --reload
```



## How it Works
We created a Slack App called [Sentiment Analyzer](https://api.slack.com/apps/A01UWSD1YMT) which has the corresponding read messages of public channels permissions - see scopes file in assets folder.

We added this Slack App (via a slash command ("/invite")) in all channels for which we would like to conduct the sentiment analysis - see also screenshot in assets folder.

We took the token from "OAUTH Tokens for your Workspace".  

... Raise an issue in case of questions.
... Raise a PR in case of improvement proposals.

## Background Info
### Retrieving Messages incl. Thread Messages
https://api.slack.com/messaging/retrieving

### Potentially Helpful Links
1. https://huggingface.co/transformers/model_doc/gpt.html  
2. https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment 
3. https://huggingface.co/transformers/quicktour.html
