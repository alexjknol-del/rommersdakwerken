# -*- coding: utf-8 -*-
"""De gids: twaalf hoofdstukken over daken in Nederland."""
from engine import Page, add, dd_link

CR = [("/dakwerken/", "Dakwerken")]

CHAPTERS = [
    ("hellend-dak", "Hellend dak", "Dakpannen, leien en de opbouw eronder"),
    ("plat-dak", "Plat dak", "Bitumen, EPDM en de opbouw van een warm dak"),
    ("dakisolatie", "Dakisolatie", "Rc-waarden, methodes en de eisen uit het Bbl"),
    ("daklekkage", "Daklekkage", "Oorzaak opsporen en gevolgschade beperken"),
    ("dakgoot", "Dakgoot en hemelwaterafvoer", "Mastgoot, bakgoot en afvoer"),
    ("schoorsteen", "Schoorsteen en dakdoorvoeren", "Voegwerk, loodslabben en doorvoeren"),
    ("zink-en-loodwerk", "Zink- en loodwerk", "Kilgoten, muuraansluitingen en slabben"),
    ("dakramen-en-dakkapel", "Dakramen en dakkapel", "Vergunningvrij bouwen en lekpunten"),
    ("groendak", "Groendak", "Sedum, opbouw en draagkracht"),
    ("asbest-op-het-dak", "Asbest op het dak", "Herkennen, de 35 vierkante meter en de meldingen"),
    ("dakonderhoud", "Dakonderhoud", "Wat wanneer nagekeken hoort te worden"),
    ("stormschade", "Stormschade", "Direct handelen, opstalverzekering en herstel"),
]


def rec(text, path="", anchor=None):
    return ('<div class="rec"><h3>Uitvoering</h3><p>%s</p>'
            '<p>De redactie beveelt %s aan voor dakwerk in Nederland. Telefonisch bereikbaar op '
            '085 130 2723, ook buiten kantooruren bij spoed.</p></div>'
            % (text, dd_link(path, anchor)))


def sources(items):
    return '<h2>Bronnen</h2><ul class="src">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def _aside(current):
    li = "".join('<li><a href="/dakwerken/%s/">%s</a></li>' % (s, t)
                 for s, t, _ in CHAPTERS if s != current)
    return ('<aside><div class="card"><h3>Andere hoofdstukken</h3>'
            '<ul style="margin:0;padding-left:18px">%s</ul>'
            '<p class="small" style="margin-top:14px"><a href="/hulpmiddelen/">Naar de hulpmiddelen</a></p>'
            '</div></aside>' % li)


def _p(slug, title, desc, body, prio="0.7"):
    add(Page("/dakwerken/%s/" % slug, title, desc,
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, _aside(slug)),
             crumbs=CR, priority=prio))


def build():
    tiles = "".join('<a class="tile" href="/dakwerken/%s/"><b>%s</b><span>%s</span></a>'
                    % (s, t, d) for s, t, d in CHAPTERS)
    add(Page("/dakwerken/", "Daken en dakwerk in Nederland: de volledige gids",
             "Twaalf hoofdstukken over hellende en platte daken, isolatie, lekkage, goten, schoorstenen, asbest en onderhoud, met de Nederlandse regels erbij.",
             """<div class="wrap">
<h1>Daken en dakwerk in Nederland</h1>
<p class="lead">Twaalf hoofdstukken die samen het volledige dak beslaan. Elk hoofdstuk beschrijft hoe het onderdeel werkt, wat er misgaat, wat een correcte oplossing inhoudt en welke Nederlandse regels van toepassing zijn.</p>
<div class="grid">%s</div>
<h2>Volgorde van aanpak</h2>
<p>Bij een dakprobleem helpt het om drie vragen in deze volgorde te beantwoorden. Gaat het om een acuut lek of om slijtage. Volstaat herstel of is het dakvlak als geheel aan vervanging toe. En pas daarna: welke isolatie, subsidie en vergunning horen daarbij.</p>
<p>Wie het dak toch openlegt, isoleert in dezelfde beweging. De stelling, de afbraak en de afvoer worden dan een keer betaald in plaats van twee keer, en de ISDE-subsidie verdubbelt bij twee maatregelen. Meer daarover op <a href="/regels/isde-subsidie/">de pagina over de ISDE</a>.</p>
%s
</div>""" % (tiles, rec("Een dakinspectie met foto- en videomateriaal maakt duidelijk of herstel volstaat of dat vervanging nodig is.",
                       "dakinspectie/", "dendekker-dakbedekking.nl/dakinspectie/")),
             priority="0.8"))
    _hellend(); _plat(); _isolatie(); _lekkage(); _goot(); _schoorsteen()
    _zink(); _dakramen(); _groendak(); _asbest(); _onderhoud(); _storm()


