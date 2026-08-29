# -*- coding: utf-8 -*-
"""Nieuwsartikelen."""
from engine import Page, add, dd_link, BASE, SITE_NAME
import datetime

CR = [("/nieuws/", "Nieuws")]
ARTICLES = []


def art(slug, date, title, desc, lead, body, sources):
    ARTICLES.append((slug, date, title, desc, lead, body, sources))


art("isde-2026-wat-verandert", "2026-01-14",
    "ISDE 2026: ventilatiebedrag erbij en ruimere eis voor biobased",
    "De ISDE ging op 5 januari 2026 open. Nieuw zijn een bedrag van 400 euro voor energiezuinige ventilatie en een verruimde MKI-eis voor biobased isolatiemateriaal.",
    "De ISDE voor woningeigenaren is op 5 januari 2026 opengegaan. Voor dakisolatie blijft het tarief 16,25 euro per vierkante meter, met verdubbeling bij twee maatregelen.",
    """<h2>Wat gelijk blijft</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Bedrag</th></tr>
<tr><td>Dakisolatie, een maatregel</td><td>16,25 euro per vierkante meter</td></tr>
<tr><td>Dakisolatie bij twee of meer maatregelen</td><td>32,50 euro per vierkante meter</td></tr>
</table></div>
<p>De voorwaarden voor dakisolatie blijven eveneens ongewijzigd: een Rd-waarde van minimaal 3,5 vierkante meter kelvin per watt voor het nieuwe materiaal, minimaal 20 en maximaal 200 vierkante meter subsidiabel, en aanvragen binnen 24 maanden na uitvoering.</p>

<h2>Wat nieuw is</h2>
<ul>
<li><b>Energiezuinige ventilatie.</b> Eenmalig 400 euro, mits gecombineerd met minstens een isolatiemaatregel.</li>
<li><b>Biobased isolatie.</b> De MKI-eis is verruimd van maximaal 0,85 naar maximaal 1,90. Daardoor komen meer biobased materialen in aanmerking voor de bonus van 5 euro per vierkante meter.</li>
</ul>
<p>MKI staat voor milieukostenindicator, een maat die de milieubelasting van een materiaal in een bedrag uitdrukt. Hoe lager, hoe beter. De verruiming betekent dat materialen die eerder net buiten de grens vielen, nu wel meetellen.</p>

<h2>Wat de verdubbeling waard is</h2>
<p>Bij honderd vierkante meter dakisolatie gaat het om 1.625 euro bij een enkele maatregel en 3.250 euro bij twee maatregelen. De tweede maatregel moet binnen 24 maanden na de eerste zijn uitgevoerd. Dat maakt het zinvol om dakisolatie te plannen samen met bijvoorbeeld vloer- of gevelisolatie, in plaats van los in de tijd.</p>

<h2>Looptijd</h2>
<p>RVO geeft aan dat de regeling doorloopt tot en met 31 december 2030. Het jaarbudget is wel eindig, dus wie werken laat uitvoeren, dient de aanvraag beter niet tot het eind van het jaar uit te stellen.</p>
<p>De <a href="/hulpmiddelen/stormschade-en-subsidiecheck/">subsidiecheck</a> op deze site rekent het bedrag door voor een ingevoerde oppervlakte, inclusief de verdubbeling en de biobased bonus.</p>""",
    ["RVO, ISDE voor woningeigenaren: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren",
     "RVO, wat wijzigt er in 2026: https://www.rvo.nl/subsidies-financiering/isde/isde-wat-wijzigt-er-2026",
     "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen"])

