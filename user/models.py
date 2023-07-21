from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User, Permission


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        staff_group = Group.objects.get(name='Staff')
        if not self.user.groups.filter(name='Staff').exists():
            self.user.groups.add(staff_group)
            self.user.user_permissions.set(staff_group.permissions.all())
        super().save(*args, **kwargs)
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        doctor_group = Group.objects.get(name='Doctor')
        if not self.user.groups.filter(name='Doctor').exists():
            self.user.groups.add(doctor_group)
            self.user.user_permissions.set(doctor_group.permissions.all())
        super().save(*args, **kwargs)

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        staff_group = Group.objects.get(name='Vendor')
        if not self.user.groups.filter(name='Vendor').exists():
            self.user.groups.add(staff_group)
            self.user.user_permissions.set(staff_group.permissions.all())
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ManyToManyField('Image')
    videos = models.ManyToManyField('Video')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

class Video(models.Model):
    video = models.FileField(upload_to='post_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        patient_group = Group.objects.get(name='Patient')
        if not self.user.groups.filter(name='Patient').exists():
            self.user.groups.add(patient_group)
            self.user.user_permissions.set(patient_group.permissions.all())
        super().save(*args, **kwargs)
