# Documentación  para SportsWorldCentral(SWC) Futbol de fantasía

Gracias por usar la API de SportsWorldCentral. Este es tu lugar único para acceder a los datos de nuestro sitio web de fútbol fantasy, www.sportsworldcentral.com.

## Indice

-[Public API] (#public-api)
-[Getting Started](#getting-started)
    - [Analytics](#analytics)
    - [Player](#player)
    - [Scoring](#scoring)
    - [Memebership](#memebership)
-[Terms of Services](#terms-of-service)
-[Example Code] (#example-code)
-[Software Development Kit (SDK)](#software-development-kit-sdk)

## Public API
*Muy pronto*

Gracias por usar la API de SportsWorldCentral. Este es tu lugar único para acceder a los datos de nuestro sitio web de fútbol fantasy, www.sportsworldcentral.com.

## Comienzo
Como todos los datos son públicos, la API de SWC no requiere ninguna autenticación. Todos los siguientes datos están disponibles usando endpoints GET que devuelven datos JSON

### Analytics
Obtén información sobre la salud del API y el conteo de ligas, equipos y jugadores

### Player
Puedes obtener una lista de todos los jugadores de la NFL, o buscar a un jugador individual por su player_id.

### Scoring

Puedes obtener una lista de actuaciones de jugadores de la NFL, incluidos los puntos de fantasía que lograron usando la puntuación de la liga SWC.

### Memebership
Obtén información sobre todas las ligas de fútbol fantasy de la SWC y los equipos que hay en ellas

## Terms of Services
Al usar la API, aceptas los siguientes términos de servicio:

## Example Code
Aquí hay un ejemplo de código en Python para acceder al endpoint de verificación de salud:

...
import httpx

HEALTH_CHECK_ENDPOINT = "/"

with httpx.Client(base_url=self.swc_base_url) as client:
    response = client.get(self.HEAD_CHECK_ENDPOINT)
    print(response.json())
...

## Software Development Kit(SDK)
*Pronto*

Este pendiente por el kit escrito en python para la API


