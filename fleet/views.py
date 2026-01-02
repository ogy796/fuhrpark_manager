from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, MaintenanceTicket, Driver
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import FileResponse
from fpdf import FPDF
import io


@login_required
def workshop_dashboard(request):
    open_tickets = MaintenanceTicket.objects.exclude(status='done').order_by('-created_at')

    return render(request, 'fleet/workshop.html', {'tickets': open_tickets })

def vehicle_list(request):
    search_query = request.GET.get('q')

    if search_query:
        all_trucks = Vehicle.objects.filter(
             Q(license_plate__icontains=search_query) |
             Q(brand_model__icontains=search_query)
        )
    else:
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

def create_vehicle_pdf(request, pk):
    truck = get_object_or_404(Vehicle, pk=pk)
    tickets = truck.maintenanceticket_set.all().order_by('-created_at')

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", style='B', size=20)
    pdf.cell(text=f"Fahrzeug-Akte: {truck.license_plate}", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(10)

    pdf.set_font("Helvetica", style='B', size=14)
    pdf.cell(text="Fahrzeug-Daten", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", size=12)
    pdf.ln(4)

    pdf.cell(text=f"Modell: {truck.brand_model}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(text=f"Baujahr: {truck.year_of_manufacture}", new_x="LMARGIN", new_y="NEXT")

    if truck.last_service:
        pdf.cell(text=f"Letzter Service: {truck.last_service}", new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.cell(text="Letzter Service: Noch nie durchgeführt", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    if truck.driver:
        pdf.cell(text=f"Aktueller Fahrer: {truck.driver} (ID: {truck.driver.license_number})", new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.cell(text="Aktueller Fahrer: -- Nicht zugewiesen --", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(15)

    pdf.set_font("Helvetica", style='B', size=14)
    pdf.cell(text="Wartungs-Historie & Schäden", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("Helvetica", size=10)

    if tickets:
        for ticket in tickets:
            datum = ticket.created_at.strftime('%d.%m.%Y')
            status = ticket.get_status_display()

            pdf.set_font("Helvetica", style='B', size=11)
            pdf.cell(text=f"[{datum}] {ticket.title} -- Status: {status}", new_x="LMARGIN", new_y="NEXT")

            pdf.set_font("Helvetica", size=10)
            pdf.multi_cell(w=0, h=5, text=f"Beschreibung: {ticket.description}")

            pdf.ln(5)
    else:
        pdf.cell(text="Keine Einträge in der Historie verbunden.", new_x="LMARGIN", new_y="NEXT")

    pdf_bytes = pdf.output()
    return FileResponse(io.BytesIO(pdf_bytes), as_attachment=True, filename=f"Akte_{truck.license_plate}.pdf")
