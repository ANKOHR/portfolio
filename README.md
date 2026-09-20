# Henry Williams — Technical Portfolio

The portfolio for Henry Williams, a Year 13 student building reliable AI, backend and automation systems with an emphasis on validation, auditability, human review and measurable evidence.

## Featured work

- [OpsPilot](https://opspilot-web-iota.vercel.app/) — auditable AI operations and workflow automation. [Repository](https://github.com/ANKOHR/opspilot) · [evidence](https://github.com/ANKOHR/opspilot/blob/main/docs/evidence.md)
- [VerityDocs](https://veritydocs-web.vercel.app/) — evidence-backed document intelligence and reconciliation. [Repository](https://github.com/ANKOHR/veritydocs) · [evidence](https://github.com/ANKOHR/veritydocs/blob/main/docs/evidence.md)
- [Axiom AP Agent](https://github.com/ANKOHR/axiom-ap-agent-prototype) — accounts-payable automation with deterministic controls and audit logging.

The site deliberately separates verified external proof from staged or synthetic capabilities. OpsPilot's evaluation cases are synthetic, and its deployed role boundary is described as a demo identity boundary rather than production authentication. VerityDocs' verified public demo uses SQLite and synchronous processing because its Railway free-tier deployment did not provision the staged Postgres/Redis/worker topology. Its OpenAI extraction adapter is not presented as externally exercised.

## Run locally

```bash
npm ci
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The portfolio is static-first: it has no database, authentication layer or unnecessary backend.

## Quality checks

```bash
npm run lint
npm run typecheck
npm run build
```

## Assets

- `public/images/` contains synthetic project screenshots and poster images.
- `public/demos/` contains the two caption-led demo videos.
- `public/Henry_Williams_Technical_CV_2026.pdf` is the final CV PDF copy used by the site.
- `docs/OUTREACH.md` contains prepared, unsent proof-first outreach drafts.

No outreach is sent by this repository, and no private inbox, OAuth secret, phone number or customer data is included.
