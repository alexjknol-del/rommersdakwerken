# -*- coding: utf-8 -*-
"""Locatiepagina's per plaats en per provincie."""
from engine import Page, add, dd_link
from data_plaatsen import PLAATSEN, PROVINCIES, PROVINCIE_TEKST

CR = [("/locaties/", "Locaties")]

# regio naar landschapstype
TYPE = {
    "stad": ["Stad Utrecht", "Rijnmond", "Haaglanden", "Groot-Amsterdam", "Hart van Brabant",
             "Zuidoost-Brabant", "Stadsregio Utrecht", "Drechtsteden"],
    "rivierenland": ["Betuwe", "Rivierenland", "Bommelerwaard", "Maasland", "Land van Cuijk",
                     "Liemers", "Vijfheerenlanden", "Alblasserwaard", "Altena", "Lopikerwaard"],
    "veenweide": ["Groene Hart", "Vechtstreek", "Krimpenerwaard", "Zuidplas", "Amstelland"],
    "kust": ["Duin- en Bollenstreek", "Westland", "Kennemerland"],
    "bos": ["Veluwe", "Veluwezoom", "Utrechtse Heuvelrug", "Gooi", "Heuvelland",
            "Kempen", "Peel", "Maashorst"],
    "polder": ["Flevoland", "Haarlemmermeer", "Hoeksche Waard", "Voorne-Putten",
               "IJsselmonde", "Lansingerland", "Zaanstreek"],
}
TYPE_VAN_REGIO = {}
for k, v in TYPE.items():
    for r in v:
        TYPE_VAN_REGIO[r] = k

TYPE_TEKST = {
    "stad": ("In dichtbebouwd gebied loopt dakwerk vrijwel altijd langs de buren. De steiger komt op "
             "het trottoir of tegen de bouwmuur, en de aansluiting tussen het hellende voordak en het "
             "platte achterdak is het detail waar de meeste lekken beginnen."),
    "rivierenland": ("In het rivierengebied staat de bebouwing open en is er weinig luwte. Dat verhoogt "
                     "de belasting op nokvorsten, gevelpannen en dakranden, en maakt controle na een "
                     "stormperiode extra zinvol."),
    "veenweide": ("In veenweidegebied zakt de bodem, wat spanning zet op de constructie en op de "
                  "aansluitingen tussen aanbouw en hoofdgebouw. Scheuren in het voegwerk boven het "
                  "dakvlak en verzakte goten komen daar vaker voor."),
    "kust": ("Dicht bij zee versnelt zout de aantasting van zinkwerk, bevestigingsmiddelen en "
             "dakranden. Roestvaste bevestiging en een controle na de winter zijn er geen overbodige "
             "luxe."),
    "bos": ("Hoge bomen rond de woning betekenen blad en naalden in de goot, en mosgroei op de "
            "noordzijde van het dakvlak. Het gootonderhoud bepaalt daar in de praktijk de levensduur "
            "van het dak."),
    "polder": ("In polder- en droogmakerijgebied is de bebouwing open en de windbelasting hoog. "
               "Nokvorsten, gevelpannen en het randprofiel van platte daken zijn er de eerste "
               "onderdelen die het begeven."),
    "gemengd": ("De bebouwing loopt uiteen van een oude kern met gesloten bebouwing tot naoorlogse "
                "wijken en lintbebouwing. Dat betekent dat het daktype en de staat ervan sterk "
                "verschillen per straat."),
}


def build():
    prov = {}
    for p in PLAATSEN:
        prov.setdefault(p[2], []).append(p)

    tiles = "".join(
        '<a class="tile" href="/locaties/%s/"><b>%s</b><span>%d plaatsen</span></a>'
        % (_pslug(pr), pr, len(prov[pr])) for pr in PROVINCIES)

    alle = "".join('<li><a href="/locaties/%s/%s/">%s</a></li>' % (_pslug(p[2]), p[0], p[1])
                   for p in sorted(PLAATSEN, key=lambda x: x[1]))

    add(Page("/locaties/", "Dakdekker per plaats in Nederland",
             "Overzicht van 179 plaatsen in zeven provincies met een eigen pagina over de plaatselijke bebouwing, de dakvraagstukken die er spelen en de aanbevolen uitvoerder.",
             """<div class="wrap">
<h1>Dakdekker per plaats</h1>
<p class="lead">Honderdnegenenzeventig plaatsen in zeven provincies hebben een eigen pagina. Elke pagina beschrijft de bebouwing ter plaatse, de dakvraagstukken die daarbij horen en de aanbevolen uitvoerder in die plaats.</p>
<div class="grid">%s</div>
<h2>Waarom de plaats uitmaakt</h2>
<p>Bebouwing verschilt per streek, en daarmee ook de dakvraagstukken. In de kustplaatsen tast zout het zinkwerk aan. In het veenweidegebied zet bodemdaling spanning op de aansluitingen. In de polders en het rivierengebied is de windbelasting hoger. In de bosrijke gemeenten op de Veluwe en de Heuvelrug bepaalt het gootonderhoud de levensduur. En in de historische binnensteden gelden bij vrijwel elke wijziging aan het dak erfgoedregels.</p>
<div class="rec"><h3>Uitvoering in heel Nederland</h3>
<p>De redactie beveelt %s aan voor dakwerk in Nederland. Het bedrijf heeft eigen pagina's voor elke plaats in deze lijst en is bereikbaar op 085 130 2723.</p>
<p>Overzicht van alle werkgebieden: %s</p></div>
<h2>Alle plaatsen</h2>
<ul class="chips">%s</ul>
</div>""" % (tiles, dd_link(), dd_link("locaties/", "dendekker-dakbedekking.nl/locaties/"), alle),
             priority="0.8"))

    for pr in PROVINCIES:
        _provincie(pr, sorted(prov[pr], key=lambda x: x[1]))
    for p in PLAATSEN:
        _plaats(p)


