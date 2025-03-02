from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate,  update_session_auth_hash, logout, login as login_django
from .models import * 
from .forms import *
from .models import MembroEquipe
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from mamutes import settings
from django.contrib import messages
import os

def login (request):
    if request.method ==  'GET':
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        user_password = request.POST.get('password')

        user = authenticate(username=username, password=user_password)

        if user is not None:
            login_django (request, user)
            return redirect ('home')
        else:
            return render (request, 'login.html', {'message': 'Usuário ou senha incorretos. Tente novamente.'})

@login_required
def logoutUser(request):
    authenticated = request.user.is_authenticated
    if authenticated == True:
        logout(request)
        return redirect('index')
    return redirect('home')

        
def isSuperUser(user):
    return user.is_superuser
    
    
@user_passes_test(isSuperUser) 
def register(request):
    areas = Area.objects.all() 
    functions = Function.objects.all() 
    if request.method == 'POST':
        fullname = request.POST.get ('fullname')
        email = request.POST.get ('email')
        username = request.POST.get ('username')
        phone = request.POST.get ('phone')
        selected_areas = request.POST.getlist('areas')
        selected_functions = request.POST.getlist('functions')

        
        if fullname and email and username and phone:
            try:
                membro = MembroEquipe.objects.create_user(
                    username=username,
                    fullname=fullname,
                    email=email,
                    phone=phone
                )

                membro.areas.set(Area.objects.filter(id__in=selected_areas))
                membro.functions.set(Function.objects.filter(id__in=selected_functions))
            
                
                membro.save()
                return HttpResponse("vc criou o membro seu bosta")

            except Exception as e:
                #messages.error(request, f"Erro ao criar o membro: {e}")
                return HttpResponse("deu alguma bosta ai")
    
       
    return render(request, 'register.html', {'areas': areas, 'functions': functions})

@login_required
def configPassword(request):
    if request.method == 'POST':
        pw_actually = request.POST.get('pw_actually')
        pw1_new = request.POST.get('pw1_new')
        pw2_new = request.POST.get('pw2_new')

        if pw_actually and pw1_new and pw2_new:
            
            user = MembroEquipe.objects.get(username=request.user.username)
            if user.check_password(pw_actually):  
                if pw1_new == pw2_new:
                    
                    user.set_password(pw1_new)
                    user.save()
                    update_session_auth_hash(request, user) 
                    print('Senha alterada com sucesso!')
                    message = 'Senha alterada com sucesso!' 
                else:
                    print( 'As novas senhas não coincidem!')
                    message = 'As senhas não coincidem!' 
            else:
                print( 'A senha atual está incorreta!')
                message = 'A senha atual está incorreta!' 
        else:
            print( 'Por favor, preencha todos os campos!')
            message = 'Por favor, preencha todos os campos!' 

        return render(request, 'pagConfig.html', {'message': message})
    return redirect('pagConfig')  # Redireciona caso o método não seja POST

def recoverAccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if MembroEquipe.objects.filter(email__exact=email).exists():
            tokenGenerator = PasswordResetTokenGenerator()
            user = MembroEquipe.objects.get(email=email)
            token = tokenGenerator.make_token(user)
            username = user.username

            send_mail(
                subject="Redefinição de senha",
                message=f"Uma requisição de redefinição de senha foi feita no site da Mamutes do Cerrado para a conta vinculada a este email, para prosseguir com a redefinição de senha basta acessar o seguinte link: http://127.0.0.1:8000/redefine_password/{username}/{token}. Caso a requisição não tenha sido feita por você, por favor ignore este email.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )

            response = {
                'mensagem': f'Enviamos um email de recuperação de conta para {email}, cheque em sua caixa postal.',
                'success': True
            }
        else:
            response = {
                'mensagem': f'Este email não existe, é necessário que o email tenha registro no sistema para recuperá-lo.',
                'success': False
            }

        return JsonResponse(response)


def redefinePassword(request, username, token):
    user = MembroEquipe.objects.get(username=username)
    generator = PasswordResetTokenGenerator()

    if request.method == "POST":
        user_password = request.POST.get("password1")
        check_password = request.POST.get("password2")

        if user_password != check_password:
            print('As senhas não coincidem')
            return render(request, 'redefinePassword.html', {
                "username": username,
                "token": token,
                "mensagem": "As senhas não coincidem."
            })

        user.set_password(user_password)
        user.save()
        print('Senha redefinida com sucesso')
        return redirect("login")

    if generator.check_token(user, token):
        print('Token válido')
        return render(request, 'redefinePassword.html', {
            "username": username,
            "token": token,
        })

    return redirect("login")


def pagConfig(response):
     return render(response,'pagConfig.html')


@login_required
def editar_usuario(request):
    if request.method == 'POST':
        # Pega os dados do formulário e atualiza o usuário
        user = request.user
        user.fullname = request.POST.get('fullname')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.phone = request.POST.get('phone')
        user.save()
        return redirect('pagConfig')  # Redireciona para a página de perfil ou outra página
    else:
        # Se o método for GET, apenas exibe o formulário com os dados atuais
        return render(request, 'pagConfig.html', {'user': request.user})



@login_required
def update_photo(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        user = request.user
        photo = request.FILES['photo']
        
        try:
            # Aqui você pode adicionar qualquer validação de imagem, como tamanho ou formato.
            if photo.size > 2 * 1024 * 1024:  # Limite de 2MB
                return JsonResponse({'error': 'A imagem deve ter no máximo 2MB!'}, status=400)
            
            # Atualiza a foto do perfil
            user.photo = photo
            user.save()
            
            # Retorna a URL da foto ou uma confirmação de sucesso
            return JsonResponse({'success': 'Foto de perfil atualizada com sucesso!', 'photo_url': user.photo.url})
        
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Erro ao atualizar a foto'}, status=500)
    
    return JsonResponse({'error': 'Nenhuma foto enviada'}, status=400)

@login_required
def delete_photo(request):
    if request.method == 'POST':
        user = request.user
        user.photo = 'fotos_membros/media/fotos_membros/default.png'  
        user.save()

        return JsonResponse({'success': True})


    return JsonResponse({'success': False, 'message': 'Método inválido.'})
