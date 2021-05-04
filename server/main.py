from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from slack_client import get_channels, get_messages

from sentiment_analyzer import get_sentiment

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
  channels = get_channels()
  return templates.TemplateResponse("index.html", {"request": request, "channels": channels})

@app.get("/channel/{slack_channel_id}", response_class=HTMLResponse)
async def channel_page(request: Request, slack_channel_id: str):
  messages = get_messages(slack_channel_id)
  summary = 0
  for message in messages:
    currentSentiment = get_sentiment(message['text'])
    summary = summary + currentSentiment
    message['sentiment'] = currentSentiment

  summary = summary / len(messages)
# weighted sentiment - more current messages shall have a higher weighe    
  return templates.TemplateResponse("channel.html", {"request": request, "messages": messages, "summary": summary})
