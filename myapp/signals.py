from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import requests

# TELEGRAM CONFIG
BOT_TOKEN = '7442741034:AAHsSXiYWtHJUFZRidYRHIgScS5HKL_5ODY'
CHAT_ID = '7741631841'

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
    }
    requests.post(url, data=data)

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        # Avtomatik Profile yaratish
        from .models import Profile
        Profile.objects.create(user=instance)

        # Telegramga xabar yuborish
        send_telegram(f"🆕 Yangi foydalanuvchi: {instance.username}")