art("isde-budget-halverwege-2026", "2026-08-07",
    "ISDE-budget 2026 voor ruim de helft geclaimd",
    "Per 3 augustus 2026 was 257,4 miljoen euro van het ISDE-budget aangevraagd, ongeveer 51,5 procent. Dakisolatie is daarin goed voor 40,0 miljoen euro.",
    "Halverwege 2026 is ongeveer de helft van het ISDE-budget geclaimd. Voor wie dakisolatie laat uitvoeren, is dat een reden om de aanvraag niet op te sparen.",
    """<h2>De stand</h2>
<p>Voor 2026 is 500 miljoen euro beschikbaar voor het geheel van zonneboilers, warmtepompen, isolatie, ventilatie, elektrisch koken en warmtenetaansluiting, plus 5 miljoen euro apart voor kleinschalige windturbines.</p>
<p>Per 3 augustus 2026 waren er 127.377 aanvragen ingediend voor 189.125 apparaten of maatregelen, samen 257,4 miljoen euro. Dat komt neer op ongeveer 51,5 procent van het budget. Van dat bedrag ging 155,7 miljoen euro naar isolatie bij particulieren, waarvan 40,0 miljoen euro specifiek naar dakisolatie.</p>

<h2>Wat dat praktisch betekent</h2>
<p>De ISDE wordt behandeld op volgorde van binnenkomst. Aanvragen kan tot 24 maanden na uitvoering van de werkzaamheden, maar dat is geen reden om te wachten: het budget van het lopende jaar is eindig, en een aanvraag die pas in een volgend jaar wordt ingediend, valt onder de dan geldende voorwaarden en bedragen.</p>
<p>Voor dakisolatie geldt in 2026 een tarief van 16,25 euro per vierkante meter, en 32,50 euro bij twee of meer maatregelen. Bij honderd vierkante meter scheelt dat 1.625 euro.</p>

<h2>Waar de aanvraag op stukloopt</h2>
<ul>
<li><b>Rd-waarde niet vermeld.</b> De factuur moet de Rd-waarde van het aangebrachte materiaal noemen. Zonder die vermelding is niet aantoonbaar dat aan de eis van minimaal 3,5 is voldaan.</li>
<li><b>Oppervlakte niet gespecificeerd.</b> Het aantal aangebrachte vierkante meters hoort eveneens op de factuur te staan.</li>
<li><b>Te klein oppervlak.</b> Onder 20 vierkante meter volgt geen subsidie.</li>
<li><b>Zelf aangebracht.</b> De isolatie moet zijn aangebracht door een bouwbedrijf.</li>
</ul>
<p>Die punten horen dus al in de offerte te staan, niet pas op de eindfactuur.</p>""",
    ["RVO, ISDE-budget: https://www.rvo.nl/subsidies-financiering/isde/budget",
     "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen"])

