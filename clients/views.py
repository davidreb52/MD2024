from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from backOffice.models import Clients
from backOffice.forms import ClientForm

@login_required
def clients_liste(request):
    print("Vue clients_liste")
    clients= Clients.objects.all()
    return render(request, 'backOffice/clients_liste.html', {'clients': clients})

@login_required   
def clients_detail(request, id):
  print("Vue clients_detail")
  client = Clients.objects.get(id= id)  # nous insérons cette ligne pour obtenir le code client
  return render(request,
                'backOffice/clients_detail.html',
                {'client': client}) # nous mettons à jour cette ligne pour passer le groupe au gabarit
@login_required
def clients_create(request):
    print("Vue clients_create")
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            client = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('clients-detail', client.CClient)
    else:
        form = ClientForm()
    return render(request,
                  'backOffice/clients_create.html',
                  {'form': form})
@login_required
def clients_update(request, id):
    client = Clients.objects.get(id= id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('clients-detail', client.id)
    else:
        form = ClientForm(instance=client)

    return render(request,
                'backOffice/clients_update.html',
                {'form': form})

@login_required
def clients_delete(request, id):
    client = Clients.objects.get(id=id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        client.delete()
        # rediriger vers la liste des groupes
        return redirect('clients-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request,
           'backOffice/clients_delete.html',
           {'client': client})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>SARL REB & ELOI</p>')

@login_required
def home(request):
    return render(request, 'backOffice/home.html')