# Závěrečná práce
## Databáze v djangu - Povinná četba
Jako závěrečný projekt jsem si vybral udělat databázi v Djangu. Techno projekt jsem si vybral, protože mě zaujala práce s databázemi. Chtěl bych se pokusit sestrojit funkční web s povinnou četbou na maturity, kde by si studenti a zájemci mohli rozvíjet své dovednosti pomocí kvízů a dalších možností. 
### Cíle
- Možnost vybírat z několika autorů a knih
- Přehledné prostředí
- Snadný přístup k informacím
- Vytvořit kvízy
- Použitelnost pro vzdělání
- Register a login systém

### Autor
- Lukáš Kůžel
### Konzultanti
- Mgr. Marek Lučný

### Technologie
- Django
- Python
- HTML, CSS
- MySQL
- Bootstrap

### Časový harmonogram a postup
#### Zaří - 4h
- Vymýšlení závěrčného projektu 
- Vytváření modelu databáze
#### Říjen -24h
- 12.10. Vytváření modelů, opakování Djanga (6h)
- 15.10. Úpravy startapss (1h)
- 16.10. Editace stránek (2h 30m)
- 21.10. Html stránky (5h)
- 27.10. Kompatibilita(6h)
- 28.10. Úprava (1h30m)
- 29.10. Úprava (2h)
#### Listopad (26h 30m)
- 1.11. Editace (30m)
- 4.11. Frontend Improvement (6h)
- 5.11. Ukládání souborů (3h)
- 13.11. Templates detail (2h)
- 17.11. Úprava hlavní stránky a url odkazů na detaily(4h 30m)
- 18.11. Login/Register startapp (3h)
- 21.11. Login/Register (2h)
- 25.11. Login/Register (4h)
- 28.11. Login/Register-messages (1h30m)
#### Prosinec
- 3.12. Login/Register-email (3h30m)
- 6.12. Login/Register-If statements (3h)
- 8.12. Login/Register-If login/forms (2h 30m)
- 10.12. Login/Register- Everyching changed (5h)
- 12.12. Login/Register- Making funcional(Login with email) (2h)
- 15.12. Profile Edit (8h 30m)
- 17.12. Profile (2h 30m)
- 18.12. Review (4h)
- 21.12. Review (9h)
- 23.12. Editing (7h)
- 24.12. Bootstrap (9h)
#### Leden ()
- 3.1. Updating-Century (2h)
- 6.1. Search bar (2h)
- 11.1. Searching (3h)
- 12.1. Editing (2h)


- V příkazovém řádku si vlezeme do složky databáze a napíšeme příkazy pro přidání superuživatele.
- docker exec -it [jmenodatabaze] bash
- python manage.py createsuperuser
- Načíst data
- python manage.py loaddata saved.json

### Odkazy
| https://docs.djangoproject.com/en/4.1/ref/applications/ |
| https://django.fun/en/qa/427054/ |
| https://stackoverflow.com/questions/20878929/css-html-putting-up-a-text-label-on-my-image |
| https://blog.hubspot.com/website/css-margin-vs-padding |
| https://techflow360.com/how-to-perform-django-form-validation-with-regex/ |
| https://docs.djangoproject.com/en/4.1/ref/forms/validation/ |
| https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms |
| https://stackoverflow.com/questions/22989515/bootstrap-add-margin-padding-space-between-columns |
| https://getbootstrap.com/docs/4.0/layout/grid/ |
| https://css-tricks.com/logic-in-css-media-queries/ |
| https://www.tangowithdjango.com/book17/chapters/login.html |
| https://dontrepeatyourself.org/post/django-custom-user-model-extending-abstractuser/ |
| https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy | 
| https://www.youtube.com/watch?v=F6qUfnqZFAE |
| https://www.youtube.com/watch?v=R6-pB5PAA6s |
| https://stackoverflow.com/questions/39652109/django-filtering-inside-of-get-context-data |

### Zdroje
| Informace o autorovi: Karel Čapek. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Karel_Čapek |
| Informace o knize: Válka s mloky. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Válka_s_Mloky |
| Informace o knize: RUR. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/R.U.R. |
| Informace o autorovi: Boris Strugackij. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Boris_Strugackij |
| Informace o autorovi: Arkadij Strugackij. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Arkadij_Strugackij |
| Informace o knize: Piknik u cesty. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Piknik_u_cesty |
| Informace o autorovi: George R. R. Martin. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/George_R._R._Martin |
| Informace o autorovi: Andrzej Sapkowski. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Andrzej_Sapkowski | 
| Informace o autorovi: John Ronald Reuel Tolkien. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/John_Ronald_Reuel_Tolkien |
| Informace o knize: Hobit aneb Cesta tam a zase zpátky. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Hobit_aneb_Cesta_tam_a_zase_zpátky |
| Informace o knize: Hra o trůny. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Hra_o_trůny |
| Informace o knize: Poslední přání. Wikipedie [online]. - [cit. 2022-12-24]. Dostupné z: https://cs.wikipedia.org/wiki/Poslední_přání |

| Obrázek Knih [online]. -: -, - [cit. 2022-11-17]. Dostupné z: https://thecommuniquechs.com/2552/opinion/what-is-the-best-book-genre/ |
