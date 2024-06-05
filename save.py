import os
import pickle


class Save:

    def load_game(self):
        if os.path.getsize('save.pickle') > 0:
            with open("save.pickle", "rb") as file:
                p2 = pickle.load(file)
                return p2

    def save_game(self, user):
        with open("save.pickle", "wb") as file:
            pickle.dump(user, file)
