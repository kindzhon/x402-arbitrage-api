# API 文档

## 基础信息

- **基础URL**: `http://127.0.0.1:5000`
- **认证**: Header中包含 `x-api-key: demo-key-123`
- **返回格式**: JSON

## 端点列表

### 1. 健康检查

**URL**: `/api/health`  
**方法**: `GET`

**响应示例**:
```json
{
  "status": "healthy",
  "service": "xiaomiao-arbitrage-api",
  "services_available": [
    "url_metadata",
    "crypto_prices",
    "market_intel",
    "web_scraper",
    "seo_meta",
    "contract_safety",
    "crypto_news",
    "agent_test"
  ],
  "services_count": 8
}
```

### 2. 定价信息

**URL**: `/api/pricing`  
**方法**: `GET`

**响应示例**:
```json
{
  "services": {
    "website_analysis": {
      "base_cost": 0.05,
      "suggested_price": 0.15,
      "profit_margin": 200,
      "description": "完整的SEO网站分析"
    },
    "crypto_analysis": {
      "base_cost": 0.12,
      "suggested_price": 0.30,
      "profit_margin": 150,
      "description": "加密市场全景分析"
    },
    "contract_safety": {
      "base_cost": 0.01,
      "suggested_price": 2.00,
      "profit_margin": 19900,
      "description": "DeFi智能合约安全审计"
    }
  }
}
```

### 3. 网站分析

**URL**: `/api/website-analysis`  
**方法**: `POST`  
**认证**: 需要

**请求参数**:
```json
{
  "url": "https://example.com"
}
```

**响应示例**:
```json
{
  "url": "https://example.com",
  "service_type": "website_analysis",
  "suggested_retail_price": 0.15,
  "profit_margin": 200,
  "analysis": {
    "seo_score": "B+",
    "loading_time": "<2s",
    "mobile_friendly": true,
    "ssl_enabled": true,
    "recommendations": [
      "优化元描述",
      "添加结构化数据",
      "改善移动体验"
    ]
  },
  "status": "demo"
}
```

### 4. 加密分析

**URL**: `/api/crypto-analysis`  
**方法**: `GET`  
**认证**: 需要

**响应示例**:
```json
{
  "service_type": "crypto_analysis",
  "suggested_retail_price": 0.30,
  "profit_margin": 150,
  "analysis": {
    "market_status": "bullish",
    "top_cryptos": {
      "BTC": {"price": "$45,230", "change": "+2.5%"},
      "ETH": {"price": "$2,890", "change": "+1.8%"},
      "SOL": {"price": "$102", "change": "+4.2%"}
    },
    "trading_opportunities": ["BTC突破45,000阻力位"],
    "risk_factors": ["监管政策变化"]
  },
  "status": "demo"
}
```

### 5. 合约安全审计

**URL**: `/api/contract-safety`  
**方法**: `POST`  
**认证**: 需要

**请求参数**:
```json
{
  "contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1"
}
```

**响应示例**:
```json
{
  "contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1",
  "service_type": "contract_safety",
  "suggested_retail_price": 2.00,
  "profit_margin": 19900,
  "security_analysis": {
    "risk_score": "B+",
    "rug_pull_risk": "低风险",
    "ownership_status": "已放弃",
    "liquidity_lock": "已锁定",
    "overall_rating": "6.5/10"
  },
  "status": "demo"
}
```

## 错误处理

### 错误响应格式
```json
{
  "error": "错误描述",
  "status": "failed"
}
```

### 常见错误码
- `400`: 请求参数错误
- `401`: 认证失败
- `404`: 端点不存在
- `500`: 服务器内部错误

## 测试示例

### cURL

```bash
# 健康检查
curl http://127.0.0.1:5000/api/health

# 网站分析
curl -X POST http://127.0.0.1:5000/api/website-analysis \
  -H "Content-Type: application/json" \
  -H "x-api-key: demo-key-123" \
  -d '{"url": "https://example.com"}'

# 加密分析
curl -H "x-api-key: demo-key-123" http://127.0.0.1:5000/api/crypto-analysis

# 合约安全审计
curl -X POST http://127.0.0.1:5000/api/contract-safety \
  -H "Content-Type: application/json" \
  -H "x-api-key: demo-key-123" \
  -d '{"contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1"}'
```

### Python

```python
import requests

BASE_URL = "http://127.0.0.1:5000"
HEADERS = {"x-api-key": "demo-key-123"}

# 健康检查
response = requests.get(f"{BASE_URL}/api/health")
print(response.json())

# 网站分析
data = {"url": "https://example.com"}
response = requests.post(f"{BASE_URL}/api/website-analysis", 
                         json=data, headers=HEADERS)
print(response.json())
```

## 速率限制

当前演示版本无速率限制。生产环境建议：
- 免费用户：100次/小时
- 付费用户：1000次/小时
- 企业用户：无限制