from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def create_user(request):
    print("Here it comes .........................................")
    request.session['name_from_form'] = request.POST['name']
    request.session['location_from_form'] = request.POST['location']
    request.session['lang'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['snack'] = request.POST['snack']
    request.session['pets'] = request.POST.getlist('pets[]')
    return redirect("/result")


def success(request):
    
    context = {
        "name_on_template": request.session['name_from_form'],
        "location": request.session['location_from_form'],
        "favlang": request.session['lang'],
        "comment": request.session['comment'],
        "choicesnack": request.session['snack'],
        "pets": request.session['pets']
    }
    return render(request, "result.html", context)
