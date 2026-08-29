# -*- coding: utf-8 -*-
"""Drie hulpmiddelen, volledig in de pagina, zonder opslag en zonder externe verzoeken."""
from engine import Page, add, dd_link

CR = [("/hulpmiddelen/", "Hulpmiddelen")]

ITEMS = [
    ("daklekkage-diagnose", "Daklekkage-diagnose",
     "Symptomen aanvinken en de meest waarschijnlijke oorzaken op volgorde krijgen"),
    ("onderhoudsplanner", "Levensduur- en onderhoudsplanner",
     "Daktype en leeftijd invullen en een onderhoudsritme met inspectiemomenten krijgen"),
    ("stormschade-en-subsidiecheck", "Stormschade- en subsidiecheck",
     "Nagaan of de storm de verzekeringsdrempel haalde en wat de ISDE oplevert"),
]


def build():
    tiles = "".join('<a class="tile" href="/hulpmiddelen/%s/"><b>%s</b><span>%s</span></a>'
                    % (s, t, d) for s, t, d in ITEMS)
    add(Page("/hulpmiddelen/", "Hulpmiddelen voor dakeigenaren",
             "Drie hulpmiddelen: een diagnose bij daklekkage, een levensduur- en onderhoudsplanner en een check op stormschade en de ISDE-subsidie.",
             """<div class="wrap">
<h1>Hulpmiddelen</h1>
<p class="lead">Drie hulpmiddelen die in de pagina zelf rekenen. Er wordt niets verzonden, niets opgeslagen en er is geen registratie nodig. De uitkomst is een indicatie en vervangt geen inspectie ter plaatse.</p>
<div class="grid">%s</div>
<h2>Waarop de uitkomsten gebaseerd zijn</h2>
<p>De subsidiecheck rekent met de ISDE-bedragen voor 2026 zoals RVO die publiceert. De stormcheck gebruikt de drempel van windkracht 7 die het Verbond van Verzekeraars hanteert en de meteorologische definities van het KNMI. De diagnose en de onderhoudsplanner werken met vuistregels uit de dakbedekkingspraktijk; die zijn indicatief en niet uit een officiele bron afkomstig.</p>
<p>Meer achtergrond staat in <a href="/dakwerken/">de gids</a> en bij <a href="/regels/">regels en subsidies</a>.</p>
</div>""" % tiles, priority="0.8"))
    _diagnose(); _planner(); _storm()


def _tool_page(slug, title, desc, body, script):
    aside = ('<aside><div class="card"><h3>Andere hulpmiddelen</h3>'
             '<ul style="margin:0;padding-left:18px">%s</ul>'
             '<p class="small" style="margin-top:12px">Alles rekent in de browser. '
             'Er worden geen gegevens bewaard of verstuurd.</p></div></aside>'
             % "".join('<li><a href="/hulpmiddelen/%s/">%s</a></li>' % (s, t)
                       for s, t, _ in ITEMS if s != slug))
    add(Page("/hulpmiddelen/%s/" % slug, title, desc,
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, aside)
             + "<script>%s</script>" % script,
             crumbs=CR, priority="0.7"))


