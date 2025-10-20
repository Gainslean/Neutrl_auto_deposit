import json

WETH_ADDRESS = '0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'
HYPERLANE_NFT_ADDRESS = '0x7daC480d20f322D2ef108A59A465CCb5749371c4'

token = {
    'usde': "0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34",
    'meth': "0xcDA86A272531e8640cD7F1a92c01839911B90bb0",
    'Base': "Base",
    'Polygon': "Polygon",
    'Ethereum': "Ethereum",
    'Avalance': "Avalance",
    'Zora': "Zora",
    'Berachain': "Berachain",
    'BNB': "BNB",
    'Scroll': "Scroll",
    'Abstract': "Abstract",
    'Karak': "Karak"
}


chain_name = {
    'Arbitrum': "Arbitrum",
    'Optimism': "Optimism",
    'Base': "Base",
    'Polygon': "Polygon",
    'Ethereum': "Ethereum",
    'Avalance': "Avalance",
    'Zora': "Zora",
    'Berachain': "Berachain",
    'BNB': "BNB",
    'Scroll': "Scroll",
    'Abstract': "Abstract",
    'Karak': "Karak"
}

rpc_url = {
    'Arbitrum': "https://rpc.ankr.com/arbitrum",
    'Optimism': "https://rpc.ankr.com/optimism",
    'Base': "https://rpc.ankr.com/base",
    'Polygon': "https://rpc.ankr.com/polygon",
    'Ethereum': "https://rpc.ankr.com/eth",
    'Avalance': "https://rpc.ankr.com/avalanche",
    'Scroll': "https://rpc.ankr.com/scroll",
    'Abstract': "https://api.mainnet.abs.xyz",
    'Mantle': "https://rpc.ankr.com/mantle",
    'Berachain': "https://berachain.leakedrpc.com",
    'BNB': "https://rpc.ankr.com/bsc",
    'Zora': "wss://zora.drpc.org",
    'Karak': "https://rpc.karak.network"
}

explorer_url = {
    'Arbitrum': "https://arbiscan.io/",
    'Optimism': "https://optimistic.etherscan.io/",
    'Base': "https://basescan.org/",
    'Scroll': "https://scrollscan.org/",
    'Polygon': "https://polygonscan.com/",
    'Ethereum': "https://etherscan.io/",
    'Avalance': "https://www.oklink.com/ru/avax/",
    'Mantle': "https://explorer.mantle.xyz/",
    'Abstract': "https://abscan.org/",
    'Berachain': "https://berachain.leakedrpc.com",
    'BNB': "https://api.mainnet.abs.xyz",
    'Zora': "https://zora.drpc.org",
    'Karak': "https://explorer.karak.network "
}

Chain_id = {
    'Ethereum': 1,
    'Optimism': 10,
    'Arbitrum': 42161,
    'Base': 8453,
    'Polygon': 137,
    'Linea': 59144,
    'Blast': 81457,
    'Mantle': 5000,
    'Avalance': 43114,
    'Abstract': 2741,
    'Scroll': 534352,
    'Berachain': 80094,
    'BNB': 56,
    'Zora': 7777777,
    'Karak': 2410
    }



COMPAD_CONTRACTS = {
    'Arbitrum': {
        'native': "0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb",
        'pool': "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
        'aawETH': "0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8"
    },
    'Base': {
        'native': "0x46e6b214b524310239732D51387075E0e70970bf",
        'pool': "0x729b3EA8C005AbC58c9150fb57Ec161296F06766",
        'aawETH': "0xD4a0e0b9149BCee3C920d2E00b5dE09138fd8bb7"
    }
}


AAVE_CONTRACTS = {
    'Arbitrum': {
        'native': "0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb",
        'pool': "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
        'aawETH': "0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8"
    },
    'Base': {
        'native': "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5",
        'pool': "0x729b3EA8C005AbC58c9150fb57Ec161296F06766",
        'aawETH': "0xD4a0e0b9149BCee3C920d2E00b5dE09138fd8bb7"
    }
}

ETH_MASK = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

TOKENS_PER_CHAIN = {
    'Arbitrum': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "USDC.e": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "ZRO": "0x6985884C4392D348587B19cb9eAAf157F13271cd",
    },
    'Optimism': {
        "ETH": "0x4200000000000000000000000000000000000006", #0x4200000000000000000000000000000000000006
        "USDC": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85"
    },
    'Ethereum': {
        "ETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    },
    'zkSync': {
        "ETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        "WETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        "USDT": "0x493257fD37EDB34451f62EDf8D2a0C418852bA4C",
        "USDC.e": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"
    },
    'Base': {
        "USDC": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
        "ETH": "0x4200000000000000000000000000000000000006"
    }
}

USDC = {
    'Arbitrum': "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
    'Optimism': "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
    'Base': "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    'Polygon': "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
    'Ethereum': "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    'Avalance': "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E"
    }

PENDLE_ROUTER_ABI = [
  {
    "inputs": [
      {"internalType": "address","name":"router","type":"address"},
      {"internalType": "address","name":"market","type":"address"},
      {"internalType": "uint256","name":"minLpOut","type":"uint256"},
      {
        "components":[
          {"internalType":"uint256","name":"guessMin","type":"uint256"},
          {"internalType":"uint256","name":"guessMax","type":"uint256"},
          {"internalType":"uint256","name":"guessOffchain","type":"uint256"},
          {"internalType":"uint256","name":"maxIteration","type":"uint256"},
          {"internalType":"uint256","name":"eps","type":"uint256"}
        ],
        "internalType":"struct ApproxParams",
        "name":"approx",
        "type":"tuple"
      },
      {
        "components":[
          {"internalType":"address","name":"tokenIn","type":"address"},
          {"internalType":"uint256","name":"netTokenIn","type":"uint256"},
          {"internalType":"address","name":"tokenMintSy","type":"address"},
          {"internalType":"address","name":"pendleSwap","type":"address"},
          {
            "components":[
              {"internalType":"uint8","name":"swapType","type":"uint8"},
              {"internalType":"address","name":"extRouter","type":"address"},
              {"internalType":"bytes","name":"extCalldata","type":"bytes"},
              {"internalType":"bool","name":"needScale","type":"bool"}
            ],
            "internalType":"struct SwapData",
            "name":"swapData",
            "type":"tuple"
          }
        ],
        "internalType":"struct TokenInput",
        "name":"input",
        "type":"tuple"
      },
      {
        "components":[
          {"internalType":"address","name":"receiver","type":"address"},
          {"internalType":"uint256","name":"feeBps","type":"uint256"},
          {"internalType":"bytes[]","name":"permit2Data","type":"bytes[]"},
          {"internalType":"bytes[]","name":"signature","type":"bytes[]"},
          {"internalType":"string","name":"referralCode","type":"string"}
        ],
        "internalType":"struct Permit",
        "name":"permit",
        "type":"tuple"
      }
    ],
    "name":"addLiquiditySingleToken",
    "outputs":[{"internalType":"uint256","name":"lpOut","type":"uint256"}],
    "stateMutability":"payable",
    "type":"function"
  }
]

with open('abis/abi.json') as file:
    ERC20_ABI = json.load(file)


with open('abis/usdn.json') as file:
    USDN = json.load(file)
