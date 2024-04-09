import logging
from modules.bolt.bolt_wrapper import BoltWrapper
from modules.route.route import listen

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    BoltWrapper(listen).start()
