import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Register, RegisterPage

def health_check(request):
    return JsonResponse({"status": "ok"})

def dashboard(request):
    today = timezone.now().date()
    register_pages = RegisterPage.objects.filter(date=today).select_related('register').prefetch_related(
        'temperature_logs', 'calibration_logs', 'waste_logs'
    )
    return render(request, 'registers/dashboard.html', {'register_pages': register_pages, 'today': today})

def register_list(request):
    registers = Register.objects.all()
    today = timezone.now().date()
    return render(request, 'registers/register_list.html', {'registers': registers, 'today': today})

def register_date_detail(request, register_id, year, month, day):
    date = datetime.date(year, month, day)
    register_page = get_object_or_404(
        RegisterPage.objects.select_related('register').prefetch_related(
            'temperature_logs', 'calibration_logs', 'waste_logs'
        ),
        register_id=register_id,
        date=date
    )
    return render(request, 'registers/register_date_detail.html', {'register_page': register_page})

def daily_bundle(request):
    today = timezone.now().date()
    register_pages = RegisterPage.objects.filter(date=today).select_related('register')
    return render(request, 'registers/daily_bundle.html', {'register_pages': register_pages, 'date': today})

def weekly_bundle(request):
    today = timezone.now().date()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)
    register_pages = RegisterPage.objects.filter(
        date__range=[start_of_week, end_of_week]
    ).select_related('register').order_by('date', 'register__name')
    return render(request, 'registers/weekly_bundle.html', {
        'register_pages': register_pages,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week
    })

def pending_due_bundle(request):
    today = timezone.now().date()
    # For now, "pending" means all pages due up to and including today.
    # A more advanced implementation might filter out "completed" pages.
    register_pages = RegisterPage.objects.filter(date__lte=today).select_related('register').order_by('date', 'register__name')
    return render(request, 'registers/pending_due_bundle.html', {'register_pages': register_pages})
