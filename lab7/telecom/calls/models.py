from django.db import models
from django.contrib.auth.models import User

class Call(models.Model):
    city = models.CharField(max_length=100)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    call_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s" % (self.subscriber.username, self.city)

    def get_excerpt(self):
        return self.details[:140] + "..." if len(self.details) > 140 else self.details
    