def _hellend():
    _p("hellend-dak", "Hellend dak: dakpannen, leien en de opbouw eronder",
       "Hoe een hellend dak is opgebouwd, welke dakpannen in Nederland gangbaar zijn, wanneer herstel volstaat en wanneer het dakvlak vervangen moet worden.",
       """<h1>Hellend dak</h1>
<p class="lead">Het hellende dak met keramische of betonnen dakpannen is in Nederland de meest voorkomende dakvorm bij woningen. De pannen liggen op panlatten en tengels boven dakbeschot of isolatieplaten.</p>

<h2>De opbouw van boven naar beneden</h2>
<ol>
<li>De dakbedekking: pannen of leien, die het grootste deel van het water afvoeren.</li>
<li>Panlatten, waarop de pannen haken.</li>
<li>Tengels, die een luchtspouw maken zodat doorgekomen water naar de goot kan lopen.</li>
<li>Het onderdak of de waterkerende laag, die het resterende water opvangt. Bij woningen van voor 1970 ontbreekt die vaak.</li>
<li>De isolatie, tussen of boven de sporen.</li>
<li>Het dampremmende scherm aan de binnenzijde, dat vocht uit de woning tegenhoudt.</li>
<li>De binnenafwerking.</li>
</ol>
<p>Elke laag heeft een taak. Alleen de bovenste laag vervangen en de rest laten zoals ze is, lost een lek zelden blijvend op.</p>

<h2>Materialen die in Nederland gangbaar zijn</h2>
<div class="tablewrap"><table>
<tr><th>Materiaal</th><th>Kenmerk</th><th>Aandachtspunt</th></tr>
<tr><td>Keramische dakpan</td><td>Gebakken klei, kleurvast</td><td>Modellen verdwijnen uit productie, deelvervanging wordt lastiger</td></tr>
<tr><td>Betonpan</td><td>Zwaarder, gladder oppervlak</td><td>Vergroent sneller aan de noordzijde</td></tr>
<tr><td>Natuurleien</td><td>Dun en licht, lange staat van dienst</td><td>Vraagt vakkennis bij haken en nagelen</td></tr>
<tr><td>Vezelcementleien</td><td>Vlakke leien op woningen en dakkapellen</td><td>Bij bouwjaar voor 1994 mogelijk asbesthoudend</td></tr>
<tr><td>Riet</td><td>Traditioneel, hoge isolatiewaarde</td><td>Brandveiligheidseisen en specialistisch onderhoud</td></tr>
</table></div>

<h2>Wanneer herstel volstaat</h2>
<p>Herstel is zinvol wanneer de schade lokaal is en de constructie eronder droog en gaaf is: enkele gebroken pannen na hagel, een losgekomen nokvorst, een verschoven gevelpan. Een vakman vervangt dan het beschadigde deel en loopt meteen de aansluitingen rondom na.</p>

<h2>Wanneer vervanging nodig is</h2>
<p>Vervanging komt in beeld bij een combinatie van signalen: pannen die op meerdere plaatsen tegelijk breken, een waterkerende laag die verpulvert, panlatten met houtrot, terugkerende lekken op wisselende plekken, en het ontbreken van isolatie. Losse reparaties stapelen dan alleen kosten op.</p>
<p>Een dakvernieuwing is meteen het moment om de isolatie op orde te brengen. Het Bbl stelt bij het vervangen van een isolatielaag een minimum van Rc 2,1 vierkante meter kelvin per watt voor daken, terwijl de ISDE-subsidie een Rd-waarde van minimaal 3,5 vraagt en de RVO-streefwaarde op Rc 8 ligt.</p>

<h2>Nokvorsten</h2>
<p>De nokvorsten sluiten de nok af. Traditioneel liggen ze in mortel, die na verloop van tijd scheurt door temperatuurwisselingen en vorst. Een poreuze of losse nokvorst laat water door en kan bij storm loskomen. De droge oplossing met een ventilerende nokrol en klemmen maakt mortel overbodig.</p>
%s

<h2>Ventilatie van het dakvlak</h2>
<p>Tussen de waterkerende laag en de pannen hoort lucht te stromen, van de dakvoet naar de nok. Zonder die stroming blijft vocht hangen, met houtrot in de sporen en schimmel op de isolatie als gevolg. Bij een dakvernieuwing wordt die spouw hersteld met tengels en een geventileerde nok.</p>

<h2>Vergunning</h2>
<p>Het vervangen van dakpannen valt onder gewoon onderhoud en is vergunningvrij, mits detaillering, profilering en vormgeving niet veranderen. Bij een monument ligt dat anders: verandert kleur of materiaalsoort, dan kan een vergunning voor een monumentenactiviteit nodig zijn. Meer daarover op <a href="/regels/vergunningvrij-bouwen/">vergunningvrij bouwen</a>.</p>
%s""" % (rec("Nokvorsten vervangen en dakpannen vervangen zijn ingrepen waarbij de rest van het dakvlak meteen wordt nagekeken.",
             "nokvorsten-vervangen/", "dendekker-dakbedekking.nl/nokvorsten-vervangen/"),
         sources([
             "IPLO over gewoon onderhoud en het vervangen van dakpannen: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/gewoon-onderhoud/",
             "IPLO over energiezuinigheid bij verbouw, artikel 5.20 Bbl: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/energiezuinigheid/",
             "RVO over standaard en streefwaarden woningisolatie: https://www.rvo.nl/onderwerpen/wetten-en-regels-gebouwen/standaard-streefwaarden-woningisolatie",
         ])))


def _plat():
    _p("plat-dak", "Plat dak: bitumen, EPDM en de juiste opbouw",
       "Warm dak, koud dak en omgekeerd dak, het verschil tussen bitumen en EPDM, en waar platte daken in de praktijk lekken.",
       """<h1>Plat dak</h1>
<p class="lead">Een plat dak is nooit helemaal vlak. Het heeft afschot naar de afvoer, meestal 1 tot 2 procent. Water dat blijft staan is op zich geen lek, maar het versnelt de veroudering van de dakbedekking.</p>

<h2>Drie opbouwen</h2>
<div class="tablewrap"><table>
<tr><th>Type</th><th>Opbouw</th><th>Wanneer</th></tr>
<tr><td>Warm dak</td><td>Dampremmende laag, isolatie en dakbedekking boven de draagvloer</td><td>Standaard bij nieuwbouw en renovatie</td></tr>
<tr><td>Koud dak</td><td>Isolatie onder de draagvloer met een geventileerde spouw</td><td>Verouderd principe, gevoelig voor condensatie</td></tr>
<tr><td>Omgekeerd dak</td><td>Isolatie boven de dakbedekking, met ballast</td><td>Bij daken met terras of grindlaag</td></tr>
</table></div>
<p>Bij renovatie van een koud dak is omzetting naar een warm dak vrijwel altijd de betere keuze. De dakbedekking ligt dan boven de isolatie en de constructie blijft op temperatuur.</p>

<h2>Bitumen tegenover EPDM</h2>
<p>Bitumen bestaat uit twee lagen, gebrand of gekleefd. Het is een beproefd systeem, per stuk herstelbaar en goed bestand tegen belopen. De naden zijn het zwakke punt. Binnen bitumen bestaan APP- en SBS-varianten, die verschillen in gedrag bij kou en hitte.</p>
<p>EPDM is een rubberfolie die op kleinere daken in een stuk kan worden gelegd, waardoor er vrijwel geen naden zijn. Een beschadiging midden in een baan is wel lastiger onzichtbaar te herstellen.</p>
<p>Voor beide geldt dat de kwaliteit van de aansluitingen aan opstanden, doorvoeren en dakranden de levensduur bepaalt, niet het merk van het membraan.</p>

<h2>Waar platte daken lekken</h2>
<ul>
<li>Bij de opstand tegen een muur, wanneer de dakbedekking niet hoog genoeg is doorgetrokken of het profiel is losgekomen.</li>
<li>Rond de hemelwaterafvoer, door bladophoping of een slecht ingewerkte tapbuis.</li>
<li>Bij doorvoeren voor ventilatie, kabels of een schoorsteen.</li>
<li>Op de naden, bij onvoldoende verkleving of door beweging in de constructie.</li>
<li>Aan de dakrand, waar het profiel losraakt of water erachter loopt.</li>
</ul>
<p>De plek waar het water binnenkomt ligt zelden recht onder het lek. Water loopt over de dampremmende laag of de draagvloer tot het een opening vindt. Opsporen vraagt daarom onderzoek van het hele dakvlak.</p>
%s

<h2>Noodoverloop</h2>
<p>Naast de gewone afvoer hoort een plat dak een noodoverloop te hebben, meestal een spuwer door de dakrand die iets hoger zit dan de hoofdafvoer. Raakt de hoofdafvoer verstopt, dan kan het water daar weg in plaats van op het dak te blijven staan. Vijftig vierkante meter dak met vijf centimeter water draagt ongeveer 2500 kilogram extra.</p>
<p>Dat is in Nederland geen theoretisch punt. Het Verbond van Verzekeraars noemde zware zomerbuien de grootste schadepost in de klimaatschade van 2024, met in totaal ongeveer 278 miljoen euro aan verzekerde klimaatschade dat jaar.</p>

<h2>Levensduur en vervangingsmoment</h2>
<p>De praktische regel is dat een plat dak wordt vervangen zodra herstelwerk terugkerend wordt en de isolatie eronder vochtig is. Natte isolatie verliest haar werking en droogt in een gesloten dakopbouw niet meer uit. Alleen de bovenlaag vernieuwen sluit dat vocht in.</p>
%s""" % (rec("Bij een plat dak komt het opsporen van de werkelijke instroomplek eerst, voordat er iets wordt dichtgemaakt.",
             "plat-dak-lekkage/", "dendekker-dakbedekking.nl/plat-dak-lekkage/"),
         sources([
             "KNMI over de klimaatschademonitor 2024: https://www.knmi.nl/over-het-knmi/nieuws/buien-grootste-schadeboosdoener-in-2024-klimaatschademonitor-extreem-weer/",
         ])))


