from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, Project
from .forms import ProfileForm, EducationForm, ProjectForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'resume/home.html')

@login_required
def profile_create(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('education_add')
        
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'resume/profile_form.html', {'form':form})

@login_required
def education_add(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.profile = profile
            edu.save()
            return redirect('project_add')
    else:
        form = EducationForm()

    return render(request, 'resume/education_form.html', {'form':form})

@login_required
def project_add(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.profile = profile
            proj.save()
            return redirect('resume_preview')
    else:
        form = ProjectForm()

    return render(request, 'resume/project_form.html', {'form': form})


@login_required
def resume_preview(request):
    profile = Profile.objects.get(user=request.user)
    education = Education.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)

    return render(request, 'resume/resume_preview.html', {
        'profile': profile,
        'education': education,
        'projects': projects
    })

@login_required
def resume_pdf(request):
    profile = Profile.objects.get(user=request.user)
    education = Education.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)

    template = get_template('resume/resume_pdf.html')
    html = template.render({
        'profile': profile,
        'education': education,
        'projects': projects
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    pisa.CreatePDF(html, dest=response)
    return response

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_create')
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})