art("klimaatschade-2025", "2026-06-26",
    "Klimaatschade 2025: ruim 155 miljoen euro, storm het grootst",
    "Het Verbond van Verzekeraars kwam voor 2025 uit op ruim 155 miljoen euro verzekerde klimaatschade, waarvan ruim 60 miljoen euro door storm.",
    "Voor 2025 bedroeg de verzekerde klimaatschade ruim 155 miljoen euro. Storm was met ruim 60 miljoen euro de grootste post, gevolgd door hagel en neerslag.",
    """<h2>De verdeling</h2>
<div class="tablewrap"><table>
<tr><th>Oorzaak</th><th>Verzekerde schade 2025</th></tr>
<tr><td>Storm</td><td>Ruim 60 miljoen euro</td></tr>
<tr><td>Hagel</td><td>Ongeveer 50 miljoen euro</td></tr>
<tr><td>Neerslag</td><td>Ongeveer 35 miljoen euro</td></tr>
<tr><td><b>Totaal</b></td><td><b>Ruim 155 miljoen euro</b></td></tr>
</table></div>
<p>Ter vergelijking: over 2024 kwam het totaal uit op ongeveer 278 miljoen euro, met zware zomerbuien als grootste post. De februaristormen van 2022 alleen al leidden tot minimaal 500 miljoen euro verzekerde schade.</p>

<h2>Wat dat betekent voor daken</h2>
<p>Hagel en storm treffen daken op verschillende manieren. Hagel breekt keramische en betonpannen, en die breuk is vanaf de grond zelden zichtbaar. Ze komt pas aan het licht bij de eerstvolgende langdurige regen. Storm neemt de onderdelen mee die al los zaten: nokvorsten in verouderde mortel, gevelpannen zonder klem en losgekomen randprofielen van platte daken.</p>
<p>Neerslagschade is een andere categorie. Daar gaat het om afvoercapaciteit: bij korte, hevige buien komt meer water op het dak dan de goot of de afvoer aankan. Een noodoverloop in de dakrand van een plat dak voorkomt dat het water op het dak blijft staan.</p>

<h2>De drempel bij een schademelding</h2>
<p>Het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 50 kilometer per uur, als drempel waarboven van storm wordt gesproken. Het KNMI hanteert de strengere meteorologische definitie van windkracht 9, een uurgemiddelde van 75 tot 88 kilometer per uur. Die twee lopen in schadegesprekken vaak door elkaar; de polisvoorwaarden bepalen wat telt.</p>
<p>Schade als gevolg van achterstallig onderhoud is niet gedekt. Inspectierapporten en foto's van eerdere jaren zijn daarom van waarde in een dossier. De <a href="/hulpmiddelen/stormschade-en-subsidiecheck/">stormcheck</a> loopt de stappen na een storm door.</p>""",
    ["Verbond van Verzekeraars, klimaatschade 2025: https://www.verzekeraars.nl/publicaties/actueel/hagel-en-storm-grootste-oorzaken-klimaatschade-in-2025",
     "KNMI, klimaatschademonitor 2024: https://www.knmi.nl/over-het-knmi/nieuws/buien-grootste-schadeboosdoener-in-2024-klimaatschademonitor-extreem-weer/",
     "Verbond van Verzekeraars over de februaristormen 2022: https://www.verzekeraars.nl/publicaties/actueel/ruim-500-miljoen-euro-schade-door-februaristormen",
     "Verbond van Verzekeraars, infographic wind: https://www.verzekeraars.nl/verzekeringsthemas/klimaat-en-duurzaamheid/praktische-hulpmiddelen/infographic-verzekerbaarheid-klimaatrisico-s/wind"])

