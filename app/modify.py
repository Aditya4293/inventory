from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .master import *
from .models import *
from .entry import *
from .modify import *


from django.contrib import messages


def modify_packing(request):
    if request.user.is_authenticated:
        user = request.user
        packings = Packing.objects.filter(user=user).order_by('date_packing')
        return render(request, 'modify/modify_packing.html', {'packings': packings})


def edit_packing(request, pk):
    packing = get_object_or_404(Packing, pk=pk)
    bundle_instances = packing.bundles.all()

    if request.method == 'POST':
        packing_form = PackingForm(request.POST, instance=packing)
        bundle_forms = [BundleForm(request.POST, instance=bundle) for bundle in bundle_instances]
        
        if packing_form.is_valid() and all(bundle_form.is_valid() for bundle_form in bundle_forms):
            packing_form.save()  # Save changes to the Packing instance
            for bundle_form in bundle_forms:
                bundle_form.save()  # Save changes to each Bundle instance
            return redirect('modify_packing')  # Redirect back to modify_packing URL
    else:
        packing_form = PackingForm(instance=packing)
        bundle_forms = [BundleForm(instance=bundle) for bundle in bundle_instances]

    context = {
        'packing': packing,
        'packing_form': packing_form,
        'bundle_forms': bundle_forms,
    }

    return render(request, 'modify/edit_packing.html', context)

def delete_bundle(request, bundle_id):
    bundle = get_object_or_404(Bundle, id=bundle_id)
    
    if request.method == 'DELETE':
        bundle.delete()
        return JsonResponse({'message': 'Bundle deleted successfully.'}, status=204)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


def modify_dispatch(request):
    # Filter packings based on whether they have a related Selected entry
    packings = Packing.objects.filter(user=request.user, selected__isnull=False).order_by('date_packing')
    return render(request, 'modify/modify_dispatch.html', {'packings': packings})

def edit_dispatch(request, pk):
    packing = get_object_or_404(Packing, pk=pk, user=request.user)
    selected_instance, created = Selected.objects.get_or_create(packing=packing)

    if request.method == 'POST':
        selected_form = SelectedForm(request.POST, instance=selected_instance)
        if selected_form.is_valid():
            selected_form.save()
            return redirect('modify_dispatch')  # Redirect back to modify_dispatch URL after saving
    else:
        selected_form = SelectedForm(instance=selected_instance)

    return render(request, 'modify/edit_dispatch.html', {'selected_form': selected_form})


def recall_dispatch(request, packing_id):
    if request.method == 'POST':
        try:
            packing = Packing.objects.get(pk=packing_id)
            for bundle in packing.bundles.all():
                bundle.status = False
                bundle.save()
            packing.selected_set.all().delete()
            messages.success(request, "Dispatch recalled successfully.")
            return redirect('modify_dispatch')
        except Packing.DoesNotExist:
            messages.error(request, "Packing record not found.")
            return redirect('index')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('modify_dispatch')
