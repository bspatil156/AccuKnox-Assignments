
#  Django signals are executed in the same thread as the caller.
#  Receiver functions are called within the same thread of execution.

import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal receiver thread ID: {threading.get_ident()}")

@receiver(post_save, sender='app.Model')
def my_signal_receiver(sender, instance, **kwargs):
    my_signal_receiver(sender, instance, **kwargs)

# We can trigger the signal by saving an instance of Model