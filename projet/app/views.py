from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *
from django.contrib import messages
# Create your views here.


def sheir(request):

    listes_des_etudiants = Etudiant.objects.all()

    return render(request, "hello_world.html", {"listes_des_etudiants": listes_des_etudiants})



def student_create(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etudiant ajouté avec succès')
            return redirect('hello_world')
        
    form = EtudiantForm()
    return render(request, "add_student.html", {"form": form})


def delete_student(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    etudiant.delete()
    messages.success(request, 'Etudiant supprimé avec succès')
    return redirect('hello_world')
    # return render(request, "delete_student.html")



def update_student(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etudiant modifié avec succès')
            return redirect('hello_world')

    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, "update_student.html", {"form": form})



def contact(request):
    return render(request, "contact.html")