art("knmi-stormen-nemen-niet-toe", "2026-03-05",
    "KNMI: het aantal stormen neemt niet toe",
    "Volgens het KNMI is er geen aanwijzing dat stormen in Nederland vaker of zwaarder worden. Sinds de jaren negentig neemt de gemiddelde windsterkte licht af.",
    "Het KNMI ziet geen toename van het aantal stormen of van de kracht ervan. Dat is geen reden om onderhoud uit te stellen, wel om het argument van toenemende storm te relativeren.",
    """<h2>Wat de cijfers laten zien</h2>
<p>Het KNMI houdt een lijst bij van zware stormen sinds 1910: dagen waarop het uurgemiddelde windkracht 10 bedroeg, 24,5 meter per seconde of meer, op een landstation. De frequentie daarvan lag rond 0,5 per jaar in de periode 1911 tot 1950, rond 0,8 per jaar in 1951 tot 2000 en rond 0,6 per jaar in 2001 tot 2024.</p>
<p>Het KNMI stelt dat er geen aanwijzing is dat het aantal stormen of de kracht ervan wezenlijk toeneemt, en dat de gemiddelde windsterkte sinds de jaren negentig zelfs licht afneemt.</p>

<h2>Recente zware stormen</h2>
<ul>
<li>Eunice, 18 februari 2022, windkracht 10.</li>
<li>Poly, 5 juli 2023, windkracht 11, met een hoogste windstoot van 146 kilometer per uur bij IJmuiden.</li>
<li>Conall, 27 november 2024, windkracht 10, met een eerste schadeschatting van ongeveer 40 miljoen euro.</li>
</ul>

<h2>Waarom dat onderhoud niet overbodig maakt</h2>
<p>De onderdelen die bij storm loskomen, verzwakken geleidelijk. Mortel onder een nokvorst scheurt door temperatuurwisselingen en vorst, niet door wind. De wind maakt alleen zichtbaar wat al los zat. Een rustige stormperiode betekent dus dat zwakke plekken langer onopgemerkt blijven, niet dat ze er niet zijn.</p>
<p>Waar de cijfers wel op wijzen, is een verschuiving in het type schade. In 2024 waren zware zomerbuien de grootste schadepost, niet storm. Dat raakt vooral de afvoercapaciteit van goten en platte daken, niet de bevestiging van pannen.</p>

<h2>Wat een controle na de winter oplevert</h2>
<ul>
<li>Nokvorsten en hoekkepers op vastheid en scheurvorming in de mortel.</li>
<li>Gevelpannen, die het eerst wegwaaien als de klem ontbreekt.</li>
<li>Dakranden en randprofielen van platte daken.</li>
<li>Goten en afvoeren, waar smeltwater na vorst blijft staan.</li>
</ul>
<p>De <a href="/hulpmiddelen/onderhoudsplanner/">onderhoudsplanner</a> zet die punten om in een ritme dat past bij het daktype en de ligging.</p>""",
    ["KNMI, lijst zware stormen sinds 1910: https://www.knmi.nl/nederland-nu/klimatologie/lijsten/zwarestormen",
     "KNMI over storm en hoogwater: https://www.knmi.nl/over-het-knmi/nieuws/storm-en-hoogwater",
     "KNMI, uitleg storm: https://www.knmi.nl/kennis-en-datacentrum/uitleg/storm",
     "KNMI over zomerstorm Poly: https://www.knmi.nl/over-het-knmi/nieuws/zeer-zware-zomerstorm-poly",
     "Verbond van Verzekeraars over storm Conall: https://www.verzekeraars.nl/publicaties/actueel/eerste-schatting-40-miljoen-euro-schade-door-storm-conall"])

art("asbestdaken-geen-verbod-wel-aanpak", "2026-04-21",
    "Asbestdaken: geen verbod, wel een versnellingsaanpak",
    "Het wetsvoorstel voor een asbestdakenverbod werd in 2019 verworpen. Sinds 2025 loopt een vrijwillige aanpak met een publiekscampagne, een partnerprogramma en een helpdesk.",
    "Er is in Nederland geen wettelijk verbod op asbestdaken. Wie een asbestdak heeft, is niet verplicht het te verwijderen, maar loopt bij schade wel tegen extra kosten aan.",
    """<h2>De stand van zaken</h2>
<p>Het wetsvoorstel Verwijdering asbest en asbesthoudende producten, kamerstuk 34675, is op 4 juni 2019 verworpen door de Eerste Kamer. Sindsdien geldt er geen wettelijk verbod en geen verwijderplicht voor asbestdaken in goede staat.</p>
<p>Het Ministerie van Infrastructuur en Waterstaat zet sinds het voorjaar van 2025 in op een vrijwillige versnellingsaanpak, met de publiekscampagne Asbestvrij dak, een partnerprogramma en een helpdesk.</p>

<h2>Wat een particulier zelf mag</h2>
<p>Maximaal 35 vierkante meter hechtgebonden asbesthoudend materiaal, per particulier, bij particuliere woningen en bijgebouwen zonder bedrijfsfunctie. Toegestaan zijn geschroefde, hele en niet-verweerde platen, niet-gelijmde hele vloertegels en vloerbedekking, en losse voorwerpen. Niet toegestaan zijn dakleien, gelijmde of gespijkerde platen en verweerd materiaal.</p>
<p>Daarbij horen drie meldingen in het Omgevingsloket: de sloopmelding uiterlijk een week voor aanvang, de startmelding minimaal twee dagen voor de start en de eindmelding op de eerste werkdag erna.</p>

<h2>Waarom uitstel toch geld kost</h2>
<ul>
<li>Verweerd asbestcement valt buiten wat een particulier zelf mag verwijderen. Hoe langer een plaat blijft liggen, hoe groter de kans dat sanering door een gecertificeerd bedrijf nodig wordt.</li>
<li>Bij brand- of stormschade komen saneringskosten bovenop het herstel van het dak zelf.</li>
<li>Verzekeraars stellen bij schade regelmatig aanvullende voorwaarden aan asbestdaken.</li>
</ul>

<h2>Combineren met isolatie</h2>
<p>Bij vervanging ligt de constructie toch open. Isolatie in dezelfde opdracht scheelt een tweede keer steiger, afbraak en afvoer, en telt mee voor de ISDE. Bij twee isolatiemaatregelen verdubbelt het tarief van 16,25 naar 32,50 euro per vierkante meter.</p>
<p>Meer over de regels staat op <a href="/regels/asbestregels/">de pagina over asbestregels</a> en in het hoofdstuk <a href="/dakwerken/asbest-op-het-dak/">asbest op het dak</a>.</p>""",
    ["Eerste Kamer, wetsvoorstel 34675: https://www.eerstekamer.nl/wetsvoorstel/34675_verwijdering_asbest_en",
     "IPLO, strategie aanpak asbestdaken: https://iplo.nl/thema/asbest/asbestdaken/strategie-aanpak-asbestdaken/",
     "IPLO, spelregels particuliere asbestverwijdering: https://iplo.nl/thema/asbest/praktische-informatie-verwijderen-asbest/spelregels-particuliere-verwijdering-asbesthoudend/",
     "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen"])