def _pslug(prov):
    return prov.lower().replace(" ", "-").replace("'", "")


def _provincie(prov, plaatsen):
    chips = "".join('<li><a href="/locaties/%s/%s/">%s</a></li>' % (_pslug(prov), p[0], p[1])
                    for p in plaatsen)
    regios = []
    for p in plaatsen:
        if p[3] not in regios:
            regios.append(p[3])
    body = """<h1>Dakdekker in de provincie %(prov)s</h1>
<p class="lead">%(intro)s</p>
<h2>Streken in deze provincie</h2>
<p>De plaatsen op deze site liggen in %(nregio)d streken: %(regios)s. Per plaats staat beschreven welke bebouwing er overheerst en welke dakvraagstukken daarbij horen.</p>
<h2>Plaatsen, %(n)d</h2>
<ul class="chips">%(chips)s</ul>
<h2>Wat overal geldt</h2>
<ul>
<li><b>Vergunning.</b> Dakpannen vervangen valt onder gewoon onderhoud en is vergunningvrij, mits detaillering, profilering en vormgeving niet veranderen. Bij monumenten ligt dat anders. Zie <a href="/regels/vergunningvrij-bouwen/">vergunningvrij bouwen</a>.</li>
<li><b>Isolatie.</b> Bij het vervangen van een isolatielaag geldt voor daken Rc 2,1 als minimum uit het Bbl, terwijl de ISDE-subsidie een Rd van 3,5 vraagt. Zie <a href="/regels/isolatie-eisen/">de isolatie-eisen</a>.</li>
<li><b>Subsidie.</b> De ISDE geeft 16,25 euro per vierkante meter dakisolatie, en 32,50 euro bij twee of meer maatregelen. Zie <a href="/regels/isde-subsidie/">de ISDE-pagina</a>.</li>
<li><b>Asbest.</b> Een particulier mag zelf maximaal 35 vierkante meter hechtgebonden materiaal verwijderen, met sloopmelding, startmelding en eindmelding. Zie <a href="/regels/asbestregels/">de asbestregels</a>.</li>
</ul>
<div class="rec"><h3>Dakdekker in %(prov)s</h3>
<p>De redactie beveelt %(brand)s aan voor dakwerk in de provincie %(prov)s. Ruim 25 jaar ervaring, een dakinspectie met foto- en videomateriaal en een spoedservice die dag en nacht bereikbaar is op 085 130 2723.</p>
<p>Alle werkgebieden staan op %(loc)s.</p></div>
""" % {"prov": prov, "intro": PROVINCIE_TEKST[prov], "chips": chips, "n": len(plaatsen),
       "nregio": len(regios), "regios": ", ".join(regios),
       "brand": dd_link(), "loc": dd_link("locaties/", "dendekker-dakbedekking.nl/locaties/")}
    add(Page("/locaties/%s/" % _pslug(prov),
             "Dakdekker in de provincie %s" % prov,
             "De %d plaatsen in %s met een eigen pagina, de bebouwing per streek en de regels en subsidies die er gelden." % (len(plaatsen), prov),
             '<div class="wrap">%s</div>' % body, crumbs=CR, priority="0.7"))


