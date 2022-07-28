from django.shortcuts import render


def login(request):
    # if request.method == 'POST':
    #     info('POST::/cadastro')
    #     usuario = request.POST['usuario']
    #     senha = request.POST['senha']
    #     confirmaSenha = request.POST['confimacaoSenha']
    #     email = request.POST['email']
    #     licencas = request.POST['licencas']
    #     print('1 - ', usuario, senha, confirmaSenha, email, licencas)

    #     # Validação de usuário
    #     if campoVazio(usuario):
    #         messages.error(request, 'Usuário não pode ser vazio')
    #         return redirect('cadastro')

    #     if Escritorio.objects.filter(username=usuario).exists():
    #         messages.error(request, 'Usuário/Escritório já cadastrado por outro usuário !!!')
    #         return redirect('cadastro')

    #     # Validação de email
    #     if campoVazio(email):
    #         messages.error(request, 'Email já cadastrado por outro usuário !!!')
    #         return redirect('cadastro')

    #     if Escritorio.objects.filter(email=email).exists():
    #         print('Email Usuario já cadastrado')
    #         return redirect('cadastro')

    #     # Validação de senha
    #     if senhasIguais(senha, confirmaSenha):
    #         messages.error(request, 'As Senhas não são iguais')
    #         return redirect('cadastro')

    #     # Criando e Cadastrando novo usuario/escritorio
    #     escritorio = Escritorio.objects.create_user(
    #         username=usuario, nomeEscritorio=usuario, email=email, password=senha, qtdChaves=licencas, is_staff=False
    #     )
    #     info(f"INSERT::cadastro - {escritorio.escritorioId=}")
    #     escritorio.save()
    #     emailBoasVindas(escritorio)

    #     messages.success(request, 'Usuário cadastrado com sucesso !!!')

    #     return redirect('login')
    # else:
    #     return render(request, 'cadastro.html')
    context: dict = {'mostraLogo': False}
    return render(request, 'login.html', context)


def cadastro(request):
    context: dict = {'mostraLogo': True}
    return render(request, 'cadastro.html', context)