from type.type import MentionEventHandlerArgs
from modules.bolt.reply import reply


def handler(args: MentionEventHandlerArgs) -> None:
    reply(
        app=args.app,
        mention_body=args.event,
        # text=f"{args.event.event.text} <@{args.event.event.user}>!",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"<@{args.event.event.user}> {args.event.event.text}",
                },
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click",
                },
            }
        ],
    )
