from django.db import models

# OneToOneField: Biron bir ob'ekt faqat bitta boshqa ob'ekt bilan bog'lanadi
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Har bir foydalanuvchiga bitta profil
    bio = models.TextField()

    def __str__(self):
        return self.user.username

# ForeignKey: Bu ob'ekt boshqa bir ob'ektga tegishli bo'lib, bir ob'ektning bir nechta nusxalari bo'lishi mumkin
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Post bir foydalanuvchiga tegishli

    def __str__(self):
        return self.title

# ManyToManyField: Bu bir nechta ob'ekt bir nechta boshqa ob'ektlar bilan bog'lanishi mumkin
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.tag.name}'
