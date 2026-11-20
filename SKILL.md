---
name: neu-research-writer
description: Draft full-text academic chapters for university-level quantitative research reports following NEU standards and Q1 structural rigor. Use when the user asks to write, expand, refine, or audit any chapter or subsection of a research report (Introduction, Literature Review, Theory and Hypotheses, Methodology, Results, Discussion, Implications, or Conclusion) from a dedicated full-report outline and live dataset outputs.
---

# NEU Research Writer

Write cohesive, publication-grade Vietnamese academic chapters for full-text research reports. Enforce strict scientific writing standards across team members while giving full priority to live empirical data, newly discovered literature, sharper author-led arguments, and rigorous two-pass quality self-auditing.

## When to Use

- Drafting full-text sections or entire chapters from a dedicated full-report outline.
- Expanding structured full-report subsections into complete academic prose for university or faculty-level research awards.
- Converting live statistical outputs (SPSS, SmartPLS, AMOS) into formatted academic tables and analytical prose.
- Auditing drafted chapters for cross-chapter consistency, statistical accuracy, presentation quality, and APA 7th formatting.
- Compiling chapter drafts and exporting publication-grade Word reports (.docx) using NEU formatting standards.

## Pre-Flight Protocol & Smart Clarification (Before Writing)

1. Check for `templates/project-context.md` (or user-provided project context). Extract the current scientific baseline (variable codes, abbreviation list, hypothesis matrix, control variables, software stack, verified reference bank) and the **dedicated full-report outline** in Section 3 (strictly separate from any initial proposal outline).
2. Check for `templates/chapter-handoff.md` when drafting downstream chapters (Results, Discussion, Implications, Conclusion) so prose aligns with actual upstream findings.
3. **Smart Clarification Gate (Pause Only When Truly Needed):**
   - Proceed directly to drafting whenever the member's intent, target section, and required inputs are clear. Never stall progress with trivial questions.
   - Pause BEFORE writing only if: (a) essential inputs are missing (such as raw tables for a Results section or the target outline), (b) the member's instruction is genuinely ambiguous, or (c) the requested angle risks drifting away from the core research questions or theoretical scope.
   - When pausing, ask a maximum of **2 to 3 concise, high-impact questions** with concrete recommended options so the member can decide quickly.

## Dynamic Module Routing

Load only the reference files required for the user's current target section to keep reasoning sharp:

| Target Section Requested | Primary Reference File(s) to Load |
| :--- | :--- |
| Dựng Outline / Cấu trúc Báo cáo toàn văn | `references/00-outline-architect.md` |
| Opening / Introduction / Research Gaps | `references/01-intro-and-gap.md` |
| Literature Review / Concepts / Theory / Hypotheses | `references/02-literature-and-hypotheses.md` |
| Methodology / Scales / Sampling / Data Analysis | `references/03-methodology.md` + `references/methods/survey-sem-guide.md` |
| Empirical Results / Model Testing | `references/04-results-and-discussion.md` + `references/methods/survey-sem-guide.md` |
| Discussion of Findings | `references/04-results-and-discussion.md` |
| Policy & Managerial Implications / Limitations / Conclusion | `references/05-implications-and-conclusion.md` |
| Lập Ma trận & Trích xuất Tóm tắt Bài báo | `references/06-literature-matrix-extractor.md` |
| Rà soát Trích dẫn & Phụ lục | `references/07-citations-and-appendices.md` |
| Ghép file, Giảm Turnitin & Paraphrase | `references/08-merge-and-paraphrase.md` |
| Ôn tập & Giả lập Hội đồng Bảo vệ | `references/09-defense-and-viva-prep.md` |
| Xuất Báo cáo toàn văn sang Word (.docx chuẩn NEU) | Chạy script `python scripts/export_to_docx.py [drafts]` |
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
   - Keep objective third-person voice consistent ("nhóm tác giả", "nhóm nghiên cứu", "nghiên cứu này") unless explicitly overridden in `project-context.md`. Avoid emotional, repetitive, or journalistic phrasing.
   - Follow APA 7th in-text citation formatting and standard Table/Figure numbering (`Bảng x.y` above table, source below; `Hình x.y` and source below figure).

