from django.shortcuts import render
from django.http import HttpResponse

import json
import os

from django.contrib import admin
from cardtemplateapp.models import *

admin.register(Personality)
admin.register(Clothing)
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the cardtemplate index.")

def cardMain(request):
    context = {}
    #fi1nd all sheets
        
    cloth_cards = []
    person_cards = []

    for person in Personality.objects.all():
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
        
    for cloth in Clothing.objects.all():
        cloth_cards.append({
            "name": cloth.name,
            "id": cloth.clothing_id})

    context["person_cards"] = person_cards
    context["cloth_cards"] = cloth_cards
        
    return render(request, "hub-page.html", context)


def cardEditorClothing(request, clothing_id=None):
    context = {}
    context['images']=[]

    try: 
        clothing = Clothing.objects.get(clothing_id=clothing_id)
        context['name'] = clothing.name
        context['owner'] = clothing.owner
        context['claim_text'] = clothing.claim_text
        context['special_text'] = clothing.special_text
        context["lp"] = clothing.lp
        context['min_adv'] = clothing.min_adv
        context['image'] =clothing.image
        context['id'] = clothing.clothing_id
    except Exception as e:
        print(e)
        print("editting NEW card")
        context['name'] = "Panties"
        context['owner'] = "Sexy Girl's "
        context['claim_text'] = "Insert text here for how to claim this item. yep. some more placeholder text. blah blah Spend 4 effort"
        context['special_text'] = "Special effects that this item can activate go here. Text Test text. Placeholder text."
        context["lp"] = 4
        context['min_adv'] = 2
        context['image'] ="/static/card_art_cropped/panties.jpg"
        context['id'] = "undefined"
    

    for file in os.listdir('cardtemplateapp/static/card_art_cropped'):
        context['images'].append(file)

    return render(request, "clothing-card.html", context)

def cardEditorPerson(request, persona_id=None):
    context = {}
    context['images']=[]

    try: 
        person = Personality.objects.get(personality_id=persona_id)
        context['name'] = person.name
        context['cost'] = person.cost
        context['persona'] = person.persona
        context['image'] = person.image
        context["active_value"] = person.active_value
        context['inactive_value'] = person.inactive_value
        context['inactive_used'] = str(person.inactive_used).lower()
        context['effect_text'] = person.effect_text
        context['flavour_text'] = person.flavour_text
        context['id'] = person.personality_id
    except Exception as e:
        print(e)
        print("editting NEW card")
        context['name'] = "Panty Thief"
        context['cost'] = 3
        context['persona'] = "Type: Pervert"
        context['image'] ="/static/card_art_cropped/panty_thief.png"
        context["active_value"] = 3
        context['inactive_value'] = 2
        context['inactive_used'] = "true"
        context['effect_text'] = "The effect of this card goes here. This is some filler text as an example"
        context['flavour_text'] = "PANTSU! Flavor text goes here."
        context['id'] = "undefined"
    

    for file in os.listdir('cardtemplateapp/static/card_art_cropped'):
        context['images'].append(file)

    
    return render(request, "one-card.html", context)

def saveChanges(request):
    data = json.loads(request.POST["payload"])
    imgURL = data["imgURL"]
    title = data["title"].strip()
    lerncost = data["lerncost"]
    effect  = data["effect"].strip()
    cardtype = data["type"].strip()
    inactiveval =data["inactiveval"].strip()
    activeval = data["activeval"].strip()
    flavortext = data["flavortext"].strip()
    inactiveused = data["inactiveused"]
    try:
        inactV = int(inactiveval)
    except ValueError:
        inactV = 0
        
    if data["cardID"].strip() != "undefined":
        cardID = int(data["cardID"].strip())
        carddata = Personality(
            name = title,
            cost = int(lerncost),
            persona = cardtype,
            active_value = int(activeval),
            inactive_value = inactV,
            inactive_used = inactiveused,
            effect_text = effect,
            flavour_text = flavortext,
            image = imgURL,
            personality_id = cardID
           )
    else:
        #savin new entry
        carddata = Personality(
            name = title,
            cost = int(lerncost),
            persona = cardtype,
            active_value = int(activeval),
            inactive_value = inactV,
            inactive_used = inactiveused,
            effect_text = effect,
            flavour_text = flavortext,
            image = imgURL,
           )
    carddata.save()
    return HttpResponse(json.dumps({"card_id":carddata.personality_id}), content_type="application/json")


def saveChangesClothing(request):
    data = json.loads(request.POST["payload"])

    if data["cardID"].strip() != "undefined":
        cardID = int(data["cardID"].strip())
        carddata = Clothing(
            name = data["itemName"].strip(),
            owner = data["owner"].strip(),
            claim_text = data["claimtext"].strip(),
            special_text = data["specialtext"].strip(),
            lp = int(data["lp"]),
            min_adv = int(data["minAdv"]),
            image = data["imgURL"],
            clothing_id = cardID
           )
    else:
        #savin new entry
        carddata = Clothing(
            name = data["itemName"].strip(),
            owner = data["owner"].strip(),
            claim_text = data["claimtext"].strip(),
            special_text = data["specialtext"].strip(),
            lp = int(data["lp"]),
            min_adv = int(data["minAdv"]),
            image = data["imgURL"]
           )
    carddata.save()

    return HttpResponse("Success")
    
    
   
