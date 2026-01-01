# Fuhrpark Manager

Ein Django-basiertes Web-System zur digitalen Verwaltung von Fahrzeugflotten, Werkstatt-Terminen und Kostenkontrolle.

Entwickelt als Portfolio-Projekt, um komplexe Geschäftslogik und Prozessverwaltung in eine moderne Web-Architektur zu übersetzen.

## Über das Projekt
Der **Fuhrpark Manager** löst das Problem der unübersichtlichen Fahrzeugverwaltung. Anstatt Excel-Listen nutzt dieses System eine relationale Datenbank, um Fahrzeuge, deren Status (z. B. "Einsatzbereit", "Werkstatt") und anfallende Kosten zentral zu erfassen. 
Besonderer Fokus lag auf der **Backend-Logik** und der **Daten-Integrität**, inspiriert durch die Anforderungen an revisionssichere Dokumentation.

## Features
* **Fahrzeug-Verwaltung (CRUD):** Anlegen, Bearbeiten und Löschen von LKW/PKW-Datensätzen.
* **Status-Tracking:** Echtzeit-Übersicht über den Fahrzeugstatus (z. B. *In Werkstatt*, *Verfügbar*).
* **User-Authentifizierung:** Login-System für Disponenten/Verwalter (Django Auth).
* **Datenbank-Architektur:** Optimierte Relationen zwischen Fahrzeugen und Historie (SQLite/PostgreSQL ready).

## Tech Stack
* **Backend:** Python 3.x, Django 5.x
* **Datenbank:** SQLite (Entwicklung), bereit für PostgreSQL (Produktion)
* **Frontend:** HTML5, CSS3 (Bootstrap Integration planned)
* **Tools:** Git, Virtualenv

## Geplante Erweiterungen (Roadmap)
Ich arbeite aktiv an der Weiterentwicklung. Als nächstes geplant:
* [ ] **Dashboard:** Grafische Auswertung der monatlichen Kosten (Charts).
* [ ] **PDF-Export:** Automatische Erstellung von Wartungsberichten.
* [ ] **UI-Polish:** Farbliche Status-Indikatoren ("Ampel-System") für bessere Übersicht.

## Installation & Setup
Du kannst das Projekt lokal klonen und testen:

1.  **Repository klonen:**
    ```bash
    git clone [https://github.com/ogy796/fuhrpark_manager.git](https://github.com/ogy796/fuhrpark_manager.git)
    cd fuhrpark_manager
    ```

2.  **Virtuelle Umgebung erstellen & aktivieren:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Datenbank migrieren:**
    ```bash
    python manage.py migrate
    ```

5.  **Server starten:**
    ```bash
    python manage.py runserver
    ```
    Das System ist nun unter `http://127.0.0.1:8000/` erreichbar.

## Über den Entwickler
**Aspiring Software Developer**

Ich komme ursprünglich aus der Jura-Welt, habe aber gemerkt, dass mir das aktive Bauen von Lösungen mehr liegt als die Theorie. Dieses Projekt ist mein Beweis, dass ich komplexe Logik nicht nur verstehen, sondern auch programmieren kann. Es ist mein erstes großes Full-Stack Projekt.