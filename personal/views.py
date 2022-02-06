from django.shortcuts import render

# Create your views here.

def renderHome(request) :
    context = {}
    return render(request, 'personal/home.html', context)


def renderAcademics(request) :
    context = {}
    return render(request, 'personal/academics.html', context)

def renderContact(request) :
    context = {}
    return render(request, 'personal/contact.html', context)

def renderHappenings(request) :
    context = {}
    return render(request, 'personal/happenings.html', context)

def renderLabs(request) :
    context = {}
    return render(request, 'personal/labs.html', context)

def renderOpportunities(request) :
    context = {}
    return render(request, 'personal/opportunities.html', context)

def renderPeople(request) :
    context = {}
    return render(request, 'personal/people.html', context)


def renderPlacements(request) :
    context = {}
    return render(request, 'personal/placements.html', context)

def renderResearch(request) :
    context = {}
    return render(request, 'personal/research.html', context)