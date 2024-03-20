from django.db import models

# Create your models here.
# 학생 모델
class Student(models.Model):
    name = models.CharField(max_length=100)

# 강사 모델
class Instructor(models.Model):
    name = models.CharField(max_length=100)

# 교과목 모델
class Subject(models.Model):
    name = models.CharField(max_length=100)

# 강의 모델
class Lecture(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

# 시험 모델
class Exam(models.Model):
    name = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

#성적 모델
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)