# sorare_api_python_queries
Python queries to Sorare's GraphQL API

The file get_nba_players.py iterates through all NBA teams and returns each players display name, team name, and "slug" in a pandas dataframe.

The file get_player_assetId.py returns a player's assetId, which can be used in the main Sorare API that gives more data such as auction history.

The file get_last_price.py returns the latest sale price using a player's assetId. It currently does not work without an API Key.

3 above queries are derived from resources within https://github.com/sorare/api
