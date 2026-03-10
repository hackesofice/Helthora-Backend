from django.db import models


class Users(models.Model):

    ROLE_CHOICES = [
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("admin", "Admin"),
    ]

    user_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=10, unique=True)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Doctors(models.Model):

    DAYS = [
        ("SUN", "Sunday"),
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
    ]

    user = models.OneToOneField(Users, on_delete=models.CASCADE)

    specialization = models.CharField(max_length=50)
    experience = models.IntegerField()

    qualifications = models.CharField(max_length=500)

    clinic_name = models.CharField(max_length=50)
    clinic_address = models.CharField(max_length=100)

    consultation_fee = models.PositiveSmallIntegerField()

    available_day = models.CharField(
        max_length=3,
        choices=DAYS
    )

    available_from = models.TimeField()
    available_till = models.TimeField()

    rating_avg = models.FloatField(default=0)
    total_reviews = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.name


class DoctorsReviews(models.Model):
    # Ratings from patients to doctors

    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Users, on_delete=models.CASCADE)

    rating = models.SmallIntegerField()
    comment = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.user.name}"


class PatientsReviews(models.Model):
    # Ratings from doctors to patients

    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Users, on_delete=models.CASCADE)

    rating = models.SmallIntegerField()
    comment = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.user.name} -> {self.patient.name}"


class Messages(models.Model):

    sender = models.ForeignKey(
        Users,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        Users,
        related_name="received_messages",
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=500)

    is_read = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} -> {self.receiver.name}"