from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Instructor, Subject, Lecture, Exam, Grade
from .serializers import StudentSerializer, InstructorSerializer, SubjectSerializer, LectureSerializer, ExamSerializer, GradeSerializer

# Create your views here.
@api_view(['GET'])
def student_detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

@api_view(['GET'])
def instructor_detail(request, instructor_id):
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
        serializer = InstructorSerializer(instructor)
        return Response(serializer.data)
    except Instructor.DoesNotExist:
        return Response({"error": "Instructor not found"}, status=404)

@api_view(['GET'])
def subject_detail(request, subject_id):
    try:
        subject = Subject.objects.get(pk=subject_id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found"}, status=404)

@api_view(['GET'])
def lecture_detail(request, lecture_id):
    try:
        lecture = Lecture.objects.get(pk=lecture_id)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)
    except Lecture.DoesNotExist:
        return Response({"error": "Lecture not found"}, status=404)

@api_view(['GET'])
def exam_detail(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)
    except Exam.DoesNotExist:
        return Response({"error": "Exam not found"}, status=404)

@api_view(['GET'])
def grade_detail(request, grade_id):
    try:
        grade = Grade.objects.get(pk=grade_id)
        serializer = GradeSerializer(grade)
        return Response(serializer.data)
    except Grade.DoesNotExist:
        return Response({"error": "Grade not found"}, status=404)