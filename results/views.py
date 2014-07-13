import re
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from forms import *
from django.core.mail import send_mail
from models import *


def home(request):
    upcoming_races = Race.objects.filter(date__gt=datetime.today())
    past_races = Race.objects.filter(date__lt=datetime.today())
    data = {
        'upcoming_races': upcoming_races,
        'past_races': past_races,
    }
    return render(request, "home.html", data)


@login_required
def bulk_results(request):
    if request.method == 'POST':
        form = BulkCreateResults(request.POST)
        if form.is_valid():
            race = form.cleaned_data['race']
            results = form.cleaned_data['results']
            for line in results.split('\n'):
                m = re.search(r'^.+(BOY|BOYS|YM|JM|SM|MM|SMM|GIRL|GIRLS|YW|JW|SW|MW|SMW).+', line)
                age_class = ""
                if m:
                    age_class = m.group(0)
                    line = line.replace(age_class, "")
                gender = 'M'
                m = re.search(r'^([0-9]+)\s([0-9]+)?\s?(\S+\s+\S+)\s+([a-zA-Z \.\-]+).+', line)
                name = "NN"
                place = 2
                if m:
                    place = m.group(1)
                    bib_number = m.group(2)
                    name = m.group(3)
                    club = m.group(4)
                racer, created = Racer.objects.get_or_create(name=name, gender=gender)





                Result.objects.create(race=race, racer=racer, place=place,
                                      start_time='0:00:00', finish_time='0:10:12',
                                      first_shoot=1, second_shoot=2, third_shoot=3,
                                      fourth_shoot=4)

            # user = form.save()
            # user.email_user("Welcome!", "Thank you, {} {} for signing up for our website.".format(user.first_name, user.last_name))
            # text_content = 'Thank you {} {} for signing up for our website on {}.'.format(user.first_name, user.last_name, user.date_joined)
            # html_content = '<h2>Thanks {} {} for signing up on {}!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined.strftime("%B %d, %Y"))
            # msg = RaceUserCreationForm("Welcome! {} {}".format(user.first_name, user.last_name), text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("bulk_results")
    else:
        form = BulkCreateResults()
    return render(request, "result/bulk_add_results.html", {
        'form': form,
    })


"""
USER PROFILES
"""

def register(request):
    if request.method == 'POST':
        form = RaceUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you, {} {} for signing up for our website.".format(user.first_name, user.last_name))
            # text_content = 'Thank you {} {} for signing up for our website on {}.'.format(user.first_name, user.last_name, user.date_joined)
            # html_content = '<h2>Thanks {} {} for signing up on {}!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined.strftime("%B %d, %Y"))
            # msg = RaceUserCreationForm("Welcome! {} {}".format(user.first_name, user.last_name), text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("profile")
    else:
        form = RaceUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    data = {
        'user': request.user,
    }
    return render(request, 'profile/profile.html', data)


@login_required
def profile_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)


"""
CLUBS
"""

def clubs(request):
    #list all clubs
    clubs = Club.objects.all()
    return render(request, "club/clubs.html", {'clubs': clubs})

def view_club(request, club_id):
    #individual club listing
    club = Club.objects.get(id=club_id)
    data = {"club": club}
    return render(request, "club/view_club.html", data)

def new_club(request):
    # add club
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = ClubForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Club object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/clubs")
    # Else if the user is looking at the form page
    else:
        form = ClubForm()
    data = {'form': form}
    return render(request, "club/new_club.html", data)

@staff_member_required
def edit_club(request, club_id):
    club = Club.objects.get(id=club_id)
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            if form.save():
                return redirect("/clubs/{}".format(club_id))
    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ClubForm(instance=club)
    data = {"club": club, "form": form}
    return render(request, "club/edit_club.html", data)

@staff_member_required
def delete_club(request, club_id):
    club = Club.objects.get(id=club_id)
    club.delete()
    return redirect("/clubs")


"""
RACES
"""

def races(request):
    #list all races
    all_races = Race.objects.all()
    return render(request, "race/races.html", {'races': all_races})

def view_race(request, race_id):
    #individual race listing
    race = Race.objects.get(id=race_id)
    data = {"race": race}
    return render(request, "race/view_race.html", data)

def new_race(request):
    # add race
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/races")
    else:
        form = RaceForm()
    data = {'form': form}
    return render(request, "race/new_race.html", data)

@staff_member_required
def edit_race(request, race_id):
    race = Race.objects.get(id=race_id)
    if request.method == "POST":
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            if form.save():
                return redirect("/races/{}".format(race_id))
    else:
        form = RaceForm(instance=race)
    data = {"race": race, "form": form}
    return render(request, "race/edit_race.html", data)

@staff_member_required
def delete_race(request, race_id):
    race = Race.objects.get(id=race_id)
    race.delete()
    return redirect("/races")


"""
RACERS
"""
def racers(request):
    #list all racers
    racers = Racer.objects.all()
    return render(request,"racer/racers.html", {'racers': racers})

def view_racer(request, racer_id):
    #individual racer listing
    results = Result.objects.filter(racer_id=racer_id)
    racer = Racer.objects.get(id=racer_id)
    # all_results = Result.objects.all()
    data = {
        "racer": racer,
        "results": results,
        # "all_results": all_results
    }
    return render(request, "racer/view_racer.html", data)

def new_racer(request):
    # add racer
    if request.method == "POST":
        form = RacerForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/racers")
    else:
        form = RacerForm()
    data = {'form': form}
    return render(request, "racer/new_racer.html", data)

@staff_member_required
def edit_racer(request, racer_id):
    racer = Racer.objects.get(id=racer_id)
    if request.method == "POST":
        form = RacerForm(request.POST, instance=racer)
        if form.is_valid():
            if form.save():
                return redirect("/racers/{}".format(racer_id))
    else:
        form = RacerForm(instance=racer)
    data = {"racer": racer, "form": form}
    return render(request, "racer/edit_racer.html", data)

@staff_member_required
def delete_racer(request, racer_id):
    racer = Racer.objects.get(id=racer_id)
    racer.delete()
    return redirect("/racers")


"""
RESULTS
"""
def results(request):
    #list all results
    past_races = Race.objects.filter(date__lt=datetime.today())
    # results = Result.objects.all()
    return render(request, "result/results.html", {'past_races': past_races})

def view_result(request, result_id):
    #individual result listing
    result = Result.objects.get(id=result_id)
    data = {"result": result}
    return render(request, "result/view_results.html", data)

def view_race_results(request, race_id):
    #individual result listing
    race = Race.objects.get(id=race_id)
    # racers = Racer.objects.filter(race__pk=race_id).all()
    results = Result.objects.filter(race__pk=race_id).all()
    data = {"race": race, "results": results}
    return render(request, "result/view_race_results.html", data)


def new_result(request):
    # add result
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/results")
    else:
        form = ResultForm()
    data = {'form': form}
    return render(request, "result/new_result.html", data)

@staff_member_required
def edit_result(request, result_id):
    result = Result.objects.get(id=result_id)
    if request.method == "POST":
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            if form.save():
                return redirect("/results/{}".format(result_id))
    else:
        form = ResultForm(instance=result)
    data = {"result": result, "form": form}
    return render(request, "result/edit_result.html", data)

@staff_member_required
def delete_result(request, result_id):
    result = Result.objects.get(id=result_id)
    result.delete()
    return redirect("/results")
