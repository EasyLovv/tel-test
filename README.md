# Test task.
* Part 1 a scrapper, located in 'scrapper' folder, based on celery
* Part 2 the backend, located in 'backend' folder, based on flask
* Part 3 was skipped

## How to launch:
1. create the .env file in the project root directory, use provided '.env.example' as a template
2. call docker-compose up command, scrapper will start to scrap the nba page and 
"put" the scores in the database via rest api, implemented in 'backend' project.
3. for testing you could change the file 'scrapper/periodic/scrap_nba.py:57' line
 
## API

There are 2 endpoints implemented:
1. All Games endpoint.
 * GET http://localhost:8000/games - return all games in the database
 * GET http://localhost:8000/games?team_name=Lakers - get all games with the team "Lakers"
2. Single Game endpoint:
 * GET http://localhost:8000/games/401161002 - get the game with specific id "401161002"
 * PUT http://localhost:8000/games/401161002 - create or update the game with specific id "401161002" (requires API_KEY)
 