DIAG_BODY = """<h1>Daklekkage-diagnose</h1>
<p class="lead">Vijf vragen over wat zichtbaar is en wanneer het optreedt. De uitkomst is een geordende lijst met de meest waarschijnlijke oorzaken, met per oorzaak wat er nagekeken hoort te worden.</p>

<div class="tool">
<form id="dg">
<fieldset><legend>1. Wat voor dak is het</legend>
<label class="opt"><input type="radio" name="dak" value="hellend" checked> Hellend dak met dakpannen of leien</label>
<label class="opt"><input type="radio" name="dak" value="plat"> Plat dak met bitumen, EPDM of een dakterras</label>
<label class="opt"><input type="radio" name="dak" value="beide"> Beide, een hellend dak met een platte aanbouw of dakkapel</label>
</fieldset>

<fieldset><legend>2. Waar is het vocht zichtbaar</legend>
<label class="opt"><input type="radio" name="plek" value="schoorsteen" checked> Tegen of vlak naast de schoorsteen</label>
<label class="opt"><input type="radio" name="plek" value="nok"> Onder de nok, hoog op zolder</label>
<label class="opt"><input type="radio" name="plek" value="muur"> Tegen een muur waar een lager dak op aansluit</label>
<label class="opt"><input type="radio" name="plek" value="voet"> Laag, aan de dakvoet of net onder de goot</label>
<label class="opt"><input type="radio" name="plek" value="raam"> Rond een dakraam, dakkapel of lichtkoepel</label>
<label class="opt"><input type="radio" name="plek" value="midden"> Midden in een plafond, zonder duidelijke aansluiting erboven</label>
<label class="opt"><input type="radio" name="plek" value="verspreid"> Op meerdere plekken tegelijk of steeds op een andere plek</label>
</fieldset>

<fieldset><legend>3. Wanneer treedt het op</legend>
<label class="opt"><input type="radio" name="moment" value="regen" checked> Tijdens of vlak na regen</label>
<label class="opt"><input type="radio" name="moment" value="wind"> Alleen bij regen met veel wind, vaak uit een bepaalde richting</label>
<label class="opt"><input type="radio" name="moment" value="hoos"> Alleen bij een hevige, kortdurende bui</label>
<label class="opt"><input type="radio" name="moment" value="koud"> Vooral bij koud weer, ook zonder regen</label>
<label class="opt"><input type="radio" name="moment" value="dooi"> Bij dooi na vorst of na sneeuw</label>
</fieldset>

<fieldset><legend>4. Hoe ziet het vocht eruit</legend>
<label class="opt"><input type="radio" name="beeld" value="scherp" checked> Een afgetekende vlek met een duidelijke rand</label>
<label class="opt"><input type="radio" name="beeld" value="druppel"> Zichtbaar druppelen of stromen</label>
<label class="opt"><input type="radio" name="beeld" value="diffuus"> Een groter, vaag vochtig vlak zonder scherpe rand</label>
<label class="opt"><input type="radio" name="beeld" value="schimmel"> Vooral schimmel of muffe geur, weinig zichtbaar water</label>
</fieldset>

<fieldset><legend>5. Hoe oud is de dakbedekking ongeveer</legend>
<label class="opt"><input type="radio" name="leeftijd" value="jong"> Minder dan 15 jaar</label>
<label class="opt"><input type="radio" name="leeftijd" value="midden" checked> 15 tot 30 jaar</label>
<label class="opt"><input type="radio" name="leeftijd" value="oud"> Meer dan 30 jaar, of onbekend</label>
</fieldset>
</form>
<div class="result" id="uit" role="status" aria-live="polite"></div>
</div>

<h2>Wat de uitkomst wel en niet is</h2>
<p>De lijst ordent oorzaken op waarschijnlijkheid, op basis van de combinatie van symptomen. Ze vervangt geen inspectie. Water loopt vaak meters ver over folie of balken voordat het naar beneden valt, waardoor de instroomplek zelden recht boven de vlek ligt.</p>
<p>Meer achtergrond staat in het hoofdstuk <a href="/dakwerken/daklekkage/">daklekkage</a>.</p>
%s""" % ('<div class="rec"><h3>Bij een acuut lek</h3><p>Een lek dat actief water doorlaat, vraagt eerst een noodherstel en daarna pas een structurele oplossing. De redactie beveelt %s aan, telefonisch bereikbaar op 085 130 2723, ook buiten kantooruren.</p></div>'
         % dd_link("daklekkage/", "dendekker-dakbedekking.nl/daklekkage/"))

