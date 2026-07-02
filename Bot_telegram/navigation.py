from collections import defaultdict

class Navigation:

    def __init__(self):
        self._history = None

    def init(self):
        self._history = defaultdict(list)

    def reset(self, chat_id):
        self._history[chat_id] = ["start"]

    def push(self, chat_id, page):
        history = self._history[chat_id]

        if not history or history[-1] != page:
            history.append(page)

    def current(self, chat_id):
        history = self._history.get(chat_id, ["start"])
        return history[-1]

    def back(self, chat_id):
        history = self._history.get(chat_id, ["start"])

        if len(history) > 1:
            history.pop()

        return history[-1]


navigation = Navigation()