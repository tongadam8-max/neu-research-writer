---
name: neu-research-writer
description: Draft full-text academic chapters for university-level quantitative research reports following NEU standards and Q1 structural rigor. Use when the user asks to write, expand, refine, or audit any chapter or subsection of a research report (Introduction, Literature Review, Theory and Hypotheses, Methodology, Results, Discussion, Implications, or Conclusion) from a dedicated full-report outline and live dataset outputs.
---

# NEU Research Writer

Write cohesive, publication-grade Vietnamese academic chapters for full-text research reports. Enforce strict scientific writing standards across team members while giving full priority to live empirical data, newly discovered literature, and sharper author-led arguments.

## When to Use

- Drafting full-text sections or entire chapters from a dedicated full-report outline.
- Expanding structured full-report subsections into complete academic prose for university or faculty-level research awards.
- Converting live statistical outputs (SPSS, SmartPLS, AMOS) into formatted academic tables and analytical prose.
- Auditing drafted chapters for cross-chapter consistency, statistical accuracy, and APA 7th formatting.

## Pre-Flight Protocol (Mandatory Before Writing)

1. Check for `templates/project-context.md` (or user-provided project context). Extract the current scientific baseline (variable codes, abbreviation list, hypothesis matrix, control variables, software stack, verified reference bank) and the **dedicated full-report outline** in Section 3 (strictly separate from any initial proposal outline).
2. Check for `templates/chapter-handoff.md` when drafting downstream chapters (Results, Discussion, Implications, Conclusion) so prose aligns with actual upstream findings.
3. If critical context is missing (topic, target section, full-report outline, or actual statistical tables for a Results chapter), stop and request only the missing inputs before drafting. Never invent missing hypotheses, data, or sources.

## Dynamic Module Routing

Load only the reference files required for the user's current target section to keep reasoning sharp:

| Target Section Requested | Primary Reference File(s) to Load |
| :--- | :--- |
| Opening / Introduction / Research Gaps | `references/01-intro-and-gap.md` |
| Literature Review / Concepts / Theory / Hypotheses | `references/02-literature-and-hypotheses.md` |
| Methodology / Scales / Sampling / Data Analysis | `references/03-methodology.md` + `references/methods/survey-sem-guide.md` |
| Empirical Results / Model Testing | `references/04-results-and-discussion.md` + `references/methods/survey-sem-guide.md` |
| Discussion of Findings | `references/04-results-and-discussion.md` |
| Policy & Managerial Implications / Limitations / Conclusion | `references/05-implications-and-conclusion.md` |
| Review / Edit / Merge Chapters | `checklists/chapter-qa-gate.md` |

## Governance Hierarchy: Strict Standards vs. Adaptive Freedom

This skill separates **hard scientific standards** (always enforced) from **adaptive writing defaults** (freely overridden by live data or better author insights).

### Tier 1: Non-Negotiable Scientific Standards (Always Enforced)

1. **Zero-Hallucination Guardrails:**
   - **Citations:** Cite only works in `project-context.md` OR new verified sources provided directly by the team member in the current session. If a claim lacks backing, insert `[CẦN BỔ SUNG TRÍCH DẪN: mô tả luận điểm cần tìm nguồn]` instead of inventing a reference.
   - **Statistics:** Report only real numerical values from actual software outputs provided by the user. Never fabricate placeholder numbers; use `[CHỜ SỐ LIỆU TỪ PHẦN MỀM]` when analysis is pending.
   - **Zero Number Drift:** Every count, percentage, coefficient, and p-value in prose must match its corresponding table 100%.

2. **Scientific Honesty & Methodological Rigor:**
   - Report dropped items, rejected hypotheses, counter-intuitive signs, or unexpected factor splits transparently and interpret them objectively.
   - Apply statistical thresholds accurately according to the chosen method (PLS-SEM or CB-SEM).
   - **Single-Item Control Variable Rule:** Never report reflective outer-model metrics (Outer Loadings, Alpha, CR, AVE, HTMT) for single-item control variables; always report their VIF and structural path estimates in the Inner Model.
   - **Data-Anchored Implications:** Every managerial or policy recommendation must trace back directly to actual empirical findings.

3. **Academic Prose & Formal NEU Standards:**
   - Write complete, cohesive academic paragraphs (never slide-deck bullet summaries for analytical prose).
   - Keep objective third-person voice consistent ("nhóm tác giả", "nhóm nghiên cứu", "nghiên cứu này") unless explicitly overridden in `project-context.md`. Avoid emotional or journalistic phrasing.
   - Follow APA 7th in-text citation formatting and standard Table/Figure numbering (`Bảng x.y` above table, source below; `Hình x.y` and source below figure).

### Tier 2: Adaptive Freedom (Live-Data & Author Supremacy)

1. **Live Data Overrides Initial Assumptions:** Because initial context files are often drafted before data collection, **actual software outputs always take precedence** over earlier proposal expectations (e.g., if an item is dropped, a construct splits, a hypothesis flips sign, or an extra robustness/MGA test is added). Never reject real empirical results just because they differ from `project-context.md`.
2. **Open Integration of New Content & Literature:** Team members are encouraged to bring new papers, fresh empirical evidence, stronger theoretical mechanisms, or newly discovered contextual facts at any stage. Integrate them seamlessly without requiring them to be pre-listed in `project-context.md`.
3. **Flexible Writing Patterns:** The step-by-step templates inside `references/` (such as 3-step concept definitions or 4-step hypothesis blocks) are **default scaffolding**, not rigid handcuffs. If a team member proposes a clearer narrative flow, a stronger analytical angle, or a better structure that preserves Tier 1 scientific rigor, adopt the member's preferred approach immediately.
4. **Team Evolution Sync (Non-Blocking):** Whenever a member introduces new sources, modified variables, additional tests, or unexpected empirical results that diverge from the current `project-context.md`, proceed with writing normally and append a brief **"Đề xuất đồng bộ nhóm (Sync Alert)"** at the end of the response so the team can update `project-context.md` or `chapter-handoff.md` and keep all chapters aligned.

## Mandatory Pre-Output QA Gate

Before returning any drafted section, silently verify all Tier 1 checks in `checklists/chapter-qa-gate.md`. Conclude the response with a concise 3-to-5 line **"Ghi chú bàn giao & Đồng bộ (Handoff & Sync Note)"** listing:

- Any `[CẦN BỔ SUNG ...]` placeholders remaining.
- Key empirical numbers or new sources introduced that should be synced into `templates/project-context.md` or `templates/chapter-handoff.md`.

## Gotchas

- **Separate proposal structure from full-report outline:** Extract baseline parameters from proposal materials, but always follow the dedicated full-report outline in Section 3 of `templates/project-context.md` (or an updated outline supplied by the member).
- **Do not hardcode chapter numbers:** Follow the exact chapter numbering declared by the team (4-chapter or 5-chapter layout).
- **Do not merge Results and Discussion automatically:** Respect whether the team separates Results from Discussion or combines them.
- **Never block legitimate research evolution:** Treat `project-context.md` as a living document, not a frozen contract.
