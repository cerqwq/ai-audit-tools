# 🔍 AI Audit Tools

AI审计工具，支持安全审计、代码审计、合规审计。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🛡️ 安全审计
- 📊 代码质量审计
- ✅ 合规审计
- 📋 审计报告生成
- 📝 审计清单设计
- 📅 审计计划生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_audit_tools import create_tools

tools = create_tools()

# 安全审计
security = tools.security_audit(code, "Python")

# 代码质量审计
quality = tools.code_quality_audit(code, "Python")

# 合规审计
compliance = tools.compliance_audit("支付系统", "PCI DSS")

# 审计报告
report = tools.generate_audit_report(findings)

# 审计清单
checklist = tools.design_audit_checklist("Web应用", "OWASP")

# 审计计划
schedule = tools.generate_audit_schedule(["API", "数据库"], "季度")
```

## 📁 项目结构

```
ai-audit-tools/
├── tools.py       # 审计工具核心
└── README.md
```

## 📄 许可证

MIT License