DIAG_JS = r"""
(function(){
 var C = {
  schoorsteen:{t:"Loodslabbe of voegwerk van de schoorsteen",w:"De loodstrook rond de schoorsteen is losgekomen, gescheurd of nooit correct in de voeg gewerkt. Ook poreus voegwerk boven het dakvlak laat water door.",n:"Loodwerk rondom, voegwerk van het metselwerk boven het dak en de afdekplaat."},
  nok:{t:"Nokvorsten en nokmortel",w:"De mortel onder de nokvorsten scheurt door temperatuurwisselingen en vorst. Bij een poreuze of losse vorst loopt water langs de nok naar binnen.",n:"Nokvorsten op vastheid, mortel op scheuren, en of de nok geventileerd is uitgevoerd."},
  muur:{t:"Muuraansluiting van een lager dakvlak",w:"Waar een lager dak of een aanbouw tegen een hogere muur komt, zit een loodslabbe of een opstand. Dat is het meest belaste detail van het dak.",n:"Hoogte en bevestiging van de opstand, de inwerking in de voeg en de aansluiting op de dakbedekking."},
  voet:{t:"Goot, gootbevestiging of aansluiting op de waterkerende laag",w:"Een goot die overloopt of achterwaarts lekt, geeft vocht laag in de constructie. Ook een waterkerende laag die niet tot in de goot doorloopt, geeft dit beeld.",n:"Afschot en bevestiging van de goot, verstopping bij de tapbuis en de aansluiting van de waterkerende laag."},
  raam:{t:"Aansluiting van dakraam, dakkapel of lichtkoepel",w:"De aansluitgoot boven het raam, de inwerking op de waterkerende laag of het afdichtingsrubber van de vleugel laat water door.",n:"Aansluitset rondom, de goot boven het raam, het rubber van de draaivleugel en de zijwangen van een dakkapel."},
  midden:{t:"Doorvoer of beschadiging midden in het dakvlak",w:"Ventilatiepannen, rookgasafvoeren, antennedoorvoeren en bevestigingen van zonnepanelen zijn losse doorbrekingen midden op het dak.",n:"Alle doorvoeren, rubbermanchetten en de bevestigingspunten van eventuele zonnepanelen."},
  verspreid:{t:"Versleten waterkerende laag of dakbedekking over het volledige vlak",w:"Wanneer het vocht steeds op een andere plek verschijnt, is meestal niet een detail maar de bedekking zelf aan het einde van de levensduur.",n:"Staat van de waterkerende laag over de volle breedte, panlatten op houtrot en de sporen."},
  wind:{t:"Inwaaiende regen onder de pannen",w:"Bij wind wordt regen onder de pannen geblazen. Met een gave waterkerende laag is dat geen probleem; zonder die laag wel.",n:"Aanwezigheid en staat van de waterkerende laag, en de zijdelingse afdichting bij gevelpannen."},
  hoos:{t:"Onderdimensionering of verstopping van de afvoer",w:"Bij korte, hevige buien komt meer water op het dak dan de goot of afvoer aankan. Dat is geen lek in de bedekking maar een afvoerprobleem.",n:"Diameter en aantal afvoeren, bladvangers, en of er een noodoverloop aanwezig is."},
  cond:{t:"Condensatie in plaats van lekkage",w:"Warme binnenlucht bereikt een koud vlak en slaat daar neer. Dat geeft vocht zonder regen, vaak diffuus verspreid en met schimmelvorming.",n:"Doorlopendheid van het dampremmende scherm, ventilatie van de zolder en luchtdichtheid rond doorvoeren en inbouwspots."},
  dooi:{t:"Sneeuwophoping of ijsvorming in de goot",w:"Smeltwater dat niet weg kan doordat de goot bevroren of verstopt is, staat tegen de dakvoet en zoekt een weg naar binnen.",n:"Goot en afvoer op verstopping, en de aansluiting van de waterkerende laag op de goot."},
  naad:{t:"Naad, opstand of dakrand van het platte dak",w:"Op een plat dak zitten de zwakke punten in de naden, aan de opstanden tegen muren en bij de dakrand. Water loopt daarna over de dampremmende laag en komt elders naar beneden.",n:"Alle naden, opstandhoogte, randprofiel en de inwerking rond de tapbuis."},
  natisol:{t:"Verzadigde isolatie onder een plat dak",w:"Wanneer water al langer in de opbouw zit, is de isolatie verzadigd. Die droogt in een gesloten dak niet meer uit en blijft vocht afgeven.",n:"Vochtmeting in de isolatielaag, eventueel met proefsleuven, voordat er iets wordt dichtgemaakt."}
 };
 var f=document.getElementById('dg'), out=document.getElementById('uit');
 function val(n){var e=f.querySelector('input[name="'+n+'"]:checked');return e?e.value:'';}
 function calc(){
  var dak=val('dak'),plek=val('plek'),mom=val('moment'),bld=val('beeld'),lft=val('leeftijd');
  var s={};
  function add(k,p){s[k]=(s[k]||0)+p;}
  if(dak==='hellend'||dak==='beide'){add('nok',7);add('voet',7);add('midden',5);add('verspreid',6);}
  if(plek in C) add(plek,50);
  if(mom==='wind'){add('wind',45);add('nok',10);}
  if(mom==='hoos'){add('hoos',40);add('voet',15);}
  if(mom==='koud'){add('cond',55);}
  if(mom==='dooi'){add('dooi',45);add('voet',15);}
  if(mom==='regen'){if(plek in C)add(plek,10);}
  if(bld==='diffuus'){add('cond',35);}
  if(bld==='schimmel'){add('cond',45);}
  if(bld==='druppel'){if(plek in C)add(plek,15);add('cond',-25);}
  if(bld==='scherp'){add('cond',-15);}
  if(dak==='plat'||dak==='beide'){add('naad',30);if(plek==='verspreid')add('natisol',30);if(lft==='oud')add('natisol',20);}
  if(dak==='hellend'){delete s.naad;delete s.natisol;}
  if(lft==='oud'){add('verspreid',25);add('nok',10);}
  if(lft==='jong'){add('verspreid',-25);add('raam',5);}
  var arr=[];for(var k in s){if(s[k]>0&&C[k])arr.push([k,s[k]]);}
  arr.sort(function(a,b){return b[1]-a[1];});
  arr=arr.slice(0,4);
  if(!arr.length){out.innerHTML='<p>Deze combinatie levert geen duidelijk beeld op. Een inspectie op het dak is dan de aangewezen stap.</p>';return;}
  var max=arr[0][1];
  var urg='gewoon', ut='Herstel binnen enkele weken volstaat, mits het water wordt opgevangen.';
  if(bld==='druppel'||mom==='hoos'){urg='hoog';ut='Er komt actief water binnen. Een noodherstel op korte termijn beperkt de gevolgschade aan isolatie, hout en pleisterwerk.';}
  if(arr[0][0]==='cond'){urg='anders';ut='Dit wijst eerder op condensatie dan op lekkage. Het dak dichtmaken verergert dat. Ventilatie en het dampremmende scherm zijn dan het aangrijpingspunt.';}
  if(arr[0][0]==='natisol'){urg='hoog';ut='Verzadigde isolatie droogt niet meer uit. Alleen de bovenlaag vernieuwen sluit het vocht in.';}
  var h='<h3>Meest waarschijnlijke oorzaken</h3>';
  h+='<p class="verdict">'+(urg==='hoog'?'Urgentie: hoog':(urg==='anders'?'Waarschijnlijk geen lekkage':'Urgentie: normaal'))+'</p><p>'+ut+'</p>';
  arr.forEach(function(p,i){
   var c=C[p[0]], pct=Math.max(18,Math.round(p[1]/max*100));
   h+='<div style="margin:16px 0"><b>'+(i+1)+'. '+c.t+'</b>'+
      '<div class="bar"><i style="width:'+pct+'%"></i></div>'+
      '<p style="margin:6px 0 4px">'+c.w+'</p>'+
      '<p class="small" style="margin:0"><b>Na te kijken:</b> '+c.n+'</p></div>';
  });
  h+='<p class="small">Indicatie op basis van de aangevinkte symptomen. De werkelijke instroomplek ligt zelden recht boven de vlek.</p>';
  out.innerHTML=h;
 }
 f.addEventListener('change',calc); calc();
})();
"""


