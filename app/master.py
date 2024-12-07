from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

  # Replace with your actual form import


def customer_main(request):
    customers = Customer.objects.filter(user=request.user)
    context = {
        'customers': customers,
    }
    return render(request, 'master/customer_main.html', context)

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Assign the currently logged-in user to the customer
            customer.save()
            return redirect('customer_main')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'master/edit_customer.html', {'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_main')
    return render(request, 'master/delete_customer.html', {'customer': customer})

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Assign the currently logged-in user to the customer
            customer.save()
            messages.success(request, 'Customer created successfully.')
            return redirect('customer_main')  # Replace 'index' with your actual success URL
    else:
        form = CustomerForm()

    # Define the list of states
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 
        'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 
        'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha (Orissa)', 'Punjab', 'Rajasthan', 'Sikkim', 
        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
        'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu',
        'Lakshadweep', 'Delhi (National Capital Territory of Delhi)', 'Puducherry', 'Ladakh'
    ]

    # Define cities for each state
    cities_by_state = {
        'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool'],
        'Arunachal Pradesh': ['Itanagar', 'Naharlagun'],
        'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon'],
        'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia'],
        'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Raigarh'],
        'Goa': ['Panaji', 'Margao', 'Vasco da Gama'],
        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Gandhinagar'],
        'Haryana': ['Faridabad', 'Gurgaon', 'Panipat', 'Ambala', 'Yamunanagar'],
        'Himachal Pradesh': ['Shimla', 'Mandi', 'Solan', 'Dharamshala', 'Kullu'],
        'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro Steel City', 'Deoghar'],
        'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum'],
        'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Malappuram'],
        'Madhya Pradesh': ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain'],
        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Aurangabad'],
        'Manipur': ['Imphal', 'Thoubal'],
        'Meghalaya': ['Shillong', 'Tura'],
        'Mizoram': ['Aizawl', 'Lunglei'],
        'Nagaland': ['Kohima', 'Dimapur'],
        'Odisha (Orissa)': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Berhampur', 'Sambalpur'],
        'Punjab': ['Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda'],
        'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Bikaner'],
        'Sikkim': ['Gangtok', 'Namchi'],
        'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem'],
        'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar', 'Ramagundam'],
        'Tripura': ['Agartala', 'Udaipur'],
        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Agra', 'Varanasi', 'Meerut'],
        'Uttarakhand': ['Dehradun', 'Haridwar', 'Rishikesh', 'Nainital', 'Mussoorie'],
        'West Bengal': ['Kolkata', 'Howrah', 'Durgapur', 'Asansol', 'Siliguri'],
        'Andaman and Nicobar Islands': ['Port Blair'],
        'Chandigarh': ['Chandigarh'],
        'Dadra and Nagar Haveli and Daman and Diu': ['Daman', 'Diu', 'Silvassa'],
        'Lakshadweep': ['Kavaratti'],
        'Delhi (National Capital Territory of Delhi)': ['New Delhi', 'North Delhi', 'South Delhi', 'East Delhi', 'West Delhi'],
        'Puducherry': ['Pondicherry', 'Karaikal', 'Mahe', 'Yanam'],
        'Ladakh': ['Leh', 'Kargil'],
    }

    return render(request, 'master/customer.html', {'form': CustomerForm(), 'states': states, 'cities_by_state': cities_by_state})


def quality(request):
    if request.method == 'POST':
        form = QualityForm(request.POST)
        if form.is_valid():
            quality = form.save(commit=False)
            quality.user = request.user  # Assign the current user to the 'user' field
            quality.save()
            return redirect('quality_main')  # Replace 'index' with your actual success URL
    else:
        form = QualityForm()

    return render(request, 'master/quality.html', {'form': form})

def quality_main(request):
    quality = Quality.objects.filter(user=request.user)
    context = {
        'quality': quality,
    }
    return render(request, 'master/quality_main.html', context)

def edit_quality(request, pk):
    quality = get_object_or_404(Quality, pk=pk)
    if request.method == 'POST':
        form = QualityForm(request.POST, instance=quality)
        if form.is_valid():
            quality = form.save(commit=False)
            quality.user = request.user  # Assign the current user to the 'user' field
            quality.save()
            return redirect('quality_main')
    else:
        form = QualityForm(instance=quality)
    return render(request, 'master/edit_quality.html', {'form': form, 'quality': quality})

def delete_quality(request, pk):
    quality = get_object_or_404(Quality, pk=pk)
    if request.method == 'POST':
        quality.delete()
        return redirect('quality_main')
    return render(request, 'master/delete_quality.html', {'quality': quality})


def point(request):
    if request.method == 'POST':
        form = pointForm(request.POST)
        if form.is_valid():
            point= form.save(commit=False)
            point.user=request.user
            point.save()
            return redirect('point_main')  # Replace 'index' with your actual success URL
    else:
        form = pointForm()

    return render(request, 'master/point.html', {'form': form})

def point_main(request):
    point = Point.objects.filter(user=request.user)
    context = {
        'point': point,
    }
    return render(request, 'master/point_main.html', context)

def edit_point(request, pk):
    point = get_object_or_404(Point, pk=pk)
    if request.method == 'POST':
        form = pointForm(request.POST, instance=point)
        if form.is_valid():
            point= form.save(commit=False)
            point.user=request.user
            point.save()
            return redirect('point_main')
    else:
        form = pointForm(instance=point)
    return render(request, 'master/edit_point.html', {'form': form, 'point': point})

def delete_point(request, pk):
    point = get_object_or_404(Point, pk=pk)
    if request.method == 'POST':
        point.delete()
        return redirect('point_main')
    return render(request, 'master/delete_point.html', {'point': point})



def brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand= form.save(commit=False)
            brand.user=request.user
            brand.save()            
            return redirect('brand_main')  # Replace 'index' with your actual success URL
    else:
        form = BrandForm()

    return render(request, 'master/brand.html', {'form': form})

def brand_main(request):
    brand = Brand.objects.filter(user=request.user)
    context = {
        'brand': brand,
    }
    return render(request, 'master/brand_main.html', context)

def edit_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand= form.save(commit=False)
            brand.user=request.user
            brand.save() 
            return redirect('brand_main')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'master/edit_brand.html', {'form': form, 'brand': brand})

def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_main')
    return render(request, 'master/delete_brand.html', {'brand': brand})