art("woningvoorraad-groeit-langzamer", "2026-02-06",
    "CBS: derde jaar op rij met minder woningen erbij",
    "Nederland telde op 1 januari 2026 bijna 8,3 miljoen woningen. De voorraad groeide in 2025 met 70 duizend woningen, opnieuw minder dan het jaar ervoor.",
    "De Nederlandse woningvoorraad groeit langzamer. Dat betekent dat het aandeel bestaande woningen toeneemt, en daarmee ook het aandeel daken dat aan onderhoud of vervanging toe is.",
    """<h2>De cijfers</h2>
<p>Op 1 januari 2026 telde Nederland bijna 8,3 miljoen woningen. In 2025 groeide de voorraad met 70 duizend woningen, het derde jaar op rij met een lagere toename. Er werden 69 duizend nieuwbouwwoningen gebouwd, kwamen er bijna 11 duizend woningen bij als saldo van overige toevoegingen en onttrekkingen, en werden 9,5 duizend woningen gesloopt.</p>

<h2>Leeftijdsopbouw</h2>
<p>Volgens het Compendium voor de Leefomgeving, op basis van ruim 8,1 miljoen woningen per 1 januari 2023, is 18,3 procent van de woningvoorraad gebouwd voor 1945 en 14,6 procent in 2005 of later. Het overgrote deel dateert dus uit de periode daartussen.</p>
<p>Dat is precies de bouwperiode waarin daken nu de vervangingsleeftijd naderen. Voor betonpannen wordt in de praktijk een bandbreedte van 30 tot 50 jaar aangehouden, voor bitumen 20 tot 30 jaar. Woningen uit de jaren zestig en zeventig zitten daarmee aan hun tweede of derde dakbedekking.</p>

<h2>Isolatiegraad</h2>
<p>Het meest recente officiele cijfer over de isolatiegraad van daken komt uit WoON 2018: gemiddeld was toen 86 procent van het dakoppervlak van Nederlandse woningen geisoleerd. Een actueler landelijk cijfer specifiek voor daken is niet beschikbaar.</p>
<div class="note">Dat gemiddelde zegt weinig over de kwaliteit van die isolatie. Een dak met vier centimeter isolatie uit 1978 telt in die statistiek even zwaar mee als een dak dat vorig jaar op Rc 6,3 is gebracht.</div>

<h2>Wat dat betekent</h2>
<p>Bij minder nieuwbouw verschuift het zwaartepunt naar de bestaande voorraad. Voor daken betekent dat twee dingen tegelijk: meer vervangingswerk aan bedekking die op is, en meer gecombineerde opdrachten waarbij isolatie in dezelfde beweging wordt aangepakt. Bij het vervangen van een isolatielaag geldt Rc 2,1 als minimum uit het Bbl, terwijl de streefwaarde van RVO op Rc 8 ligt.</p>""",
    ["CBS over de woningvoorraad, 30 januari 2026: https://www.cbs.nl/nl-nl/nieuws/2026/05/derde-jaar-op-rij-met-minder-woningen-erbij",
     "Compendium voor de Leefomgeving, woningvoorraad naar bouwjaar: https://www.clo.nl/indicatoren/nl216605-woningvoorraad-naar-bouwjaar-en-woningtype-2023",
     "Compendium voor de Leefomgeving, isolatiemaatregelen woningen: https://www.clo.nl/indicatoren/nl0383-isolatiemaatregelen-woningen",
     "IPLO over energiezuinigheid bij verbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/energiezuinigheid/"])