def _diagnose():
    _tool_page("daklekkage-diagnose", "Daklekkage-diagnose: van symptoom naar waarschijnlijke oorzaak",
               "Vijf vragen over de plek, het moment en het beeld van het vocht leiden naar de meest waarschijnlijke oorzaken van een daklekkage, met wat er nagekeken hoort te worden.",
               DIAG_BODY, DIAG_JS)


PLAN_BODY = """<h1>Levensduur- en onderhoudsplanner</h1>
<p class="lead">Daktype, materiaal, leeftijd en omgeving bepalen samen hoe vaak een dak nagekeken hoort te worden en hoeveel jaar de bedekking normaal nog meegaat. Deze planner zet dat om in een ritme en een jaarplanning.</p>

<div class="tool">
<form id="pl">
<label class="field"><b>Type dak</b>
<select name="type">
<option value="keramisch">Hellend dak, keramische dakpannen</option>
<option value="beton">Hellend dak, betonpannen</option>
<option value="natuurlei">Hellend dak, natuurleien</option>
<option value="vezellei">Hellend dak, vezelcementleien</option>
<option value="riet">Hellend dak, riet</option>
<option value="bitumen">Plat dak, bitumen</option>
<option value="epdm">Plat dak, EPDM</option>
<option value="zink">Plat of hellend dak, zink</option>
</select></label>

<label class="field"><b>Leeftijd van de dakbedekking in jaren</b>
<input type="number" name="leeftijd" min="0" max="120" step="1" value="25"></label>

<label class="field"><b>Omgeving</b>
<select name="omgeving">
<option value="open">Open ligging, weinig bomen</option>
<option value="loof">Loofbomen dicht bij de woning</option>
<option value="naald">Naaldbomen dicht bij de woning</option>
<option value="stad">Gesloten stadsbebouwing</option>
<option value="kust">Binnen enkele kilometers van de kust</option>
</select></label>

<label class="field"><b>Windbelasting</b>
<select name="wind">
<option value="normaal">Normaal, bebouwde omgeving</option>
<option value="hoog">Open ligging, polder, rivierengebied of kust</option>
</select></label>

<label class="field"><b>Onderhoud tot nu toe</b>
<select name="hist">
<option value="regelmatig">Regelmatig, goten en dak worden jaarlijks nagekeken</option>
<option value="soms">Af en toe, geen vast ritme</option>
<option value="nooit">Nooit of niet bekend</option>
</select></label>
</form>
<div class="result" id="pout" role="status" aria-live="polite"></div>
</div>

<h2>Waar de cijfers vandaan komen</h2>
<p>De aangehouden levensduren zijn vuistregels uit de dakbedekkingspraktijk. Er is geen officiele Nederlandse bron die per materiaal een verwachte levensduur publiceert; RVO, IPLO, Milieu Centraal en het CBS doen dat niet. De getallen zijn dus indicatief en niet als norm bedoeld. De werkelijke staat van een dak hangt sterker af van de uitvoering en het onderhoud dan van het materiaal alleen.</p>
<p>Het onderhoudsritme sluit aan bij wat in het hoofdstuk <a href="/dakwerken/dakonderhoud/">dakonderhoud</a> staat.</p>
%s""" % ('<div class="rec"><h3>Inspectie</h3><p>Een periodieke inspectie met foto- en videomateriaal legt vast wat er is nagekeken. De redactie beveelt %s aan.</p></div>'
         % dd_link("dakinspectie/", "dendekker-dakbedekking.nl/dakinspectie/"))

