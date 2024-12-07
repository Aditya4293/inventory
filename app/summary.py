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
from .report import *
from decimal import Decimal  # Import Decimal for precise arithmetic operations
from django.utils import timezone
from collections import defaultdict
from datetime import datetime, timedelta


from django.contrib import messages


def customer_report(request):
    # Fetch customers associated with the current user
    customers = Customer.objects.filter(user=request.user)

    # Fetch packings associated with the current user
    packings = Packing.objects.filter(user=request.user)

    context = {
        'customers': customers,
        'packings': packings,
    }
    return render(request, 'summary/customer_report.html', context)


def dispatch_summary(request):
    # Fetch selected bill numbers associated with the current user
    selected_data = Selected.objects.filter(packing__user=request.user).values_list('bill_no', flat=True)

    # Fetch bundle data associated with the current user
    bundle_data = Bundle.objects.filter(bundle_entry__user=request.user, status=True, bill_no__isnull=False).select_related('bundle_entry')

    context = {
        'selected_data': selected_data,
        'bundle_data': bundle_data,
    }
    return render(request, 'summary/dispatch_summary.html', context)



def transport_report(request):
    # Fetch selected items and related data associated with the current user
    selected_items = Selected.objects.filter(packing__user=request.user, bill_no__isnull=False)

    # Fetch distinct vehicle numbers associated with the current user from packing_slip_new
    vehicle_numbers = packing_slip_new.objects.filter(user=request.user).values_list('vehicle_no', flat=True).distinct()

    # Prepare data structure to collect data for each bill_no
    data_by_bill_no = {}

    for selected in selected_items:
        bill_no = selected.bill_no
        if bill_no not in data_by_bill_no:
            data_by_bill_no[bill_no] = {
                'vehicle_no': None,
                'date': selected.date,
                'point': selected.packing.point.point if selected.packing.point else '',  # Adjusted line
                'quality': selected.packing.quality.quality_no if selected.packing.quality else '',
                'bundles': [],
                'party_name': selected.name,
                'bill_no': bill_no,
            }

    # Populate vehicle_no for each bill_no associated with the current user
    for bill_no, data in data_by_bill_no.items():
        packing_slip = packing_slip_new.objects.filter(user=request.user, bill_no=bill_no).first()
        if packing_slip:
            data['vehicle_no'] = packing_slip.vehicle_no

    # Populate bundles for each bill_no associated with the current user
    for selected in selected_items:
        bill_no = selected.bill_no
        bundles = Bundle.objects.filter(bundle_entry__id=selected.packing.id)
        for bundle in bundles:
            bundle_info = {
                'weight': bundle.weight,
            }
            data_by_bill_no[bill_no]['bundles'].append(bundle_info)

    context = {
        'data_by_bill_no': data_by_bill_no.values(),
        'vehicle_numbers': vehicle_numbers,
    }

    return render(request, 'summary/transport_report.html', context)

