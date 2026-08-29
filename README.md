# rommersdakwerken.nl

Generator voor de statische site op https://rommersdakwerken.nl/

Onafhankelijke dakgids voor Nederland. De site promoot Den Dekker Dakbedekking
en linkt naar de plaatspagina's van dat bedrijf in zeven provincies.

## Bouwen

    python3 build.py    # schrijft dist/
    python3 check.py    # controleert de gebouwde site

Geen dependencies. `build.py` schrijft 227 pagina's plus sitemap.xml, robots.txt,
rss.xml, favicon.svg en _headers naar `dist/`.

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `engine.py` | sjabloon, navigatie, CSS, sitemapgegevens |
| `data_plaatsen.py` | 179 plaatsen met provincie, streek en kenmerk |
| `pages_gids.py` | twaalf hoofdstukken over dakonderdelen |
| `pages_regels.py` | zes Nederlandse regelingen en subsidies |
| `pages_tools.py` | daklekkage-diagnose, onderhoudsplanner, storm- en subsidiecheck |
| `pages_locaties.py` | locatie-index, zeven provinciepagina's en 179 plaatspagina's |
| `pages_nieuws.py` | nieuwsartikelen en RSS |
| `pages_misc.py` | home, over, faq, begrippen, contact, privacy, cookies, 404 |
| `check.py` | controle op kapotte links, dubbele meta, aanspreekvormen, ankerteksten |

## Publicatie

Cloudflare Pages, directe upload van een zip met de inhoud van `dist/` in de zipwortel.