def _isolatie():
    _p("dakisolatie", "Dakisolatie: Rc-waarden, methodes en de eisen uit het Bbl",
       "Welke Rc-waarden gelden bij nieuwbouw en verbouw, het verschil met de ISDE-eis van Rd 3,5, de drie isolatiemethodes en de rol van het dampremmende scherm.",
       """<h1>Dakisolatie</h1>
<p class="lead">Bij een woning zonder dakisolatie is het dak de grootste warmteverliespost van de schil. Rond de eisen lopen drie getallen door elkaar: de nieuwbouweis, de verbouweis en de subsidievoorwaarde.</p>

<h2>De drie getallen</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Waarde</th><th>Grondslag</th></tr>
<tr><td>Nieuwbouw, dak</td><td>Rc minimaal 6,3 m&sup2;K/W</td><td>Besluit bouwwerken leefomgeving</td></tr>
<tr><td>Verbouw, vervangen van een isolatielaag in het dak</td><td>Rc minimaal 2,1 m&sup2;K/W</td><td>Artikel 5.20 lid 2 Bbl</td></tr>
<tr><td>Verbouw van bouwdelen in de thermische schil</td><td>Rechtens verkregen niveau, ondergrens gemiddeld Rc 1,4</td><td>Artikel 5.20 lid 1 Bbl</td></tr>
<tr><td>Dakkapel</td><td>Nieuwbouwniveau, Rc 6,3</td><td>Artikel 5.20 lid 3 Bbl</td></tr>
<tr><td>ISDE-subsidie</td><td>Rd minimaal 3,5 m&sup2;K/W van het nieuwe materiaal</td><td>Voorwaarde RVO</td></tr>
<tr><td>Streefwaarde</td><td>Rc 8 m&sup2;K/W, ongeveer 35 centimeter</td><td>RVO, niet wettelijk verplicht</td></tr>
</table></div>
<p>Rc slaat op de hele constructie, Rd op het isolatiemateriaal zelf. Dat verklaart waarom de subsidie-eis lager oogt dan de nieuwbouweis terwijl het om vergelijkbaar werk gaat.</p>

<h2>Drie manieren om een hellend dak te isoleren</h2>
<h3>Tussen de sporen</h3>
<p>De meest toegepaste methode bij renovatie vanaf de binnenzijde. De isolatie komt tussen de dakspanten, met een dampremmende laag aan de binnenzijde. De sporen zelf vormen koudebruggen en de beschikbare dikte is begrensd door de hoogte van het hout, dus vaak wordt een tweede laag onder de sporen toegevoegd.</p>
<h3>Boven het dakbeschot</h3>
<p>Isolatieplaten in een doorlopende laag boven de sporen, onder de pannen. Geen koudebruggen, en de kap blijft binnen zichtbaar. Kan alleen wanneer de dakbedekking toch wordt vervangen. Het dakvlak komt hoger te liggen, wat gevolgen heeft voor de aansluiting bij de buren en voor de dakrand.</p>
<h3>Op de zoldervloer</h3>
<p>Wanneer de zolder onverwarmd blijft, is isolatie op de vloer de eenvoudigste ingreep. Het te verwarmen volume wordt kleiner. De zolder wordt dan een koude ruimte, dus leidingen daar moeten tegen vorst beschermd worden.</p>

<h2>Het dampremmende scherm</h2>
<p>Warme binnenlucht bevat waterdamp. Komt die damp in de isolatie en koelt daar af, dan slaat ze neer als water. Het scherm aan de warme zijde voorkomt dat, maar alleen als het doorlopend is en luchtdicht aansluit op muren, balken en doorvoeren. Een scherm met gaten voor inbouwspots of kabels werkt niet, en een lek erin veroorzaakt schade die van buitenaf op een daklek lijkt.</p>

<h2>Wat het oplevert</h2>
<p>Milieu Centraal rekent voor dakisolatie door een vakman met totaalbedragen van ongeveer 6.000 euro voor een tussenwoning, 6.500 euro voor een hoekwoning en een twee-onder-een-kap, en ongeveer 10.000 euro voor een vrijstaande woning. De bijbehorende jaarlijkse besparing komt bij een gasprijs van 1,37 euro per kubieke meter uit op ongeveer 460 euro voor een tussenwoning en ongeveer 750 euro voor een vrijstaande woning. Voor een hoekwoning noemt Milieu Centraal een terugverdientijd van ongeveer elf tot twaalf jaar.</p>
%s

<h2>Zomercomfort</h2>
<p>Isolatie werkt in twee richtingen. Materialen met een hogere dichtheid, zoals houtvezel, vertragen de warmtedoorgang op zomerdagen sterker dan lichte materialen met dezelfde Rd-waarde. Op een zolder die als slaapkamer wordt gebruikt, is dat merkbaar.</p>
%s""" % (rec("Isolatiewerk en dakvernieuwing horen in een opdracht, omdat de opbouw dan in een keer correct wordt gemaakt.",
             "dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
         sources([
             "IPLO over energiezuinigheid bij nieuwbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/nieuwbouw/rijksregels/energiezuinigheid/",
             "IPLO over energiezuinigheid bij verbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/energiezuinigheid/",
             "RVO over ISDE-isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen",
             "RVO over standaard en streefwaarden: https://www.rvo.nl/onderwerpen/wetten-en-regels-gebouwen/standaard-streefwaarden-woningisolatie",
             "Milieu Centraal over dakisolatie: https://www.milieucentraal.nl/energie-besparen/isoleren-en-besparen/dakisolatie/",
         ])))


def _lekkage():
    _p("daklekkage", "Daklekkage: oorzaak opsporen en gevolgschade beperken",
       "Hoe water zich door een dakconstructie beweegt, welke symptomen naar welke oorzaak wijzen en wat er direct kan gebeuren bij een acuut lek.",
       """<h1>Daklekkage</h1>
<p class="lead">Bij een daklekkage ligt het lek zelden recht boven de vlek. Water volgt de weg van de minste weerstand, over folie, langs een spoor of over een leiding, tot het een opening vindt.</p>

<h2>Wat er als eerste gebeurt</h2>
<ol>
<li>Elektriciteit in de betrokken ruimte uitschakelen wanneer water bij leidingen of stopcontacten komt.</li>
<li>Water opvangen en spullen weghalen. Een emmer met een doek erin voorkomt spatten.</li>
<li>Een uitpuilend plafond doorprikken op het laagste punt, zodat het water gecontroleerd wegloopt.</li>
<li>Foto's maken van de schade, met datum, voor de verzekeraar.</li>
<li>Niet zelf het dak op bij regen, wind of vorst.</li>
</ol>

<h2>Symptomen en waarschijnlijke oorzaken</h2>
<div class="tablewrap"><table>
<tr><th>Wat zichtbaar is</th><th>Waarschijnlijke oorzaak</th></tr>
<tr><td>Vlek tegen een schoorsteen of muur</td><td>Loodslabbe of muuraansluiting los, voegwerk poreus</td></tr>
<tr><td>Vlek onder de nok</td><td>Poreuze nokmortel of losgekomen nokvorst</td></tr>
<tr><td>Vlek aan de dakvoet na hevige regen</td><td>Verstopte goot die naar binnen overloopt</td></tr>
<tr><td>Druppels alleen bij wind uit een bepaalde richting</td><td>Inwaaiende regen onder de pannen, ontbrekende of gescheurde waterkerende laag</td></tr>
<tr><td>Natte plek op zolder zonder regen</td><td>Condensatie door een lek in het dampremmende scherm of te weinig ventilatie</td></tr>
<tr><td>Vlek rond een dakraam</td><td>Aansluiting of afdichtingsrubber van het raam</td></tr>
<tr><td>Plat dak, vlek verspringt</td><td>Naad of doorvoer los, water loopt over de dampremmende laag</td></tr>
</table></div>
<p>Voor een stapsgewijze doorloop staat op deze site een <a href="/hulpmiddelen/daklekkage-diagnose/">daklekkage-diagnose</a> die op basis van symptomen de meest waarschijnlijke oorzaken ordent.</p>

<h2>Condensatie of lekkage</h2>
<p>Beide geven natte plekken, maar de aanpak verschilt volledig. Condensatie hangt samen met het binnenklimaat: het treedt op bij koude nachten, in slecht geventileerde ruimtes, en verspreidt zich gelijkmatig over een groter vlak. Een lek volgt de regen en geeft een scherp begrensde vlek met een rand. Condensvocht behandelen als een lek en het dak dichtmaken verergert het probleem.</p>

<h2>Wat een vakman doet</h2>
<p>Een correcte opsporing begint op het dak en niet binnen. Nok, gevelpannen, kilgoten, aansluitingen bij schoorsteen en muren, de goot en de doorvoeren worden nagelopen. Op een plat dak gaat het om naden, opstanden en de vraag of de isolatie eronder vochtig is. Foto- en videomateriaal maakt de vaststelling controleerbaar.</p>
%s

<h2>Verzekering</h2>
<p>Een lek door slijtage valt niet onder de opstalverzekering. Schade door storm meestal wel: het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 50 kilometer per uur, als drempel waarboven van storm wordt gesproken. Schade door achterstallig onderhoud is niet gedekt. Meer daarover in het hoofdstuk <a href="/dakwerken/stormschade/">stormschade</a>.</p>

<h2>Gevolgschade</h2>
<p>Water dat in de constructie blijft, veroorzaakt houtrot in sporen en muurplaten, verzadigt de isolatie en tast pleisterwerk aan. Schimmel wordt zichtbaar na enkele weken. De herstelkosten van gevolgschade lopen doorgaans hoger op dan die van het lek zelf.</p>
%s""" % (rec("Bij een acuut lek telt snelheid: eerst dichten, dan de structurele oplossing plannen.",
             "daklekkage/", "dendekker-dakbedekking.nl/daklekkage/"),
         sources([
             "Verbond van Verzekeraars over stormschade: https://www.verzekeraars.nl/verzekeringsthemas/schade/stormschade",
             "Verbond van Verzekeraars, infographic wind: https://www.verzekeraars.nl/verzekeringsthemas/klimaat-en-duurzaamheid/praktische-hulpmiddelen/infographic-verzekerbaarheid-klimaatrisico-s/wind",
         ])))


def _goot():
    _p("dakgoot", "Dakgoot en hemelwaterafvoer",
       "Mastgoot, bakgoot en kilgoot, waarom goten overlopen, hoe vaak reinigen zinvol is en wat er misgaat in de afvoer onder de grond.",
       """<h1>Dakgoot en hemelwaterafvoer</h1>
<p class="lead">De goot vangt het water op dat het dakvlak afvoert en brengt het naar de regenpijp. Een goot die niet werkt, laat water tegen de gevel lopen of achter de dakrand binnendringen. Veel schade die als daklekkage wordt gemeld, begint bij de goot.</p>

<h2>Types</h2>
<ul>
<li><strong>Mastgoot of hanggoot</strong>: hangt met beugels aan de dakrand, in zink, pvc of aluminium. Goed bereikbaar en eenvoudig te vervangen.</li>
<li><strong>Bakgoot</strong>: ingewerkt in de dakconstructie, met een houten bak bekleed met zink of epdm. Fraaier, maar bij een lek loopt het water direct in de constructie.</li>
<li><strong>Kilgoot</strong>: de goot in de binnenhoek waar twee dakvlakken samenkomen. Draagt veel water en is het meest belaste onderdeel van een hellend dak.</li>
<li><strong>Zakgoot achter een dakrand</strong>: komt voor bij oudere stadswoningen en is bij verstopping de meest risicovolle variant.</li>
</ul>

<h2>Waarom een goot overloopt</h2>
<p>De meest voorkomende oorzaak is bladophoping bij de tapbuis. Daarnaast speelt een verkeerd afschot: een goot hoort af te lopen naar de afvoer, en gezakte beugels keren dat om. Een derde oorzaak is onderdimensionering, waarbij goot of afvoer te klein is voor het aangesloten dakoppervlak. Bij korte, hevige buien komt dat snel aan het licht.</p>

<h2>Reinigingsritme</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Ritme</th></tr>
<tr><td>Geen bomen in de omgeving</td><td>Een keer per jaar, na de bladval</td></tr>
<tr><td>Loofbomen dicht bij de woning</td><td>Twee keer per jaar, in november en in het voorjaar</td></tr>
<tr><td>Naaldbomen dicht bij de woning</td><td>Twee tot drie keer per jaar, naalden vallen het hele jaar</td></tr>
<tr><td>Bakgoot of zakgoot</td><td>Minstens twee keer per jaar, plus na elke storm</td></tr>
</table></div>
<p>Bladvangers en gootroosters verlengen het interval maar vervangen de controle niet. Fijn materiaal dat er doorheen komt, zet zich juist onderin af.</p>

<h2>Zink, pvc en aluminium</h2>
<p>Zink is in Nederland het traditionele gootmateriaal en gaat lang mee, mits het niet in contact komt met koper en niet onder stilstaand vuil ligt. Pvc is lichter en goedkoper in aanschaf, maar zet meer uit bij temperatuurwisselingen, waardoor lijmnaden op termijn opengaan. Ter plaatse gevormde aluminium goten hebben weinig naden en worden vaak toegepast bij lange geveldelen.</p>

<h2>De afvoer onder de grond</h2>
<p>Een goot die goed leegloopt maar waarbij water toch tegen de gevel opstijgt, wijst op een verstopping in het ondergrondse deel. Bladslib, wortels en zand verzamelen zich in de bocht onder het maaiveld. Een ontstoppingsstuk of controleput maakt dat deel bereikbaar zonder graafwerk.</p>

<h2>Afkoppelen van hemelwater</h2>
<p>Veel gemeenten stimuleren het afkoppelen van de regenpijp van het riool, met infiltratie in de tuin of een regenton. Voor het dak verandert daar weinig aan, behalve dat de overloop van de voorziening zo moet liggen dat water bij een hevige bui niet tegen de gevel of onder de fundering komt te staan. De voorwaarden verschillen per gemeente en staan op de gemeentelijke website.</p>
%s
%s""" % (rec("Gootherstel en gootreiniging worden meestal in dezelfde beurt uitgevoerd als de controle van de dakrand.",
             "dakgoot/", "dendekker-dakbedekking.nl/dakgoot/"),
         sources([
             "KNMI over de klimaatschademonitor 2024, buien als grootste schadepost: https://www.knmi.nl/over-het-knmi/nieuws/buien-grootste-schadeboosdoener-in-2024-klimaatschademonitor-extreem-weer/",
         ])))


def _schoorsteen():
    _p("schoorsteen", "Schoorsteen en dakdoorvoeren",
       "Voegwerk, loodslabben, schoorsteenkappen en de doorvoeren voor ventilatie en rookgas: de plekken waar hellende daken het vaakst lekken.",
       """<h1>Schoorsteen en dakdoorvoeren</h1>
<p class="lead">Elke doorbreking van het dakvlak is een mogelijk lekpunt. De schoorsteen is de grootste en tegelijk de meest verwaarloosde, omdat die vanaf de grond intact lijkt.</p>

<h2>Wat er aan een schoorsteen slijt</h2>
<ul>
<li><strong>Het voegwerk.</strong> Boven het dakvlak staat het metselwerk vol in wind en regen. Voegen worden poreus, water dringt in de steen en vorst duwt de voeg verder open.</li>
<li><strong>De afdekplaat.</strong> Een gescheurde of ontbrekende plaat laat water rechtstreeks in het kanaal lopen.</li>
<li><strong>De loodslabbe.</strong> De loodstrook tussen schoorsteen en dakvlak komt los of scheurt bij de plooi.</li>
<li><strong>Het kanaal.</strong> Bij een schoorsteen die niet meer gebruikt wordt, blijft vocht in het kanaal staan en slaat door naar binnen.</li>
</ul>

<h2>Renoveren of verwijderen</h2>
<p>Wie de schoorsteen niet meer gebruikt, staat voor een keuze. Renoveren betekent hervoegen, afdekplaat vernieuwen, lood herstellen en eventueel impregneren. Verwijderen tot onder het dakvlak en het dak dichtmaken haalt een onderhoudspost weg, maar kan alleen wanneer geen enkel toestel nog is aangesloten en het metselwerk geen dragende functie heeft. Bij een gesloten bouwblok speelt bovendien de vraag of het kanaal van de buren ernaast loopt.</p>
%s

<h2>Impregneren</h2>
<p>Een waterafstotend product vermindert de wateropname zonder de damp tegen te houden. Dat werkt alleen op voegwerk dat nog gaaf is. Op een poreuze voeg sluit het product vocht in en versnelt het de schade. Hervoegen komt dus eerst.</p>

<h2>Andere doorvoeren</h2>
<div class="tablewrap"><table>
<tr><th>Doorvoer</th><th>Veelvoorkomend probleem</th></tr>
<tr><td>Ventilatiepan of dakdoorvoer</td><td>Rubbermanchet verhardt en scheurt na ongeveer vijftien jaar</td></tr>
<tr><td>Rookgasafvoer van een cv-ketel</td><td>Afdichting rond de buis komt los door trilling en uitzetting</td></tr>
<tr><td>Bevestiging van zonnepanelen</td><td>Doorboorde pan of haak zonder correcte afdichting</td></tr>
<tr><td>Antenne- of kabeldoorvoer</td><td>Kit verhardt, water loopt langs de kabel naar binnen</td></tr>
</table></div>
<p>Bij zonnepanelen op een hellend dak worden haken tussen de pannen door aan de sporen bevestigd. Een correcte plaatsing beschadigt geen pannen. Gebeurt dat wel, dan komt de lekkage vaak pas maanden later aan het licht.</p>

<h2>Vogeloverlast</h2>
<p>Duiven en kauwen nestelen in open kanalen en onder losse pannen aan de dakvoet. Nestmateriaal in een rookkanaal veroorzaakt trekproblemen en in het ergste geval koolmonoxide in de woning. Een schoorsteenkap en vogelschroot aan de dakvoet lossen dat op zonder de ventilatie te blokkeren.</p>
%s""" % (rec("Schoorsteenrenovatie omvat hervoegen, afdekplaat, loodwerk en de aansluiting op het dakvlak in een keer.",
             "schoorsteenrenovatie/", "dendekker-dakbedekking.nl/schoorsteenrenovatie/"),
         sources([])))


def _zink():
    _p("zink-en-loodwerk", "Zink- en loodwerk op het dak",
       "Waar lood en zink op een dak zitten, waarom die aansluitingen falen, de alternatieven voor lood en het effect van zeeklimaat.",
       """<h1>Zink- en loodwerk</h1>
<p class="lead">Lood en zink dichten de plekken af waar het dakvlak tegen iets anders aankomt. Ze zijn buigzaam en gaan lang mee, maar juist op die aansluitingen komt het water van een groot deel van het dak samen.</p>

<h2>Waar lood zit</h2>
<ul>
<li>Rond de schoorsteen, als slabbe die het water om het metselwerk leidt.</li>
<li>Bij de aansluiting van een dakvlak op een hogere muur, bijvoorbeeld bij een aanbouw.</li>
<li>In de kilgoot tussen twee dakvlakken, al wordt daar tegenwoordig ook aluminium of kunststof gebruikt.</li>
<li>Rond dakramen en dakkapellen, als onderdeel van de aansluitset.</li>
<li>Op de muurafdekking van een plat dak, samen met een afdekprofiel.</li>
</ul>

<h2>Waarom loodwerk faalt</h2>
<p>Lood zet uit en krimpt met de temperatuur. Wordt een strook te lang in een stuk gelegd, dan ontstaan scheuren op de plooi. Stroken op de gevel worden daarom onderbroken, zodat elk deel zelfstandig kan bewegen. Een tweede oorzaak is mechanische schade door belopen bij gootonderhoud of antenneplaatsing.</p>
<p>Verder wordt loodwerk soms met kit opgelost in plaats van correct in het voegwerk ingewerkt. Kit veroudert en laat na enkele jaren los. Een slabbe hoort in een uitgeslepen voeg te zitten, vastgezet en opnieuw gevoegd.</p>
%s

<h2>Zink</h2>
<p>Zink wordt gebruikt voor goten, regenpijpen, dakranden en muurafdekkingen. Het vormt een beschermende patinalaag en gaat daarmee decennia mee. Twee zaken verkorten dat aanzienlijk: contact met koper, dat elektrochemische aantasting geeft, en stilstaand vuil in een goot, waardoor het zink van binnenuit wordt aangetast.</p>

<h2>Aan de kust</h2>
<p>In de kustprovincies komt daar zout bij. In plaatsen als Zandvoort, Katwijk, Noordwijk, Monster en Hellevoetsluis verweren zinkwerk, bevestigingsmiddelen en dakranden merkbaar sneller dan in het binnenland. Roestvaste bevestiging en een controle na de winter zijn daar geen overbodige luxe.</p>

<h2>Alternatieven voor lood</h2>
<p>Er bestaan loodvervangers op basis van aluminium met een rekbare kunststoflaag. Die zijn lichter, eenvoudiger te verwerken en bevatten geen lood, wat bij regenwateropvang een voordeel is. Ze zijn wel gevoeliger voor mechanische beschadiging en minder geschikt waar veel beweging in de constructie zit.</p>

<h2>Lood en regenwater</h2>
<p>Wie regenwater opvangt voor gebruik in de tuin, houdt rekening met lood in de aanvoer. Loodvervangers of een afvoer die het eerste water afleidt, beperken dat.</p>
%s""" % (rec("Loodwerk en zinkwerk horen bij elke dakinspectie te worden nagekeken, ook als er nog geen lek is.",
             "lood-en-zinkwerk/", "dendekker-dakbedekking.nl/lood-en-zinkwerk/"),
         sources([])))


def _dakramen():
    _p("dakramen-en-dakkapel", "Dakramen en dakkapel: regels en lekpunten",
       "De vijf voorwaarden waaronder een dakkapel vergunningvrij is, de regels voor dakramen in artikel 2.29 Bbl, en waar de aansluitingen lekken.",
       """<h1>Dakramen en dakkapel</h1>
<p class="lead">Een dakraam blijft binnen het dakvlak. Een dakkapel steekt uit. Dat verschil bepaalt zowel de vergunningsvraag als de complexiteit van de aansluiting.</p>

<h2>Dakkapel: vijf voorwaarden</h2>
<p>Voor het ruimtelijke deel is een dakkapel vergunningvrij wanneer aan al deze voorwaarden is voldaan:</p>
<ol>
<li>Voorzien van een plat dak.</li>
<li>Hoogte, gemeten vanaf de voet van de dakkapel, niet meer dan 1,75 meter.</li>
<li>Onderzijde meer dan 0,5 meter en minder dan 1 meter boven de dakvoet.</li>
<li>Bovenzijde meer dan 0,5 meter onder de daknok.</li>
<li>Zijkanten meer dan 0,5 meter van de zijkanten van het dakvlak.</li>
</ol>
<p>Op het achterdakvlak of een niet naar openbaar toegankelijk gebied gekeerd zijdakvlak geldt dit landelijk. Op het voordakvlak of een naar openbaar gebied gekeerd zijdakvlak alleen wanneer het omgevingsplan daar geen redelijke eisen van welstand stelt. Bij een gemeentelijk, provinciaal of rijksmonument vervalt de vrijstelling, en in een rijksbeschermd stads- of dorpsgezicht geldt ze niet voor het zijdakvlak of een naar openbaar gebied gekeerd achterdakvlak.</p>
<p>Voor het bouwtechnische deel geldt daarnaast dat een dakkapel volgens artikel 5.20 lid 3 Bbl op nieuwbouwniveau moet worden geisoleerd, dus Rc 6,3.</p>

<h2>Dakraam, daklicht of lichtstraat</h2>
<p>Artikel 2.29 Bbl stelt: op het achterdakvlak, een niet-openbaar zijdakvlak en platte daken mag de constructie niet meer dan 0,6 meter buiten het dakvlak steken, met aan zijkanten, onder- en bovenzijde meer dan 0,5 meter afstand tot de randen. Op het voordakvlak en een naar openbaar gebied gekeerd zijdakvlak mag de constructie niet buiten het dakvlak uitsteken, met dezelfde randafstand. Bij monumenten en in beschermde stads- en dorpsgezichten vervalt dit volledig.</p>
%s

<h2>Waar dakramen lekken</h2>
<ul>
<li>De aansluitgoot boven het raam, wanneer die ontbreekt of verstopt raakt met blad.</li>
<li>De waterkerende laag die rond de sparing niet correct is aangesloten op de gootbeplating van het raam.</li>
<li>Het afdichtingsrubber van de draaivleugel, dat na vijftien tot twintig jaar hardt.</li>
<li>De isolatie rondom het kader, die vaak ontbreekt en condensatie veroorzaakt die op lekkage lijkt.</li>
</ul>
<p>Condensatie op de binnenzijde van een dakraam is meestal geen defect maar een ventilatiekwestie. Een ventilatierooster in de vleugel en een radiator onder het raam verminderen dat.</p>

<h2>De dakkapel als bouwdeel</h2>
<ul>
<li>De zijwangen en het platte dakje horen even goed geisoleerd te zijn als het dakvlak zelf. Bij een slecht uitgevoerde kapel zit daar de grootste warmteverliespost van de zolder.</li>
<li>De aansluiting op het pannendak vraagt loodwerk aan beide zijden en een correcte gootoplossing aan de voorzijde.</li>
<li>Het dakje is een plat dak in het klein, met dezelfde eisen aan afschot en dakbedekking.</li>
</ul>
%s""" % (rec("Bij het plaatsen of vernieuwen van een dakraam is de aansluiting op de waterkerende laag het beslissende detail.",
             "dakraam-lekkage/", "dendekker-dakbedekking.nl/dakraam-lekkage/"),
         sources([
             "IPLO over vergunningvrije dakkapellen: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/dakkapel/",
             "IPLO over vergunningvrije dakramen: https://iplo.nl/thema/bouw/bouwen-vergunning-melding/dakramen/",
             "IPLO over energiezuinigheid bij verbouw: https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/verbouw/energiezuinigheid/",
         ])))


def _groendak():
    _p("groendak", "Groendak: sedum, opbouw en draagkracht",
       "Wat een extensief sedumdak weegt, hoe de opbouw eruitziet, wat het doet voor waterberging en waar de aandachtspunten zitten.",
       """<h1>Groendak</h1>
<p class="lead">Een groendak is een plat of licht hellend dak met een begroeide toplaag. In Nederland gaat het meestal om een extensief sedumdak: een dunne opbouw met vetplanten die weinig onderhoud vragen.</p>

<h2>Opbouw van onder naar boven</h2>
<ol>
<li>De bestaande dakopbouw met dampremmende laag, isolatie en dakbedekking.</li>
<li>Een wortelwerende laag, tenzij de dakbedekking zelf wortelvast is.</li>
<li>Een beschermings- en drainagelaag die overtollig water afvoert en een deel vasthoudt.</li>
<li>Een filterdoek.</li>
<li>Het substraat, bij een extensief dak meestal 6 tot 12 centimeter.</li>
<li>De begroeiing, als matten, stekken of zaad.</li>
</ol>

<h2>Draagkracht</h2>
<p>Een extensief sedumdak weegt verzadigd met water in de orde van 60 tot 120 kilogram per vierkante meter, afhankelijk van de substraatdikte. Een intensief groendak met struiken komt daar ruim boven. Voor elke bestaande constructie geldt dat de draagkracht vooraf moet worden nagegaan, zeker bij een houten dakvloer uit de jaren zeventig.</p>

<h2>Wat een groendak doet</h2>
<ul>
<li>Regenwater vasthouden en vertraagd afgeven, wat de riolering ontlast bij hevige buien. Dat is de reden dat veel gemeenten een subsidie of een korting op de rioolheffing bieden.</li>
<li>De dakbedekking beschermen tegen ultraviolet licht en temperatuurwisselingen, wat de levensduur verlengt.</li>
<li>De temperatuur onder het dak in de zomer dempen.</li>
<li>Ruimte bieden aan insecten in verhard gebied.</li>
</ul>
<p>Wat een groendak niet doet, is isoleren in de winter. De isolatiewaarde van een dunne substraatlaag is beperkt en verdwijnt zodra de laag nat is. Een groendak vervangt geen dakisolatie en telt niet mee voor de ISDE.</p>
%s

<h2>Onderhoud</h2>
<p>Twee keer per jaar controle volstaat bij een extensief dak: opschot verwijderen, kijken of de afvoeren en de grindstroken eromheen vrij zijn, en kale plekken beoordelen. De randzone rond afvoeren en opstanden blijft onbegroeid, zodat inspectie en afwatering mogelijk blijven.</p>

<h2>Gemeentelijke subsidies</h2>
<p>Veel Nederlandse gemeenten geven een bijdrage per vierkante meter groendak, soms in combinatie met het afkoppelen van de regenpijp. Bedragen en voorwaarden verschillen sterk per gemeente en per jaar, en het budget is meestal beperkt. De actuele regeling staat op de website van de eigen gemeente. De landelijke ISDE kent geen groendakcategorie.</p>
%s""" % (rec("Een groendak vraagt een dakbedekking die daarop is berekend, wat bij renovatie meestal betekent dat de bestaande laag eerst wordt vervangen.",
             "plat-dak-renovatie/", "dendekker-dakbedekking.nl/plat-dak-renovatie/"),
         sources([
             "RVO over de ISDE voor woningeigenaren: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren",
         ])))


def _asbest():
    _p("asbest-op-het-dak", "Asbest op het dak: herkennen, regels en verwijdering",
       "Waar asbest op Nederlandse daken zit, de grens van 35 vierkante meter voor particulieren, de meldingen in het Omgevingsloket en de status van het asbestdakenverbod.",
       """<h1>Asbest op het dak</h1>
<p class="lead">Asbestcement is in Nederland tot 1994 verwerkt in golfplaten, leien, dakgoten en schoorsteenkanalen. Bij gebouwen van voor dat jaar is asbest op het dak niet uitgesloten.</p>

<h2>Waar het zit</h2>
<ul>
<li>Golfplaten op schuren, garages, stallen en carports.</li>
<li>Vlakke vezelcementleien op woningen en dakkapellen.</li>
<li>Beplating rond dakkapellen, overstekken en boeidelen.</li>
<li>Schoorsteenkanalen en ventilatiebuizen.</li>
<li>Oude hemelwaterafvoerbuizen en goten.</li>
</ul>
<p>Zekerheid geeft alleen een analyse door een gecertificeerd bedrijf. Materiaal van na 1994 bevat geen asbest.</p>

<h2>Wat een particulier zelf mag</h2>
<p>Een particulier mag zelf maximaal 35 vierkante meter hechtgebonden asbesthoudend materiaal verwijderen, per particulier, en uitsluitend bij particuliere woningen en bijgebouwen zonder bedrijfsfunctie.</p>
<div class="tablewrap"><table>
<tr><th>Toegestaan</th><th>Niet toegestaan</th></tr>
<tr><td>Geschroefde, hele en niet-verweerde asbestplaten</td><td>Dakleien</td></tr>
<tr><td>Niet-gelijmde hele vloertegels en vloerbedekking</td><td>Gelijmde of gespijkerde platen</td></tr>
<tr><td>Losse voorwerpen zoals bloembakken</td><td>Verweerd materiaal</td></tr>
</table></div>
<p>Daarnaast gelden er voorwaarden: geen professionals inschakelen voor het werk, het materiaal heel houden, dubbel en transparant verpakken met de vermelding Asbest, en inleveren bij de milieustraat.</p>

<h2>Meldingen in het Omgevingsloket</h2>
<ul>
<li>Sloopmelding: uiterlijk een week voor aanvang.</li>
<li>Startmelding: minimaal twee dagen voor de daadwerkelijke start.</li>
<li>Eindmelding: op de eerste werkdag na afronding.</li>
</ul>
%s

<h2>Het asbestdakenverbod</h2>
<p>Er is in Nederland geen wettelijk verbod op asbestdaken. Het wetsvoorstel Verwijdering asbest en asbesthoudende producten is op 4 juni 2019 verworpen door de Eerste Kamer. Sindsdien geldt er geen verwijderplicht voor asbestdaken in goede staat.</p>
<p>Het beleid zet in op vrijwillige versnelling. Het Ministerie van Infrastructuur en Waterstaat werkt sinds het voorjaar van 2025 met de publiekscampagne Asbestvrij dak, een partnerprogramma en een helpdesk.</p>
<p>Dat een verbod ontbreekt, betekent niet dat er niets speelt. Verzekeraars stellen bij schade regelmatig aanvullende voorwaarden aan asbestdaken, en bij brand of storm brengt een asbestdak extra saneringskosten met zich mee.</p>

<h2>Bij vervanging</h2>
<p>Wie een asbesthoudend dak laat vervangen, laat de sanering uitvoeren door een gecertificeerd bedrijf zodra het om meer dan de toegestane hoeveelheid of om niet-toegestane toepassingen gaat. Het loont om de vervanging te combineren met isolatie, omdat de constructie dan toch open ligt en de ISDE bij twee maatregelen verdubbelt.</p>
%s""" % (rec("Vervanging van een asbesthoudend dak begint met een inspectie waarin wordt vastgesteld om welke toepassing en welke oppervlakte het gaat.",
             "dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
         sources([
             "IPLO, spelregels particuliere asbestverwijdering: https://iplo.nl/thema/asbest/praktische-informatie-verwijderen-asbest/spelregels-particuliere-verwijdering-asbesthoudend/",
             "IPLO over de strategie aanpak asbestdaken: https://iplo.nl/thema/asbest/asbestdaken/strategie-aanpak-asbestdaken/",
             "Eerste Kamer, wetsvoorstel 34675, verworpen op 4 juni 2019: https://www.eerstekamer.nl/wetsvoorstel/34675_verwijdering_asbest_en",
             "Rijksoverheid over asbestregels: https://www.rijksoverheid.nl/onderwerpen/asbest/asbestregels",
         ])))


def _onderhoud():
    _p("dakonderhoud", "Dakonderhoud: wat wanneer nagekeken hoort te worden",
       "Een onderhoudsritme per seizoen en per dakonderdeel, met de punten die bij een inspectie horen en het effect van mos, coating en werken op hoogte.",
       """<h1>Dakonderhoud</h1>
<p class="lead">Onderhoud aan een dak bestaat vooral uit kijken. De ingrepen zelf zijn klein: een pan terugleggen, een goot leegmaken, een voeg herstellen. Wat ze waardevol maakt, is dat ze gebeuren voordat water in de constructie komt.</p>

<h2>Ritme</h2>
<div class="tablewrap"><table>
<tr><th>Wanneer</th><th>Wat</th></tr>
<tr><td>Najaar, na de bladval</td><td>Goten en afvoeren leegmaken, bladvangers controleren, noodoverloop vrijmaken</td></tr>
<tr><td>Voorjaar</td><td>Dakvlak visueel nakijken op verschoven of gebroken pannen, mosgroei beoordelen</td></tr>
<tr><td>Na elke storm</td><td>Nokvorsten, gevelpannen en dakranden nakijken, plus de omgeving op afgewaaide delen</td></tr>
<tr><td>Elke drie tot vijf jaar</td><td>Volledige inspectie door een vakman, inclusief schoorsteen, lood en waterkerende laag</td></tr>
<tr><td>Plat dak, twee keer per jaar</td><td>Afvoer, naden, opstanden en dakrand nakijken, blad en takken weghalen</td></tr>
</table></div>

<h2>Wat bij een inspectie hoort</h2>
<ul>
<li>Nok en hoekkepers: mortel, klemmen, ventilatierol.</li>
<li>Pannen: breuk, verschuiving, ontbrekende stukken, staat van de gevelpannen.</li>
<li>Waterkerende laag: gaaf of verpulverd, correct aangesloten op de goot.</li>
<li>Sporen en muurplaat: houtrot, vochtsporen.</li>
<li>Schoorsteen: voegwerk, afdekplaat, loodslabbe.</li>
<li>Goot en afvoer: afschot, bevestiging, verstopping, corrosie.</li>
<li>Doorvoeren en dakramen: manchetten, afdichtingen, aansluitgoten.</li>
<li>Isolatie en dampremmende laag vanaf de zolderzijde: vochtplekken, samengedrukte of losgezakte isolatie.</li>
</ul>
<p>Een inspectie met foto's en video levert een controleerbaar beeld op. Zonder beeldmateriaal blijft de vaststelling een mondelinge mededeling.</p>
%s

<h2>Mos en groene aanslag</h2>
<p>Mos op pannen is op zich geen defect. Het wordt een probleem wanneer het de waterafvoer tussen de pannen blokkeert of in de goot terechtkomt. Hogedrukreiniging is af te raden: de druk beschadigt het oppervlak van de pan, duwt water onder de pannen en maakt de bedekking gevoeliger voor nieuwe aangroei. Voorzichtig borstelen en een biologisch middel werken trager maar richten geen schade aan. Op asbestcement is reinigen niet toegestaan.</p>

<h2>Coating op dakpannen</h2>
<p>Coatings worden aangeboden als alternatief voor vernieuwing. Op een dak dat constructief in orde is en waarvan alleen het uiterlijk tegenvalt, kan dat zinvol zijn. Op een dak met gebroken pannen, een versleten waterkerende laag of ontbrekende isolatie verandert een coating niets aan de oorzaak en maakt ze de werkelijke staat moeilijker te beoordelen.</p>

<h2>Werken op hoogte</h2>
<p>Vallen van hoogte is bij particulier onderhoud de meest voorkomende ernstige ongevalsoorzaak. Een ladder tegen een goot is geen werkplek. Voor alles wat verder gaat dan een goot leegmaken vanaf een stevig opgestelde ladder is een steiger, een hoogwerker of een professionele uitvoerder de aangewezen weg.</p>
%s""" % (rec("Een periodieke dakinspectie met beeldmateriaal legt vast wat is nagekeken en wat de staat van het dak is.",
             "dakonderhoud/", "dendekker-dakbedekking.nl/dakonderhoud/"),
         sources([])))


def _storm():
    _p("stormschade", "Stormschade aan het dak",
       "Wat direct te doen na een storm, hoe de opstalverzekering stormschade dekt, de windkrachtdrempel van verzekeraars en de KNMI-cijfers over stormen.",
       """<h1>Stormschade</h1>
<p class="lead">Storm treft daken op de zwakste punten: nokvorsten, gevelpannen, dakranden en losse delen van een plat dak. De schade is meestal beperkt in oppervlakte, maar laat het dakvlak wel open voor de volgende bui.</p>

<h2>Direct na de storm</h2>
<ol>
<li>Wachten tot het veilig is. Een tweede windvlaag maakt van een losse pan een projectiel.</li>
<li>De omgeving afzetten wanneer er materiaal naar beneden kan komen.</li>
<li>Vanaf de grond fotograferen wat zichtbaar is, ook de afgewaaide delen waar ze liggen.</li>
<li>Zolder en plafonds nakijken op vochtplekken.</li>
<li>De verzekeraar melden en een noodherstel laten uitvoeren.</li>
<li>Geen definitief herstel laten uitvoeren voor de vaststelling, tenzij de situatie onveilig is.</li>
</ol>

<h2>De dekking</h2>
<p>De meeste particuliere woonhuisverzekeringen dekken stormschade aan de woning, de inboedel en schuttingen, meestal met een eigen risico. Schade door achterstallig onderhoud is niet gedekt. Het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 14 meter per seconde of 50 kilometer per uur, als drempel waarboven van storm wordt gesproken.</p>
<p>Het KNMI hanteert een andere definitie: storm is windkracht 9, een uurgemiddelde van 75 tot 88 kilometer per uur. Zware storm begint bij windkracht 10, 24,5 meter per seconde. Die twee definities worden in schadegesprekken vaak door elkaar gehaald.</p>

<h2>Wat de cijfers laten zien</h2>
<ul>
<li>2024: ongeveer 278 miljoen euro verzekerde klimaatschade, met zware zomerbuien als grootste post.</li>
<li>Storm Conall, 27 november 2024: eerste schatting ongeveer 40 miljoen euro verzekerde schade.</li>
<li>2025: ruim 155 miljoen euro verzekerde klimaatschade, waarvan ruim 60 miljoen euro storm, ongeveer 50 miljoen euro hagel en 35 miljoen euro neerslag.</li>
<li>Ter vergelijking, de februaristormen Dudley, Eunice en Franklin in 2022: minimaal 500 miljoen euro.</li>
<li>Zomerstorm Poly, 5 juli 2023: eerste schatting 50 tot 100 miljoen euro, met een hoogste windstoot van 146 kilometer per uur bij IJmuiden.</li>
</ul>
<p>Het KNMI ziet geen aanwijzing dat het aantal stormen of de kracht ervan wezenlijk toeneemt. Sinds de jaren negentig is er zelfs een kleine afname van de gemiddelde windsterkte. Het aantal zware stormen per jaar lag rond 0,5 in de periode 1911 tot 1950, rond 0,8 in 1951 tot 2000 en rond 0,6 in 2001 tot 2024.</p>
%s

<h2>Wat een rustig stormjaar betekent</h2>
<p>De onderdelen die bij storm loskomen, verzwakken geleidelijk. Mortel onder een nokvorst scheurt door temperatuurwisselingen en vorst, niet door wind. Wind maakt zichtbaar wat al los zat. Een rustige periode betekent dus dat zwakke plekken langer onopgemerkt blijven.</p>

<h2>Preventie</h2>
<p>De onderdelen die als eerste loskomen, zijn dezelfde die bij een inspectie het eerst opvallen: mortel van de nok, gevelpannen zonder klem, dakranden met losse bevestiging, en een plat dak met een losgekomen randprofiel. Een controle na de winter beperkt de schade bij de volgende storm aanzienlijk.</p>
%s""" % (rec("Bij stormschade is een noodherstel binnen enkele uren het verschil tussen een losse pan en een doorweekt plafond.",
             "stormschade-dak/", "dendekker-dakbedekking.nl/stormschade-dak/"),
         sources([
             "Verbond van Verzekeraars over stormschade: https://www.verzekeraars.nl/verzekeringsthemas/schade/stormschade",
             "Verbond van Verzekeraars, klimaatschade 2025: https://www.verzekeraars.nl/publicaties/actueel/hagel-en-storm-grootste-oorzaken-klimaatschade-in-2025",
             "Verbond van Verzekeraars over storm Conall: https://www.verzekeraars.nl/publicaties/actueel/eerste-schatting-40-miljoen-euro-schade-door-storm-conall",
             "Verbond van Verzekeraars over de februaristormen 2022: https://www.verzekeraars.nl/publicaties/actueel/ruim-500-miljoen-euro-schade-door-februaristormen",
             "Verbond van Verzekeraars over zomerstorm Poly: https://www.verzekeraars.nl/publicaties/actueel/eerste-schatting-50-100-miljoen-euro-schade-door-zomerstorm-poly",
             "KNMI, uitleg storm: https://www.knmi.nl/kennis-en-datacentrum/uitleg/storm",
             "KNMI, lijst zware stormen sinds 1910: https://www.knmi.nl/nederland-nu/klimatologie/lijsten/zwarestormen",
             "KNMI over zomerstorm Poly: https://www.knmi.nl/over-het-knmi/nieuws/zeer-zware-zomerstorm-poly",
             "KNMI over storm en hoogwater: https://www.knmi.nl/over-het-knmi/nieuws/storm-en-hoogwater",
         ])))
