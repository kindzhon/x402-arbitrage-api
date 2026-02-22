# 🦎 OpenClaw Cloud

在 Streamlit Cloud 上部署 OpenClaw，提供云端 AI 代理和消息服务。

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenClaw](https://img.shields.io/badge/OpenClaw-2026-4B4B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmNjg2OCIgZD0iTTEyIDJDMTIgMiA0IDggNCAxNGMwIDMuMzEgMi42OSA2IDYgNmgyYzAgMi4yMSAxLjc5IDQgNCA0czQtMS43OSA0LTRoMmMzLjMxIDAgNi0yLjY5IDYtNiAwLTYtOC0xMi04LTEyeiIvPjwvc3ZnPg==)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ 功能特性

- 🤖 **AI 代理** - 支持多模型（NVIDIA、Ollama、自定义）
- 💬 **消息服务** - QQ、Telegram、Discord 等多平台支持
- ⏰ **定时任务** - Cron 调度、一次性提醒、周期性任务
- 🔌 **插件系统** - 可扩展的插件架构
- 🧠 **记忆管理** - 长期记忆和会话历史
- 🌐 **云端部署** - 一键部署到 Streamlit Cloud

## 🚀 快速开始

### 1. 部署到 Streamlit Cloud

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)

1. Fork 此仓库
2. 在 Streamlit Cloud 添加你的仓库
3. 配置环境变量（见下方）
4. 完成！

### 2. 配置环境变量

在 Streamlit Cloud 的 **Secrets Management** 中添加：

```toml
# .streamlit/secrets.toml

# Gateway 配置（必须）
OPENCLAW_GATEWAY_URL = "ws://your-server:18789"
OPENCLAW_GATEWAY_TOKEN = "your-gateway-token"

# QQ Bot 配置（可选）
QQ_BOT_APP_ID = "your-app-id"
QQ_BOT_SECRET = "your-secret"
```

### 3. 本地测试

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/openclaw-streamlit.git
cd openclaw-streamlit

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run streamlit_app.py
```

访问：http://localhost:8501

## 📖 文档

- [📋 部署指南](DEPLOY.md) - 详细部署步骤
- [🦎 OpenClaw 文档](https://docs.openclaw.ai)
- [📊 Streamlit 文档](https://docs.streamlit.io)

## 🏗️ 架构说明

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  Streamlit      │  WebSocket│  OpenClaw        │  HTTP   │  AI Models      │
│  Cloud          │◄────────►│  Gateway         │◄───────►│  (NVIDIA, etc.) │
│  (streamlit.app)│         │  (Your Server)   │         │                 │
└─────────────────┘         └──────────────────┘         └─────────────────┘
         │                          │
         │                          │
         ▼                          ▼
┌─────────────────┐         ┌──────────────────┐
│  Users          │         │  Message Platforms│
│  (Browser)      │         │  (QQ, Telegram)  │
└─────────────────┘         └──────────────────┘
```

**关键点**:
- Streamlit Cloud 无法访问本地网络
- 需要部署公网可访问的 Gateway
- 或使用内网穿透工具（ngrok、cloudflared）

## 🔐 安全建议

- ✅ **永远不要**将 Token 提交到 GitHub
- ✅ 使用 Streamlit Secrets Management
- ✅ Gateway 启用 TLS 加密
- ✅ 定期更换 Token
- ✅ 限制 Gateway 访问 IP

## 📦 项目结构

```
openclaw-streamlit/
├── streamlit_app.py          # 主应用
├── requirements.txt          # Python 依赖
├── README.md                 # 本文件
├── DEPLOY.md                 # 部署指南
├── .streamlit/
│   ├── config.toml          # Streamlit 配置
│   └── .gitignore           # Secrets 忽略
└── .gitignore               # Git 忽略文件
```

## 🛠️ 开发

### 本地开发环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run streamlit_app.py
```

### 贡献代码

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 代理框架
- [Streamlit](https://streamlit.io) - 快速构建 Web 应用
- [NVIDIA](https://www.nvidia.com) - AI 模型支持

## 📞 联系方式

- 💬 Discord: https://discord.com/invite/clawd
- 📧 Email: support@openclaw.ai
- 🌐 Website: https://openclaw.ai

---

**Made with ❤️ by the OpenClaw Team**
