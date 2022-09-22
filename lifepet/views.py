from django.shortcuts import render, get_object_or_404, redirect
from .models import Cadastro
from .forms import CadastroForm

def consultar(request): 
    search = request.GET.get("search")
    select = request.GET.get("select")
    
    if search:
        if select == "nome":
            consulta = Cadastro.objects.all().filter(nome__icontains=search)
    
        elif select == "telefone":
            consulta = Cadastro.objects.all().filter(telefone__icontains=search)
            
        else:
            consulta = Cadastro.objects.all().filter(email__icontains=search)
    
        return render(request, "consulta.html", {"consulta":consulta})
    
    else:
        return render(request, "consulta.html")

def search(request, id):
    consulta = get_object_or_404(Cadastro, pk=id)        
    form = CadastroForm(instance=consulta)   
    if request.method == "POST":
        form = CadastroForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "search.html", {"form":form, "consulta":consulta})
    
    else:
        return render(request, "search.html", {"form":form, "consulta":consulta})

def cadastro(request):
    form = CadastroForm()
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "cadastro.html", {"form":form})
    else: 
        return render(request, "cadastro.html", {"form":form})

        
def editar(request, id):
    consulta = get_object_or_404(Cadastro, pk=id)
    form = CadastroForm(instance=consulta)   
    if request.method == "POST":
        form = CadastroForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "editar.html", {"form":form, "consulta":consulta})
            
    else:
        return render(request, "editar.html", {"form":form, "consulta":consulta})
    
   
    
def deletar(request, id):
    campo = get_object_or_404(Cadastro, pk=id)
    campo.delete()
    return redirect("/")