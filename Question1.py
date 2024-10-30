
# Django signals are executed synchronously.
# When a signal is sent, the execution of the current code pauses until
# all the connected receivers have finished processing the signal.

# Code : 
from django.db.models.signals import post_save
from django.dispatch import receiver

def slow_task():
    import time
    time.sleep(5)

@receiver(post_save, sender='app.Model')
def my_signal_receiver(sender, instance, **kwargs):
    slow_task()

# We can trigger the signal by saving an instance of Model
