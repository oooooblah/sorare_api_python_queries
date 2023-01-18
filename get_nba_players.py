# First install:
# pip install gql[aiohttp]

import asyncio
import pandas as pd
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport



async def main():


    transport = AIOHTTPTransport(
        url="https://api.sorare.com/sports/graphql",
        # headers = {"Authorization": "Bearer <TheUserAccessToken>"}
    )

    async with Client(transport=transport) as session:
        
        query = gql(
            """
            query nbaRoster($teamslug: String!) {
  nbaTeam(slug: $teamslug){
    
    id
    players{
      id
      slug
      age
      displayName
      team{
        name
      }
    }
  }
}
        """
        )

        list_one = ["atlanta-hawks","boston-celtics","brooklyn-nets","charlotte-hornets","chicago-bulls","cleveland-cavaliers","dallas-mavericks","denver-nuggets","detroit-pistons","golden-state-warriors","houston-rockets","indiana-pacers","la-clippers","los-angeles-lakers","memphis-grizzlies","miami-heat","milwaukee-bucks","minnesota-timberwolves","new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder","orlando-magic","philadelphia-76ers","phoenix-suns","portland-trail-blazers","sacramento-kings","san-antonio-spurs","toronto-raptors","utah-jazz","washington-wizards"]
        list_names =[]
        list_teams = []
        list_slugs = []
        for i in list_one:
          string3 = {"teamslug": i}
          result = await session.execute(query, variable_values=string3)

          for card in result["nbaTeam"]["players"]:
            list_names.append(card["displayName"])
            list_teams.append(card["team"]["name"])
            list_slugs.append(card["slug"])
        data = {'playerName': list_names, 'Team': list_teams, 'slug': list_slugs}
        df = pd.DataFrame(data)
        print(df)




asyncio.run(main())