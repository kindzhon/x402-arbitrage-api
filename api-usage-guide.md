# 📚 8个套利服务使用指南 - 完整教程

## 🎯 快速开始

### 🔑 API密钥
- **默认密钥：** `demo-key-123`
- **生产密钥：** 通过环境变量 `X402_API_KEY` 配置

### 🌐 服务地址
- **基本URL：** http://127.0.0.1:5000
- **API前缀：** `/api/`

---

## 📖 详细服务使用教程

### 1️⃣ **网站SEO分析服务** 📊
**端点：** `POST /api/website-analysis`

#### 请求示例：
```bash
curl -X POST http://127.0.0.1:5000/api/website-analysis \
  -H "Content-Type: application/json" \
  -H "x-api-key: demo-key-123" \
  -d '{
    "url": "https://example.com"
  }'
```

#### 请求参数：
```json
{
  "url": "https://example.com"  // 必需：目标网站URL
}
```

#### 预期响应：
```json
{
  "url": "https://example.com",
  "service_type": "website_analysis",
  "cost_breakdown": {
    "url_metadata": 0.01,
    "seo_meta": 0.02,
    "web_scraper": 0.02
  },
  "total_cost": 0.05,
  "suggested_retail_price": 0.15,
  "profit_margin": 200,
  "analysis": {
    "page_title": "示例网站的标题",
    "meta_description": "网站描述信息",
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

#### 使用场景：
- **SEO代理：** 为客户网站提供快速SEO审计
- **网站主：** 评估自己的网站SEO效果
- **数字营销：** 竞争对手分析

---

### 2️⃣ **加密市场分析服务** 📈
**端点：** `GET /api/crypto-analysis`

#### 请求示例：
```bash
curl -X GET "http://127.0.0.1:5000/api/crypto-analysis" \
  -H "x-api-key: demo-key-123"
```

#### 预期响应：
```json
{
  "timestamp": "2026-02-15T11:35:00",
  "service_type": "crypto_analysis",
  "cost_breakdown": {
    "crypto_prices": 0.01,
    "market_intelligence": 0.01,
    "daily_news": 0.10
  },
  "total_cost": 0.12,
  "suggested_retail_price": 0.30,
  "profit_margin": 150,
  "analysis": {
    "market_status": "bullish",
    "top_cryptos": {
      "BTC": {
        "price": "$45,230",
        "change_24h": "+2.5%",
        "volume_24h": "$28B"
      }
    },
    "sentiment": "中性偏多头",
    "key_news": [
      "比特币ETF流入创记录",
      "机构投资者持续增持"
    ],
    "trading_opportunities": [
      "BTC突破45,000阻力位",
      "ETH表现相对较弱，考虑套利"
    ],
    "risk_factors": [
      "监管政策变化",
      "技术分析显示超买"
    ]
  },
  "status": "demo"
}
```

#### 使用场景：
- **交易员：** 快速获取市场全景
- **投资者：** 制定投资决策
- **分析师：** 生成市场报告

---

### 3️⃣ **DeFi合约安全审计** 🛡️
**端点：** `POST /api/contract-safety`

#### 请求示例：
```bash
curl -X POST http://127.0.0.1:5000/api/contract-safety \
  -H "Content-Type: application/json" \
  -H "x-api-key: demo-key-123" \
  -d '{
    "contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1"
  }'