### Tier 2: Adaptive Freedom (Live-Data & Author Supremacy)

1. **Live Data Overrides Initial Assumptions:** Because initial context files are often drafted before data collection, **actual software outputs always take precedence** over earlier proposal expectations (e.g., if an item is dropped, a construct splits, a hypothesis flips sign, or an extra robustness/MGA test is added). Never reject real empirical results just because they differ from `project-context.md`.
2. **Open Integration of New Content & Literature:** Team members are encouraged to bring new papers, fresh empirical evidence, stronger theoretical mechanisms, or newly discovered contextual facts at any stage. Integrate them seamlessly without requiring them to be pre-listed in `project-context.md`.
3. **Flexible Writing Patterns:** The step-by-step templates inside `references/` (such as 3-step concept definitions or 4-step hypothesis blocks) are **default scaffolding**, not rigid handcuffs. If a team member proposes a clearer narrative flow, a stronger analytical angle, or a better structure that preserves Tier 1 scientific rigor, adopt the member's preferred approach immediately.
4. **Team Evolution Sync (Non-Blocking):** Whenever a member introduces new sources, modified variables, additional tests, or unexpected empirical results that diverge from the current `project-context.md`, proceed with writing normally and note the change in the closing Sync Alert.

## Mandatory 2-Pass Self-Audit & Post-Write Protocol

Before delivering any drafted text (or finalizing edits to a `.md` chapter file), execute two distinct silent revision passes using `checklists/chapter-qa-gate.md`. Fix all defects directly in the text before showing the final version to the user:

- **Pass 1 - Substance, Logic & Data Integrity Audit:** Verify every number against tables (totals, percentages, coefficients, p-values), verify every citation against provided sources, check alignment with theoretical mechanisms and control-variable rules, and ensure claims never overreach the evidence.
- **Pass 2 - Presentation, Format & Academic Polish Audit:** Verify `Bảng x.y` / `Hình x.y` numbering and placement, decimal separator consistency, APA 7th in-text format, smooth paragraph transitions, and strict NEU academic tone. Strip out robotic AI clichés, filler adjectives, and repetitive sentence openings.

*(File-editing rule: When writing directly to a workspace `.md` file, write the draft, re-read the file to perform Pass 1 and Pass 2 edits in place, and present only the clean final result.)*

### Required Closing Notes (Concise, Objective)

At the end of every drafted section, append two brief blocks:

1. **Phản biện trọng tâm (Objective Focus Review):**
   - Point out ONLY genuine gaps where the current input under-explores the core research focus (e.g., describing symptoms without linking to underlying theory, stating a rejected hypothesis without explaining contextual mechanisms, or recommendations missing the strongest predictor).
   - **Strict Anti-Nitpicking Rule:** Never invent weaknesses just to fill this section. If the member's content is already tight and on-focus, state clearly: *"Nội dung đã bám sát trọng tâm nghiên cứu và cơ chế cốt lõi của đề tài."*
2. **Ghi chú bàn giao & Đồng bộ (Handoff & Sync Note):**
   - List remaining `[CẦN BỔ SUNG ...]` placeholders (if any).
   - List new verified sources, modified variables, or empirical metrics that should be synced into `templates/project-context.md` or `templates/chapter-handoff.md`.

## Gotchas

- **Separate proposal structure from full-report outline:** Extract baseline parameters from proposal materials, but always follow the dedicated full-report outline in Section 3 of `templates/project-context.md` (or an updated outline supplied by the member).
- **Do not hardcode chapter numbers:** Follow the exact chapter numbering declared by the team (4-chapter or 5-chapter layout).
- **Do not merge Results and Discussion automatically:** Respect whether the team separates Results from Discussion or combines them.
- **Never block legitimate research evolution:** Treat `project-context.md` as a living document, not a frozen contract.
- **Never fabricate audit feedback:** Both Pass 1/Pass 2 edits and the Focus Review must be strictly grounded in actual text defects or genuine analytical gaps.
