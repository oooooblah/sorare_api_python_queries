# First install:
# pip install gql[aiohttp]

import asyncio
import pandas as pd
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from pyparsing import null_debug_action

player_assetId = "0x04000834edfe8c67ce6c8e1eae7526f7049c9f743e40b1e3b8014735a767e9e8"

#uncomment below variable "api_key" and put your api key in the string, then uncomment the "headers" variable in transport variable in async def main

# api_key = ""

async def main():


    transport = AIOHTTPTransport(
        url="https://api.sorare.com/graphql",
        
        # headers = {"APIKEY": api_key}
    )

    async with Client(transport=transport) as session:
        
        query = gql("""   query GetNBACardsPrices($assetIds: [String!]!) {
    tokens {
      nfts(
        assetIds: $assetIds
      ) {
        latestEnglishAuction {
          bestBid {
            amount
            amountInFiat { eur gbp usd }
          }
        }
      }
    }
  }""")
        
        query_variable = {"assetIds": player_assetId}
        result = await session.execute(query, variable_values=query_variable)
        print(result)

asyncio.run(main())