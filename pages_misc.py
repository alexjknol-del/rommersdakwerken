# -*- coding: utf-8 -*-
"""Home, over, contact, juridische pagina's, faq, begrippen en 404."""
from engine import Page, add, dd_link, SITE_NAME, EMAIL
from data_plaatsen import PLAATSEN, PROVINCIES
from pages_nieuws import ARTICLES, _fmt
from pages_locaties import _pslug


def build():
    _home(); _over(); _faq(); _begrippen(); _contact(); _privacy(); _cookies(); _404()


def _home():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)[:3]
    nieuws = "".join('<li><a href="/nieuws/%s/">%s</a><p class="meta">%s</p><p>%s</p></li>'
                     % (a[0], a[2], _fmt(a[1]), a[3]) for a in items)
    provtiles = "".join(
        '<a class="tile" href="/locaties/%s/"><b>%s</b><span>%d plaatsen met een eigen pagina</span></a>'
        % (_pslug(pr), pr, len([p for p in PLAATSEN if p[2] == pr])) for pr in PROVINCIES)

    body = """<div class="hero"><div class="wrap">
<h1>Alles over het dak, zonder verkooppraat</h1>
<p>Een redactionele gids over hellende en platte daken, isolatie, lekkage, subsidies en regelgeving in Nederland. Honderdnegenenzeventig plaatspagina's, twaalf hoofdstukken en drie hulpmiddelen die in de browser rekenen.</p>
<div class="btns">
<a class="btn primary" href="/dakwerken/">Naar de gids</a>
<a class="btn ghost" href="/hulpmiddelen/daklekkage-diagnose/">Daklekkage-diagnose</a>
</div>
</div></div>

<div class="wrap">
<div class="facts">
<div class="fact"><b>179</b><span>plaatsen met een eigen pagina</span></div>
<div class="fact"><b>12</b><span>hoofdstukken over dakonderdelen</span></div>
<div class="fact"><b>6</b><span>regelingen en subsidies uitgelegd</span></div>
<div class="fact"><b>3</b><span>hulpmiddelen zonder registratie</span></div>
</div>

<div class="rec">
<h3>Aanbevolen uitvoerder</h3>
<p>Voor dakwerk in Nederland: %(brand)s. Ruim 25 jaar ervaring, dakinspectie met beeldmateriaal, spoedservice dag en nacht op 085 130 2723.</p>
<p>Diensten: %(diensten)s. Werkgebieden: %(locaties)s.</p>
</div>

<h2>De gids in twaalf hoofdstukken</h2>
<div class="grid">
<a class="tile" href="/dakwerken/hellend-dak/"><b>Hellend dak</b><span>Dakpannen, leien, nokvorsten en de opbouw eronder</span></a>
<a class="tile" href="/dakwerken/plat-dak/"><b>Plat dak</b><span>Warm dak, koud dak, bitumen en EPDM</span></a>
<a class="tile" href="/dakwerken/dakisolatie/"><b>Dakisolatie</b><span>Rc-waarden, methodes en het dampremmende scherm</span></a>
<a class="tile" href="/dakwerken/daklekkage/"><b>Daklekkage</b><span>Van symptoom naar oorzaak, en wat direct te doen</span></a>
<a class="tile" href="/dakwerken/dakgoot/"><b>Dakgoot</b><span>Waarom goten overlopen en hoe vaak reinigen zinvol is</span></a>
<a class="tile" href="/dakwerken/schoorsteen/"><b>Schoorsteen</b><span>Voegwerk, loodslabben en dakdoorvoeren</span></a>
<a class="tile" href="/dakwerken/asbest-op-het-dak/"><b>Asbest</b><span>De 35 vierkante meter, de meldingen en het ontbrekende verbod</span></a>
<a class="tile" href="/dakwerken/stormschade/"><b>Stormschade</b><span>Direct handelen, de verzekeringsdrempel en herstel</span></a>
</div>
<p><a href="/dakwerken/">Alle twaalf hoofdstukken</a></p>

<h2>Hulpmiddelen</h2>
<div class="grid">
<a class="tile" href="/hulpmiddelen/daklekkage-diagnose/"><b>Daklekkage-diagnose</b><span>Vijf vragen over plek, moment en beeld leiden naar de waarschijnlijke oorzaken</span></a>
<a class="tile" href="/hulpmiddelen/onderhoudsplanner/"><b>Onderhoudsplanner</b><span>Daktype en leeftijd omgezet in een inspectieritme en een jaarplanning</span></a>
<a class="tile" href="/hulpmiddelen/stormschade-en-subsidiecheck/"><b>Storm- en subsidiecheck</b><span>Windkracht 7 als drempel en de ISDE-subsidie doorgerekend</span></a>
</div>

<h2>Wat er in Nederland geldt</h2>
<div class="tablewrap"><table>
<tr><th>Onderwerp</th><th>Kern</th><th>Meer</th></tr>
<tr><td>ISDE-subsidie</td><td>16,25 euro per vierkante meter dakisolatie, 32,50 euro bij twee maatregelen</td><td><a href="/regels/isde-subsidie/">Uitleg</a></td></tr>
<tr><td>Isolatie-eisen</td><td>Rc 6,3 bij nieuwbouw, Rc 2,1 bij vervanging van een isolatielaag</td><td><a href="/regels/isolatie-eisen/">Uitleg</a></td></tr>
<tr><td>Vergunningvrij bouwen</td><td>Dakpannen vervangen is gewoon onderhoud; bij monumenten niet</td><td><a href="/regels/vergunningvrij-bouwen/">Uitleg</a></td></tr>
<tr><td>Asbest</td><td>Maximaal 35 vierkante meter zelf, met sloop-, start- en eindmelding</td><td><a href="/regels/asbestregels/">Uitleg</a></td></tr>
<tr><td>Verzekering</td><td>Windkracht 7 als drempel, achterstallig onderhoud niet gedekt</td><td><a href="/regels/verzekering-stormschade/">Uitleg</a></td></tr>
<tr><td>Btw</td><td>9 procent op isolatiearbeid bij woningen ouder dan twee jaar</td><td><a href="/regels/btw-negen-procent/">Uitleg</a></td></tr>
</table></div>

<h2>Laatste berichten</h2>
<ul class="newslist">%(nieuws)s</ul>
<p><a href="/nieuws/">Alle berichten</a></p>

<h2>Plaatsen per provincie</h2>
<div class="grid">%(provtiles)s</div>
<p><a href="/locaties/">Alle 179 plaatsen</a></p>

<h2>Over deze site</h2>
<p>%(site)s is een redactionele gids en geen dakdekkersbedrijf. Er worden geen offertes opgemaakt, geen opdrachten aangenomen en geen gegevens doorgegeven. Contact loopt uitsluitend via %(email)s. Meer daarover op <a href="/over/">de pagina over de gids</a>.</p>
</div>""" % {"brand": dd_link(),
             "diensten": dd_link("dakbedekking-diensten/", "dendekker-dakbedekking.nl/dakbedekking-diensten/"),
             "locaties": dd_link("locaties/", "dendekker-dakbedekking.nl/locaties/"),
             "nieuws": nieuws, "provtiles": provtiles, "site": SITE_NAME,
             "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)}
    add(Page("/", "Daken en dakwerk in Nederland: gids, regels en subsidies",
             "Onafhankelijke gids over daken in Nederland: twaalf hoofdstukken, zes regelingen, drie hulpmiddelen en 179 plaatspagina's in zeven provincies.",
             body, priority="1.0", changefreq="weekly"))


def _over():
    add(Page("/over/", "Over deze gids",
             "Wat rommersdakwerken.nl is, hoe de redactie werkt, waarom er naar een uitvoerder wordt verwezen en wat er met het domein is gebeurd.",
             """<div class="wrap">
<h1>Over deze gids</h1>
<p class="lead">%(site)s is een redactionele gids over daken en dakwerk in Nederland. De site is geen dakdekkersbedrijf, geen bemiddelaar en geen offerteplatform.</p>

<h2>Wat de site doet</h2>
<ul>
<li>Uitleggen hoe dakonderdelen werken en wat er misgaat, in twaalf hoofdstukken.</li>
<li>De Nederlandse regels en subsidies samenvatten met de datum en de bron erbij.</li>
<li>Drie hulpmiddelen aanbieden die in de browser rekenen, zonder registratie en zonder opslag.</li>
<li>Per plaats beschrijven welke bebouwing er staat en welke dakvraagstukken daarbij horen.</li>
<li>Een uitvoerder aanbevelen voor wie het werk wil laten uitvoeren.</li>
</ul>

<h2>Wat de site niet doet</h2>
<ul>
<li>Geen offertes opmaken of aanvragen doorsturen.</li>
<li>Geen contactformulier aanbieden. Contact loopt uitsluitend via %(email)s.</li>
<li>Geen gegevens van bezoekers verzamelen, opslaan of doorgeven.</li>
<li>Geen advertenties tonen.</li>
</ul>

<h2>Over het domein</h2>
<p>Het domein rommersdakwerken.nl was eerder in gebruik door een dakwerkenbedrijf. Die site bestaat niet meer. Het domein is opnieuw in gebruik genomen als informatieve gids over daken in Nederland. Deze site heeft geen band met het vroegere bedrijf en presenteert zich daar ook niet als opvolger van.</p>

<h2>Hoe de redactie werkt</h2>
<p>Elke bewering over regelgeving, subsidies, drempels of cijfers wordt onderbouwd met een bron die onderaan de pagina staat, met volledige URL zodat ze rechtstreeks te openen is. Waar een cijfer niet uit een officiele bron te halen is, staat dat er expliciet bij. Dat geldt bijvoorbeeld voor de levensduur van dakmaterialen en voor prijzen per vierkante meter: daarvoor bestaat geen Nederlandse officiele publicatie, dus de gebruikte bandbreedtes zijn vuistregels uit de praktijk en geen norm.</p>
<p>De belangrijkste bronnen zijn RVO, IPLO, het Besluit bouwwerken leefomgeving via wetten.overheid.nl, de Belastingdienst, het KNMI, het Verbond van Verzekeraars, het CBS, het Compendium voor de Leefomgeving en Milieu Centraal.</p>

<h2>Uitvoerder</h2>
<p>Wie het werk wil laten uitvoeren, vindt op deze site een vaste aanbeveling: %(brand)s, bereikbaar op 085 130 2723. Andere uitvoerders, advertenties of vergelijkingsmodules staan er niet op.</p>

<h2>Werkgebied</h2>
<p>De plaatspagina's beslaan 179 plaatsen in Noord-Brabant, Limburg, Gelderland, Utrecht, Zuid-Holland, Noord-Holland en Flevoland. Voor de rest van Nederland zijn de hoofdstukken en de regelgeving even goed van toepassing; alleen de plaatsspecifieke beschrijving ontbreekt dan.</p>

<h2>Correcties</h2>
<p>Regelgeving verandert en subsidiebedragen worden aangepast. Wie een fout of een verouderde vermelding ziet, kan dat melden via %(email)s. Correcties worden doorgevoerd met vermelding van de bron.</p>
</div>""" % {"site": SITE_NAME, "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
             "brand": dd_link()}, priority="0.7"))


FAQ = [
    ("Hoe lang gaat een dak in Nederland mee",
     "Dat hangt af van het materiaal en van het onderhoud. In de praktijk worden bandbreedtes aangehouden van 50 tot 80 jaar voor keramische dakpannen, 30 tot 50 jaar voor betonpannen, 20 tot 30 jaar voor bitumen en 30 tot 50 jaar voor EPDM. Die getallen zijn vuistregels; er bestaat geen officiele Nederlandse publicatie met levensduren per materiaal. De waterkerende laag en de constructie zijn vaak eerder aan vervanging toe dan de bedekking zelf."),
    ("Welke Rc-waarde is verplicht voor een dak",
     "Bij nieuwbouw geldt Rc 6,3 vierkante meter kelvin per watt. Bij het vervangen of vernieuwen van een isolatielaag in het dak geldt volgens artikel 5.20 lid 2 Bbl minimaal Rc 2,1. Bij verbouw van bouwdelen in de thermische schil geldt het rechtens verkregen niveau met een ondergrens van gemiddeld Rc 1,4. Voor een dakkapel geldt het nieuwbouwniveau van Rc 6,3."),
    ("Hoeveel ISDE-subsidie is er voor dakisolatie",
     "In 2026 is dat 16,25 euro per vierkante meter, en 32,50 euro bij twee of meer maatregelen. Biobased isolatiemateriaal geeft 5 euro per vierkante meter extra. De Rd-waarde van het nieuwe materiaal moet minimaal 3,5 zijn, het oppervlak minimaal 20 en maximaal 200 vierkante meter."),
    ("Moet ik twee maatregelen nemen voor ISDE",
     "Nee. Een isolatiemaatregel volstaat voor subsidie. Het bedrag verdubbelt wel bij een tweede isolatiemaatregel of bij combinatie met een warmtepomp, zonneboiler of warmtenetaansluiting, mits de volgende maatregel binnen 24 maanden na de vorige is uitgevoerd."),
    ("Is een vergunning nodig om dakpannen te vervangen",
     "Nee, het vervangen van dakpannen valt onder gewoon onderhoud, mits detaillering, profilering en vormgeving niet veranderen. Bij een monument ligt dat anders: verandert de kleur of de materiaalsoort, dan kan een vergunning voor een monumentenactiviteit nodig zijn."),
    ("Wanneer is een dakkapel vergunningvrij",
     "Bij vijf voorwaarden tegelijk: een plat dak, hoogte vanaf de voet niet meer dan 1,75 meter, onderzijde meer dan 0,5 en minder dan 1 meter boven de dakvoet, bovenzijde meer dan 0,5 meter onder de daknok, en zijkanten meer dan 0,5 meter van de zijkanten van het dakvlak. Op het voordakvlak geldt dit alleen als het omgevingsplan geen redelijke eisen van welstand stelt, en bij monumenten geldt het niet."),
    ("Mag ik zelf asbest van mijn dak halen",
     "Een particulier mag maximaal 35 vierkante meter hechtgebonden asbesthoudend materiaal zelf verwijderen, bij een particuliere woning of een bijgebouw zonder bedrijfsfunctie. Toegestaan zijn geschroefde, hele en niet-verweerde platen. Dakleien, gelijmde of gespijkerde platen en verweerd materiaal vallen daarbuiten. Er horen drie meldingen bij: sloopmelding, startmelding en eindmelding."),
    ("Zijn asbestdaken verboden",
     "Nee. Het wetsvoorstel voor een asbestdakenverbod is op 4 juni 2019 verworpen door de Eerste Kamer. Er geldt geen verwijderplicht voor asbestdaken in goede staat. Sinds 2025 loopt wel een vrijwillige versnellingsaanpak met een publiekscampagne en een helpdesk."),
    ("Vanaf welke windkracht spreekt de verzekeraar van storm",
     "Het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 14 meter per seconde of 50 kilometer per uur. Het KNMI hanteert een strengere meteorologische definitie: storm is windkracht 9, een uurgemiddelde van 75 tot 88 kilometer per uur. De polisvoorwaarden bepalen wat voor de dekking telt."),
    ("Wat valt niet onder de stormdekking",
     "Schade die het gevolg is van achterstallig onderhoud, en slijtage of veroudering van de dakbedekking zelf. Een nokvorst die al jaren los lag, valt daaronder. Inspectierapporten en foto's van eerdere jaren helpen om aan te tonen dat het dak in orde was."),
    ("Wat is het verschil tussen condensatie en lekkage",
     "Condensatie treedt op bij koud weer, ook zonder regen, geeft een diffuus vochtig vlak zonder scherpe rand en gaat vaak samen met schimmel of een muffe geur. Een lek volgt de regen en geeft een scherp begrensde vlek. Condensvocht behandelen als een lek en het dak dichtmaken verergert het probleem."),
    ("Geldt het btw-tarief van 9 procent voor dakwerk",
     "Alleen voor het aanbrengen van isolatiemateriaal aan woningen ouder dan twee jaar, en dan uitsluitend voor de arbeidskosten. Het materiaal zelf valt onder 21 procent en moet apart op de factuur staan. Overig dakwerk, waaronder dakkapellen en sloopwerk, valt onder 21 procent."),
    ("Hoe vaak moet een dakgoot gereinigd worden",
     "Zonder bomen in de omgeving volstaat een keer per jaar, na de bladval. Bij loofbomen dicht bij de woning twee keer per jaar, bij naaldbomen twee tot drie keer. Bij een bakgoot of zakgoot minstens twee keer per jaar plus na elke storm, omdat het water daar bij verstopping naar binnen loopt."),
    ("Is hogedrukreiniging van dakpannen verstandig",
     "Nee. De druk beschadigt het oppervlak van de pan, duwt water onder de pannen en maakt de bedekking gevoeliger voor nieuwe aangroei. Op asbestcement is reinigen niet toegestaan."),
    ("Vervangt een groendak de dakisolatie",
     "Nee. De isolatiewaarde van een dunne substraatlaag is beperkt en verdwijnt zodra de laag nat is. Een groendak houdt wel regenwater vast, beschermt de dakbedekking tegen ultraviolet licht en dempt de temperatuur in de zomer. Het telt niet mee voor de ISDE."),
    ("Wat kost dakisolatie ongeveer",
     "Milieu Centraal rekent voor dakisolatie door een vakman met ongeveer 6.000 euro voor een tussenwoning, 6.500 euro voor een hoekwoning en een twee-onder-een-kap, en ongeveer 10.000 euro voor een vrijstaande woning. Prijzen per vierkante meter voor dakpannen, bitumen of goten zijn niet uit een officiele bron te halen."),
]


def _faq():
    qa = "".join("<h2>%s</h2><p>%s</p>" % (q, a) for q, a in FAQ)
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    add(Page("/veelgestelde-vragen/", "Veelgestelde vragen over daken en dakwerk",
             "Zestien vragen over levensduur, isolatie-eisen, ISDE-subsidie, vergunningen, verzekering, asbest en onderhoud, met de Nederlandse regels erbij.",
             """<div class="wrap">
<h1>Veelgestelde vragen</h1>
<p class="lead">Zestien vragen die het vaakst terugkomen, met het antwoord zoals het in Nederland geldt. Uitgebreidere uitleg staat in <a href="/dakwerken/">de gids</a> en bij <a href="/regels/">regels en subsidies</a>.</p>
%s
<div class="rec"><h3>Uitvoering</h3><p>Aanbevolen uitvoerder: %s, 085 130 2723.</p></div>
</div>""" % (qa, dd_link()), priority="0.7", schema=schema))


BEGRIPPEN = [
    ("Bakgoot", "Goot die is ingewerkt in de dakconstructie, met een houten bak bekleed met zink of epdm. Bij een lek loopt het water direct in de constructie."),
    ("Bitumen", "Dakbedekking voor platte daken, in twee lagen aangebracht met de vlam of met kleefmiddel. Bestaat in APP- en SBS-varianten."),
    ("Dakbeschot", "De plaatlaag of beplanking op de sporen, waarop de tengels en panlatten worden bevestigd."),
    ("Dakvoet", "Het laagste punt van een hellend dak, waar het dakvlak op de goot uitkomt."),
    ("Dampremmende laag", "Laag aan de warme zijde van de isolatie die waterdamp uit de woning tegenhoudt. Een gat erin veroorzaakt vocht dat op een daklek lijkt."),
    ("EPDM", "Rubberfolie voor platte daken, op kleinere daken vaak in een stuk gelegd."),
    ("Gevelpan", "Pan aan de zijkant van een hellend dak, langs de topgevel. Waait bij storm als eerste weg als de klem ontbreekt."),
    ("Hechtgebonden asbest", "Asbestvezels die vast in een dragermateriaal zitten, meestal cement. Onder voorwaarden mag een particulier daar maximaal 35 vierkante meter van verwijderen."),
    ("ISDE", "Investeringssubsidie duurzame energie en energiebesparing. De landelijke subsidie voor onder meer dakisolatie, uitgevoerd door RVO."),
    ("Kilgoot", "Goot in de binnenhoek waar twee dakvlakken samenkomen. Voert veel water af en is het meest belaste onderdeel van een hellend dak."),
    ("Koud dak", "Plat dak waarbij de isolatie onder de draagvloer ligt met een geventileerde spouw. Verouderd principe, gevoelig voor condensatie."),
    ("Loodslabbe", "Loodstrook die de aansluiting tussen dakvlak en schoorsteen of muur afdicht."),
    ("MKI", "Milieukostenindicator. Maat die de milieubelasting van een materiaal in een bedrag uitdrukt, gebruikt bij de biobased bonus in de ISDE."),
    ("Nokvorst", "Gebogen pan die de nok van een hellend dak afsluit. Ligt traditioneel in mortel, tegenwoordig vaker droog met klemmen en een ventilerende nokrol."),
    ("Noodoverloop", "Spuwer in de dakrand van een plat dak, iets hoger dan de hoofdafvoer, die voorkomt dat water op het dak blijft staan bij een verstopping."),
    ("Opstand", "Verticaal deel waar de dakbedekking van een plat dak tegen een muur of dakrand omhoog loopt."),
    ("Panlat", "Horizontale lat waarop de dakpannen haken."),
    ("Rc-waarde", "Warmteweerstand van een hele constructie, in vierkante meter kelvin per watt. Hoe hoger, hoe beter."),
    ("Rd-waarde", "Warmteweerstand van een isolatiemateriaal zelf. De ISDE stelt hier de eis van minimaal 3,5."),
    ("Rechtens verkregen niveau", "Het kwaliteitsniveau dat een bouwwerk op het moment van verbouwing legaal heeft. Uitgangspunt bij verbouw volgens artikel 5.20 lid 1 Bbl."),
    ("Sporen", "De schuine dakbalken van een hellend dak, waartussen of waarboven wordt geisoleerd."),
    ("Tapbuis", "Verbindingsstuk tussen goot en regenpijp. De plek waar de meeste verstoppingen ontstaan."),
    ("Tengel", "Lat onder de panlatten die een luchtspouw maakt zodat water en vocht kunnen wegstromen."),
    ("U-waarde", "Warmtedoorgangscoefficient van een constructie, in watt per vierkante meter kelvin. Hoe lager, hoe beter."),
    ("Vezelcement", "Cementgebonden plaatmateriaal voor leien en golfplaten. Bij bouwjaren voor 1994 mogelijk asbesthoudend."),
    ("Warm dak", "Plat dak waarbij dampremmende laag, isolatie en dakbedekking allemaal boven de draagvloer liggen. De standaardopbouw."),
    ("Waterkerende laag", "Folie of plaat onder de pannen die water opvangt dat langs de bedekking doorkomt en het naar de goot afvoert."),
]


def _begrippen():
    rows = "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % (t, d) for t, d in BEGRIPPEN)
    add(Page("/begrippen/", "Begrippenlijst daken en dakwerk",
             "Zevenentwintig termen uit de dakbedekking en de Nederlandse regelgeving, kort uitgelegd.",
             """<div class="wrap">
<h1>Begrippenlijst</h1>
<p class="lead">Zevenentwintig termen die in offertes, inspectierapporten en regelgeving terugkomen.</p>
<div class="tablewrap"><table><tr><th>Term</th><th>Betekenis</th></tr>%s</table></div>
<p><a href="/dakwerken/">Terug naar de gids</a></p>
</div>""" % rows, priority="0.5"))


def _contact():
    add(Page("/contact/", "Contact",
             "Contact met de redactie van rommersdakwerken.nl loopt uitsluitend per e-mail. Er is geen contactformulier en er worden geen offertes opgemaakt.",
             """<div class="wrap">
<h1>Contact</h1>
<p class="lead">Contact met de redactie loopt uitsluitend per e-mail, via %(email)s.</p>

<h2>Waarvoor</h2>
<ul>
<li>Correcties op de inhoud, bij voorkeur met de bron erbij.</li>
<li>Vragen over de werkwijze van de redactie.</li>
<li>Meldingen van kapotte links of technische problemen.</li>
</ul>

<h2>Waarvoor niet</h2>
<p>%(site)s is een redactionele gids en geen dakdekkersbedrijf. Er worden geen offertes opgemaakt, geen opdrachten aangenomen, geen prijzen opgegeven en geen aanvragen doorgestuurd. Er is bewust geen contactformulier op de site, zodat er ook geen gegevens van bezoekers worden verwerkt.</p>

<h2>Wie werk wil laten uitvoeren</h2>
<p>De aanbevolen uitvoerder is %(brand)s, rechtstreeks bereikbaar:</p>
<ul>
<li>Telefonisch op 085 130 2723, ook buiten kantooruren bij spoed</li>
<li>Per e-mail op info@dendekker-dakbedekking.nl</li>
<li>Via de website %(url)s</li>
</ul>
<p>Aanvragen die per e-mail bij deze redactie binnenkomen, worden niet doorgestuurd.</p>
</div>""" % {"email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL), "site": SITE_NAME,
             "brand": dd_link(),
             "url": dd_link("", "https://www.dendekker-dakbedekking.nl/")}, priority="0.5"))


def _privacy():
    add(Page("/privacybeleid/", "Privacybeleid",
             "Welke gegevens rommersdakwerken.nl verwerkt, namelijk zo goed als geen, en welke rechten bezoekers hebben onder de AVG.",
             """<div class="wrap">
<h1>Privacybeleid</h1>
<p class="lead">%(site)s verwerkt geen persoonsgegevens van bezoekers. Deze pagina legt uit wat dat concreet betekent.</p>

<h2>Geen formulieren, geen accounts</h2>
<p>De site heeft geen contactformulier, geen inschrijving, geen account en geen zoekfunctie die iets registreert. Er is dus geen invoerveld waarin persoonsgegevens terechtkomen.</p>

<h2>Geen statistiek en geen advertenties</h2>
<p>Er draait geen bezoekersstatistiek, geen advertentienetwerk en geen scriptbibliotheek van derden. De pagina's laden uitsluitend bestanden van het eigen domein. Er vertrekken geen verzoeken naar externe servers bij het bekijken van een pagina.</p>

<h2>De hulpmiddelen</h2>
<p>De daklekkage-diagnose, de onderhoudsplanner en de storm- en subsidiecheck rekenen volledig in de browser. Wat wordt ingevuld, verlaat het apparaat niet, wordt nergens opgeslagen en is na het sluiten van de pagina verdwenen.</p>

<h2>E-mail</h2>
<p>Wie mailt naar %(email)s, deelt daarmee een e-mailadres en de inhoud van het bericht. Die berichten worden gebruikt om te antwoorden en om correcties door te voeren, en worden niet gedeeld met derden. Ze worden bewaard zolang dat voor de afhandeling nodig is.</p>

<h2>Serverlogs</h2>
<p>De site draait op Cloudflare Pages. De hostingpartij houdt technische logbestanden bij die nodig zijn voor de werking en de beveiliging van het netwerk, waaronder IP-adressen. De redactie heeft die gegevens niet nodig en gebruikt ze niet. Meer over de verwerking door die partij staat op https://www.cloudflare.com/privacypolicy/</p>

<h2>Uitgaande links</h2>
<p>De site verwijst naar de website van Den Dekker Dakbedekking en naar bronnen van overheden en organisaties. Op die websites gelden hun eigen voorwaarden en privacyverklaring. Deze redactie heeft daar geen zeggenschap over.</p>

<h2>Rechten</h2>
<p>Onder de Algemene verordening gegevensbescherming bestaat het recht op inzage, correctie, verwijdering, beperking en bezwaar. Omdat er geen bezoekersgegevens worden verwerkt, is er in de praktijk alleen iets in te zien of te verwijderen wanneer er eerder is gemaild. Een verzoek daarover kan naar %(email)s</p>
<p>Wie meent dat er iets misgaat met de verwerking van persoonsgegevens, kan een klacht indienen bij de Autoriteit Persoonsgegevens, https://www.autoriteitpersoonsgegevens.nl</p>

<h2>Wijzigingen</h2>
<p>Wijzigingen aan dit beleid worden op deze pagina gepubliceerd. Laatste aanpassing: augustus 2026.</p>
</div>""" % {"site": SITE_NAME, "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)},
             priority="0.3"))


def _cookies():
    add(Page("/cookiebeleid/", "Cookiebeleid",
             "Rommersdakwerken.nl plaatst geen cookies en gebruikt geen lokale opslag. Deze pagina legt uit wat dat betekent.",
             """<div class="wrap">
<h1>Cookiebeleid</h1>
<p class="lead">%(site)s plaatst geen cookies. Er is daarom ook geen cookiebanner.</p>

<h2>Wat er niet gebeurt</h2>
<ul>
<li>Geen functionele cookies, want er is niets om te onthouden: geen account, geen winkelwagen, geen voorkeuren.</li>
<li>Geen analytische cookies, want er wordt geen bezoekersstatistiek bijgehouden.</li>
<li>Geen advertentie- of trackingcookies, want er staan geen advertenties op de site.</li>
<li>Geen local storage en geen session storage. De hulpmiddelen rekenen in het geheugen van de pagina en bewaren niets.</li>
<li>Geen ingesloten video's, kaarten, lettertypes of scripts van derden. Alles wat een pagina laadt, komt van het eigen domein.</li>
</ul>

<h2>Waarom dat kan</h2>
<p>De site bestaat uit statische pagina's. Er is geen server die per bezoeker iets moet onthouden en er zijn geen externe diensten ingebouwd. Dat maakt cookies overbodig.</p>

<h2>Hoe dat te controleren</h2>
<p>In elke gangbare browser toont het ontwikkelaarsvenster onder het tabblad voor opslag welke cookies een site plaatst. Voor deze site blijft die lijst leeg. Onder het netwerktabblad is te zien dat er geen verzoeken naar andere domeinen vertrekken.</p>

<h2>Andere websites</h2>
<p>Wie via een link naar de website van Den Dekker Dakbedekking of naar een bron van een overheid gaat, komt op een site met een eigen cookiebeleid. Deze redactie heeft daar geen zeggenschap over.</p>

<h2>Wijzigingen</h2>
<p>Mocht dit ooit veranderen, dan wordt dat op deze pagina vermeld voordat het wordt doorgevoerd. Laatste aanpassing: augustus 2026.</p>
</div>""" % {"site": SITE_NAME}, priority="0.3"))


def _404():
    add(Page("/404.html", "Pagina niet gevonden",
             "Deze pagina bestaat niet of is verplaatst. Vanaf hier zijn de gids, de regels, de plaatsen en de hulpmiddelen bereikbaar.",
             """<div class="wrap">
<h1>Pagina niet gevonden</h1>
<p class="lead">Deze pagina bestaat niet, of ze is verplaatst.</p>
<div class="grid">
<a class="tile" href="/"><b>Home</b><span>Terug naar de startpagina</span></a>
<a class="tile" href="/dakwerken/"><b>De gids</b><span>Twaalf hoofdstukken over dakonderdelen</span></a>
<a class="tile" href="/regels/"><b>Regels en subsidies</b><span>Zes Nederlandse regelingen</span></a>
<a class="tile" href="/locaties/"><b>Locaties</b><span>Honderdnegenenzeventig plaatsen</span></a>
<a class="tile" href="/hulpmiddelen/"><b>Hulpmiddelen</b><span>Diagnose, planner en checks</span></a>
<a class="tile" href="/nieuws/"><b>Nieuws</b><span>Actuele berichten met bronvermelding</span></a>
</div>
</div>""", noindex=True, priority="0.1"))
