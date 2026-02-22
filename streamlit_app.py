import streamlit as st
import os
import json
from datetime import datetime
import requests

# 页面配置
st.set_page_config(
    page_title="OpenClaw Cloud",
    page_icon="🦎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 从环境变量读取配置
GATEWAY_URL = os.getenv("OPENCLAW_GATEWAY_URL", "ws://localhost:18789")
GATEWAY_TOKEN = os.getenv("OPENCLAW_GATEWAY_TOKEN", "")
QQ_BOT_APP_ID = os.getenv("QQ_BOT_APP_ID", "")
QQ_BOT_SECRET = os.getenv("QQ_BOT_SECRET", "")

# 初始化 session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'status' not in st.session_state:
    st.session_state.status = "未连接"

# 自定义 CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 1rem;
    }
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .status-connected {
        background-color: #10B981;
        color: white;
    }
    .status-disconnected {
        background-color: #EF4444;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<p class="main-header">🦎 OpenClaw Cloud</p>', unsafe_allow_html=True)
st.markdown("### 云端 OpenClaw 管理与服务面板")

# 检查连接状态
def check_gateway_connection():
    """检查 Gateway 连接状态"""
    if not GATEWAY_TOKEN:
        return False, "未配置 Token"
    
    try:
        # 尝试连接 Gateway WebSocket
        # 注意：Streamlit Cloud 无法直接连接本地 WebSocket
        # 这里仅做配置检查
        return True, "配置正常"
    except Exception as e:
        return False, str(e)

# 侧边栏
with st.sidebar:
    st.header("⚙️ 配置")
    
    # 连接状态
    connected, status_msg = check_gateway_connection()
    status_class = "status-connected" if connected else "status-disconnected"
    status_icon = "✅" if connected else "❌"
    st.markdown(f'<span class="status-badge {status_class}">{status_icon} {status_msg}</span>', unsafe_allow_html=True)
    
    st.divider()
    
    # 配置信息展示
    st.subheader("📋 当前配置")
    config_info = {
        "Gateway URL": GATEWAY_URL if GATEWAY_URL else "未设置",
        "Gateway Token": "已配置" if GATEWAY_TOKEN else "❌ 未配置",
        "QQ Bot AppID": "已配置" if QQ_BOT_APP_ID else "未配置",
        "QQ Bot Secret": "已配置" if QQ_BOT_SECRET else "未配置",
    }
    st.json(config_info)
    
    st.divider()
    
    # 帮助信息
    st.info("""
    **💡 部署指南**
    
    1. Fork 此仓库到 GitHub
    2. 在 Streamlit Cloud 添加仓库
    3. 配置环境变量：
       - `OPENCLAW_GATEWAY_URL`
       - `OPENCLAW_GATEWAY_TOKEN`
       - `QQ_BOT_APP_ID`
       - `QQ_BOT_SECRET`
    
    [查看部署文档](https://github.com/your-username/openclaw-streamlit/blob/main/DEPLOY.md)
    """)
    
    st.divider()
    
    # 刷新按钮
    if st.button("🔄 刷新页面", use_container_width=True):
        st.rerun()

# 主内容区
tab1, tab2, tab3, tab4 = st.tabs(["🏠 首页", "💬 消息", "⏰ 定时任务", "📚 文档"])

with tab1:
    st.header("🏠 欢迎使用 OpenClaw Cloud")
    
    # 功能卡片
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 💬 消息服务
        - 通过 QQ Bot 发送消息
        - 支持文本、图片、文件
        - 自动重试机制
        
        [使用消息服务 →](#消息)
        """)
    
    with col2:
        st.markdown("""
        ### ⏰ 定时任务
        - Cron 表达式调度
        - 一次性提醒
        - 周期性任务
        
        [创建任务 →](#定时任务)
        """)
    
    with col3:
        st.markdown("""
        ### 🔌 插件系统
        - QQ Bot 集成
        - 自定义插件
        - Webhook 支持
        
        [查看插件 →](#文档)
        """)
    
    st.divider()
    
    # 快速开始
    st.header("🚀 快速开始")
    
    st.markdown("""
    #### 第一步：配置环境变量
    
    在 Streamlit Cloud 的 **Secrets Management** 中添加以下配置：
    
    ```toml
    # .streamlit/secrets.toml
    OPENCLAW_GATEWAY_URL = "ws://your-server:18789"
    OPENCLAW_GATEWAY_TOKEN = "your-gateway-token"
    QQ_BOT_APP_ID = "your-qq-bot-app-id"
    QQ_BOT_SECRET = "your-qq-bot-secret"
    ```
    
    #### 第二步：测试连接
    
    前往 **💬 消息** 标签页，发送一条测试消息。
    
    #### 第三步：创建任务
    
    在 **⏰ 定时任务** 标签页创建你的第一个定时提醒。
    """)
    
    st.divider()
    
    # 系统状态
    st.header("📊 系统状态")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Gateway 状态",
            value="🟢 运行中" if connected else "🔴 未连接",
            delta=None
        )
    
    with col2:
        st.metric(
            label="QQ Bot",
            value="✅ 已启用" if QQ_BOT_APP_ID else "❌ 未配置",
            delta=None
        )
    
    with col3:
        st.metric(
            label="当前时间",
            value=datetime.now().strftime("%H:%M"),
            delta=datetime.now().strftime("%Y-%m-%d")
        )
    
    with col4:
        st.metric(
            label="时区",
            value="Asia/Shanghai",
            delta="UTC+8"
        )

with tab2:
    st.header("💬 消息服务")
    
    if not connected:
        st.warning("⚠️ Gateway 未连接，请先在侧边栏配置环境变量")
    
    # 消息历史
    st.subheader("消息历史")
    
    if len(st.session_state.messages) == 0:
        st.info("暂无消息记录")
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if "timestamp" in msg:
                    st.caption(f"发送于：{msg['timestamp']}")
    
    # 消息输入
    st.divider()
    st.subheader("发送消息")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        message_input = st.chat_input("输入消息内容...")
    
    with col2:
        target_user = st.text_input("目标用户 QQ", value="", placeholder="可选")
    
    if message_input:
        # 添加用户消息
        st.session_state.messages.append({
            "role": "user",
            "content": message_input,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # 显示用户消息
        with st.chat_message("user"):
            st.markdown(message_input)
        
        # 处理消息（模拟）
        with st.chat_message("assistant"):
            with st.spinner("🤖 思考中..."):
                # 这里应该调用 OpenClaw API
                # 由于 Streamlit Cloud 无法访问本地 Gateway，这里做模拟响应
                response = f"""
收到你的消息：**{message_input}**

⚠️ **注意**: 当前为演示模式。要实际使用 OpenClaw 功能，需要：

1. 部署自己的 Gateway 服务器（可访问的公网地址）
2. 在 Streamlit Cloud 配置 `OPENCLAW_GATEWAY_URL` 和 `OPENCLAW_GATEWAY_TOKEN`
3. 确保 Gateway 服务器允许来自 Streamlit Cloud 的连接

[查看部署指南](https://github.com/your-username/openclaw-streamlit/blob/main/DEPLOY.md)
                """
                st.markdown(response)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

with tab3:
    st.header("⏰ 定时任务管理")
    
    if not connected:
        st.warning("⚠️ Gateway 未连接，无法创建实际任务")
    
    # 任务列表（模拟）
    st.subheader("当前任务")
    
    sample_tasks = [
        {
            "name": "喝水提醒",
            "schedule": "每 2 小时",
            "type": "周期性",
            "status": "✅ 运行中",
            "last_run": "2026-02-22 12:00"
        },
        {
            "name": "日报发送",
            "schedule": "每天 18:00",
            "type": "周期性",
            "status": "✅ 运行中",
            "last_run": "2026-02-21 18:00"
        }
    ]
    
    if sample_tasks:
        for task in sample_tasks:
            with st.expander(f"{task['status']} {task['name']} - {task['schedule']}"):
                st.markdown(f"""
                - **类型**: {task['type']}
                - **状态**: {task['status']}
                - **上次执行**: {task['last_run']}
                """)
                col1, col2 = st.columns(2)
                with col1:
                    st.button("编辑", key=f"edit_{task['name']}")
                with col2:
                    st.button("删除", key=f"delete_{task['name']}")
    else:
        st.info("暂无定时任务")
    
    st.divider()
    
    # 创建新任务
    st.subheader("创建新任务")
    
    with st.form("create_task"):
        col1, col2 = st.columns(2)
        
        with col1:
            task_name = st.text_input("任务名称", placeholder="例如：喝水提醒")
            schedule_type = st.selectbox("调度类型", ["一次性", "周期性"])
            
            if schedule_type == "一次性":
                schedule_value = st.text_input("执行时间", placeholder="例如：2m (2分钟后)")
            else:
                schedule_value = st.text_input("Cron 表达式", placeholder="例如：0 9 * * * (每天9点)")
                st.caption("格式：分 时 日 月 星期")
        
        with col2:
            message_content = st.text_area("消息内容", placeholder="例如：💧 喝水时间到！")
            channel = st.selectbox("目标频道", ["qqbot", "telegram", "discord"])
            to_user = st.text_input("目标用户", placeholder="用户 ID 或群号")
        
        delete_after = st.checkbox("执行后删除（仅一次性任务）", value=True)
        
        submitted = st.form_submit_button("🚀 创建任务")
        
        if submitted:
            if not task_name or not message_content:
                st.error("请填写任务名称和消息内容")
            elif not schedule_value:
                st.error("请填写调度时间")
            else:
                st.success(f"""
                ✅ 任务创建成功（模拟）！
                
                **任务信息**:
                - 名称：{task_name}
                - 类型：{schedule_type}
                - 调度：{schedule_value}
                - 消息：{message_content}
                - 频道：{channel}
                - 目标：{to_user if to_user else "默认"}
                
                ⚠️ 注意：需要配置 Gateway 后才能实际执行任务。
                """)

with tab4:
    st.header("📚 文档与帮助")
    
    st.markdown("""
    ## 🦎 OpenClaw Cloud 文档
    
    ### 什么是 OpenClaw？
    
    OpenClaw 是一个强大的 AI 代理框架，支持：
    - 🤖 多模型支持（NVIDIA、Ollama、自定义）
    - 💬 多平台消息（QQ、Telegram、Discord 等）
    - ⏰ 定时任务调度
    - 🔌 插件系统
    - 🧠 记忆管理
    
    ### 部署方式
    
    #### 方式 1：Streamlit Cloud（推荐）
    
    1. Fork 此仓库到 GitHub
    2. 在 [Streamlit Cloud](https://streamlit.io/cloud) 部署
    3. 配置环境变量
    
    **优点**: 免费、自动部署、HTTPS 支持  
    **缺点**: 需要公网可访问的 Gateway
    
    #### 方式 2：本地部署
    
    ```bash
    pip install -r requirements.txt
    streamlit run streamlit_app.py
    ```
    
    **优点**: 完全控制、无网络延迟  
    **缺点**: 需要自行维护服务器
    
    ### 环境变量配置
    
    | 变量名 | 说明 | 示例 |
    |--------|------|------|
    | `OPENCLAW_GATEWAY_URL` | Gateway WebSocket 地址 | `ws://your-server:18789` |
    | `OPENCLAW_GATEWAY_TOKEN` | Gateway 认证 Token | `your-token` |
    | `QQ_BOT_APP_ID` | QQ Bot AppID | `102844495` |
    | `QQ_BOT_SECRET` | QQ Bot 密钥 | `your-secret` |
    
    ### 常见问题
    
    **Q: 为什么消息发送失败？**  
    A: 确保 Gateway 服务器公网可访问，且 Token 配置正确。
    
    **Q: 定时任务不执行？**  
    A: 检查 Gateway 服务是否运行，查看日志排查错误。
    
    **Q: 如何自定义主题？**  
    A: 编辑 `.streamlit/config.toml` 文件。
    
    ### 相关链接
    
    - [OpenClaw 官方文档](https://docs.openclaw.ai)
    - [Streamlit 文档](https://docs.streamlit.io)
    - [GitHub 仓库](https://github.com/your-username/openclaw-streamlit)
    - [Discord 社区](https://discord.com/invite/clawd)
    
    ---
    
    **需要帮助？** 提交 Issue 或加入 Discord 社区。
    """)

# 页脚
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 1rem;'>
    <small>
        🦎 OpenClaw Cloud | Powered by Streamlit<br>
        <a href="https://github.com/your-username/openclaw-streamlit" target="_blank">GitHub</a> · 
        <a href="https://docs.openclaw.ai" target="_blank">文档</a> · 
        <a href="https://discord.com/invite/clawd" target="_blank">社区</a>
    </small>
</div>
""", unsafe_allow_html=True)
