"""
AI Audit Tools - AI审计工具
支持安全审计、代码审计、合规审计
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIAuditTools:
    """
    AI审计工具
    支持：安全、代码、合规
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def security_audit(self, code: str, language: str) -> Dict:
        """安全审计"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请对以下{language}代码进行安全审计：

{code[:2000]}

请返回JSON格式：
{{
    "risk_level": "high/medium/low",
    "vulnerabilities": [
        {{"type": "类型", "severity": "严重程度", "location": "位置", "fix": "修复建议"}}
    ],
    "best_practices": ["最佳实践"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"audit": content}

    def code_quality_audit(self, code: str, language: str) -> Dict:
        """代码质量审计"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请对以下{language}代码进行质量审计：

{code[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "issues": [
        {{"type": "类型", "severity": "严重程度", "description": "描述", "fix": "修复建议"}}
    ],
    "metrics": {{"complexity": "复杂度", "maintainability": "可维护性"}}
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"quality": content}

    def compliance_audit(self, system: str, standard: str) -> Dict:
        """合规审计"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请对{system}进行{standard}合规审计：

请返回JSON格式：
{{
    "compliance_score": 1-100,
    "compliant": ["符合项"],
    "non_compliant": ["不符合项"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"compliance": content}

    def generate_audit_report(self, findings: Dict) -> str:
        """生成审计报告"""
        if not self.client:
            return "LLM客户端未配置"

        findings_text = json.dumps(findings, ensure_ascii=False)

        prompt = f"""请根据以下审计发现生成报告：

{findings_text}

要求：
1. 执行摘要
2. 详细发现
3. 风险评估
4. 建议措施"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_audit_checklist(self, system_type: str, standard: str) -> Dict:
        """设计审计清单"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{system_type}设计{standard}审计清单：

请返回JSON格式：
{{
    "categories": [
        {{"name": "类别", "items": ["检查项"], "weight": "权重"}}
    ],
    "scoring": "评分标准"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"checklist": content}

    def generate_audit_schedule(self, systems: List[str], frequency: str) -> Dict:
        """生成审计计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        systems_text = ", ".join(systems)

        prompt = f"""请生成审计计划：

系统：{systems_text}
频率：{frequency}

请返回JSON格式：
{{
    "schedule": [
        {{"system": "系统", "frequency": "频率", "scope": "范围", "responsible": "负责人"}}
    ],
    "reporting": "报告流程"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"schedule": content}


def create_tools(**kwargs) -> AIAuditTools:
    """创建审计工具"""
    return AIAuditTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Audit Tools")
    print()

    # 测试
    audit = tools.security_audit("def login(user, pwd):\n    query = f'SELECT * FROM users WHERE name={user}'", "Python")
    print(json.dumps(audit, ensure_ascii=False, indent=2))
