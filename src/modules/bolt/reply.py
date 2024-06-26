from slack_bolt import App
from slack_sdk.web.slack_response import SlackResponse
from type.type import MentionBody
from typing import Any, Optional


def reply(
    app: App,
    mention_body: MentionBody,
    text: Optional[str] = None,
    blocks: list[dict[Any, Any]] = [],
) -> SlackResponse:
    res: SlackResponse = app.client.chat_postMessage(
        channel=mention_body.event.channel,
        text=text,
        blocks=blocks,
        thread_ts=(
            mention_body.event.thread_ts
            if mention_body.event.thread_ts is not None
            else mention_body.event.ts
        ),
        unfurl_links=False,
    )
    return res
