from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .forms import JobForm



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

    return render(request, 'jobs/jobs/my-postings.html', {
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
            messages.success(request, 'Job posting created successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()

    return render(request, 'jobs/jobs/job_form.html', {
        'form': form,
        'title': 'New Job Posting'
    })


@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if job.employer != request.user:
        messages.error(request, 'You do not have permission to edit this job posting!')
        return redirect('my-postings')

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job posting updated successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/jobs/job_form.html', {
        'form': form,
        'title': 'Edit Job Posting',
        'job': job
    })


@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if job.employer != request.user:
        messages.error(request, 'You do not have permission to delete this job posting!')
        return redirect('my-postings')

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job posting deleted successfully!')
        return redirect('my-postings')

    return render(request, 'jobs/jobs/job_confirm_delete.html', {'job': job})


@login_required
def my_jobs(request):
    jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    return render(request, 'jobs/jobs/my_jobs.html', {'jobs': jobs})