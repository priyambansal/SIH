from django.shortcuts import render

# Create your views here.
def WhyStudyInIndia(request):
	return render(request, 'StudyInIndia/why_study_in_india.html')

def StudyPermits(request):
	return render(request, 'StudyInIndia/study_permits.html')
	
def Scholarship(request):
	return render(request, 'StudyInIndia/scholarship.html')

def WorkOpp(request):
	return render(request, 'StudyInIndia/work_opp.html')

