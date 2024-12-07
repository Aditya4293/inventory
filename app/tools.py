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
from django.utils.timezone import make_aware
from django.views.decorators.http import require_POST



from django.contrib import messages


def packing_slip_new(request):
    if request.method == 'POST':
        form = Packing_slip_new(request.POST)
        if form.is_valid():
            packing_slip = form.save(commit=False)
            packing_slip.user = request.user  # Assign the current user to the 'user' field
            packing_slip.save()
            return redirect('index')  # Replace 'index' with the URL you want to redirect to after successful form submission
    else:
        form = Packing_slip_new()
    
    # Fetch selected data associated with the current user
    selected_data = Selected.objects.filter(packing__user=request.user).values_list('bill_no', 'date')

    context = {
        'selected_data': selected_data,
        'form': form,
    }
    return render(request, 'tools/packing_slip_new.html', context)



def packing_slip(request):
    # Fetch selected bill numbers associated with the current user
    selected_data = Selected.objects.filter(packing__user=request.user).values_list('bill_no', flat=True)

    # Fetch bundle data associated with the current user
    bundle_data = Bundle.objects.filter(bundle_entry__user=request.user, status=True, bill_no__isnull=False)
    
    # Convert bundle_data queryset to a list if needed
    bundle_data_list = list(bundle_data)

    context = {
        'selected_data': selected_data,
        'bundle_data': bundle_data_list,
    }
    return render(request, 'tools/packing_slip.html', context)



def remove_data(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')

        if selected_date:
            # Perform deletion of records before the selected date
            # Example logic to delete Packing records older than the selected date
            packings_to_delete = Packing.objects.filter(user=request.user, date_packing__lt=selected_date)
            packings_to_delete.delete()

            # Redirect to the same page or any desired URL after deletion
            return redirect('remove_data')  # Redirect to the same view or modify the URL

    # Handle GET requests here
    # Fetch packings associated with the current user
    packings = Packing.objects.filter(user=request.user)
    
    return render(request, 'tools/remove_data.html', {'packings': packings})