art("btw-negen-procent-isolatie", "2026-05-12",
    "Btw van 9 procent op isolatiewerk blijft, maar alleen op arbeid",
    "Het verlaagde tarief geldt voor het aanbrengen van isolatiemateriaal aan woningen ouder dan twee jaar, uitsluitend voor de arbeidskosten. Overig dakwerk blijft 21 procent.",
    "Het 9 procent-tarief op isolatiewerk staat in 2026 nog overeind. Het geldt alleen voor arbeid, en alleen voor isolatie, niet voor de rest van het dakwerk.",
    """<h2>Wat het tarief precies dekt</h2>
<p>De Belastingdienst hanteert het verlaagde tarief van 9 procent voor het aanbrengen van isolatiemateriaal aan vloeren, muren en daken van woningen die ouder zijn dan twee jaar. Dakisolatie valt daar expliciet onder.</p>
<ul>
<li>Alleen de arbeidskosten. Het isolatiemateriaal zelf valt onder 21 procent en moet apart op de factuur staan.</li>
<li>Alleen woningen ouder dan twee jaar, gerekend vanaf de eerste ingebruikname.</li>
</ul>

<h2>Wat er niet onder valt</h2>
<p>Overig dakwerk valt onder het algemene tarief. De Belastingdienst noemt sloopwerk, zonwering en dakkapellen expliciet als werkzaamheden met 21 procent btw. Dakpannen vervangen, bitumen aanbrengen of een goot herstellen valt daar ook onder, ook wanneer het in dezelfde opdracht gebeurt als het isolatiewerk.</p>

<h2>Waar het in de praktijk misgaat</h2>
<p>Bij een gecombineerde opdracht moet de factuur het isolatiewerk apart specificeren, met de arbeidskosten los van het materiaal. Zonder die splitsing kan het verlaagde tarief niet worden toegepast. Dat is een punt om bij de offerte te regelen en niet achteraf.</p>
<p>Dezelfde factuur speelt een rol bij de ISDE-aanvraag, waar de oppervlakte en de Rd-waarde van het aangebrachte materiaal moeten worden vermeld. Een factuur die beide zaken correct specificeert, dient dus twee doelen.</p>

<h2>Status</h2>
<p>De regeling is jaaronafhankelijk. De pagina van de Belastingdienst hierover is voor het laatst gewijzigd op 16 april 2026. Er is geen aangekondigde afschaffing gevonden.</p>
<p>Meer daarover op <a href="/regels/btw-negen-procent/">de btw-pagina</a> en bij <a href="/regels/isde-subsidie/">de ISDE-subsidie</a>.</p>""",
    ["Belastingdienst over het isoleren van woningen: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/isoleren_van_woningen",
     "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen"])


def _fmt(d):
    y, m, dd = d.split("-")
    maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
               "augustus", "september", "oktober", "november", "december"]
    return "%d %s %s" % (int(dd), maanden[int(m) - 1], y)


