from django.db import models


# Create your models here.

class Bookmark(models.Model):
    user_uuid = models.UUIDField(null=False, blank=False)
    document_uuid = models.UUIDField(null=False, blank=False)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookmarks'
        constraints = [
            models.UniqueConstraint(fields=['user_uuid', 'document_uuid'], name='bookmark')
        ]


class Upload(models.Model):
    document_uuid = models.UUIDField(primary_key=True, unique=True, null=False, blank=False)
    user_uuid = models.UUIDField(null=False, blank=False)
    upload_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'uploads'


class Rate(models.Model):
    user_uuid = models.UUIDField(null=False, blank=False)
    document_uuid = models.UUIDField(null=False, blank=False)
    rate_value = models.IntegerField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rates'
        constraints = [
            models.UniqueConstraint(fields=['user_uuid', 'document_uuid'], name='rate')
        ]


class DocumentAuthor(models.Model):
    document_uuid = models.UUIDField(null=False, blank=False)
    author_uuid = models.UUIDField(null=False, blank=False)

    class Meta:
        db_table = 'document_author'
        constraints = [
            models.UniqueConstraint(fields=['document_uuid', 'author_uuid'], name='authors_of_documents')
        ]
