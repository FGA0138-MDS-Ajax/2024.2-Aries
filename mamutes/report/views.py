import profile
from django.http import JsonResponse
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import AccidentLog, FlightLog,Meeting,Area,MembroEquipe
from .forms import FlightForm,MeetingsForm
from django.contrib.auth.decorators import login_required

# Listar todos os voos
def flight_list(request):
    flight = FlightLog.objects.all()
    return render(request, 'report/flight_list.html', {'flights': flight})


from django.shortcuts import render, redirect
from .models import FlightLog

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import FlightLog, AccidentLog  # Certifique-se de importar os modelos corretos

@login_required
def flights(request):

    flights = FlightLog.objects.all()
    count_flights = FlightLog.objects.all().count()
    count_accidents = FlightLog.objects.filter(occurred_accident = True).count()
    sum_stars = FlightLog.objects.aggregate(Sum('flight_success_rating'))['flight_success_rating__sum']

    if sum_stars != 0:
        mid_sucess = sum_stars/count_flights
    else: 
        mid_sucess= 0
    mid_sucess = round(mid_sucess, 2)
    if count_flights != 0:
        accidents_percentage = (count_accidents / count_flights) * 100
        accidents_percentage = round(accidents_percentage, 2)
    else: 
        accidents_percentage = 0

    profiles = MembroEquipe.objects.all()

    context = {
        'flights': flights,
        'profiles': profiles,
        'count_flights': count_flights,
        'count_accidents': count_accidents,
        'accidents_percentage':  accidents_percentage,
        'mid_sucess':mid_sucess
    }
    if request.method == 'POST':
        filter_search = request.POST.get('search')
        print(filter_search)
        flights = FlightLog.objects.filter(title__icontains=filter_search)
        context['flights'] = flights
        return render(request, 'flights.html', context)
    return render(request, 'flights.html', context)



def flight_create(request):
    if request.method == 'POST':
        occurred_accident = request.POST.get('occurred_accident') == 'on'  # Converte direto para booleano
        print(occurred_accident)

        try:
            # Criando o objeto FlightLog e salvando no banco
            flight_log = FlightLog.objects.create(
                title=request.POST.get('title'),
                date=request.POST.get('date'),
                start_time=request.POST.get('start_time'),
                end_time=request.POST.get('end_time'),
                location=request.POST.get('location'),
                flight_objective_description=request.POST.get('flight_objective_description'),
                results=request.POST.get('results'),
                pilot_impressions=request.POST.get('pilot_impressions'),
                improvements=request.POST.get('improvements'),
                wind_speed=request.POST.get('wind_speed'),
                wind_direction=request.POST.get('wind_direction'),
                atmospheric_pressure=request.POST.get('atmospheric_pressure'),
                total_takeoff_weight=request.POST.get('total_takeoff_weight'),
                flight_cycles=request.POST.get('flight_cycles'),
                telemetry_link=request.POST.get('telemetry_link'),
                occurred_accident=occurred_accident,
                flight_success_rating = request.POST.get('stars') or 0,
            )

            # Adicionando membros da equipe ao FlightLog
            team_members = request.POST.get('responsibles')
            

            if team_members:
                team_members_ids = [int(id.strip()) for id in team_members.split(',') if id.strip().isdigit()]
                flight_log.team_members.set(team_members_ids)  # Define os membros corretamente
            
            print(f"FlightLog criado com ID: {flight_log.id}")

            # Criando log de acidente se necessário
            if occurred_accident:
                AccidentLog.objects.create(
                    id_flightLog=flight_log,
                    description=request.POST.get('descriptionAccident'),
                    damaged_parts=request.POST.get('damaged_parts'),
                    damaged_parts_photo=request.POST.get('damaged_parts_photo')  # Corrigido para usar FILES corretamente
                )

            return redirect('flights')  # Redireciona corretamente

        except Exception as e:
            print(f"Erro ao criar o flight log: {e}")
            return HttpResponseBadRequest("Ocorreu um erro ao criar o log de voo.")

    return render(request, 'flights.html')  # Renderiza a página em caso de GET