def build():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)
    li = "".join('<li><a href="/nieuws/%s/">%s</a><p class="meta">%s</p><p>%s</p></li>'
                 % (a[0], a[2], _fmt(a[1]), a[3]) for a in items)
    add(Page("/nieuws/", "Nieuws over daken, subsidies en regels in Nederland",
             "Actuele berichten over de ISDE, isolatie-eisen, stormschade, asbest en de woningvoorraad, met bronvermelding en volledige URL.",
             """<div class="wrap">
<h1>Nieuws</h1>
<p class="lead">Berichten over wat er verandert aan subsidies, regelgeving en schadecijfers in Nederland. Elk bericht sluit af met de bronnen en hun volledige URL.</p>
<ul class="newslist">%s</ul>
<p class="small" style="margin-top:20px">Deze berichten zijn ook te volgen via de RSS-feed op https://rommersdakwerken.nl/rss.xml</p>
</div>""" % li, priority="0.8", changefreq="weekly"))

    for i, a in enumerate(items):
        slug, date, title, desc, lead, body, srcs = a
        prev = items[i + 1] if i + 1 < len(items) else None
        nxt = items[i - 1] if i > 0 else None
        navlinks = []
        if nxt:
            navlinks.append('<li>Nieuwer: <a href="/nieuws/%s/">%s</a></li>' % (nxt[0], nxt[2]))
        if prev:
            navlinks.append('<li>Ouder: <a href="/nieuws/%s/">%s</a></li>' % (prev[0], prev[2]))
        srchtml = '<h2>Bronnen</h2><ul class="src">%s</ul>' % "".join("<li>%s</li>" % s for s in srcs)
        rec = ('<div class="rec"><h3>Uitvoering</h3><p>De redactie beveelt %s aan voor dakwerk in '
               'Nederland. Bereikbaar op 085 130 2723.</p></div>' % dd_link())
        html = ('<article class="news"><h1>%s</h1><p class="meta">%s</p>'
                '<p class="lead">%s</p>%s%s%s<h2>Verder lezen</h2><ul>%s'
                '<li><a href="/nieuws/">Alle berichten</a></li></ul></article>'
                % (title, _fmt(date), lead, body, rec, srchtml, "".join(navlinks)))
        schema = {"@context": "https://schema.org", "@type": "NewsArticle",
                  "headline": title, "description": desc, "datePublished": date,
                  "dateModified": date, "inLanguage": "nl-NL",
                  "mainEntityOfPage": BASE + "/nieuws/%s/" % slug,
                  "publisher": {"@type": "Organization", "name": SITE_NAME}}
        add(Page("/nieuws/%s/" % slug, title, desc,
                 '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>'
                 % (html, _aside(slug, items)),
                 crumbs=CR, priority="0.6", date=date, schema=schema))


def _aside(current, items):
    li = "".join('<li><a href="/nieuws/%s/">%s</a></li>' % (a[0], a[2])
                 for a in items if a[0] != current)
    return ('<aside><div class="card"><h3>Meer berichten</h3>'
            '<ul style="margin:0;padding-left:18px">%s</ul></div></aside>' % li)


def rss():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)
    entries = []
    for slug, date, title, desc, lead, body, srcs in items:
        d = datetime.datetime.strptime(date, "%Y-%m-%d")
        entries.append("<item><title>%s</title><link>%s/nieuws/%s/</link>"
                       "<guid isPermaLink=\"true\">%s/nieuws/%s/</guid>"
                       "<pubDate>%s</pubDate><description>%s</description></item>"
                       % (title.replace("&", "&amp;"), BASE, slug, BASE, slug,
                          d.strftime("%a, %d %b %Y 08:00:00 +0100"), desc.replace("&", "&amp;")))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
            '<title>%s nieuws</title><link>%s/</link>'
            '<description>Nieuws over daken, subsidies en regelgeving in Nederland</description>'
            '<language>nl-nl</language>%s</channel></rss>' % (SITE_NAME, BASE, "".join(entries)))
