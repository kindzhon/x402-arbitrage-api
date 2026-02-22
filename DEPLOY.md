# 🦎 OpenClaw Cloud - Streamlit 部署指南

将 OpenClaw 部署到 Streamlit Cloud (streamlit.app)，提供云端 AI 代理服务。

## 📋 目录

- [快速开始](#快速开始)
- [部署步骤](#部署步骤)
- [配置环境变量](#配置环境变量)
- [Gateway 服务器部署](#gateway-服务器部署)
- [常见问题](#常见问题)

---

## 🚀 快速开始

### 1. Fork 仓库到 GitHub

```bash
# 或者直接在 GitHub 网页上点击 Fork 按钮
git clone https://github.com/YOUR_USERNAME/openclaw-streamlit.git
cd openclaw-streamlit
```

### 2. 推送到你的 GitHub

```bash
git add .
git commit -m "Initial commit: OpenClaw Streamlit app"
git push origin main
```

### 3. 在 Streamlit Cloud 部署

1. 访问 [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. 点击 **"New app"**
3. 选择你的 GitHub 仓库
4. 设置主文件路径：`streamlit_app.py`
5. 点击 **"Deploy!"**

### 4. 配置环境变量

在 Streamlit Cloud 控制台：

1. 进入你的应用设置
2. 找到 **"Secrets Management"**
3. 添加以下配置（见下方）

---

## 🔐 配置环境变量

### 方式 1：Streamlit Secrets (推荐)

在 Streamlit Cloud 的 **Secrets Management** 中添加：

```toml
# .streamlit/secrets.toml

# Gateway 配置（必须）
OPENCLAW_GATEWAY_URL = "ws://your-server-ip:18789"
OPENCLAW_GATEWAY_TOKEN = "your-gateway-token"

# QQ Bot 配置（可选）
QQ_BOT_APP_ID = "102844495"
QQ_BOT_SECRET = "your-qq-bot-secret"

# 其他配置（可选）
OPENCLAW_WORKSPACE = "/app/workspace"
```

### 方式 2：本地测试

创建 `.streamlit/secrets.toml` 文件（**不要提交到 Git**）：

```bash
# 添加到 .gitignore
echo ".streamlit/secrets.toml" >> .gitignore

# 创建配置
cat > .streamlit/secrets.toml << EOF
OPENCLAW_GATEWAY_URL = "ws://localhost:18789"
OPENCLAW_GATEWAY_TOKEN = "your-local-token"
QQ_BOT_APP_ID = "your-app-id"
QQ_BOT_SECRET = "your-secret"
EOF
```

---

## 🖥️ Gateway 服务器部署

**重要**: Streamlit Cloud 无法访问你的本地网络，需要部署公网可访问的 Gateway。

### 方案 1：云服务器部署（推荐）

使用 VPS（如 AWS、DigitalOcean、阿里云）：

```bash
# 1. 安装 OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. 配置 Gateway 监听公网
openclaw configure

# 编辑 ~/.openclaw/openclaw.json
# 修改 gateway.bind 为 "0.0.0.0"
# 修改 gateway.mode 为 "remote"

# 3. 启动 Gateway
openclaw gateway start

# 4. 开放防火墙端口
sudo ufw allow 18789/tcp

# 5. 获取 Token
cat ~/.openclaw/openclaw.json | grep token
```

### 方案 2：内网穿透（测试用）

使用 ngrok 或 cloudflared：

```bash
# 使用 ngrok
ngrok http 18789

# 获取公网地址，例如：wss://abc123.ngrok.io
# 将此地址配置到 OPENCLAW_GATEWAY_URL
```

### 方案 3：Docker 部署

```bash
docker run -d \
  --name openclaw-gateway \
  -p 18789:18789 \
  -v ~/.openclaw:/root/.openclaw \
  openclaw/gateway:latest
```

---

## 📁 项目结构

```
openclaw-streamlit/
├── streamlit_app.py          # 主应用
├── requirements.txt          # Python 依赖
├── .streamlit/
│   ├── config.toml          # Streamlit 配置
│   └── secrets.toml         # 密钥配置（不提交）
├── .gitignore               # Git 忽略文件
├── README.md                # 项目说明
└── DEPLOY.md                # 部署指南（本文件）
```

---

## 🔒 安全建议

### 1. 保护 Token

- ✅ **永远不要**将 Token 提交到 GitHub
- ✅ 使用 Streamlit Secrets Management
- ✅ 定期更换 Token
- ✅ 限制 Gateway 访问 IP

### 2. Gateway 安全配置

```json
{
  "gateway": {
    "auth": {
      "mode": "token",
      "token": "使用强随机 Token"
    },
    "bind": "0.0.0.0",
    "port": 18789,
    "tls": {
      "enabled": true,
      "cert": "/path/to/cert.pem",
      "key": "/path/to/key.pem"
    }
  }
}
```

### 3. .gitignore 配置

确保以下文件不被提交：

```gitignore
# 密钥配置
.streamlit/secrets.toml
.env
*.pem
*.key

# 日志
*.log
logs/

# 本地配置
.openclaw/openclaw.json
```

---

## 🧪 本地测试

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# Windows PowerShell
$env:OPENCLAW_GATEWAY_URL="ws://localhost:18789"
$env:OPENCLAW_GATEWAY_TOKEN="your-token"

# Linux/Mac
export OPENCLAW_GATEWAY_URL="ws://localhost:18789"
export OPENCLAW_GATEWAY_TOKEN="your-token"
```

### 3. 启动应用

```bash
streamlit run streamlit_app.py
```

访问：http://localhost:8501

---

## ⚠️ 常见问题

### Q1: 部署后显示 "Gateway 未连接"

**原因**: Streamlit Cloud 无法访问本地 Gateway

**解决**:
1. 部署公网可访问的 Gateway（见上方）
2. 或使用内网穿透工具
3. 检查防火墙设置

### Q2: WebSocket 连接失败

**原因**: 端口未开放或协议错误

**解决**:
- 确保使用 `ws://` 或 `wss://` 前缀
- 检查云服务器防火墙
- 确认 Gateway 正在运行：`openclaw gateway status`

### Q3: QQ Bot 消息发送失败

**原因**: QQ Bot 配置错误或未授权

**解决**:
- 检查 AppID 和 Secret
- 确认 QQ Bot 插件已启用
- 查看 Gateway 日志：`openclaw logs`

### Q4: 部署后页面空白

**原因**: 依赖安装失败或代码错误

**解决**:
```bash
# 在 Streamlit Cloud 控制台查看日志
# 检查 requirements.txt 是否完整
# 本地测试：streamlit run streamlit_app.py
```

### Q5: 如何更新部署？

**解决**:
```bash
# 推送代码到 GitHub
git add .
git commit -m "Update: 描述你的更改"
git push origin main

# Streamlit Cloud 会自动重新部署
```

---

## 📊 监控与日志

### 查看 Streamlit Cloud 日志

1. 进入应用控制台
2. 点击 **"Logs"** 标签
3. 查看实时日志

### 查看 Gateway 日志

```bash
# 实时日志
openclaw logs --follow

# 最近 100 行
openclaw logs --tail 100

# 导出日志
openclaw logs > gateway.log
```

---

## 🎨 自定义

### 修改主题

编辑 `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### 添加功能

在 `streamlit_app.py` 中添加新的 tab 或组件。

---

## 📞 支持

- **OpenClaw 文档**: https://docs.openclaw.ai
- **Streamlit 文档**: https://docs.streamlit.io
- **Discord 社区**: https://discord.com/invite/clawd
- **GitHub Issues**: https://github.com/YOUR_USERNAME/openclaw-streamlit/issues

---

## 📝 检查清单

部署前确认：

- [ ] 已 Fork 仓库到 GitHub
- [ ] 已配置 `.gitignore`
- [ ] 已部署公网 Gateway
- [ ] 已获取 Gateway Token
- [ ] 已在 Streamlit Cloud 配置 Secrets
- [ ] 已测试本地运行
- [ ] 已更新 README 中的链接

---

**祝你部署成功！** 🎉