PLAN_JS = r"""
(function(){
 var M={
  keramisch:{n:"keramische dakpannen",lo:50,hi:80,note:"Kleurvast en lang meegaand. De waterkerende laag eronder is doorgaans eerder aan vervanging toe dan de pannen zelf."},
  beton:{n:"betonpannen",lo:30,hi:50,note:"Zwaarder dan keramiek en gevoeliger voor vergroening aan de noordzijde."},
  natuurlei:{n:"natuurleien",lo:60,hi:100,note:"Zeer lange staat van dienst. De bevestiging, haken of nagels, bepaalt in de praktijk het vervangingsmoment."},
  vezellei:{n:"vezelcementleien",lo:30,hi:50,note:"Bij een dak van voor 1994 is asbest niet uitgesloten. Reinigen is dan niet toegestaan en verwijdering volgt de asbestregels."},
  riet:{n:"riet",lo:25,hi:45,note:"De nok vraagt vaker vernieuwing dan het vlak. Noordzijden gaan korter mee dan zuidzijden."},
  bitumen:{n:"bitumen",lo:20,hi:30,note:"Twee lagen, per stuk herstelbaar. De naden en de opstanden bepalen de levensduur."},
  epdm:{n:"EPDM",lo:30,hi:50,note:"Weinig naden op kleinere daken. Beschadigingen midden in een baan zijn lastiger onzichtbaar te herstellen."},
  zink:{n:"zink",lo:35,hi:60,note:"Gaat lang mee zolang het niet in contact komt met koper en niet onder stilstaand vuil ligt."}
 };
 var f=document.getElementById('pl'), out=document.getElementById('pout');
 function v(n){return f.querySelector('[name="'+n+'"]').value;}
 function calc(){
  var t=v('type'), m=M[t], lft=parseInt(v('leeftijd')||'0',10);
  if(isNaN(lft)||lft<0)lft=0; if(lft>120)lft=120;
  var om=v('omgeving'), wi=v('wind'), hi=v('hist');
  var factor=1;
  if(hi==='nooit')factor-=0.15; else if(hi==='soms')factor-=0.07;
  if(wi==='hoog')factor-=0.07;
  if(om==='naald')factor-=0.05; else if(om==='loof')factor-=0.03; else if(om==='kust')factor-=0.08;
  var lo=Math.round(m.lo*factor), up=Math.round(m.hi*factor);
  var restLo=lo-lft, restHi=up-lft;
  var fase, kleur;
  if(restHi<=0){fase='Voorbij de verwachte levensduur';kleur='hi';}
  else if(restLo<=0){fase='In de vervangingszone';kleur='hi';}
  else if(restLo<=10){fase='Laatste fase, vervanging binnen tien jaar in beeld';kleur='';}
  else {fase='Onderhoudsfase';kleur='ok';}
  var interval=5;
  if(t==='bitumen'||t==='epdm')interval=3;
  if(restLo<=10)interval=Math.min(interval,3);
  if(restHi<=0)interval=2;
  if(hi==='nooit')interval=Math.min(interval,3);
  var goot='een keer per jaar, na de bladval';
  if(om==='loof')goot='twee keer per jaar, in november en in het voorjaar';
  if(om==='naald')goot='twee tot drie keer per jaar, naalden vallen het hele jaar door';
  if(t==='bitumen'||t==='epdm')goot='twee keer per jaar, plus na elke storm';
  var h='<h3>'+m.n.charAt(0).toUpperCase()+m.n.slice(1)+', '+lft+' jaar oud</h3>';
  h+='<p class="verdict"><span class="tag '+kleur+'">'+fase+'</span></p>';
  var pct=Math.min(100,Math.round(lft/((lo+up)/2)*100));
  h+='<div class="bar"><i style="width:'+pct+'%"></i></div>';
  h+='<p class="small">Verbruikte levensduur ten opzichte van het gemiddelde van de bandbreedte.</p>';
  if(restHi>0){
   h+='<p>Bij de ingevulde omstandigheden ligt de verwachte resterende levensduur tussen '+Math.max(0,restLo)+' en '+restHi+' jaar. De bandbreedte voor dit materiaal is '+lo+' tot '+up+' jaar, gecorrigeerd voor omgeving, windbelasting en onderhoudsgeschiedenis.</p>';
  } else {
   h+='<p>De bedekking is ouder dan de bandbreedte van '+lo+' tot '+up+' jaar die voor dit materiaal wordt aangehouden. Dat betekent niet dat vervanging vandaag nodig is, wel dat de staat van de waterkerende laag en de constructie leidend wordt in plaats van de leeftijd.</p>';
  }
  h+='<p class="small">'+m.note+'</p>';
  h+='<h3 style="margin-top:18px">Ritme</h3><ul>';
  h+='<li><b>Volledige inspectie door een vakman:</b> elke '+interval+' jaar.</li>';
  h+='<li><b>Goten en afvoeren:</b> '+goot+'.</li>';
  h+='<li><b>Visuele controle vanaf de grond:</b> in het voorjaar en na elke storm.</li>';
  if(t==='bitumen'||t==='epdm')h+='<li><b>Plat dak specifiek:</b> naden, opstanden, dakrand en de noodoverloop twee keer per jaar nakijken.</li>';
  if(t==='riet')h+='<li><b>Riet specifiek:</b> de nokafwerking apart beoordelen, die gaat korter mee dan het vlak.</li>';
  if(t==='vezellei'&&lft>=32)h+='<li><b>Let op:</b> bij een dak van voor 1994 is asbest niet uitgesloten. Reinigen is dan niet toegestaan.</li>';
  if(om==='kust')h+='<li><b>Kustligging:</b> zink, bevestigingsmiddelen en dakranden jaarlijks nakijken; zout versnelt de aantasting.</li>';
  if(wi==='hoog')h+='<li><b>Open ligging:</b> nokvorsten, gevelpannen en dakranden extra nakijken na wind.</li>';
  h+='</ul>';
  h+='<h3 style="margin-top:18px">Jaarplanning</h3><div class="tablewrap"><table>'+
     '<tr><th>Periode</th><th>Actie</th></tr>'+
     '<tr><td>Maart en april</td><td>Dakvlak visueel nakijken op verschoven of gebroken delen, mosgroei beoordelen</td></tr>'+
     '<tr><td>Juni</td><td>Platte daken en dakramen nakijken voor het buienseizoen</td></tr>'+
     '<tr><td>November</td><td>Goten en afvoeren leegmaken, noodoverloop vrijmaken</td></tr>'+
     '<tr><td>Na elke storm</td><td>Nok, gevelpannen, dakrand en de omgeving op afgewaaide delen controleren</td></tr>'+
     '</table></div>';
  h+='<p class="small">Indicatie. Vuistregels uit de praktijk, geen norm.</p>';
  out.innerHTML=h;
 }
 f.addEventListener('input',calc); f.addEventListener('change',calc); calc();
})();
"""


