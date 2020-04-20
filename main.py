import time
from notes import notify_me
from config import PHRASES_SITE
from get_phrases import get_phrases

if __name__ == "__main__":
    while True:
        mensajes = get_phrases(PHRASES_SITE)
        for m in mensajes:
            if len(m) > 1:
                notify_me(m['author'], m['phrase'])
            time.sleep(300)
