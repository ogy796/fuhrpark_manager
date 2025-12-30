from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, MaintenanceTicket, Driver
from .forms import TicketForm
from django.contrib.auth.decorators import login_required


@login_required
def workshop_dashboard(request):
    open_tickets = MaintenanceTicket.objects.exclude(status='done').order_by('-created_at')

    return render(request, 'fleet/workshop.html', {'tickets': open_tickets })

def vehicle_list(request):
    all_trucks = Vehicle.objects.all()
    context = {'trucks': all_trucks}

    return render(request, 'fleet/vehicle_list.html', context)

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    context = {'vehicle': vehicle}
    return render(request, 'fleet/vehicle_detail.html', context)

def add_ticket(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.vehicle = vehicle
            ticket.save()
            return redirect ('vehicle_detail', vehicle_id=vehicle.id)
        
    else:
            form = TicketForm()

    return render(request, 'fleet/add_ticket.html', {'form': form, 'vehicle': vehicle})

@login_required
def close_ticket(request, ticket_id):
     ticket = get_object_or_404(MaintenanceTicket, pk=ticket_id)

     ticket.status = 'done'
     ticket.save()

     return redirect('workshop_dashboard')