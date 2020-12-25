from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from .forms import *
import requests
from django.db.models.functions import Now


def home(request):
    return render(request, 'AplikacjaW/index.html')

def client(request):
    
    return render(request, 'AplikacjaW/client.html')
def workerlogin(request):
    return render(request, 'AplikacjaW/workerlogin.html')

def test(request):
    
    return render(request, 'AplikacjaW/test.html')

def show_allstuff(request):
    
    magazyn_sprzet = Magazyn.objects.filter(czyuszkodzony=0, czywypozyczony=0)
    return render(request, 'AplikacjaW/client_allstuff.html', {'magazyn_sprzet':magazyn_sprzet})
def client_clientstuff(request):
    
    return render(request, 'AplikacjaW/client_clientstuff.html')


def post_client(request):
    login=request.POST['login']
    password=request.POST['password']
    phone_number=request.POST['phonenumber']
    
    client_id=Klienci.objects.filter(imie=login, nazwisko=password, telefonkontaktowy=phone_number)
    if not client_id:
        return render(request, 'AplikacjaW/test.html')
    cclient_id = client_id[0].idklienta
    
    client_stuff = Magazyn.objects.raw('select magazyn.idsprzetu,typ,rozmiar,kolor,cena,wypozyczenia.datawypozyczenia from magazyn inner join wypozyczenia on magazyn.idsprzetu = wypozyczenia.idsprzetu where wypozyczenia.idklienta=%s', [cclient_id])
    return render(request, 'AplikacjaW/client_clientstuff_table.html', {'klient_sprzet':client_stuff})



def workerlogin_verify(request):
    login=request.POST['login']
    password=request.POST['password']
    worker_id=Pracownicy.objects.filter(imie=login, nazwisko=password)
    if not worker_id:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!NIC TU NIE MA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return render(request, 'AplikacjaW/test.html')
    request = None  
    return redirect('/workerpage')


def workerpage(request):
    return render(request, 'AplikacjaW/workerpage.html')

def workerpage_addstuff(request):
    
    if request.method=='POST':
        
            
            typ_sprzetu = request.POST['typ_sprzetu']
            rozmiar_sprzetu= request.POST['rozmiar_sprzetu']
            kolor_sprzetu= request.POST['kolor_sprzetu']
            cena_sprzetu= request.POST['cena_sprzetu']
            czy_uszkodzony=request.POST['czy_uszkodzony']
            
            Magazyn.objects.create(typ=typ_sprzetu,rozmiar=rozmiar_sprzetu,kolor=kolor_sprzetu,czyuszkodzony=czy_uszkodzony,czywypozyczony=0, cena=cena_sprzetu)
    
    
    form=NameForm() 
    
    return render(request, 'AplikacjaW/workerpage_addstuff.html', {'form':form})

def workerpage_deletestuff(request):
    magazyn_sprzet = Magazyn.objects.filter(czywypozyczony=0)
    if request.method=='POST':
        id_sprzetu=request.POST['id_sprzetu']
        Magazyn.objects.filter(idsprzetu=id_sprzetu).delete()
        return render(request, 'AplikacjaW/workerpage_deletestuff.html', {'magazyn_sprzet':magazyn_sprzet})


    
    return render(request, 'AplikacjaW/workerpage_deletestuff.html', {'magazyn_sprzet':magazyn_sprzet})

def workerpage_returnstuff_verify(request):
    if request.method=='GET':
        print(' JESTEM GETEM')
        return render(request, 'AplikacjaW/workerpage_clientstuff_verify.html')
    elif request.method=='POST':
        print('dupa')
        login=request.POST['login']
        print(login)
        password=request.POST['password']
        phone_number=request.POST['phonenumber']
    
        client_id=Klienci.objects.filter(imie=login, nazwisko=password, telefonkontaktowy=phone_number)
        if not client_id:
            return render(request, 'AplikacjaW/test.html')
        cclient_id = client_id[0].idklienta
        return render(request, 'AplikacjaW/workerpage_returnstuff_verify_post.html', {'client_id':cclient_id})


    
def workerpage_clientstuff(request):
    
    cclient_id = request.POST['client_id']
    client_stuff = Magazyn.objects.raw('select magazyn.idsprzetu,typ,rozmiar,kolor,cena,wypozyczenia.idwypozyczenia,wypozyczenia.datawypozyczenia,wypozyczenia.datazakonczeniawypozyczenia from magazyn inner join wypozyczenia on magazyn.idsprzetu = wypozyczenia.idsprzetu where wypozyczenia.idklienta=%s', [cclient_id])
    for i in client_stuff:
        
        data_wypozyczenia=i.datawypozyczenia
        data_zakonczenia_wypozyczenia=i.datazakonczeniawypozyczenia
        
        if data_wypozyczenia==data_zakonczenia_wypozyczenia:
            i.datazakonczeniawypozyczenia='Brak'
        
    return render(request, 'AplikacjaW/workerpage_clientstuff.html', {'klient_sprzet':client_stuff, 'cclient_id':cclient_id})

def workerpage_returnstuff(request):

    id_sprzetu = request.POST['id_sprzetu']
    id_wypozyczenia = request.POST['id_wypozyczenia']
    client_id=request.POST['client_id']
    idsprzetu_update=Magazyn.objects.filter(idsprzetu=id_sprzetu).update(czywypozyczony=False)
    #zyuszkodzony_update=Magazyn.objects.raw('UPDATE magazyn SET czyuszkodzony = true WHERE idsprzetu=%s',[id_sprzetu])
    data_zakonczenia_wypozyczenia_update = Wypozyczenia.objects.filter(idwypozyczenia=id_wypozyczenia).update(datazakonczeniawypozyczenia=Now())
    #Wypozyczenia.objects.raw('UPDATE wypozyczenia SET datazakonczeniawypozyczenia = NOW() WHERE idwypozyczenia = %s', [id_wypozyczenia])
    
    return render(request, 'AplikacjaW/workerpage_returnstuff_verify_post.html', {'client_id':client_id})
