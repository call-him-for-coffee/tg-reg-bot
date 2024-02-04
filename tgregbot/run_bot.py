import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tgregbot.settings')
django.setup()

from mainapp.tgbot.bot import run

if __name__ == "__main__":
    run()