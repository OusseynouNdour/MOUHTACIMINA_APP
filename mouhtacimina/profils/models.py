from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class MemberType(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.type_name

class Member(models.Model):
    class Ufr(models.TextChoices):
        SAT = 'SAT',
        SEG = 'SEG',
        IPSL = 'IPSL',
        Sante = '2S',
        AGRO = '2SATA',
        DROIT = 'SJP',
        Langue = 'LSH',
        TEACH = 'SEFS',
        SPORT = 'STAPS'

    class Martial_status(models.TextChoices):
        Marie = 'Marié',
        Celib = 'Célibataire'

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    member_type = models.ForeignKey(MemberType, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(auto_now_add=True)
    address = models.fields.CharField(max_length=100)
    study_level = models.fields.CharField(max_length=20)
    ufr = models.fields.CharField(choices=Ufr.choices, max_length=5)
    speciality = models.fields.CharField(max_length=20)
    promo = models.fields.CharField(max_length=3)
    statut = models.fields.CharField(max_length=20)
    activity = models.fields.CharField(max_length=20)
    Marital_status = models.fields.CharField(choices=Martial_status.choices,max_length=12)

    def __str__(self):
        return self.username

