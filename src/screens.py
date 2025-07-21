class BaseScreen:
    def __init__(self):
        pass

    def __call__(self):
        return {
            "message_text": "Text of a message.",
            "reply_keyboard": None
        }
