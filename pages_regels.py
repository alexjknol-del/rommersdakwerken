# -*- coding: utf-8 -*-
"""Regels en subsidies in Nederland."""
from engine import Page, add, dd_link

CR = [("/regels/", "Regels en subsidies")]

ITEMS = [
    ("isde-subsidie", "ISDE-subsidie voor dakisolatie",
     "16,25 euro per vierkante meter, verdubbeling bij twee maatregelen"),
    ("isolatie-eisen", "Isolatie-eisen uit het Bbl",
     "Rc 6,3 bij nieuwbouw, Rc 2,1 bij het vervangen van een isolatielaag"),
    ("vergunningvrij-bouwen", "Vergunningvrij bouwen aan het dak",
     "Dakpannen, dakramen, dakkapellen en de regels bij monumenten"),
    ("asbestregels", "Asbestregels",
     "35 vierkante meter, de meldingen en de status van het asbestdakenverbod"),
    ("verzekering-stormschade", "Verzekering en stormschade",
     "Windkracht 7 als drempel, dekking en uitsluitingen"),
    ("btw-negen-procent", "Btw van 9 procent op isolatiewerk",
     "Alleen arbeidsloon, alleen bij woningen ouder dan twee jaar"),
]


def sources(items):
    return '<h2>Bronnen</h2><ul class="src">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def _p(slug, title, desc, body):
    aside = ('<aside><div class="card"><h3>Meer over regels en subsidies</h3>'
             '<ul style="margin:0;padding-left:18px">%s</ul></div></aside>'
             % "".join('<li><a href="/regels/%s/">%s</a></li>' % (s, t)
                       for s, t, _ in ITEMS if s != slug))
    add(Page("/regels/%s/" % slug, title, desc,
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, aside),
             crumbs=CR, priority="0.7"))


