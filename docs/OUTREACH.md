# Proof-first outreach templates

These are prepared drafts only. They are not sent from this repository.

## A. AI automation, integrations or backend

Hi [Name] — I noticed [specific operational process] is part of your team’s work. I’ve built OpsPilot, a deployed workflow platform that turns incoming events into typed steps, permissioned tool calls and human approval gates. The public proof includes a separately verified Gmail OAuth path, idempotent event handling, checkpoint replay and a full execution trace; the demo defaults to sandbox data. You can inspect the repository and evidence here: https://github.com/ANKOHR/opspilot. If useful, I’d be glad to spend 20 minutes mapping one repetitive workflow in your stack and identifying what should stay deterministic versus model-driven. I’m a Year 13 student available for scoped remote work, around 10–14 hours/week during term.

One-line DM: I built and publicly verified OpsPilot for approval-gated workflows, Gmail OAuth and replayable traces — would a short workflow-mapping call be useful? https://github.com/ANKOHR/opspilot

## B. OCR, documents, finance or extraction

Hi [Name] — if your team is handling PDFs, scans or spreadsheets where an extracted number still needs to be trusted, VerityDocs may be relevant. I built and deployed an evidence-backed document pipeline that runs real Dockerized Tesseract OCR, keeps bounding-box provenance with fields, validates financial arithmetic in Python and routes conflicts to review. In the public synthetic proof, £8,000 + £1,600 passes, while a deliberately inconsistent £9,900 gross produces `FIN-001: FAIL`. The evidence record also covers duplicate detection and tenant-boundary checks: https://github.com/ANKOHR/veritydocs/blob/main/docs/evidence.md. Would you be open to a short conversation about one document process that currently needs manual checking?

One-line DM: VerityDocs turns OCR output into source-linked, validated records and flags wrong totals for review — I’d be glad to compare it with one document process you operate. https://veritydocs-web.vercel.app/

## C. AP or finance automation

Hi [Name] — I’ve been studying the point where accounts-payable automation needs controls rather than another chat interface. VerityDocs demonstrates source-backed invoice extraction, deterministic VAT arithmetic, duplicate detection and review routing. Alongside it, my Axiom AP Agent prototype focuses on payment-policy controls, idempotency and audit logging, with staging evidence kept separate from claims about provider dispatch. Relevant links: https://github.com/ANKOHR/veritydocs and https://github.com/ANKOHR/axiom-ap-agent-prototype. If you have a narrow invoice, exception or payment-approval workflow that is currently spreadsheet-heavy, could I ask you a few questions and return a small, testable automation outline? I’m available for scoped remote technical work during term.

One-line DM: I’ve built evidence-backed invoice validation plus an AP controls prototype; is there one exception workflow you’d be willing to describe? https://github.com/ANKOHR/axiom-ap-agent-prototype
