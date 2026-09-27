import Image from "next/image";

const proofLinks = {
  evalforge: {
    live: "https://evalforge-web.vercel.app",
    repo: "https://github.com/ANKOHR/evalforge",
    evidence: "https://github.com/ANKOHR/evalforge/blob/main/docs/evidence.md",
  },
  tracebrowser: {
    live: "https://tracebrowser-web.vercel.app",
    repo: "https://github.com/ANKOHR/tracebrowser",
    evidence: "https://github.com/ANKOHR/tracebrowser/blob/main/docs/evidence.md",
  },
  opspilot: {
    live: "https://opspilot-web-iota.vercel.app/",
    repo: "https://github.com/ANKOHR/opspilot",
    evidence: "https://github.com/ANKOHR/opspilot/blob/main/docs/evidence.md",
    video: "/demos/opspilot.mp4",
  },
  veritydocs: {
    live: "https://veritydocs-web.vercel.app/",
    repo: "https://github.com/ANKOHR/veritydocs",
    evidence: "https://github.com/ANKOHR/veritydocs/blob/main/docs/evidence.md",
    video: "/demos/veritydocs.mp4",
  },
};

const capabilities = [
  "Agent evaluation and regression gates",
  "Reliable AI workflow systems",
  "Python / FastAPI backends",
  "Tool permissions and human approval",
  "Browser automation and traceability",
  "Document AI, OCR and provenance",
  "TypeScript / Next.js",
  "Integrations, APIs and OAuth",
];

function ExternalLink({ href, children, className = "" }: { href: string; children: React.ReactNode; className?: string }) {
  return <a className={className} href={href} target="_blank" rel="noreferrer">{children}<span aria-hidden="true">↗</span></a>;
}

function ArrowLink({ href, children }: { href: string; children: React.ReactNode }) {
  return <ExternalLink href={href} className="arrow-link">{children}</ExternalLink>;
}

