from moralis import evm_api

api_key = "ZzBsfl8N1zg1e1aEhspJakIGPez8RaHhkCkg4pZzhZBQDTEa8OSZtyPJ9MTBHess"
params = {
    "address": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "chain": "eth"
}

result = evm_api.token.get_token_price(
    api_key=api_key,
    params=params,
)

print(result)