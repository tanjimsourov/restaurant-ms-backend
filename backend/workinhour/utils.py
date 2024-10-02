import face_recognition
import numpy as np
from .models import Person

def match_person_by_photo(image):
    img = Image.open(image)
    img_array = np.array(img)

    # Detect and encode faces in the image
    face_locations = face_recognition.face_locations(img_array)
    face_encodings = face_recognition.face_encodings(img_array, face_locations)

    if not face_encodings:
        return None  # No faces found in the CCTV footage

    target_face_encoding = face_encodings[0]

    # Compare the face encoding with all stored persons
    for person in Person.objects.all():
        if person.face_encoding:
            known_face_encoding = np.frombuffer(person.face_encoding, dtype=np.float64)
            matches = face_recognition.compare_faces([known_face_encoding], target_face_encoding, tolerance=0.6)
            if matches[0]:
                return person

    return None
