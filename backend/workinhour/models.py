from django.db import models
from django.utils import timezone
import face_recognition
from PIL import Image
import numpy as np


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='person_photos/')
    face_encoding = models.BinaryField(blank=True, null=True)  # Store face encoding as binary
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            img = np.array(img)
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)

            if face_encodings:
                self.face_encoding = face_encodings[0].tobytes()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CCTVCamera(models.Model):
    location = models.CharField(max_length=100)
    camera_id = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.camera_id} - {self.location}'


class CCTVFootage(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField()
    camera = models.ForeignKey(CCTVCamera, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cctv_footage/')
    is_entry = models.BooleanField(default=True)  # True for entry, False for exit

    def __str__(self):
        return f"{self.person} - {self.camera} - {'Entry' if self.is_entry else 'Exit'} - {self.timestamp}"
