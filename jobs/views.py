from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Job
from .forms import CompanyForm, JobForm


def company_list(request):
    companies = Company.objects.all().order_by('-created_at')
    return render(request, 'jobs/company/company_list.html', {'companies': companies})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'jobs/company/company_detail.html', {'company': company})


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            messages.success(request, 'Kompaniya muvaffaqiyatli yaratildi!')
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm()

    return render(request, 'jobs/company/company_form.html', {
        'form': form,
        'title': 'Yangi kompaniya'
    })


@login_required
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if company.owner != request.user:
        messages.error(request, 'Sizda bu kompaniyani tahrirlash huquqi yo\'q!')
        return redirect('company_list')

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kompaniya muvaffaqiyatli yangilandi!')
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)

    return render(request, 'jobs/company/company_form.html', {
        'form': form,
        'title': 'Kompaniyani tahrirlash',
        'company': company
    })


@login_required
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if company.owner != request.user:
        messages.error(request, 'Sizda bu kompaniyani o\'chirish huquqi yo\'q!')
        return redirect('company_list')

    if request.method == 'POST':
        company.delete()
        messages.success(request, 'Kompaniya o\'chirildi!')
        return redirect('company_list')

    return render(request, 'jobs/company/company_confirm_delete.html', {'company': company})


@login_required
def my_companies(request):
    companies = Company.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'jobs/company/my_companies.html', {'companies': companies})


def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')

    category = request.GET.get('category')
    job_type = request.GET.get('job_type')
    location = request.GET.get('location')

    if category:
        jobs = jobs.filter(category__icontains=category)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'jobs/jobs/job_list.html', {
        'jobs': jobs,
        'job_types': Job.JOBTYPES,
    })


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/jobs/job_detail.html', {'job': job})


@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            messages.success(request, 'Vakansiya muvaffaqiyatli yaratildi!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()

    return render(request, 'jobs/jobs/job_form.html', {
        'form': form,
        'title': 'Yangi vakansiya'
    })


@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if job.employer != request.user:
        messages.error(request, 'Sizda bu vakansiyani tahrirlash huquqi yo\'q!')
        return redirect('job_list')

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vakansiya muvaffaqiyatli yangilandi!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/jobs/job_form.html', {
        'form': form,
        'title': 'Vakansiyani tahrirlash',
        'job': job
    })


@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if job.employer != request.user:
        messages.error(request, 'Sizda bu vakansiyani o\'chirish huquqi yo\'q!')
        return redirect('job_list')

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Vakansiya o\'chirildi!')
        return redirect('job_list')

    return render(request, 'jobs/jobs/job_confirm_delete.html', {'job': job})


@login_required
def my_jobs(request):
    jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    return render(request, 'jobs/jobs/my_jobs.html', {'jobs': jobs})