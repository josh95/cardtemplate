from django.shortcuts import render
from django.http import HttpResponse
from cardtemplateapp.models import *
import json
import os

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the cardtemplate index.")

def cardMain(request):
    context = {}
    #find all sheets
    if player_id is None:
        player_id = 0
        
    cloth_cards = []
    person_cards = []

    """for sheet in Sheets.objects.filter(player_id = player_id):
        character_sheets.append({
            "name": sheet.character_name,
            "image" : sheet.img_url,
            "description" : sheet.description,
            "id": sheet.sheet_id})
    """
    for person in Personality.objects:
        person_cards.append({
            "id": person.personality_id,
            "name": person.name,
            "cost": person.cost ,
            "persona": person.persona,
            "active_value": person.active_value,
            "inactive_value" : person.inactive_value,
            "inactive_used" : person.inactive_used,
            "effect_text" : person.effect_text,
            "flavour_text" : person.flavour_text,
            "image" : person.image
            })
        
    for cloth in Clothing.objects:
        cloth_cards.append({
            "name": sheet.character_name,
            "image" : sheet.img_url,
            "description" : sheet.description,
            "id": sheet.sheet_id})
        
    return render(request, "card_main.html", context)


def cardEditorClothing(request, clothing_id=None):
    context = {}
    return HttpResponse(clothing_id)

def cardEditorPerson(request, persona_id=None):
    context = {}
    context['images']=[]
    for file in os.listdir('cardtemplateapp\static\card_art_cropped'):
        context['images'].append(file)
    return render(request, "one-card.html", context)