def build():
    tiles = "".join('<a class="tile" href="/regels/%s/"><b>%s</b><span>%s</span></a>'
                    % (s, t, d) for s, t, d in ITEMS)
    add(Page("/regels/", "Regels en subsidies voor dakwerk in Nederland",
             "De ISDE-subsidie, de isolatie-eisen uit het Besluit bouwwerken leefomgeving, vergunningvrij bouwen, asbestregels, verzekering en het btw-tarief, met de stand van augustus 2026.",
             """<div class="wrap">
<h1>Regels en subsidies</h1>
<p class="lead">Zes regelingen bepalen wat er bij dakwerk mag, moet en wordt vergoed. Deze pagina's zetten per regeling op een rij wat geldt, met de datum en de bron erbij. De stand is die van augustus 2026.</p>
<div class="grid">%s</div>
<div class="note">Regelingen veranderen, subsidiebudgetten raken op. Per 3 augustus 2026 was ongeveer 51,5 procent van het ISDE-budget van 2026 geclaimd. De officiele bron blijft leidend en staat onderaan elke pagina met volledige URL vermeld.</div>
<h2>Volgorde die tijd bespaart</h2>
<ol>
<li>Nagaan of het pand een monument is of in een beschermd stads- of dorpsgezicht ligt. Dat bepaalt of vergunningvrij bouwen van toepassing is.</li>
<li>Nagaan of er asbesthoudend materiaal op het dak ligt. Dat bepaalt de werkwijze, de meldingen en de planning.</li>
<li>Bepalen welke maatregelen samen kunnen worden uitgevoerd. Bij twee isolatiemaatregelen verdubbelt de ISDE.</li>
<li>Pas daarna offertes vergelijken, want de subsidievoorwaarden stellen eisen aan de Rd-waarde en aan de oppervlakte.</li>
</ol>
</div>""" % tiles, priority="0.8"))

    _p("isde-subsidie", "ISDE-subsidie voor dakisolatie in 2026",
       "Bedrag per vierkante meter, de Rd-eis van 3,5, de minimale oppervlakte, de verdubbeling bij twee maatregelen en de stand van het budget.",
       """<h1>ISDE-subsidie voor dakisolatie</h1>
<p class="lead">De Investeringssubsidie duurzame energie en energiebesparing vergoedt een deel van de kosten van dakisolatie. Aanvragen voor 2026 zijn open sinds 5 januari 2026, 12.00 uur. RVO geeft aan dat de regeling doorloopt tot en met 31 december 2030.</p>

<h2>Bedragen</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Bedrag</th></tr>
<tr><td>Dakisolatie, een maatregel</td><td>16,25 euro per vierkante meter</td></tr>
<tr><td>Dakisolatie bij twee of meer maatregelen</td><td>32,50 euro per vierkante meter</td></tr>
<tr><td>Biobased isolatiemateriaal</td><td>5 euro per vierkante meter extra</td></tr>
<tr><td>Energiezuinige ventilatie, nieuw in 2026</td><td>400 euro eenmalig, mits gecombineerd met minstens een isolatiemaatregel</td></tr>
</table></div>
<p>Het tarief is gelijk voor hellende en platte daken. Per 2026 is de MKI-eis voor biobased materiaal verruimd van maximaal 0,85 naar maximaal 1,90.</p>

<h2>Voorwaarden</h2>
<ul>
<li>Rd-waarde van het nieuw aangebrachte isolatiemateriaal: minimaal 3,5 vierkante meter kelvin per watt.</li>
<li>Minimale oppervlakte 20 vierkante meter, maximaal subsidiabel 200 vierkante meter.</li>
<li>Aanvragen binnen 24 maanden na uitvoering van de werkzaamheden.</li>
<li>Twee maatregelen zijn niet verplicht. Een isolatiemaatregel volstaat, maar het bedrag verdubbelt bij een tweede isolatiemaatregel of bij combinatie met een warmtepomp, zonneboiler of warmtenetaansluiting. De volgende maatregel moet binnen 24 maanden na de vorige zijn uitgevoerd.</li>
</ul>

<h2>Wat de verdubbeling in de praktijk betekent</h2>
<p>Bij 100 vierkante meter dakisolatie gaat het om 1.625 euro bij een enkele maatregel en 3.250 euro bij twee maatregelen. Dat verschil is de reden om dakisolatie te plannen samen met bijvoorbeeld vloer- of gevelisolatie, en niet los in de tijd.</p>

<h2>Budget 2026</h2>
<p>Voor 2026 is 500 miljoen euro beschikbaar voor het geheel van zonneboilers, warmtepompen, isolatie, ventilatie, elektrisch koken en warmtenetaansluiting, plus 5 miljoen euro apart voor kleinschalige windturbines. Stand per 3 augustus 2026: 127.377 aanvragen voor 189.125 apparaten of maatregelen, samen 257,4 miljoen euro, ongeveer 51,5 procent van het budget. Daarvan ging 155,7 miljoen euro naar isolatie bij particulieren, waarvan 40,0 miljoen euro naar dakisolatie.</p>
<div class="note">De <a href="/hulpmiddelen/stormschade-en-subsidiecheck/">subsidiecheck</a> op deze site rekent het bedrag door voor een ingevoerde oppervlakte, inclusief de verdubbeling en de biobased bonus.</div>
%s
%s""" % ('<div class="rec"><h3>Uitvoering</h3><p>De Rd-waarde van het toegepaste materiaal en de aangebrachte oppervlakte horen in de offerte en op de factuur te staan, want daarop wordt de aanvraag beoordeeld.</p><p>De redactie beveelt %s aan voor dakwerk in Nederland.</p></div>' % dd_link("dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
         sources([
             "RVO, ISDE voor woningeigenaren: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren",
             "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen",
             "RVO, wat wijzigt er in 2026: https://www.rvo.nl/subsidies-financiering/isde/isde-wat-wijzigt-er-2026",
             "RVO, ISDE-budget: https://www.rvo.nl/subsidies-financiering/isde/budget",
         ])))

    _p("isolatie-eisen", "Isolatie-eisen voor daken in het Bbl",
       "Rc 6,3 bij nieuwbouw, Rc 2,1 bij het vervangen van een isolatielaag, het rechtens verkregen niveau en de streefwaarde van Rc 8.",
       """<h1>Isolatie-eisen uit het Bbl</h1>
<p class="lead">Het Besluit bouwwerken leefomgeving stelt eisen aan de warmteweerstand van daken. Die eisen verschillen sterk tussen nieuwbouw en verbouw, en dat verschil verklaart veel misverstanden in offertes.</p>

<h2>Nieuwbouw</h2>
<div class="tablewrap"><table>
<tr><th>Onderdeel</th><th>Eis</th></tr>
<tr><td>Dak</td><td>Rc minimaal 6,3 m&sup2;K/W</td></tr>
<tr><td>Gevel</td><td>Rc minimaal 4,7 m&sup2;K/W</td></tr>
<tr><td>Vloer boven de begane grond</td><td>Rc minimaal 3,7 m&sup2;K/W</td></tr>
<tr><td>Elk afzonderlijk onderdeel van de scheidingsconstructie</td><td>Rc minimaal 2,6 m&sup2;K/W</td></tr>
<tr><td>Ramen, deuren en kozijnen</td><td>U maximaal 2,2 W/m&sup2;K per onderdeel, gemiddeld maximaal 1,65</td></tr>
</table></div>

<h2>Verbouw en renovatie, artikel 5.20 Bbl</h2>
<ul>
<li><b>Lid 1.</b> Verbouw van bouwdelen in de thermische schil: het rechtens verkregen niveau, met als ondergrens gemiddeld Rc 1,4 m&sup2;K/W.</li>
<li><b>Lid 2.</b> Vervangen of vernieuwen van isolatielagen of van ramen en deuren: dak minimaal Rc 2,1, gevel minimaal Rc 1,4, vloer minimaal Rc 2,6, ramen en deuren maximaal U 2,2.</li>
<li><b>Lid 3.</b> Dakkapellen: nieuwbouwniveau, dus Rc 6,3 voor het dak.</li>
<li><b>Lid 4.</b> Ingrijpende renovatie: nieuwbouweisen op het gerenoveerde deel.</li>
</ul>
<p>Het rechtens verkregen niveau is het niveau dat het bouwwerk op het moment van de verbouwing legaal heeft. Bij een woning uit 1965 zonder dakisolatie ligt dat laag, wat betekent dat de ondergrens van Rc 1,4 in beeld komt zodra de thermische schil wordt aangepakt.</p>

<h2>Wettelijke eis tegenover streefwaarde</h2>
<p>RVO publiceert daarnaast een streefwaarde voor het dak van Rc 8 m&sup2;K/W, ongeveer 35 centimeter isolatie. Die waarde is niet wettelijk verplicht maar geeft aan wat er nodig is voor een woning die klaar is voor verwarming zonder aardgas.</p>
<div class="note">Het verschil is groot: Rc 2,1 is een wettelijk minimum bij vervanging, Rd 3,5 is de subsidievoorwaarde voor het materiaal, Rc 6,3 geldt bij nieuwbouw en Rc 8 is de streefwaarde. Bij een dakvernieuwing is het zinvol te vragen welke waarde de offerte hanteert.</div>

<h2>Een kanttekening bij de artikelnummers</h2>
<p>IPLO noemt artikel 4.152 Bbl voor de Rc-waarden bij nieuwbouw, artikel 4.153 voor de U-waarden en artikel 4.154 voor luchtdoorlatendheid. De inhoudsopgave van het Bbl op wetten.overheid.nl noemt artikel 4.150 bij thermische isolatie. Wie zich op een artikelnummer wil beroepen, controleert dat in de actuele wettekst op https://wetten.overheid.nl/BWBR0041297</p>
%s""" % sources([
           "IPLO over energiezuinigheid bij nieuwbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/nieuwbouw/rijksregels/energiezuinigheid/",
           "IPLO over energiezuinigheid bij verbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/energiezuinigheid/",
           "IPLO over het rechtens verkregen niveau: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/rechtens-verkregen-niveau/",
           "Besluit bouwwerken leefomgeving: https://wetten.overheid.nl/BWBR0041297",
           "RVO over standaard en streefwaarden woningisolatie: https://www.rvo.nl/onderwerpen/wetten-en-regels-gebouwen/standaard-streefwaarden-woningisolatie",
       ]))

    _p("vergunningvrij-bouwen", "Vergunningvrij bouwen aan het dak",
       "Wanneer dakpannen vervangen, dakisolatie, een dakkapel en een dakraam vergunningvrij zijn, en wat er anders is bij monumenten.",
       """<h1>Vergunningvrij bouwen aan het dak</h1>
<p class="lead">Veel dakwerk is vergunningvrij, maar de grens ligt op detail. Het draait om de vraag of detaillering, profilering en vormgeving veranderen, en of het pand een monument is.</p>

<h2>Dakpannen vervangen</h2>
<p>Het vervangen van dakpannen valt onder gewoon onderhoud en is vergunningvrij, mits detaillering, profilering en vormgeving niet veranderen. IPLO verwijst daarbij naar uitspraak 201501400/1/A1.</p>
<p>Bij monumenten geldt artikel 2.30 lid 1 Bbl strenger. Verandert de kleur of de materiaalsoort, dan kan een vergunning voor een monumentenactiviteit nodig zijn, mede op grond van artikel 13.11 lid 1 Bal en de gemeentelijke erfgoedverordening.</p>

<h2>Dakisolatie</h2>
<p>Isolatie aan de binnenzijde raakt de buitenzijde van het bouwwerk niet en valt daarmee buiten de vergunningplicht voor het ruimtelijke deel. Isolatie aan de buitenzijde verandert de vormgeving en detaillering en valt dan niet meer onder gewoon onderhoud.</p>
<div class="note">Er is geen IPLO-pagina gevonden die dit met zoveel woorden voor dakisolatie bevestigt. Wie buitenom isoleert en het dakvlak daarmee hoger legt, vraagt dat het beste na bij de eigen gemeente voordat de offerte wordt getekend.</div>

<h2>Dakkapel</h2>
<p>Vergunningvrij voor het ruimtelijke deel bij vijf voorwaarden: een plat dak, hoogte vanaf de voet niet meer dan 1,75 meter, onderzijde meer dan 0,5 en minder dan 1 meter boven de dakvoet, bovenzijde meer dan 0,5 meter onder de daknok, en zijkanten meer dan 0,5 meter van de zijkanten van het dakvlak.</p>
<p>Op het achterdakvlak of een niet naar openbaar toegankelijk gebied gekeerd zijdakvlak geldt dit landelijk. Op het voordakvlak of een naar openbaar gebied gekeerd zijdakvlak alleen wanneer het omgevingsplan daar geen redelijke eisen van welstand stelt. Bij een gemeentelijk, provinciaal of rijksmonument vervalt de vrijstelling, en in een rijksbeschermd stads- of dorpsgezicht geldt ze niet voor het zijdakvlak of een naar openbaar gebied gekeerd achterdakvlak.</p>

<h2>Dakraam, daklicht of lichtstraat</h2>
<p>Artikel 2.29 Bbl: op het achterdakvlak, een niet-openbaar zijdakvlak en platte daken mag de constructie niet meer dan 0,6 meter buiten het dakvlak steken, met aan alle randen meer dan 0,5 meter afstand. Op het voordakvlak en een naar openbaar gebied gekeerd zijdakvlak mag de constructie niet buiten het dakvlak uitsteken, met dezelfde randafstand. Bij monumenten en in beschermde stads- en dorpsgezichten vervalt dit volledig.</p>

<h2>Monumenten</h2>
<p>Vergunningvrij is bij een monument uitsluitend gelijkwaardig herstel: kapotte dakpannen vervangen door hetzelfde type, of een rieten dak opstoppen, waarbij materiaalsoort, kleur, vorm, detaillering en profilering niet veranderen. Alles daarbuiten vraagt een vergunning voor een monumentenactiviteit.</p>
%s""" % sources([
           "IPLO over gewoon onderhoud: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/gewoon-onderhoud/",
           "IPLO over vergunningvrije dakkapellen: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/dakkapel/",
           "IPLO over vergunningvrije dakramen: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/dakramen/",
           "Monumenten.nl over vergunningsvrije werkzaamheden aan een monument: https://www.monumenten.nl/monumenten-onderhouden/wetten-en-regels/welke-werkzaamheden-aan-een-monument-zijn-vergunningsvrij",
       ]))

    _p("asbestregels", "Asbestregels bij dakwerk",
       "De grens van 35 vierkante meter voor particulieren, wat wel en niet is toegestaan, de meldingen in het Omgevingsloket en de status van het asbestdakenverbod.",
       """<h1>Asbestregels</h1>
<p class="lead">Voor asbest op daken gelden vaste regels over wie wat mag verwijderen en welke meldingen daarbij horen. Een landelijk verbod op asbestdaken is er niet.</p>

<h2>Wat een particulier zelf mag</h2>
<p>Maximaal 35 vierkante meter hechtgebonden asbesthoudend materiaal, per particulier, en uitsluitend bij particuliere woningen en bijgebouwen zonder bedrijfsfunctie.</p>
<div class="tablewrap"><table>
<tr><th>Toegestaan</th><th>Niet toegestaan</th></tr>
<tr><td>Geschroefde, hele en niet-verweerde asbestplaten</td><td>Dakleien</td></tr>
<tr><td>Niet-gelijmde hele vloertegels en vloerbedekking</td><td>Gelijmde of gespijkerde platen</td></tr>
<tr><td>Losse voorwerpen zoals bloembakken</td><td>Verweerd materiaal</td></tr>
</table></div>
<p>Overige voorwaarden: geen professionals inschakelen voor de verwijdering, het materiaal heel houden, dubbel en transparant verpakken met de vermelding Asbest, en inleveren bij de milieustraat.</p>

<h2>Meldingen</h2>
<ul>
<li>Sloopmelding in het Omgevingsloket, uiterlijk een week voor aanvang.</li>
<li>Startmelding, minimaal twee dagen voor de daadwerkelijke start.</li>
<li>Eindmelding, op de eerste werkdag na afronding.</li>
</ul>

<h2>Het asbestdakenverbod</h2>
<p>Het wetsvoorstel Verwijdering asbest en asbesthoudende producten, kamerstuk 34675, is op 4 juni 2019 verworpen door de Eerste Kamer. Er is sindsdien geen wettelijk verbod en geen verwijderplicht voor asbestdaken in goede staat.</p>
<p>Het Ministerie van Infrastructuur en Waterstaat zet sinds het voorjaar van 2025 in op een vrijwillige versnellingsaanpak, met de publiekscampagne Asbestvrij dak, een partnerprogramma en een helpdesk.</p>
<div class="note">Het aantal resterende vierkante meters asbestdak in Nederland is niet uit een officiele bron te halen. Getallen die daarover circuleren zijn schattingen.</div>

<h2>Praktisch bij een dakvernieuwing</h2>
<p>Gaat het om meer dan 35 vierkante meter of om een niet-toegestane toepassing, dan verloopt de verwijdering via een gecertificeerd saneringsbedrijf. Dat vraagt planning: de sanering gaat vooraf aan het nieuwe dak, en beide stappen worden op elkaar afgestemd zodat de constructie niet onnodig lang openligt.</p>
%s""" % sources([
           "IPLO, spelregels particuliere asbestverwijdering: https://iplo.nl/thema/asbest/praktische-informatie-verwijderen-asbest/spelregels-particuliere-verwijdering-asbesthoudend/",
           "IPLO, strategie aanpak asbestdaken: https://iplo.nl/thema/asbest/asbestdaken/strategie-aanpak-asbestdaken/",
           "Eerste Kamer, wetsvoorstel 34675: https://www.eerstekamer.nl/wetsvoorstel/34675_verwijdering_asbest_en",
           "Rijksoverheid over asbestregels: https://www.rijksoverheid.nl/onderwerpen/asbest/asbestregels",
       ]))

    _p("verzekering-stormschade", "Verzekering en stormschade aan het dak",
       "Wat de opstalverzekering dekt, de drempel van windkracht 7, de uitsluiting van achterstallig onderhoud en de schadecijfers van 2022 tot 2025.",
       """<h1>Verzekering en stormschade</h1>
<p class="lead">Stormschade aan het dak valt in de meeste gevallen onder de woonhuisverzekering. Waar het misgaat, is bij de vraag of er sprake was van storm en of het dak in goede staat verkeerde.</p>

<h2>De drempel</h2>
<p>Het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 14 meter per seconde of 50 kilometer per uur, als drempel waarboven van storm wordt gesproken. Het KNMI hanteert een strengere meteorologische definitie: storm is windkracht 9, een uurgemiddelde van 75 tot 88 kilometer per uur.</p>
<p>Die twee definities lopen in schadegesprekken vaak door elkaar. Voor de polis telt de definitie die de verzekeraar hanteert, en die staat in de polisvoorwaarden.</p>

<h2>Wat doorgaans gedekt is</h2>
<ul>
<li>Schade aan de woning, de inboedel en schuttingen door storm, meestal met een eigen risico.</li>
<li>Noodherstel om verdere schade te voorkomen, mits gemeld.</li>
</ul>

<h2>Wat doorgaans niet gedekt is</h2>
<ul>
<li>Schade die het gevolg is van achterstallig onderhoud. Een nokvorst die al jaren los lag valt daaronder.</li>
<li>Slijtage en veroudering van de dakbedekking zelf.</li>
<li>Schade aan losse voorwerpen buiten, afhankelijk van de polis.</li>
</ul>
<p>Dat maakt de onderhoudsgeschiedenis relevant in een schadedossier. Inspectierapporten en foto's van eerdere jaren tonen aan dat het dak in orde was.</p>

<h2>Schadecijfers</h2>
<div class="tablewrap"><table>
<tr><th>Periode</th><th>Verzekerde schade</th></tr>
<tr><td>Februaristormen 2022, Dudley, Eunice en Franklin</td><td>Minimaal 500 miljoen euro</td></tr>
<tr><td>Zomerstorm Poly, 5 juli 2023</td><td>Eerste schatting 50 tot 100 miljoen euro</td></tr>
<tr><td>Klimaatschade 2024 totaal</td><td>Ongeveer 278 miljoen euro, met zomerbuien als grootste post</td></tr>
<tr><td>Storm Conall, 27 november 2024</td><td>Eerste schatting ongeveer 40 miljoen euro</td></tr>
<tr><td>Klimaatschade 2025 totaal</td><td>Ruim 155 miljoen euro, waarvan ruim 60 miljoen euro storm</td></tr>
</table></div>
<p>Voor 2026 is nog geen gepubliceerd stormschadecijfer van het Verbond beschikbaar.</p>

<h2>Melden</h2>
<p>De volgorde bij een schademelding: wachten tot het veilig is, fotograferen vanaf de grond, de binnenzijde nakijken, melden bij de verzekeraar, en een noodherstel laten uitvoeren om verdere schade te voorkomen. Definitief herstel volgt na de vaststelling. De <a href="/hulpmiddelen/stormschade-en-subsidiecheck/">stormcheck</a> loopt die stappen door.</p>
%s""" % sources([
           "Verbond van Verzekeraars over stormschade: https://www.verzekeraars.nl/verzekeringsthemas/schade/stormschade",
           "Verbond van Verzekeraars, infographic wind: https://www.verzekeraars.nl/verzekeringsthemas/klimaat-en-duurzaamheid/praktische-hulpmiddelen/infographic-verzekerbaarheid-klimaatrisico-s/wind",
           "Verbond van Verzekeraars, klimaatschade 2025: https://www.verzekeraars.nl/publicaties/actueel/hagel-en-storm-grootste-oorzaken-klimaatschade-in-2025",
           "KNMI, klimaatschademonitor 2024: https://www.knmi.nl/over-het-knmi/nieuws/buien-grootste-schadeboosdoener-in-2024-klimaatschademonitor-extreem-weer/",
           "KNMI, uitleg storm: https://www.knmi.nl/kennis-en-datacentrum/uitleg/storm",
       ]))

    _p("btw-negen-procent", "Btw van 9 procent op isolatiewerk",
       "Het verlaagde tarief geldt alleen voor arbeidskosten bij het isoleren van woningen ouder dan twee jaar; overig dakwerk valt onder 21 procent.",
       """<h1>Btw van 9 procent</h1>
<p class="lead">Voor het aanbrengen van isolatiemateriaal aan vloeren, muren en daken van woningen ouder dan twee jaar geldt het verlaagde btw-tarief van 9 procent. Dakisolatie valt daar expliciet onder.</p>

<h2>Wat er precies onder valt</h2>
<ul>
<li>Alleen de arbeidskosten. Het isolatiemateriaal zelf valt onder 21 procent en moet apart op de factuur staan.</li>
<li>Alleen woningen die ouder zijn dan twee jaar, gerekend vanaf de eerste ingebruikname.</li>
</ul>

<h2>Wat er niet onder valt</h2>
<p>Overig dakwerk valt niet onder het verlaagde tarief. De Belastingdienst noemt sloopwerk, zonwering en dakkapellen expliciet als werkzaamheden met 21 procent btw. Het vervangen van dakpannen, het aanbrengen van bitumen of het herstellen van een goot valt dus onder het algemene tarief, ook wanneer dat in dezelfde opdracht gebeurt als het isolatiewerk.</p>
<div class="note">Bij een gecombineerde opdracht is het van belang dat de factuur het isolatiewerk apart specificeert, met de arbeidskosten los van het materiaal. Zonder die splitsing kan het verlaagde tarief niet worden toegepast.</div>

<h2>Status van de regeling</h2>
<p>De regeling is jaaronafhankelijk. De pagina van de Belastingdienst hierover is voor het laatst gewijzigd op 16 april 2026. Er is geen aangekondigde afschaffing gevonden.</p>

<h2>Samenloop met de ISDE</h2>
<p>Het verlaagde btw-tarief en de ISDE-subsidie sluiten elkaar niet uit. De subsidie wordt berekend op basis van de aangebrachte oppervlakte en de Rd-waarde, niet op basis van het factuurbedrag, dus de btw-behandeling heeft daar geen invloed op.</p>
%s""" % sources([
           "Belastingdienst over het isoleren van woningen en het 9 procent-tarief: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/isoleren_van_woningen",
           "RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen",
       ]))
