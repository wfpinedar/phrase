import time
from plyer import notification


def notify_me(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'happy.ico',
        timeout=20,

    )