export default function Home() {
  return (
    <main>
      <header className="site-header">
        <a className="wordmark" href="#top" aria-label="Henry Williams home"><span>HW</span><strong>Henry Williams</strong></a>
        <nav aria-label="Primary navigation"><a href="#work">Work</a><a href="#capabilities">Capabilities</a><a href="#about">About</a></nav>
        <a className="header-contact" href="mailto:henry.williams85.contact@gmail.com">Get in touch <span aria-hidden="true">↗</span></a>
      </header>

      <section className="hero section-shell" id="top">
        <div className="hero-copy">
          <p className="eyebrow">SOFTWARE / APPLIED AI ENGINEER <span>·</span> LONDON</p>
          <h1>Systems for the part where <em>trust</em> matters.</h1>
          <p className="hero-lede">I build reliable agent systems, evaluation infrastructure, backend software and automation with an emphasis on validation, auditability, human review and measurable evidence.</p>
          <div className="hero-actions"><a className="button button-primary" href="#work">View selected work <span aria-hidden="true">↓</span></a><a className="button button-quiet" href="/Henry_Williams_Technical_CV_2026.pdf" download>Download CV <span aria-hidden="true">↗</span></a></div>
          <div className="availability"><span className="status-dot" />Available for scoped part-time technical work alongside school</div>
        </div>
        <div className="hero-visual" aria-label="System design principles">
          <div className="visual-topline"><span>OPERATING PRINCIPLES</span><span>01—03</span></div>
          <div className="signal-stack"><div className="signal-row"><span className="signal-index">01</span><strong>Interpret</strong><span className="signal-note">structured outputs</span></div><div className="signal-line" /><div className="signal-row"><span className="signal-index">02</span><strong>Validate</strong><span className="signal-note">deterministic rules</span></div><div className="signal-line" /><div className="signal-row"><span className="signal-index">03</span><strong>Govern</strong><span className="signal-note">review + audit</span></div></div>
          <div className="visual-footer"><span>proof before promise</span><span className="mono">HW / 2026</span></div>
        </div>
      </section>

      <section className="signal-strip section-shell" aria-label="Portfolio summary"><div><strong>05</strong><span>selected systems</span></div><div><strong>04</strong><span>public proof surfaces</span></div><div><strong>CI</strong><span>regression-backed builds</span></div><div><strong>01</strong><span>clear claim boundary</span></div></section>

      <section className="work-section section-shell" id="work">
        <div className="section-heading"><div><p className="eyebrow">SELECTED WORK</p><h2>Built systems, not just demos.</h2></div><p>Five systems spanning agent evaluation, durable operations, browser reliability, document intelligence and controlled external action.</p></div>
        <article className="project-card project-blue"><div className="project-meta"><span>01 / FLAGSHIP</span><span>OPS / WORKFLOWS</span></div><div className="project-grid"><div className="project-copy"><p className="project-kicker">Auditable AI operations and workflow automation</p><h3>OpsPilot</h3><p>Human-supervised business workflows that turn events into typed steps, permissioned tools, approvals and replayable traces. The showcase is an inbound revenue workflow with a separately verified Gmail OAuth path.</p><div className="proof-list"><span>60 backend tests</span><span>Gmail OAuth lane</span><span>Approval + replay</span><span>Idempotency</span></div><div className="project-links"><ArrowLink href={proofLinks.opspilot.live}>Live demo</ArrowLink><ArrowLink href={proofLinks.opspilot.repo}>GitHub</ArrowLink><ArrowLink href={proofLinks.opspilot.evidence}>Evidence</ArrowLink><a className="video-link" href={proofLinks.opspilot.video}>Watch demo <span aria-hidden="true">▶</span></a></div><p className="claim-note">Deployed role enforcement is documented under the demo identity boundary; production authentication is not claimed.</p></div><div className="project-media"><Image src="/images/opspilot-dashboard.png" alt="OpsPilot overview dashboard showing workflow activity and system health" fill sizes="(max-width: 900px) 100vw, 58vw" /></div></div></article>
        <article className="project-card project-amber"><div className="project-meta"><span>02 / FLAGSHIP</span><span>DOCS / DATA</span></div><div className="project-grid project-grid-reverse"><div className="project-copy"><p className="project-kicker">Evidence-backed document intelligence and reconciliation</p><h3>VerityDocs</h3><p>PDF, spreadsheet and image processing that keeps extracted values attached to their source. Real Dockerized Tesseract OCR, bounding-box provenance, deterministic financial checks and human review are visible in the public proof.</p><div className="proof-list"><span>49 backend tests</span><span>Tesseract OCR</span><span>Bounding-box evidence</span><span>FIN-001 review</span></div><div className="project-links"><ArrowLink href={proofLinks.veritydocs.live}>Live demo</ArrowLink><ArrowLink href={proofLinks.veritydocs.repo}>GitHub</ArrowLink><ArrowLink href={proofLinks.veritydocs.evidence}>Evidence</ArrowLink><a className="video-link" href={proofLinks.veritydocs.video}>Watch demo <span aria-hidden="true">▶</span></a></div><p className="claim-note">The verified public demo uses SQLite and synchronous processing; the Postgres / Redis / worker topology remains staged.</p></div><div className="project-media"><Image src="/images/veritydocs-evidence.png" alt="VerityDocs evidence viewer showing a selected field and source-level provenance" fill sizes="(max-width: 900px) 100vw, 58vw" /></div></div></article>
        <article className="small-project"><div><p className="eyebrow">03 / EVAL INFRASTRUCTURE</p><h3>EvalForge</h3></div><p>Regression testing for LLM, RAG and agent systems with versioned datasets, deterministic graders, failure taxonomy and release gates that can block regressions even when headline metrics improve.</p><div className="small-project-links"><ArrowLink href={proofLinks.evalforge.live}>Live dashboard</ArrowLink><ArrowLink href={proofLinks.evalforge.repo}>View repository</ArrowLink></div></article>
        <article className="small-project"><div><p className="eyebrow">04 / AGENT RELIABILITY</p><h3>TraceBrowser</h3></div><p>Replayable browser automation with bounded execution, assertions, checkpoints, screenshots and evidence for every action. Built around explicit failure states rather than opaque autonomy.</p><div className="small-project-links"><ArrowLink href={proofLinks.tracebrowser.live}>Live dashboard</ArrowLink><ArrowLink href={proofLinks.tracebrowser.repo}>View repository</ArrowLink></div></article>
        <article className="small-project"><div><p className="eyebrow">05 / CONTROLLED ACTION</p><h3>Axiom AP Agent</h3></div><p>Accounts-payable automation prototype focused on deterministic parsing, payment-policy controls, idempotency and audit logging. The execution-authority boundary stays separate from agent reasoning.</p><ArrowLink href="https://github.com/ANKOHR/axiom-ap-agent-prototype">View repository</ArrowLink></article>
      </section>

      <section className="capabilities-section section-shell" id="capabilities"><div className="section-heading"><div><p className="eyebrow">CAPABILITIES</p><h2>Useful at the seams.</h2></div><p>Backend systems, model boundaries and the operational detail between them.</p></div><div className="capability-grid">{capabilities.map((capability, index) => <div className="capability" key={capability}><span>{String(index + 1).padStart(2, "0")}</span><strong>{capability}</strong></div>)}</div></section>

      <section className="about-section section-shell" id="about"><div className="about-copy"><p className="eyebrow">ABOUT</p><h2>Curious about systems that have to hold up outside the notebook.</h2><p>I’m Henry, a Year 13 student at Richard Challoner School building practical software around messy inputs, explicit boundaries and observable outcomes.</p><p>I’m looking for scoped, part-time remote work where I can contribute to agent evaluation, AI engineering, backend systems, integrations, reliability tooling or internal automation.</p></div><div className="about-details"><div><span>EDUCATION</span><strong>Richard Challoner School</strong><small>A Levels: Mathematics, Physics and German · Year 13</small></div><div><span>LANGUAGES</span><strong>English · French · German</strong></div><div><span>AVAILABILITY</span><strong>Scoped part-time work alongside school</strong><small>Remote technical projects, trials or junior contributions</small></div><div><span>CONTACT</span><strong><a href="mailto:henry.williams85.contact@gmail.com">henry.williams85.contact@gmail.com</a></strong><small><ExternalLink href="https://github.com/ANKOHR">github.com/ANKOHR</ExternalLink></small></div></div></section>

      <footer className="site-footer section-shell"><span>Henry Williams / Software & Applied AI Engineer</span><span>Built with evidence, not adjectives.</span><a href="#top">Back to top ↑</a></footer>
    </main>
  );
}