```

#### 请求参数：
```json
{
  "contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1"  // 必需：以太坊合约地址
}
```

#### 预期响应：
```json
{
  "contract_address": "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1",
  "service_type": "contract_safety",
  "cost_breakdown": {
    "contract_safety": 0.01,
    "market_intelligence": 0.01
  },
  "total_cost": 0.02,
  "suggested_retail_price": 2.00,
  "profit_margin": 9900,
  "security_analysis": {
    "risk_score": "B+",
    "rug_pull_risk": "低风险",
    "ownership_status": "已放弃",
    "liquidity_lock": "已锁定",
    "audit_status": "未审计",
    "vulnerabilities": [
      "缺少紧急暂停机制",
      "未使用重入攻击保护"
    ],
    "security_recommendations": [
      "实施紧急暂停机制",
      "添加重入攻击防护",
      "获得专业安全审计"
    ],
    "overall_rating": "6.5/10"
  },
  "market_data": {
    "tvl": "$1.2M",
    "holder_count": 234,
    "transaction_count_24h": 156
  },
  "status": "demo"
}
```

#### 使用场景：
- **DeFi投资者：** 评估项目安全性
- **项目方：** 自我安全审计
- **机构：** 投资决策支持

---

### 4️⃣ **健康检查** ✅
**端点：** `GET /api/health`

#### 请求示例：
```bash
curl -X GET "http://127.0.0.1:5000/api/health"
```

#### 预期响应：
```json
{
  "status": "healthy",
  "service": "xiaomiao-arbitrage-api",
  "timestamp": "2026-02-15T11:35:15",
  "services_available": [
    "website_analysis",
    "crypto_analysis", 
    "contract_safety"
  ],
  "version": "1.0.0",
  "uptime": "9h 35m"
}
```

#### 使用场景：
- 监控服务状态
- 集成测试
- 故障诊断

---

### 5️⃣ **定价查询** 💰
**端点：** `GET /api/pricing`

#### 请求示例：
```bash
curl -X GET "http://127.0.0.1:5000/api/pricing"
```

#### 预期响应：
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
      "description": "全面加密市场分析"
    },
    "contract_safety": {
      "base_cost": 0.02,
      "suggested_price": 2.00,
      "profit_margin": 9900,
      "description": "DeFi智能合约安全审计"
    }
  },
  "beta_discount": 0.5,
  "free_trial": true
}
```

#### 使用场景：
- 定价信息查询
- 成本结构分析
- 营销参考

---

## 🎯 Python集成示例

### 基础客户端类
```python
import requests
import json

class XiaomiaoClient:
    def __init__(self, api_key="demo-key-123", base_url="http://127.0.0.1:5000"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }
    
    def website_analysis(self, url):
        """网站SEO分析"""
        data = {"url": url}
        response = requests.post(f"{self.base_url}/api/website-analysis", 
                               json=data, headers=self.headers)
        return response.json()
    
    def crypto_analysis(self):
        """加密市场分析"""
        response = requests.get(f"{self.base_url}/api/crypto-analysis", 
                              headers=self.headers)
        return response.json()
    
    def contract_safety(self, contract_address):
        """DeFi合约安全审计"""
        data = {"contract_address": contract_address}
        response = requests.post(f"{self.base_url}/api/contract-safety",
                               json=data, headers=self.headers)
        return response.json()
    
    def health_check(self):
        """健康检查"""
        response = requests.get(f"{self.base_url}/api/health")
        return response.json()
    
    def pricing(self):
        """定价查询"""
        response = requests.get(f"{self.base_url}/api/pricing")
        return response.json()
```

### 使用示例
```python
# 创建客户端
client = XiaomiaoClient()

# 1. 网站SEO分析
print("=== 网站分析 ===")
result = client.website_analysis("https://example.com")
print(f"SEO得分：{result['analysis']['seo_score']}")
print(f"建议售价：${result['suggested_retail_price']}")

# 2. 加密市场分析
print("\n=== 加密分析 ===")
result = client.crypto_analysis()
print(f"市场状态：{result['analysis']['market_status']}")
print(f"投资机会：{result['analysis']['trading_opportunities']}")

# 3. DeFi安全审计
print("\n=== 合约审计 ===")
contract = "0x742d35Cc6634C0532925a3b8D4c9e96B4A7C5bF1"
result = client.contract_safety(contract)
print(f"风险评级：{result['security_analysis']['risk_score']}")
print(f"风险因子：{result['security_analysis']['rug_pull_risk']}")

# 4. 健康检查
print("\n=== 服务状态 ===")
result = client.health_check()
print(f"状态：{result['status']}")
print(f"可用服务：{result['services_available']}")

# 5. 定价信息
print("\n=== 定价信息 ===")
pricing = client.pricing()
for service, info in pricing['services'].items():
    print(f"{service}: ${info['base_cost']} → ${info['suggested_price']}")
```

---

## 🌐 前端集成示例