def _planner():
    _tool_page("onderhoudsplanner", "Levensduur- en onderhoudsplanner voor het dak",
               "Daktype, leeftijd, omgeving en onderhoudsgeschiedenis omgezet in een verwachte resterende levensduur, een inspectie-interval en een jaarplanning.",
               PLAN_BODY, PLAN_JS)


STORM_BODY = """<h1>Stormschade- en subsidiecheck</h1>
<p class="lead">Twee losse checks. De eerste gaat na of een storm de drempel haalde die verzekeraars hanteren. De tweede rekent uit wat de ISDE-subsidie voor dakisolatie oplevert.</p>

<h2>Stormcheck</h2>
<div class="tool">
<form id="st">
<label class="field"><b>Hoogste gemeten windsnelheid in de omgeving, in kilometer per uur</b>
<input type="number" name="kmh" min="0" max="250" step="1" value="70"></label>
<label class="field"><b>Wat is er beschadigd</b>
<select name="wat">
<option value="pannen">Losgewaaide of gebroken dakpannen of leien</option>
<option value="nok">Nokvorsten losgekomen</option>
<option value="plat">Dakbedekking van een plat dak opgewaaid</option>
<option value="goot">Goot of regenpijp losgerukt</option>
<option value="boom">Schade door een omgevallen boom of tak</option>
<option value="lek">Water binnen na de storm</option>
</select></label>
<label class="field"><b>Staat van het dak voor de storm</b>
<select name="staat">
<option value="goed">Goed, recent nagekeken of onderhouden</option>
<option value="onbekend">Onbekend, geen recente inspectie</option>
<option value="slecht">Er waren al losse of beschadigde delen</option>
</select></label>
</form>
<div class="result" id="stout" role="status" aria-live="polite"></div>
</div>

<h2>ISDE-check voor dakisolatie</h2>
<div class="tool">
<form id="pr">
<label class="field"><b>Te isoleren dakoppervlakte in vierkante meter</b>
<input type="number" name="m2" min="0" max="600" step="1" value="90"></label>
<label class="field"><b>Aantal maatregelen</b>
<select name="aantal">
<option value="1">Alleen dakisolatie</option>
<option value="2" selected>Twee of meer maatregelen, of combinatie met warmtepomp, zonneboiler of warmtenet</option>
</select></label>
<label class="field"><b>Isolatiemateriaal</b>
<select name="materiaal">
<option value="regulier">Regulier isolatiemateriaal</option>
<option value="biobased">Biobased isolatiemateriaal</option>
</select></label>
<label class="field"><b>Rd-waarde van het nieuwe isolatiemateriaal</b>
<input type="number" name="rd" min="0" max="12" step="0.1" value="4"></label>
<label class="field"><b>Energiezuinige ventilatie in dezelfde periode</b>
<select name="vent"><option value="nee">Nee</option><option value="ja">Ja</option></select></label>
</form>
<div class="result" id="prout" role="status" aria-live="polite"></div>
</div>

<h2>Waar deze uitkomsten op gebaseerd zijn</h2>
<p>De stormcheck gebruikt de drempel van windkracht 7, ongeveer 50 kilometer per uur, die het Verbond van Verzekeraars hanteert, en daarnaast de meteorologische definities van het KNMI, dat pas vanaf windkracht 9 van storm spreekt.</p>
<p>De ISDE-check rekent met de bedragen voor 2026 zoals RVO die publiceert: 16,25 euro per vierkante meter bij een maatregel, 32,50 euro bij twee of meer, 5 euro per vierkante meter extra voor biobased materiaal, een minimale Rd-waarde van 3,5, een minimale oppervlakte van 20 vierkante meter en een maximum van 200 vierkante meter. Details op <a href="/regels/isde-subsidie/">de ISDE-pagina</a>.</p>
<ul class="src">
<li>Verbond van Verzekeraars, infographic wind: https://www.verzekeraars.nl/verzekeringsthemas/klimaat-en-duurzaamheid/praktische-hulpmiddelen/infographic-verzekerbaarheid-klimaatrisico-s/wind</li>
<li>Verbond van Verzekeraars over stormschade: https://www.verzekeraars.nl/verzekeringsthemas/schade/stormschade</li>
<li>KNMI, uitleg storm: https://www.knmi.nl/kennis-en-datacentrum/uitleg/storm</li>
<li>RVO, ISDE isolatiemaatregelen: https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren/isolatiemaatregelen</li>
<li>RVO, wat wijzigt er in 2026: https://www.rvo.nl/subsidies-financiering/isde/isde-wat-wijzigt-er-2026</li>
</ul>
%s""" % ('<div class="rec"><h3>Herstel na storm</h3><p>Een noodherstel dat het dakvlak dichtmaakt, voorkomt dat de volgende bui de schade vergroot. De redactie beveelt %s aan, bereikbaar op 085 130 2723.</p></div>'
         % dd_link("stormschade-dak/", "dendekker-dakbedekking.nl/stormschade-dak/"))

