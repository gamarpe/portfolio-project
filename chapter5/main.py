"""FastAPI program - Chapter 4"""

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date

import crud, schemas
from database import SessionLocal

app = FastAPI()
api_description = """
Esta API ofrece acceso de solo  lectura a la información de la API de Fantasy Football de SportsWorldCentral (SWC). Los endpoints están agrupados en las siguientes categorías: 
## Analytics 
Obtén información sobre la salud de la API y el conteo de ligas, equipos y jugadores.

## Player 
Puedes obtener una lista de jugadores de la NFL o buscar a un jugador individual por su player_id.
 
## Score
Puedes obtener una lista de actuaciones de jugadores de la NFL, incluyendo los puntos de fantasía que anotaron usando la puntuación de la liga SWC.
 
## Membership 
Obtén información sobre todas las ligas de fantasy football de SWC y los equipos que hay en ellas.
"""

# Constructor de FastAPI con detalles adicionales añadidos para la Especificación OpenAPI

app = FastAPI(
    description=api_description,
    title="API de Futbol de fantasía de Sports World Central",
    version="0.1",
)


# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    "/",
    summary="Verifica el estado de la API de Futbol de Fantasía SWC",
    tags=["analytics"],
)
async def root():
    return {"message": "API en buen estado"}


@app.get(
    "/v0/players/",
    response_model=list[schemas.Player],
    summary="Obten los nombre de los jugadores que coinciden con tus parametros de busqueda",
    tags=["player"],
)
def read_players(
    skip: int = Query(
        0,
        description="El número de elementos que se deben omitir al inicio de la llamada API",
    ),
    limit: int = Query(
        100,
        description="El número de registros a devolver después de los registros saltados",
    ),
    minimum_last_changed_date: date = Query(
        None,
        description="La fecha mínima de cambio que quieres para devolver registros. Excluye cualquier registro cambiado antes de la fecha fijada",
    ),
    first_name: str = Query(None, description="Nombre de pila del jugador"),
    last_name: str = Query(None, description="Apellido del jugador"),
    db: Session = Depends(get_db),
):
    players = crud.get_players(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        first_name=first_name,
        last_name=last_name,
    )
    return players


@app.get(
    "/v0/players/{player_id}",
    response_model=schemas.Player,
    summary="Obtén un jugador usando el ID de jugador, que es interno de SWC",
    description="Si tienes un ID de jugador SWC de un jugador de otra llamada de API como v0_get_players, puedes llamar a esta API usando el ID del jugador",
    response_description="Un jugador de la NFL",
    operation_id="v0_get_players_by_player_id",
    tags=["player"],
)
def read_player(player_id: int, db: Session = Depends(get_db)):
    player = crud.get_player(db, player_id=player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return player


@app.get(
    "/v0/performances/",
    response_model=list[schemas.Performance],
    summary="Obten estadisticas de rendimiento semanales segun parametros de busqueda",
    tags=["scoring"],
)
def read_performances(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    db: Session = Depends(get_db),
):
    performances = crud.get_performances(
        db, skip=skip, limit=limit, min_last_changed_date=minimum_last_changed_date
    )
    return performances


@app.get(
    "/v0/leagues/{league_id}",
    response_model=schemas.League,
    summary="Obten una liga por su descritor numerico id",
    tags=["memebership"],
)
def read_league(league_id: int, db: Session = Depends(get_db)):
    league = crud.get_league(db, league_id=league_id)
    if league is None:
        raise HTTPException(status_code=404, detail="Liga no encontrada")
    return league


@app.get(
    "/v0/leagues/",
    response_model=list[schemas.League],
    summary="Obten todas las ligas de futbol de fantasia SWC segun parametros de busqueda ",
    tags=["memebership"],
)
def read_leagues(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    league_name: str = None,
    db: Session = Depends(get_db),
):
    leagues = crud.get_leagues(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        league_name=league_name,
    )
    return leagues


@app.get(
    "/v0/teams/",
    response_model=list[schemas.Team],
    summary="Obten todos los euipos de Futbol de fantasía segun parametros de busqueda",
    tags=["memebership"],
)
def read_teams(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    team_name: str = None,
    league_id: int = None,
    db: Session = Depends(get_db),
):
    teams = crud.get_teams(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        team_name=team_name,
        league_id=league_id,
    )
    return teams


@app.get(
    "/v0/counts/",
    response_model=schemas.Counts,
    summary="Obten algunos datos numéricos relativos a ligas, equipo y jugadores  en futbol de fantasís SWC",
    tags=["analytics"],
)
def get_count(db: Session = Depends(get_db)):
    counts = schemas.Counts(
        league_count=crud.get_league_count(db),
        team_count=crud.get_team_count(db),
        player_count=crud.get_player_count(db),
    )
    return counts
