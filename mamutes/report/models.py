from django.db import models
from Users.models import MembroEquipe
from django.core.validators import MinValueValidator, MaxValueValidator

class Minutes(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    responsible = models.ForeignKey(MembroEquipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class FlightLog(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    document_username = models.CharField(max_length=255)
    pilot_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    team_members = models.TextField()  
    flight_success_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) 
    flight_objective_description = models.TextField() #########
    results = models.TextField()  
    pilot_impressions = models.TextField()
    improvements = models.TextField()
    wind_speed = models.DecimalField(max_digits=4, decimal_places=3) 
    wind_direction = models.CharField(max_length=100)  
    atmospheric_pressure = models.DecimalField(max_digits=4, decimal_places=3)  
    total_takeoff_weight = models.DecimalField(max_digits=4, decimal_places=3) 
    flight_cycles = models.PositiveIntegerField()
    telemetry_link = models.URLField()
    occurred_accident = models.BooleanField(default=False)

    def __str__(self):
        return f"Flight Log {self.id} - {self.date} by {self.pilot_name}"

class AccidentLog(models.Model):
    id = models.AutoField(primary_key=True)
    id_flightLog = models.ForeignKey(FlightLog, on_delete=models.CASCADE)
    description = models.TextField()  
    damaged_parts = models.TextField() 
    damaged_parts_photo = models.URLField() 
    was_turbulent = models.BooleanField(default=False)  
    pilot_flight_count = models.PositiveIntegerField()  
    pilot_impressions = models.TextField()  

    def __str__(self):
        return f"Accident Log {self.id} - Flight {self.flight_log.id}"