STORM_JS = r"""
(function(){
 var f=document.getElementById('st'), out=document.getElementById('stout');
 function v(n){return f.querySelector('[name="'+n+'"]').value;}
 function calc(){
  var k=parseFloat(v('kmh')); if(isNaN(k)||k<0)k=0; if(k>250)k=250;
  var wat=v('wat'), st=v('staat');
  var h='';
  if(k>=50){
   h+='<p class="verdict"><span class="tag hi">Boven windkracht 7</span></p>';
   h+='<p>Het Verbond van Verzekeraars hanteert windkracht 7, ongeveer 14 meter per seconde of 50 kilometer per uur, als drempel waarboven van storm wordt gesproken. Bij '+k+' kilometer per uur is die drempel gehaald.</p>';
  } else {
   h+='<p class="verdict">Onder windkracht 7</p>';
   h+='<p>Bij '+k+' kilometer per uur wordt de drempel van ongeveer 50 kilometer per uur niet gehaald. Schade die dan toch optreedt, wijst meestal op een bestaand gebrek in de bevestiging. De polisvoorwaarden bepalen wat de eigen verzekeraar hanteert.</p>';
  }
  if(k>=117)h+='<p class="small">Ter vergelijking: het KNMI spreekt boven 117 kilometer per uur van orkaankracht, windkracht 12.</p>';
  else if(k>=103)h+='<p class="small">Ter vergelijking: het KNMI noemt dit zeer zware storm, windkracht 11.</p>';
  else if(k>=89)h+='<p class="small">Ter vergelijking: het KNMI noemt dit zware storm, windkracht 10.</p>';
  else if(k>=75)h+='<p class="small">Ter vergelijking: het KNMI spreekt van storm bij windkracht 9, een uurgemiddelde van 75 tot 88 kilometer per uur.</p>';
  else h+='<p class="small">Het KNMI spreekt pas vanaf 75 kilometer per uur uurgemiddeld van storm. De drempel van de verzekeraar ligt lager dan de meteorologische definitie.</p>';
  if(st==='slecht')h+='<p><b>Aandachtspunt.</b> Schade als gevolg van achterstallig onderhoud is niet gedekt. Wanneer er al losse delen waren, kan de verzekeraar daarnaar verwijzen.</p>';
  if(st==='onbekend')h+='<p><b>Aandachtspunt.</b> Zonder recent inspectierapport is de staat van het dak voor de storm lastig aan te tonen. Foto\'s van eerdere jaren helpen daarbij.</p>';
  if(wat==='boom')h+='<p>Bij schade door een omgevallen boom speelt ook de vraag wie eigenaar is van de boom en of er sprake was van gebrekkig onderhoud. Dat loopt via een andere dekking dan storm.</p>';
  if(wat==='lek')h+='<p>Water binnen na een storm vraagt eerst een noodherstel om het dakvlak dicht te maken, en pas daarna definitief herstel.</p>';
  if(wat==='plat')h+='<p>Bij een opgewaaid plat dak is de vraag of het randprofiel en de kleefverbinding intact waren. Dat bepaalt of het als stormschade of als gebrek wordt aangemerkt.</p>';
  h+='<h3 style="margin-top:16px">Stappen</h3><ol>'+
     '<li>Wachten tot het veilig is en de omgeving afzetten.</li>'+
     '<li>Vanaf de grond fotograferen, ook de afgewaaide delen waar ze liggen.</li>'+
     '<li>Zolder en plafonds nakijken op vochtplekken.</li>'+
     '<li>De verzekeraar melden en een noodherstel laten uitvoeren.</li>'+
     '<li>Geen definitief herstel laten uitvoeren voor de vaststelling, tenzij de situatie onveilig is.</li>'+
     '</ol><p class="small">Indicatie. De polisvoorwaarden van de eigen woonhuisverzekering blijven bepalend.</p>';
  out.innerHTML=h;
 }
 f.addEventListener('input',calc); f.addEventListener('change',calc); calc();

 var g=document.getElementById('pr'), o2=document.getElementById('prout');
 function w(n){return g.querySelector('[name="'+n+'"]').value;}
 function eur(x){return x.toLocaleString('nl-NL',{minimumFractionDigits:0,maximumFractionDigits:0});}
 function calc2(){
  var m2=parseFloat(w('m2')), aantal=w('aantal'), mat=w('materiaal'),
      rd=parseFloat(w('rd')), vent=w('vent');
  if(isNaN(m2)||m2<0)m2=0; if(isNaN(rd)||rd<0)rd=0;
  var h='';
  if(m2<20){
   h+='<p class="verdict">Oppervlakte te klein</p><p>De ISDE stelt een minimum van 20 vierkante meter dakisolatie. Onder dat oppervlak volgt geen subsidie.</p>';
   o2.innerHTML=h;return;
  }
  if(rd<3.5){
   h+='<p class="verdict"><span class="tag hi">Rd-waarde te laag</span></p><p>De ISDE vraagt een Rd-waarde van minimaal 3,5 vierkante meter kelvin per watt voor het nieuw aangebrachte materiaal. Bij '+rd.toString().replace('.',',')+' wordt daar niet aan voldaan en volgt geen subsidie.</p>';
   o2.innerHTML=h;return;
  }
  var subs=Math.min(m2,200);
  var tarief = (aantal==='2') ? 32.50 : 16.25;
  var bonus = (mat==='biobased') ? 5 : 0;
  var bedrag = subs*(tarief+bonus);
  var ventbedrag = (vent==='ja') ? 400 : 0;
  h+='<p class="verdict">Indicatie: '+eur(Math.round(bedrag+ventbedrag))+' euro</p>';
  h+='<div class="tablewrap"><table><tr><th>Onderdeel</th><th>Berekening</th><th>Bedrag</th></tr>';
  h+='<tr><td>Dakisolatie</td><td>'+subs+' m&sup2; x '+tarief.toFixed(2).replace('.',',')+' euro</td><td>'+eur(Math.round(subs*tarief))+' euro</td></tr>';
  if(bonus)h+='<tr><td>Biobased bonus</td><td>'+subs+' m&sup2; x 5,00 euro</td><td>'+eur(Math.round(subs*bonus))+' euro</td></tr>';
  if(ventbedrag)h+='<tr><td>Energiezuinige ventilatie</td><td>eenmalig</td><td>'+eur(ventbedrag)+' euro</td></tr>';
  h+='<tr><td><b>Totaal</b></td><td></td><td><b>'+eur(Math.round(bedrag+ventbedrag))+' euro</b></td></tr></table></div>';
  if(m2>200)h+='<p class="small">Boven 200 vierkante meter telt het meerdere niet mee. Er is gerekend met 200 vierkante meter.</p>';
  if(aantal==='1'){
   var extra=subs*(32.50+bonus)+ventbedrag-(bedrag+ventbedrag);
   h+='<p><b>Bij een tweede maatregel</b> verdubbelt het tarief naar 32,50 euro per vierkante meter. Dat scheelt in dit geval '+eur(Math.round(extra))+' euro. De tweede maatregel moet binnen 24 maanden na de eerste zijn uitgevoerd.</p>';
  }
  h+='<h3 style="margin-top:16px">Voorwaarden</h3><ul>'+
     '<li>Rd-waarde van het nieuwe materiaal minimaal 3,5 vierkante meter kelvin per watt.</li>'+
     '<li>Minimaal 20 en maximaal 200 vierkante meter subsidiabel.</li>'+
     '<li>Aanvragen binnen 24 maanden na uitvoering.</li>'+
     '<li>Uitvoering door een bouwbedrijf, met een factuur waarop de oppervlakte en de Rd-waarde staan.</li>'+
     '</ul>';
  h+='<p class="small">Indicatie op basis van de gepubliceerde ISDE-bedragen voor 2026. De toekenning gebeurt door RVO op basis van het dossier, en het budget is eindig.</p>';
  o2.innerHTML=h;
 }
 g.addEventListener('input',calc2); g.addEventListener('change',calc2); calc2();
})();
"""


def _storm():
    _tool_page("stormschade-en-subsidiecheck", "Stormschade- en subsidiecheck voor het dak",
               "Nagaan of een storm de drempel van windkracht 7 haalde die verzekeraars hanteren, en berekenen wat de ISDE-subsidie voor dakisolatie in 2026 oplevert.",
               STORM_BODY, STORM_JS)
