from django.db import models
from Users.models import MembroEquipe, Area
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
    title = models.CharField(max_length=255, null=True, blank=True)

    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()
    
    location = models.CharField(max_length=255)
    
    pilot_name = models.ManyToManyField(MembroEquipe, related_name='pilot_flight_logs')

    team_members = models.ManyToManyField(MembroEquipe, related_name='team_flight_logs')
    
    flight_success_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], null=True) 

    flight_objective_description = models.TextField() #########

    results = models.TextField()  

    pilot_impressions = models.TextField()

    improvements = models.TextField()

    wind_speed = models.DecimalField(max_digits=6, decimal_places=2) 

    wind_direction = models.CharField(max_length=100)  

    atmospheric_pressure = models.DecimalField(max_digits=5, decimal_places=3)  

    total_takeoff_weight = models.DecimalField(max_digits=6, decimal_places=2) 

    flight_cycles = models.PositiveIntegerField()

    telemetry_link = models.URLField()

    occurred_accident = models.BooleanField(default=False)

    def __str__(self):
        return f"Flight Log {self.id} - {self.date} by {self.pilot_name}"

class AccidentLog(models.Model):
    id = models.AutoField(primary_key=True)
    id_flightLog = models.ForeignKey(FlightLog, on_delete=models.CASCADE, related_name="accident")


    description = models.TextField()  

    damaged_parts = models.TextField() 

    damaged_parts_photo = models.URLField(null=True, blank=True) 

    def __str__(self):
        return f"Accident Log {self.id} - Flight {self.flight_log.id}"

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    meeting_date = models.DateField()
    meeting_time_begin = models.TimeField()
    meeting_time_end = models.TimeField()
    local = models.CharField(max_length=255)
    is_remote = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=False)
    other_participants = models.TextField(blank=True, null=True)
    pauta = models.CharField(blank=True, null=True, max_length=255)
    areas = models.ManyToManyField(Area)  
    # responsible = models.ManyToManyField(MembroEquipe)
     
    # def get_responsibles(self):
    #     """
    #     Retorna uma lista com os nomes de todos os responsáveis.
    #     """
    #     return [responsible.fullname for responsible in self.responsible.all()]

    def __str__(self):
        return f"Reunião: {self.title} - {self.meeting_date.strftime('%d/%m/%Y %H:%M')} - Áreas: {', '.join([area.name for area in self.areas.all()])}"
