import os

import pandas as pd
from dune_client.client import DuneClient
from dune_client.types import QueryParameter
from dune_client.query import QueryBase


dune = DuneClient.from_env()


def get_upkeeps(chain="ethereum"):
    query = QueryBase(
        name="@gosuto/cla_chain_upkeeps",
        query_id=3889683,
        params=[
            QueryParameter.enum_type(name="chain", value=chain),
        ],
    )
    print(f"Querying upkeeps for {chain}")
    return dune.run_query_dataframe(query)


if __name__ == "__main__":
    dfs = []
    for chain in [
        "ethereum",
        "arbitrum",
        "polygon",
        "optimism",
        "avalanche_c",
        "base",
        "gnosis",
    ]:
        dfs.append(get_upkeeps(chain))
    os.makedirs("../../out", exist_ok=True)
    pd.concat(dfs).to_csv("../../out/upkeeps.csv", index=False)