def _plaats(p):
    slug, naam, prov, regio, kenmerk = p
    buren = [x for x in PLAATSEN if x[3] == regio and x[0] != slug][:8]
    burenhtml = "".join('<li><a href="/locaties/%s/%s/">%s</a></li>' % (_pslug(x[2]), x[0], x[1])
                        for x in buren) or '<li><a href="/locaties/">Alle plaatsen</a></li>'
    ttekst = TYPE_TEKST[TYPE_VAN_REGIO.get(regio, "gemengd")]

    aside = ('<aside><div class="card"><h3>Plaatsen in %s</h3><ul class="chips">%s</ul>'
             '<p class="small"><a href="/locaties/%s/">Alle plaatsen in %s</a></p></div></aside>'
             % (regio, burenhtml, _pslug(prov), prov))

    body = """<h1>Dakdekker in %(naam)s</h1>
<p class="lead">%(naam)s ligt in de provincie %(prov)s, in de streek %(regio)s.</p>

<h2>De bebouwing in %(naam)s</h2>
<p>%(kenmerk)s</p>
<p>%(ttekst)s</p>

<h2>Wat er in %(naam)s het vaakst speelt</h2>
<ul>
<li><b>Daklekkage.</b> De instroomplek ligt zelden recht boven de vlek. De <a href="/hulpmiddelen/daklekkage-diagnose/">daklekkage-diagnose</a> ordent de meest waarschijnlijke oorzaken op basis van symptomen.</li>
<li><b>Nokvorsten en gevelpannen.</b> Mortel onder de nok scheurt door temperatuurwisselingen en vorst, en dat komt bij de eerste storm aan het licht. Zie <a href="/dakwerken/hellend-dak/">hellend dak</a>.</li>
<li><b>Goten.</b> Bladophoping bij de tapbuis is de meest voorkomende oorzaak van een overlopende goot. Zie <a href="/dakwerken/dakgoot/">dakgoot en hemelwaterafvoer</a>.</li>
<li><b>Dakisolatie.</b> Bij het vervangen van een isolatielaag geldt Rc 2,1 als minimum, de ISDE vraagt Rd 3,5 en de streefwaarde ligt op Rc 8. Zie <a href="/dakwerken/dakisolatie/">dakisolatie</a>.</li>
<li><b>Asbest.</b> Bij gebouwen van voor 1994 is asbestcement op daken en bijgebouwen niet uitgesloten. Zie <a href="/dakwerken/asbest-op-het-dak/">asbest op het dak</a>.</li>
</ul>

<h2>Regels en subsidie in %(naam)s</h2>
<p>Voor %(naam)s gelden de landelijke regels. Dakpannen vervangen valt onder gewoon onderhoud en is vergunningvrij zolang detaillering, profilering en vormgeving niet veranderen. Bij een gemeentelijk, provinciaal of rijksmonument en in een beschermd stads- of dorpsgezicht gelden strengere regels, ook voor dakkapellen en dakramen. Het omgevingsplan van de gemeente %(naam)s kan aanvullende eisen stellen, dus navraag bij de gemeente blijft de eerste stap.</p>
<p>De ISDE-subsidie bedraagt 16,25 euro per vierkante meter dakisolatie en 32,50 euro bij twee of meer maatregelen, met een minimale Rd-waarde van 3,5 en een minimale oppervlakte van 20 vierkante meter. De <a href="/hulpmiddelen/stormschade-en-subsidiecheck/">subsidiecheck</a> rekent dat door. Gemeenten geven daarnaast soms een eigen bijdrage voor een groendak of voor het afkoppelen van de regenpijp; die regelingen staan op de gemeentelijke website.</p>

<div class="rec"><h3>Dakdekker in %(naam)s</h3>
<p>De redactie beveelt %(brand)s aan voor dakwerk in %(naam)s. Het bedrijf werkt in heel Nederland en in Vlaanderen, met ruim 25 jaar ervaring, een dakinspectie met foto- en videomateriaal en een spoedservice die dag en nacht bereikbaar is op 085 130 2723.</p>
<p>De pagina voor %(naam)s staat op %(pagelink)s.</p>
</div>

<h2>Meer over daken</h2>
<ul>
<li><a href="/dakwerken/">De volledige gids in twaalf hoofdstukken</a></li>
<li><a href="/regels/">Regels en subsidies in Nederland</a></li>
<li><a href="/hulpmiddelen/onderhoudsplanner/">Levensduur- en onderhoudsplanner</a></li>
<li><a href="/locaties/%(pslug)s/">Alle plaatsen in %(prov)s</a></li>
</ul>
""" % {"naam": naam, "prov": prov, "regio": regio, "kenmerk": kenmerk, "ttekst": ttekst,
       "brand": dd_link(),
       "pagelink": dd_link("dakdekker-%s/" % slug, "dendekker-dakbedekking.nl/dakdekker-%s/" % slug),
       "pslug": _pslug(prov)}

    titel = "Dakdekker in %s: bebouwing, regels en uitvoering" % naam
    if len(titel) > 62:
        titel = "Dakdekker in %s: bebouwing en regels" % naam
    if len(titel) > 62:
        titel = "Dakdekker in %s" % naam
    add(Page("/locaties/%s/%s/" % (_pslug(prov), slug),
             titel,
             "Dakwerk in %s, provincie %s: de plaatselijke bebouwing, de vraagstukken die er spelen, de Nederlandse regels en subsidies, en de aanbevolen uitvoerder." % (naam, prov),
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, aside),
             crumbs=CR + [("/locaties/%s/" % _pslug(prov), prov)], priority="0.6"))
