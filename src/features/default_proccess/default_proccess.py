from type.type import MentionEventHandlerArgs
from modules.bolt.reply import reply


def handler(args: MentionEventHandlerArgs) -> None:
    reply(
        app=args.app,
        mention_body=args.event,
        text="Hel1lo, World!",
    )
