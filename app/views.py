from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.http import HttpResponse
from .models import SCHOOL
from .serializer import SchoolSerializer


def home(request):
    return render(request, 'home.html')

def school_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year_of_establishment = request.POST.get('year_of_establishment')
        location = request.POST.get('location')
        image = request.FILES.get('image')

        school = SCHOOL(
            name=name,
            year_of_establishment=year_of_establishment,
            location=location,
            image=image
        )
        school.save()
        return HttpResponse("School information saved successfully.")
    return render(request, 'school_form.html')

# /use drf for makeing api
class SchoolDataAPI(APIView):
    def get(self, request):
        schools = SCHOOL.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)