# Django signals do not run in the same database transaction as the caller.
# The receiver functions will execute in a separate transaction.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender='app.Model')
def my_signal_receiver(sender, instance, **kwargs):
    with transaction.atomic():
        
        instance.related_field = 'new_value'
        instance.save()

# We can trigger the signal within the transaction.