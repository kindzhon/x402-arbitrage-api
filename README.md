# x402 Arbitrage API System

Monetized API endpoints with x402 payment protocol for arbitrage services.

## Services

### 1. Website Analysis ($0.05)
```bash
POST /api/website-analysis
{"url": "https://example.com"}
```

### 2. Crypto Analysis ($0.12)
```bash
POST /api/crypto-analysis
{"symbol": "BTC"}
```

### 3. Contract Safety ($0.01)
```bash
POST /api/contract-safety
{"address": "0x..."}
```

## Pricing

| Service | Cost | Price | Margin |
|---------|------|-------|--------|
| Website Analysis | $0.05 | $0.15 | 200% |
| Crypto Analysis | $0.12 | $0.30 | 150% |
| Contract Safety | $0.01 | $2.00 | 19,900% |

## Installation

```bash
pip install -r requirements.txt
python xiaomiao-simple-api.py
```

## API Endpoints

- `GET /` - API info
- `GET /api/health` - Health check
- `GET /api/pricing` - Pricing info
- `POST /api/website-analysis` - Website metadata
- `POST /api/crypto-analysis` - Crypto prices + analysis
- `POST /api/contract-safety` - Smart contract audit

## License

MIT