### JavaScript客户端
```javascript
class XiaomiaoAPIClient {
    constructor(apiKey = 'demo-key-123', baseURL = 'http://127.0.0.1:5000') {
        this.apiKey = apiKey;
        this.baseURL = baseURL;
        this.headers = {
            'Content-Type': 'application/json',
            'x-api-key': apiKey
        };
    }
    
    async websiteAnalysis(url) {
        const response = await fetch(`${this.baseURL}/api/website-analysis`, {
            method: 'POST',
            headers: this.headers,
            body: JSON.stringify({ url: url })
        });
        return await response.json();
    }
    
    async cryptoAnalysis() {
        const response = await fetch(`${this.baseURL}/api/crypto-analysis`, {
            method: 'GET',
            headers: this.headers
        });
        return await response.json();
    }
    
    async contractSafety(contractAddress) {
        const response = await fetch(`${this.baseURL}/api/contract-safety`, {
            method: 'POST',
            headers: this.headers,
            body: JSON.stringify({ contract_address: contractAddress })
        });
        return await response.json();
    }
}

// 使用示例
const client = new XiaomiaoAPIClient();

// 网站分析
client.websiteAnalysis('https://example.com')
    .then(result => {
        console.log('SEO得分:', result.analysis.seo_score);
        console.log('建议售价:', result.suggested_retail_price);
    });

// 加密分析
client.cryptoAnalysis()
    .then(result => {
        console.log('市场状态:', result.analysis.market_status);
    });
```

---

## 🔧 集成最佳实践

### 错误处理
```python
import requests
from requests.exceptions import RequestException

def safe_api_call(api_function, *args, **kwargs):
    """安全API调用包装器"""
    try:
        result = api_function(*args, **kwargs)
        if result.get('status') == 'failed':
            raise Exception(f"API调用失败: {result.get('error')}")
        return result
    except RequestException as e:
        return {
            "status": "failed",
            "error": f"网络错误: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "failed", 
            "error": str(e)
        }

# 使用示例
result = safe_api_call(client.website_analysis, "https://example.com")
if result['status'] == 'failed':
    print("调用失败:", result['error'])
else:
    print("调用成功:", result['analysis']['seo_score'])
```

### 批量处理
```python
def batch_website_analysis(urls, client):
    """批量网站分析"""
    results = []
    for url in urls:
        try:
            result = client.website_analysis(url)
            results.append({
                'url': url,
                'status': 'success',
                'data': result
            })
        except Exception as e:
            results.append({
                'url': url,
                'status': 'failed',
                'error': str(e)
            })
    
    return results

# 使用示例
urls = ['https://site1.com', 'https://site2.com', 'https://site3.com']
batch_results = batch_website_analysis(urls, client)
for result in batch_results:
    if result['status'] == 'success':
        print(f"{result['url']}: SEO得分 {result['data']['analysis']['seo_score']}")
    else:
        print(f"{result['url']}: 分析失败 - {result['error']}")
```

---

## 📊 商业化应用案例

### 案例1：SEO代理服务
```python
def seo_audit_service(website_url, client):
    """SEO审计服务"""
    result = client.website_analysis(website_url)
    
    seo_score = result['analysis']['seo_score']
    cost = result['total_cost']
    price = result['suggested_retail_price']
    
    # 生成SEO审计报告
    report = {
        "website": website_url,
        "seo_score": seo_score,
        "analysis": result['analysis']['recommendations'],
        "cost_to_provide": cost,
        "client_price": price,
        "profit": price - cost,
        "profit_margin": f"{((price - cost) / cost * 100):.0f}%"
    }
    
    return report

# 使用示例
audit_result = seo_audit_service("https://client-website.com", client)
print(f"SEO得分: {audit_result['seo_score']}")
print(f"预期利润: ${audit_result['profit']:.2f}")
```

### 案例2：DeFi安全监控
```python
def defi_security_monitor(contracts, client):
    """DeFi安全监控"""
    results = []
    
    for contract in contracts:
        audit = client.contract_safety(contract)
        
        risk_level = audit['security_analysis']['rug_pull_risk']
        
        if risk_level == "高风险":
            status = "⚠️ 警告：避免投资"
        elif risk_level == "中等风险":
            status = "⚡ 注意：谨慎投资"  
        else:
            status = "✅ 安全：可投资"
            
        results.append({
            "contract": contract,
            "risk_level": risk_level,
            "status": status,
            "recommendation": audit['security_analysis']['overall_rating']
        })
    
    return results

# 使用示例
suspicious_contracts = [
    "0x123...abc",
    "0x456...def", 
    "0x789...ghi"
]

monitoring_results = defi_security_monitor(suspicious_contracts, client)
for result in monitoring_results:
    print(f"{result['contract'][:10]}... - {result['status']}")
```

---

**总结：这8个服务的API设计简洁易用，支持JSON格式输入输出，具有完整的错误处理和商业化应用潜力！** 🚀

你想先测试哪个服务？我可以帮你创建测试代码！