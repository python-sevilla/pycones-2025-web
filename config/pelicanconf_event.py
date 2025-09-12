# -*- coding: utf-8 -*-
import json
import random


def load_json_from_data(filename):
    with open(f"./data/{filename}", "r", encoding="utf-8") as file:
        return json.load(file)


JOBS = load_json_from_data("jobs.json")
TEAM = load_json_from_data("team.json")
VOLUNTEERS = load_json_from_data("volunteers.json")
PAST_EDITIONS = load_json_from_data("past_editions.json")
SPONSORS = load_json_from_data("sponsors.json")
ADDONS = load_json_from_data("add-ons.json")
KEYNOTERS = load_json_from_data("keynoters.json")
ORGANIZERS = load_json_from_data("organizers.json")
FILA0 = load_json_from_data("fila0.json")
EVENT_TITLE = "PyConES 2025"
EVENT_SUBTITLE = "Sevilla"
EVENT_DESCRIPTION_MINI = "PyConES, la conferencia de Python más importante de España"
EVENT_DESCRIPTION = """
🚀 ¡Llega PyConES, el gran evento de Python en España! 🐍

Forma parte de la mayor conferencia nacional de Python, donde cientos de entusiastas, profesionales y empresas se reúnen para compartir conocimientos, inspirarse y hacer comunidad.
<br>
📅 Charlas de alto nivel, talleres prácticos y networking con los mejores del sector.
💡 Descubre oportunidades profesionales únicas y lleva tus habilidades al siguiente nivel.
🤝 ¿Tienes una empresa? Conviértete en patrocinador y consigue una visibilidad inigualable en el corazón de la comunidad Python.

🎟️ ¡No te lo pierdas! Únete a la revolución Python en PyConES. ¡Te esperamos!
"""


YOUTUBE_LINK = "https://www.youtube.com/PythonEspa%C3%B1aOficial"
GITHUB_LINK = "https://github.com/python-spain"
EMAIL_LINK = "mailto:contacto@2025.es.pycon.org"
LINKEND_LINK = (
    "https://es.linkedin.com/company/python-espa%C3%B1a?trk=public_post_feed-actor-name"
)

INSTAGRAM_LINK = "https://www.instagram.com/pycon_es/"
BLUESKY_LINK = "https://web-cdn.bsky.app/profile/did:plc:irbbd7hhbmqhoklzmlfx2sju"
MASTODON_LINK = None
TELEGRAM_LINK = None
TWITTER_LINK = None


TICKETS_LINK = "/tickets.html"
PRETIX_TICKETS_LINK = "https://pretix.eu/python-spain/pycones-2025/"


CALL_FOR_PAPERS_LINK = "https://pretalx.com/pycones-2025/cfp"
SPONSORS_DOSSIER_ES = "/theme/files/[ES]PyConES25.pdf"
SPONSORS_DOSSIER_EN = "/theme/files/[EN]PyConES25.pdf"

# https://google-map-generator.com/
MAP_IFRAME_LINK = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3435.750650979095!2d-5.939984388292738!3d37.35524047197774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd126fada8bb9993%3A0xf1425beda6074232!2sUniversidad%20Pablo%20de%20Olavide%20Sevilla!5e0!3m2!1ses!2ses!4v1743432763703!5m2!1ses!2ses"

# https://cookie-bar.eu/
COOKIES_SCRIPT = None


MAILJET_IFRAME_URL = None
MAILJET_TOKEN = None

GOOGLE_PHOTOS_URL = "https://photos.app.goo.gl/k8Ruv1TDgnzSwC9w7"
GOOGLE_PHOTOS_TITLE = "PyCon ES 2025"
GOOGLE_PHOTOS_DESCRIPTION = "PyCon ES 2025"


WALLPAPERS = [
    "/theme/images/assets/fondo_oscuro.png",
]

SELECTED_WALLPAPER = random.choice(WALLPAPERS)

EVENT_DATE_STR = "Los días 17, 18 y 19 de octubre."

EVENT_WARNINGS = [
    # {
    #     "message": "En construcción 🛠️",
    #     "color": "is-danger",  # "is-warning, is-success, is-danger,  is-info"
    # }
]
