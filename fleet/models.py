from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True, verbose_name="Kennzeichen")
    brand_model = models.CharField(max_length=100, verbose_name="Hersteller & Model")
    year_of_manufacture = models.IntegerField(verbose_name="Baujahr")
    last_service = models. DateField(null=True, blank=True, verbose_name="Letzter Service")
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fahrer")
    

    def __str__(self):
        return f"{self.license_plate} ({self.brand_model})"

class Driver(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Vorname")
    last_name = models.CharField(max_length=50, verbose_name="Nachname")
    license_number = models.CharField(max_length=50, unique=True, verbose_name="Führerschein-Nr.1")
    license_expiry = models.DateField(verbose_name="Ablaufdatum Führerschein")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    

class MaintenanceTicket(models.Model):
    STATUS_CHOICES = [
        ('new', 'Neu / Offen'),
        ('in_progress', 'In Bearbeitung'),
        ('done', 'Erledigt')
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name="Betroffenes Fahrzeug")

    title = models.CharField(max_length=100, verbose_name="Problem (Titel)")
    description = models.TextField(verbose_name="Detaillierte Beschreibung")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Erstellt am")

    def __str__(self):
        return f"Ticket: {self.title} ({self.vehicle.license_plate})"
    
    


    
