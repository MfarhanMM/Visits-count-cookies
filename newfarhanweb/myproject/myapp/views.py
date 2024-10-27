from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    #name = "Admin"
    #age = 10
    all_person = Person.objects.all() #.filter(age=25)
    return render(request,"index.html",{"all_person":all_person})#, {"name":name, "age":age})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        #print(name, age)
        # บันทึักข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "Saved successfully")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else :
        return render(request,"form.html")

#def form(request):
    #return HttpResponse("<h1>แบบฟอร์ม</h1>")

def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Updated successfully")
        return redirect("/")
    
    else:
    # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person":person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "Deleted successfully")
    return redirect("/")