from django.db import models
from app1.models import CustomUser  # Import CustomUser from app1
from PIL import Image
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    def save(self, *args, **kwargs):
        kwargs['force_insert'] = kwargs.get('force_insert', False)
        super().save(*args, **kwargs)
        if self.image and hasattr(self.image, 'path') and self.image.path != 'default.jpg':  # Check if image is not default.jpg
            try:
                img = Image.open(self.image.path)
                if img.width > 300 or img.height > 300:
                    dimension = (300, 300)
                    img.thumbnail(dimension)
                    img.save(self.image.path)
            except FileNotFoundError:
                pass 
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
