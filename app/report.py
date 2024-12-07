from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import *
from .master import *
from .models import *
from .entry import *
from .modify import *
from decimal import Decimal  # Import Decimal for precise arithmetic operations
from django.utils import timezone
from collections import defaultdict
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


from django.contrib import messages


@login_required
def packing_book(request):
    packings = Packing.objects.filter(user=request.user)
    return render(request, 'report/packing_book.html', {'packings': packings})

@login_required
def stock_book(request):
    packings = Packing.objects.prefetch_related('bundles').filter(bundles__status=False, user=request.user).distinct()
    return render(request, 'report/stock_book.html', {'packings': packings})

@login_required
def dispatch_book(request):
    packings = Packing.objects.prefetch_related('bundles').filter(bundles__status=True, user=request.user).distinct()
    selected = Selected.objects.filter(packing__user=request.user)
    return render(request, 'report/dispatch_book.html', {'packings': packings, 'selected': selected})

@login_required
def size_book(request):
    packings = Packing.objects.filter(user=request.user)
    sizes = Packing.objects.filter(user=request.user).values_list('bundles__sizes', flat=True).distinct()
    return render(request, 'report/size_book.html', {'packings': packings, 'sizes': sizes})

@login_required
def stock_summary(request):
    packings = Packing.objects.prefetch_related('bundles').filter(user=request.user).all()
    brands = Brand.objects.filter(user=request.user)

    grouped_data = {}
    for packing in packings:
        for bundle in packing.bundles.all():
            key = (packing.point, packing.quality, packing.brand.brand)
            if key not in grouped_data:
                grouped_data[key] = {
                    'point': packing.point,
                    'quality': packing.quality,
                    'sizes_weights': {},
                    'count': 0,
                    'total_weight': Decimal(0),
                    'brand': packing.brand.brand,
                }
            size = bundle.sizes
            weight = Decimal(bundle.weight)
            if size in grouped_data[key]['sizes_weights']:
                grouped_data[key]['sizes_weights'][size] += weight
            else:
                grouped_data[key]['sizes_weights'][size] = weight

            grouped_data[key]['count'] += 1
            grouped_data[key]['total_weight'] += weight

    grouped_data_list = list(grouped_data.values())

    return render(request, 'report/stock_summary.html', {'packings': grouped_data_list, 'brands': brands})

@login_required
def lot_summary(request):
    date_filter = request.GET.get('date', None)
    if date_filter:
        date_filter = datetime.strptime(date_filter, '%Y-%m-%d')
    else:
        date_filter = timezone.now()

    packings = Packing.objects.prefetch_related('bundles').filter(date_packing__lte=date_filter, user=request.user).all()
    brands = Brand.objects.all()

    grouped_data = {}
    for packing in packings:
        key = (packing.lot_no, packing.point, packing.quality)
        if key not in grouped_data:
            grouped_data[key] = {
                'date_packing': packing.date_packing,
                'lot_no': packing.lot_no,
                'point': packing.point,
                'quality': packing.quality,
                'sizes_weights': {},
                'count': 0,
                'total_weight': Decimal(0),
            }
        for bundle in packing.bundles.all():
            size = bundle.sizes
            weight = Decimal(bundle.weight)
            if size in grouped_data[key]['sizes_weights']:
                grouped_data[key]['sizes_weights'][size] += weight
            else:
                grouped_data[key]['sizes_weights'][size] = weight

            grouped_data[key]['count'] += 1
            grouped_data[key]['total_weight'] += weight

    for item in grouped_data.values():
        item['sizes_weights'] = ', '.join(f'{size}={weight}' for size, weight in item['sizes_weights'].items())

    grouped_data_list = list(grouped_data.values())

    return render(request, 'report/lot_summary.html', {'packings': grouped_data_list, 'brands': brands})

@login_required
def production_register(request):
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    else:
        start_date = timezone.now() - timezone.timedelta(days=365)
        end_date = timezone.now()

    packings = Packing.objects.prefetch_related('bundles').filter(date_packing__range=(start_date, end_date), user=request.user).all()
    brands = Brand.objects.all()

    data_by_date = defaultdict(list)
    for packing in packings:
        for bundle in packing.bundles.all():
            item = {
                'date_packing': packing.date_packing,
                'lot_no': packing.lot_no,
                'weight': Decimal(bundle.weight),
                'bundle': bundle.bundle,
                'quality': packing.quality,
                'point': packing.point,
                'brand': packing.brand,
            }
            data_by_date[packing.date_packing].append(item)

    grouped_data = []
    for date_packing, items in data_by_date.items():
        date_total_weight = sum(item['weight'] for item in items)
        date_total_bundles = len(items)
        for item in items:
            grouped_data.append(item)

        grouped_data.append({
            'date_packing': date_packing,
            'lot_no': 'Total',
            'weight': date_total_weight,
            'bundle': date_total_bundles,
            'quality': '',
            'point': '',
            'brand': ''
        })

    return render(request, 'report/production_register.html', {'packings': grouped_data, 'brands': brands})

@login_required
def lot_register(request):
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    else:
        start_date = timezone.now() - timezone.timedelta(days=365)
        end_date = timezone.now()

    packings = Packing.objects.prefetch_related('bundles').filter(date_packing__range=(start_date, end_date), user=request.user).all()[:5]

    data_by_date = defaultdict(list)
    for packing in packings:
        for bundle in packing.bundles.all():
            pack_kgs = packing.total_weight if packing.total_weight else 0
            lot_weight = packing.lot_kgs if packing.lot_kgs else 0
            shortage = lot_weight - float(pack_kgs) if lot_weight else 0
            percentage = (shortage / lot_weight) * 100 if lot_weight else 0

            item = {
                'lot_no': packing.lot_no,
                'quality': packing.quality,
                'lot_weight': lot_weight,
                'sheet': bundle.sheet,
                'bundle': bundle.bundle,
                'pack_kgs': pack_kgs,
                'shortage': shortage,
                'percentage': percentage,
            }
            data_by_date[packing.date_packing].append(item)

    grouped_data = []
    for date_packing, items in data_by_date.items():
        date_total_weight = sum(item['lot_weight'] for item in items)
        date_total_bundles = len(items)
        for item in items:
            grouped_data.append(item)

        grouped_data.append({
            'lot_no': 'Total',
            'quality': '',
            'lot_weight': date_total_weight,
            'sheet': '',
            'bundle': date_total_bundles,
            'pack_kgs': '',
            'shortage': '',
            'percentage': ''
        })

    return render(request, 'report/lot_register.html', {'packings': grouped_data})