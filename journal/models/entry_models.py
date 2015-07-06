from django.db import models

# The following are used for activity and entry logging.


class Entry(models.Model):
    """Entry object used for journaling"""
    ENTRY_TYPES = (
        ('T', 'Text'),
        ('I', 'Image'),
        ('V', 'Video'),
        ('L', 'Link'),
    )
    stu_email = models.EmailField()
    activity_pk = models.CharField(max_length=30)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=1, choices=ENTRY_TYPES)
    entry = models.TextField()
    # if entry_type == 'T':
    #     entry = models.TextField()
    # elif entry_type == 'I':
    #     entry = models.ImageField()
    # elif entry_type == 'V':
    #     entry = models.URLField()  # Web links to Youtube or else where
    # elif entry_type == 'L':
    #     entry = models.URLField()  # Web links to Youtube or else where

    def __str__(self):
        return str(self.last_modified) + ' : ' + self.entry
