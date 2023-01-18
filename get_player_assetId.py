# First install:
# pip install gql[aiohttp]

import asyncio
import pandas as pd
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from pyparsing import null_debug_action

def make_string():
  player = "nic-claxton-19990417"
  year = "2022"
  version = "rare"
  card_num = "150"
  player_string = player + "-" + year + "-" + version + "-" + card_num
  return player_string


async def main():


    transport = AIOHTTPTransport(
        url="https://api.sorare.com/sports/graphql",
        # headers = {"Authorization": "Bearer <TheUserAccessToken>"}
    )

    async with Client(transport=transport) as session:
        
        query = gql("""  query GetNBACardsAssetIds($slugs: [String!]) {
    nbaCards(slugs: $slugs) {
      assetId
      player {
        displayName
      }
    }
  }""")
        player_string = make_string()
        query_variable = {"slugs": player_string}
        result = await session.execute(query, variable_values=query_variable)
        print(result)

asyncio.run(main())