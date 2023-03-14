from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
        # added dependency to enable using models from app2 in move_m1
        # ('news_app', '0004_foobar'),
    ]
