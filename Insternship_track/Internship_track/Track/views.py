from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . import dbCon

def add(request):
    return render(request, 'add.html')
def addsave(request):
    if request.method == "POST":
        regno = request.POST['regno']
        name = request.POST['name']
        department = request.POST['department']
        company = request.POST['company']
        duration = request.POST['duration']
        domain = request.POST['domain']
        mail = request.POST['mail']

        data = {
            "regno": regno,
            "name": name,
            "department": department,
            "company": company,
            "duration": duration,
            "domain": domain,
            "mail": mail
        }

        dbCon.col.insert_one(data)
        return redirect('listdata')
    else:
        return redirect('add')  # fallback if accessed without POST

def listdata(request):
    interns = dbCon.col.find()
    return render(request, 'list.html', {'var': interns})
def edit(request, regno):
    entry = dbCon.col.find_one({"regno": regno})
    if request.method == 'POST':
        name = request.POST["name"]
        department = request.POST["department"]
        company = request.POST["company"]
        duration = request.POST["duration"]
        domain = request.POST["domain"]
        mail = request.POST["mail"]
        dbCon.col.update_one(
            {"regno": regno},
            {"$set": {
                "name": name,
                "department": department,
                "company": company,
                "duration": duration,
                "domain": domain,
                "mail": mail
            }}
        )
        return redirect('listdata')
    return render(request, 'edit.html', {"entry": entry})
def delete(request, regno):
    dbCon.col.delete_one({"regno": regno})
    return redirect('listdata')