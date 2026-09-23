# 20-fde-engineering

NARRATIVES = {
    "what-is-fde": """# What Is an FDE (Forward Deployed Engineer)

Embedded with customers to discover problems, ship integrations, and harden AI in **their** environment—part consultant, part senior IC.

Success = production adoption metrics, not demo applause.
""",
    "customer-discovery": """# Customer Discovery

Ask what decision the AI output drives, who is liable if wrong, and what systems must integrate.

Avoid “build ChatGPT for Excel” until workflow and ROI are concrete.
""",
    "requirement-discovery": """# Requirement Discovery

Translate vague asks into SLAs, data sources, auth model, eval criteria, and rollout phases.

Write the **non-goals** explicitly—scope creep kills FDE engagements.
""",
    "solution-design": """# Solution Design (FDE)

Prefer boring architecture: gateway + RAG + HITL over autonomous agent swarms on week two.

Diagram data flows and trust boundaries for security review early.
""",
    "enterprise-integrations": """# Enterprise Integrations

SSO, SCIM, VPC peering, ServiceNow, Salesforce—AI feature must live inside existing IT tickets and change windows.

Plan for 6-month procurement, not 6-day API keys.
""",
    "data-integration": """# Data Integration

Connectors with ACL sync, incremental updates, legal hold on deletion.

Customer data never trains your foundation model without contract language saying so.
""",
    "customer-deployment": """# Customer Deployment

Helm/Terraform in their cloud; air-gap options; runbooks their ops can own.

Handoff checklist beats “we'll stay on Slack forever.”
""",
    "debugging-production": """# Debugging Production (FDE)

Reproduce with trace IDs; compare retrieval IDs; check index lag; verify prompt version.

Bring hypotheses and fixed timelines—customers forgive depth, not vagueness.
""",
    "technical-communication": """# Technical Communication

Write exec summaries (risk, cost, timeline) and engineer docs (APIs, failure modes) for the same project.

One slide per architecture decision with trade-offs named.
""",
    "architecture-presentations": """# Architecture Presentations

Lead with constraints and SLOs, then diagram, then phased roadmap.

Anticipate security and legal questions—don't defer to “the model is smart.”
""",
    "stakeholder-management": """# Stakeholder Management

Map sponsor, blocker, daily user, and procurement. Align demo dates with eval readiness.

Say no to scope that breaks safety or timeline—credibly, with alternatives.
""",
}
