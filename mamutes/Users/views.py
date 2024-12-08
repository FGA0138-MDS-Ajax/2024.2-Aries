from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as login_django
from .models import * 
from .forms import *
from .models import MembroEquipe
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from mamutes import settings


def login (request):
    if request.method ==  'GET':
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django (request, user)
            return HttpResponse("boa paizao deu certo")
            
        else:
            return HttpResponse("Credenciais inválidas.")

        
def isSuperUser(user):
    return user.is_superuser
    
    
@user_passes_test(isSuperUser) 
def cadastro(request):
     return render(request, 'cadastro.html')

def recuperarConta(request):
    
    if request.method == 'GET':
        return render(request, 'recuperarConta.html')
    else:
        email = request.POST.get('email')

        if MembroEquipe.objects.filter(email__exact=email).exists():
            geradorToken = PasswordResetTokenGenerator()
            usuario = MembroEquipe.objects.get(email=email)
            token = geradorToken.make_token(usuario)
            username = usuario.username

            send_mail(
                subject="Redefinição de senha",
                message=f"Uma requisição de redefinição de senha foi feita no site da Mamutes do Cerrado para a conta vinculada a este email, para prosseguir com a redefinição de senha basta acessar o seguinte link: http://127.0.0.1:8000/redefinirSenha/{username}/{token}. Caso a requisição não tenha sido feita por você, por favor ignore este email.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )

            
            context = {
                'mensagem': f'Enviamos um email de recuperação de conta para {email}, cheque em sua caixa postal.',
            }

            return render(request, 'recuperarConta.html', context)
        
        else:
            context = {
                'mensagem': f'Este email não existe, é necessário que o email tenha registro no sistema para recuperá-lo.',
            }
            return render(request, 'recuperarConta.html', context)
def redefinirSenha(request, username, token):
    usuario = MembroEquipe.objects.get(username=username)
    gerador = PasswordResetTokenGenerator()

    if request.method == "POST":
        senha = request.POST.get("password1")
        confirmar_senha = request.POST.get("password2")

        if senha != confirmar_senha:
            print('As senhas não coincidem')
            return render(request, 'redefinirSenha.html', {
                "username": username,
                "token": token,
                "mensagem": "As senhas não coincidem."
            })

        usuario.set_password(senha)
        usuario.save()
        print('Senha redefinida com sucesso')
        return redirect("login")

    if gerador.check_token(usuario, token):
        print('Token válido')
        return render(request, 'redefinirSenha.html', {
            "username": username,
            "token": token,
        })

    return redirect("login") 