# Editar um voo existente
def flight_edit(request, id):
    flight = get_object_or_404(FlightLog, id=id)
    profiles = MembroEquipe.objects.all()

    # Tenta obter um log de acidente relacionado ao voo, se existir
    accident_log = AccidentLog.objects.filter(id_flightLog=flight).first()

    if request.method == 'POST':
        try:
            flight.title = request.POST.get('title')
            flight.date = request.POST.get('date')
            flight.start_time = request.POST.get('start_time')
            flight.end_time = request.POST.get('end_time')
            flight.location = request.POST.get('location')
            flight.wind_speed = request.POST.get('wind_speed', 0)
            flight.wind_direction = request.POST.get('wind_direction')
            flight.atmospheric_pressure = request.POST.get('atmospheric_pressure', 0)
            flight.flight_objective_description = request.POST.get('flight_objective_description')
            flight.results = request.POST.get('results')
            flight.pilot_impressions = request.POST.get('pilot_impressions')
            flight.improvements = request.POST.get('improvements')
            flight.total_takeoff_weight = request.POST.get('total_takeoff_weight')
            flight.telemetry_link = request.POST.get('telemetry_link')
            flight.flight_success_rating = request.POST.get('stars') or 0

            # Verifica se houve acidente
            occurred_accident = 'occurred_accident' in request.POST
            flight.occurred_accident = occurred_accident

            flight.save()

            # Atualiza os membros responsáveis
            team_members = request.POST.get('responsibles')
            if team_members:
                team_members_ids = [int(id.strip()) for id in team_members.split(',') if id.strip().isdigit()]
                flight.team_members.set(team_members_ids)

            # Se houver um acidente, cria ou atualiza o log de acidente
            if occurred_accident:
                if accident_log:
                    accident_log.description = request.POST.get('descriptionAccident')
                    accident_log.damaged_parts = request.POST.get('damaged_parts')
                    accident_log.damaged_parts_photo = request.POST.get('damaged_parts_photo')
                    accident_log.save()
                else:
                    AccidentLog.objects.create(
                        id_flightLog=flight,
                        description=request.POST.get('descriptionAccident'),
                        damaged_parts=request.POST.get('damaged_parts'),
                        damaged_parts_photo=request.POST.get('damaged_parts_photo')
                    )
            else:
                # Se o acidente foi removido, exclui o log de acidente se existir
                if accident_log:
                    accident_log.delete()

            return redirect('flights')

        except Exception as e:
            print(f"Erro ao editar o flight log: {e}")
            return HttpResponseBadRequest("Ocorreu um erro ao editar o log de voo.")

    context = {
        'flight': flight,
        'profiles': profiles,
        'accident_log': accident_log  # Passa o acidente para o template
    }
    return render(request, '_editFlight.html', context)

# Deletar um voo
def flight_delete(request, id):
    flight = get_object_or_404(FlightLog, id=id)
    if request.method == 'POST':
        flight.delete()
        return redirect('flights')
    return redirect('flights')

def image_to_base64(image):
    """
    Converte a imagem do campo ImageField para uma string base64.
    Lida tanto com arquivos de imagem quanto com dados binários.
    """
    if isinstance(image, bytes):  # Se image já for um objeto de bytes
        return base64.b64encode(image).decode('utf-8')
    
    if image:
        with open(image.path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')



@login_required
def meetings(request):
    profiles = MembroEquipe.objects.all()
    meetings = Meeting.objects.all()
    items = []

    search_meetings = request.GET.get("search", "")
    if search_meetings:
        meetings = meetings.filter(title__icontains=search_meetings)
    
    order = request.GET.get("order", "recentes")
    if order == "recentes":
        meetings = meetings.order_by("-meeting_date") 
    elif order == "antigos":
        meetings = meetings.order_by("meeting_date")

    areas = Area.objects.all()
    areas_select = request.GET.getlist("areas", [])

    if areas_select:
        meetings = meetings.filter(areas__id__in=areas_select).distinct()

    # for meeting in meetings:
    #     responsible_profiles = meeting.responsible.all()
    #     responsible_photos = []
        
    #     for resp in responsible_profiles:
    #         if resp.photo:
    #             responsible_photos.append(image_to_base64(resp.photo))
    #         else:
    #             responsible_photos.append(None)
    #     pair_r_p = list(zip(meeting.get_responsibles(), responsible_photos))
    #     meeting.responsibles_list = pair_r_p

    for profile in profiles:
            if profile.photo:
                profile.photo_base64 = image_to_base64(profile.photo)
            else:  
                profile.photo_base64 = None
    if request.method == 'POST':
        post_data = request.POST.copy()  # Cria uma cópia dos dados para modificar

        # Converter os IDs de "responsibles" para uma lista
        # responsibles_ids = post_data.get("responsibles", "")
        # if responsibles_ids:  # Se não estiver vazio
        #     post_data.setlist("responsible", responsibles_ids.split(","))  # Ajusta para ManyToManyField

        # Converter os IDs de "areas" para lista (caso já existisse no código)
        post_data.setlist("areas", post_data.get("areas", "").split(","))

        # Criar e validar o formulário
        form = MeetingsForm(post_data)
        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            meeting = form.save(commit=False)  # Salva sem ManyToMany
            meeting.save()  # Primeiro salva a instância

            # Adiciona os relacionamentos ManyToMany manualmente
            # meeting.responsible.set(post_data.getlist("responsible"))  
            meeting.areas.set(post_data.getlist("areas"))

            return redirect('meetingsquadro')
    else:
        form = MeetingsForm()
    
    return render(request, 'meetings.html',
    {'form': form,
     'items': items,
     'meetings': meetings,
     "areas": areas,
     "areas_select": areas_select,
     "order": order,
     "profiles": profiles,
     "search_meetings": search_meetings,})


def membros_por_area(request, area_id):
    """Retorna os membros de uma determinada área."""
    area = get_object_or_404(Area, id=area_id)
    membros = area.membros.all()  # Pega todos os membros que pertencem a essa área
    print("membros:  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(membros)
    membros_data = [
        {
            "id": membro.id,
            "fullname": membro.fullname,
            "email": membro.email,
            "phone": membro.phone,
            "photo": membro.photo.url if membro.photo else None,
        }
        for membro in membros
    ]

    return JsonResponse({"membros": membros_data})

def delete_meeting(request, meeting_id):
    if request.method == "POST":
        meeting = get_object_or_404(Meeting, id=meeting_id)
        meeting.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)