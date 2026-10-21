# Graph Report - skolapraha  (2026-10-21)

## Corpus Check
- 85 files · ~238,791 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .woff2 16, .toml 4, (none) 4)

## Summary
- 2358 nodes · 5846 edges · 103 communities (88 shown, 15 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 190 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `24d89e54`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- live-browser.js
- modern-screenshot.umd.js
- Module
- quill.js
- el
- a
- setLiveState
- i
- initGlobalBar
- m
- w
- build.py
- news-editor.js
- renderDesignVisual
- initPageChat
- .forEach
- connectSSE
- n
- Components
- live.md
- mountSvelteComponentVariant
- New visual work
- b
- N
- new-work.md
- createLiveBrowserDomHelpers
- Rt
- onboard.md
- import_vos.py
- SKILL.md
- The Toolkit
- createLiveBrowserSessionState
- .listen
- o
- _
- serve
- x
- initGlobalBar
- animate.md
- Handle `generate`
- h
- Generate Report
- page.py
- optimize.md
- Scan mode (approach C: auto-extract, then confirm descriptive language)
- Hardening Dimensions
- Product
- critique.md
- Simplify the Design
- r
- re
- clarify.md
- Nielsen's 10 Heuristics
- Generate Combined Critique Report
- document.md
- polish.md
- quieter.md
- .remove
- captureElementToBlob
- actOnAgentTarget
- Init flow
- Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)
- make_logo.py
- vercel.json
- Common Cognitive Load Violations
- iOS platform
- Operate mode depth (and Read notes)
- Shape
- generate.md
- adapt.md
- Android platform
- Responsive Design
- Persona-Based Design Testing
- Extract Flow
- image
- Clean
- Generate Report
- Cognitive Load Assessment
- Impeccable Finish Reviewer
- Impeccable Manual Edit Applier
- live-browser-ignores.js
- $impeccable hooks
- render
- Diagnostic Scan
- Visualize: Direction Comps & Asset Production
- Analysis, architecture and roadmap
- R
- Impeccable Documenter
- Heuristics Scoring Guide
- Handler
- de
- Region map
- .mcp.json
- Brand compliance and the school logo
- CLAUDE.md
- QA report (19 Oct 2026)
- legacy-url-map.md
- enableInlineEdit
- Operate
- Persuade and Experience

## God Nodes (most connected - your core abstractions)
1. `de` - 67 edges
2. `_` - 66 edges
3. `i` - 64 edges
4. `Module()` - 51 edges
5. `m` - 51 edges
6. `length()` - 51 edges
7. `h()` - 48 edges
8. `o` - 47 edges
9. `s` - 45 edges
10. `n` - 42 edges

## Surprising Connections (you probably didn't know these)
- `Step 1: Parse the request` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/generate.md → build.py
- `Painted material` --references--> `image()`  [INFERRED]
  .agents/skills/impeccable/reference/region-map.md → static/js/vendor/quill-2.0.3/quill.js
- `After approval: the comp becomes a spec` --references--> `image()`  [INFERRED]
  .agents/skills/impeccable/reference/visualize.md → static/js/vendor/quill-2.0.3/quill.js
- `Where things are` --references--> `image()`  [INFERRED]
  README.md → static/js/vendor/quill-2.0.3/quill.js
- `Schema (for reference)` --references--> `events()`  [INFERRED]
  docs/publishing.md → api/page.py

## Import Cycles
- None detected.

## Communities (103 total, 15 thin omitted)

### Community 0 - "live-browser.js"
Cohesion: 0.03
Nodes (131): addManualContextText(), applyEditing(), applyGlobalBarLabelState(), applyLiveBarPreference(), applyPlaceholderSizingStyles(), beginEditPin(), bindEditBadgeProxy(), bufferToBase64() (+123 more)

### Community 1 - "modern-screenshot.umd.js"
Cohesion: 0.09
Nodes (55): ae(), be(), bt(), Ce(), s(), Ct(), de(), dt() (+47 more)

### Community 2 - "Module"
Cohesion: 0.06
Nodes (31): Module(), a(), Aa(), bb(), c(), cc(), a(), d() (+23 more)

### Community 3 - "quill.js"
Cohesion: 0.06
Nodes (48): attach(), buildItem(), buildLabel(), buildOptions(), buildPicker(), clean(), close(), constructor() (+40 more)

### Community 4 - "el"
Cohesion: 0.07
Nodes (58): actionLabel(), applyConfigureBarChrome(), bindConfigureCountPillTooltip(), bindConfigureInlineControlHover(), bindConfigureModifierPillHover(), buildConfigureActionControl(), buildConfigureCountControl(), buildConfigureRow() (+50 more)

### Community 6 - "setLiveState"
Cohesion: 0.10
Nodes (59): abortSvelteComponentInjection(), beginNewLiveConfiguration(), buildInsertPlaceholderSnapshotFromDom(), buildPickedAnchorSnapshot(), cancelEditing(), cancelEditingToPicking(), cancelInsertConfigure(), captureAndEmit() (+51 more)

### Community 7 - "i"
Cohesion: 0.06
Nodes (3): getText(), i, v()

### Community 8 - "initGlobalBar"
Cohesion: 0.16
Nodes (28): clearStoredManualApplyState(), handleManualEditActivity(), hasTextRows(), check(), hidePendingApplyDock(), manualApplyLoadingText(), manualApplyStateKey(), manualEditEventForCurrentPage() (+20 more)

### Community 9 - "m"
Cohesion: 0.08
Nodes (13): A(), add(), appendChild(), attachUI(), d(), getHTML(), insertAt(), keys() (+5 more)

### Community 10 - "w"
Cohesion: 0.12
Nodes (12): i(), d(), f, g, l, p, S, T() (+4 more)

### Community 11 - "build.py"
Cohesion: 0.10
Nodes (31): breadcrumbs(), crumbs_html(), _descendants(), enhance_body(), fix_img(), enhance_files(), event_slug(), events_list() (+23 more)

### Community 12 - "news-editor.js"
Cohesion: 0.08
Nodes (53): Accounts, sign-in, roles, Publishing (news, events, notices, galleries), Running it locally, Schema (for reference), Security, What can be published, addCategory(), afterSignIn() (+45 more)

### Community 13 - "renderDesignVisual"
Cohesion: 0.08
Nodes (35): buildCollapsible(), buildColorModels(), buildListHtml(), buildRadiiModels(), buildTypographyModels(), cssSafe(), designEmptyMessage(), escapeHtml() (+27 more)

### Community 14 - "initPageChat"
Cohesion: 0.08
Nodes (51): armPageChatForTyping(), attachSteerFocusDebug(), attachSteerFocusGuard(), buildSteerProcessingDots(), buildSteerQueueHint(), clearSteerAwaitTimer(), clearSteerFocusRecoverTimer(), collapsePageChat() (+43 more)

### Community 16 - "connectSSE"
Cohesion: 0.06
Nodes (84): applyParamDefaults(), applyParamValue(), applyPlaceholderDimensions(), applySavedSessionMeta(), buildParamsPanel(), checkpointPayload(), clampVariantIndex(), clearHandled() (+76 more)

### Community 18 - "Components"
Cohesion: 0.07
Nodes (29): Buttons, Calendar block, Colors, Components, Content-status bar (preview only), Content-status (preview only), Design System: VOŠZ Suverénního řádu maltézských rytířů, Do: (+21 more)

### Community 19 - "live.md"
Cohesion: 0.08
Nodes (22): Apply at system scale, Audit before choosing, Choose a strategy, Contrast and perception, Live-mode signature params, Verify, Visitor mode, Cleanup (+14 more)

### Community 20 - "mountSvelteComponentVariant"
Cohesion: 0.07
Nodes (44): abandonForeignSession(), abandonSupersededGo(), acceptedDomAlreadyClean(), applyOriginalAttrsToSvelteAnchor(), clearHandledWrapperReloadStamp(), commitAcceptedSvelteComponentToDom(), componentModuleCandidates(), copyToClipboard() (+36 more)

### Community 21 - "New visual work"
Cohesion: 0.08
Nodes (23): Monorepo notes, Opting out of the boot check, Step 1: Run the pass, Step 2: Act by severity, Step 3: Deprecated fields are binding, Step 4: Do not overclaim on truth drift, What this owns, and what it does not, 1. Decide what is already true (+15 more)

### Community 22 - "b"
Cohesion: 0.11
Nodes (13): b(), build(), copy(), descendant(), Et(), f, find(), getFormat() (+5 more)

### Community 23 - "N"
Cohesion: 0.10
Nodes (4): E(), g(), N, w()

### Community 24 - "new-work.md"
Cohesion: 0.10
Nodes (18): Recommended Actions, Craft (deprecated alias), Apply, Live-mode signature params, Set the spatial thesis, Two isolated assessments, Verify, Visitor mode (+10 more)

### Community 25 - "createLiveBrowserDomHelpers"
Cohesion: 0.16
Nodes (15): createLiveBrowserDomHelpers(), activeElementDeep(), cloneWithoutChrome(), copyTextViaSelection(), cssId(), liveUiRoot(), makeFrozenAnchor(), raiseHitModal() (+7 more)

### Community 27 - "onboard.md"
Cohesion: 0.09
Nodes (22): Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption, Guided Tours & Walkthroughs (+14 more)

### Community 28 - "import_vos.py"
Cohesion: 0.16
Nodes (13): convert(), fetch(), local_upload(), main(), NoRedirect, original_image(), page_fragment(), relink() (+5 more)

### Community 29 - "SKILL.md"
Cohesion: 0.10
Nodes (15): Before you finish, Scope is sovereign, The amplification, The skeleton test, Why it reads flat, Craft floor, Refuse, Verify (+7 more)

### Community 30 - "The Toolkit"
Cohesion: 0.10
Nodes (20): Animate complex properties, Assess What "Extraordinary" Means Here, For data-heavy interfaces, For functional UI, For performance-critical UI, For visual/marketing surfaces, Implement with Discipline, Interact with the device (+12 more)

### Community 31 - "createLiveBrowserSessionState"
Cohesion: 0.19
Nodes (17): createLiveBrowserSessionState(), clearHandled(), clearScrollY(), clearSession(), isHandled(), loadSession(), markHandled(), nextCheckpointRevision() (+9 more)

### Community 32 - ".listen"
Cohesion: 0.10
Nodes (21): Bt(), Ct(), formula(), Ft(), getBounds(), Gt(), hide(), e() (+13 more)

### Community 33 - "o"
Cohesion: 0.09
Nodes (22): applyDelta(), attribute(), deleteText(), descendants(), formatLine(), formatText(), getDelta(), h() (+14 more)

### Community 34 - "_"
Cohesion: 0.07
Nodes (16): _, ae, ce, delete(), _handleTokenChanged(), _initRealtimeClient(), _initSupabaseAuthClient(), insert() (+8 more)

### Community 35 - "serve"
Cohesion: 0.14
Nodes (15): Act on the receipt, Assemble and review, Plan and asset review, Plan, capture, serve, Core Rule, Decision Comps, Impeccable Asset Producer, Input Contract (+7 more)

### Community 37 - "initGlobalBar"
Cohesion: 0.10
Nodes (35): agentHasWorkInFlight(), agentStatusText(), barPaletteForTheme(), brandMarkSvg(), buildDesignHeader(), cursorForInsertAxis(), designPanelCss(), detectPageTheme() (+27 more)

### Community 38 - "animate.md"
Cohesion: 0.12
Nodes (14): Accessibility and control, Choose material by meaning, Find the job, Implement to the runtime, Set the motion thesis, Timing and easing, Verify, Visitor mode (+6 more)

### Community 39 - "Handle `generate`"
Cohesion: 0.08
Nodes (22): 1. Read the screenshot (if present), 2. Wrap the element, 3. Load the action's reference, 4. Plan three variants: identity first, then mode, then axes, 5. Apply the freeform prompt (if present), 6. Deliver variants, 7. Parameters (composition-sized, 0-4 per variant), 8. Signal done (+14 more)

### Community 40 - "h"
Cohesion: 0.11
Nodes (8): E(), ee(), h(), m, re(), se, te(), z()

### Community 41 - "Generate Report"
Cohesion: 0.13
Nodes (14): 1. Accessibility (A11y), 2. Performance, 3. Theming, 4. Responsive Design, 5. Implementation Integrity (CRITICAL), Audit Health Score, Detailed Findings by Severity, Diagnostic Scan (+6 more)

### Community 42 - "page.py"
Cohesion: 0.15
Nodes (16): as_event(), as_news(), cached(), dynamic_pages(), events(), file_info(), full_posts(), human_size() (+8 more)

### Community 43 - "optimize.md"
Cohesion: 0.14
Nodes (13): Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), Interaction to Next Paint (INP < 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance, Network Optimization (+5 more)

### Community 44 - "Scan mode (approach C: auto-extract, then confirm descriptive language)"
Cohesion: 0.15
Nodes (13): Component translation rules, Narrative mapping, Scan mode (approach C: auto-extract, then confirm descriptive language), Schema, Step 1: Find the design assets, Step 2: Auto-extract what can be auto-extracted, Step 2b: Stage the frontmatter, Step 3: Ask the user for qualitative language (+5 more)

### Community 45 - "Hardening Dimensions"
Cohesion: 0.15
Nodes (11): Accessibility Resilience, Assess Hardening Needs, Edge Cases & Boundary Conditions, Error Handling, Hardening Dimensions, Input Validation & Sanitization, Internationalization (i18n), Performance Resilience (+3 more)

### Community 46 - "Product"
Cohesion: 0.15
Nodes (12): Accessibility & Inclusion, Brand Commitments, Capabilities and Constraints, Evidence on Hand, Operating Context, Platform, Positioning, Product (+4 more)

### Community 47 - "critique.md"
Cohesion: 0.17
Nodes (11): Action Summary, Ask the User, Assessment A: Design Review, Assessment B: Detector + Browser Evidence, Assessment Orchestration, Deliver the Report, Hard Invariants, Persist the Snapshot (+3 more)

### Community 48 - "Simplify the Design"
Cohesion: 0.17
Nodes (11): Assess Current State, Code Simplification, Content Simplification, Document Removed Complexity, Information Architecture, Interaction Simplification, Layout Simplification, Plan Simplification (+3 more)

### Community 49 - "r"
Cohesion: 0.17
Nodes (7): C(), n(), r(), i, o, then(), ue()

### Community 50 - "re"
Cohesion: 0.13
Nodes (5): photos_of(), main(), Page, redirect_rules(), resolves()

### Community 51 - "clarify.md"
Cohesion: 0.18
Nodes (10): Actions and navigation, Audit the language, Errors and permissions, Forms, Help and instructional text, Loading, empty, and success states, Rewrite by function, Set the message hierarchy (+2 more)

### Community 52 - "Nielsen's 10 Heuristics"
Cohesion: 0.18
Nodes (11): 10. Help and Documentation, 1. Visibility of System Status, 2. Match Between System and Real World, 3. User Control and Freedom, 4. Consistency and Standards, 5. Error Prevention, 6. Recognition Rather Than Recall, 7. Flexibility and Efficiency of Use (+3 more)

### Community 53 - "Generate Combined Critique Report"
Cohesion: 0.18
Nodes (11): Design Health Score, Design Specificity Verdict, Generate Combined Critique Report, Minor Observations, Overall Impression, Persona Red Flags, Priority Issues, Questions to Consider (+3 more)

### Community 54 - "document.md"
Cohesion: 0.18
Nodes (10): Pitfalls, Seed mode, Step 1: Route through new-work's workshop, Step 2: Write seed DESIGN.md, Step 3: Confirm, Style guidelines, The frontmatter: token schema, The markdown body: eight sections (canonical order) (+2 more)

### Community 55 - "polish.md"
Cohesion: 0.18
Nodes (10): 1. Establish the system, 2. Gather the evidence, 3. Triage, 4. Polish the whole path, 5. Verify and finish, Color, imagery, and icons, Content and code, Flow and hierarchy (+2 more)

### Community 56 - "quieter.md"
Cohesion: 0.18
Nodes (10): Assess Current State, Color Refinement, Composition Refinement, Motion Reduction, Plan Refinement, Refine the Design, Simplification, Verify Quality (+2 more)

### Community 57 - ".remove"
Cohesion: 0.07
Nodes (16): c, clone(), deleteAt(), enforceAllowedChildren(), formatAt(), isolate(), moveChildren(), offset() (+8 more)

### Community 58 - "captureElementToBlob"
Cohesion: 0.12
Nodes (20): averageRgb01(), captureChromeNodes(), captureElementFromRenderedAncestor(), captureElementToBlob(), compileShader(), cssColorToRgb01(), dominantRgb01(), findBackdropAncestor() (+12 more)

### Community 59 - "actOnAgentTarget"
Cohesion: 0.29
Nodes (17): actOnAgentTarget(), agentTargetBusyReason(), agentTargetOverlayGone(), agentTargetTaken(), claimAgentTarget(), claimAndActOnAgentTarget(), declineAgentTargetBusy(), declineAgentTargetUnresolvable() (+9 more)

### Community 60 - "Init flow"
Cohesion: 0.20
Nodes (10): Completion gate, Init flow, Step 1: Load current state, Step 2: Explore the project, Step 3: Interview for product truth, Step 4: Write PRODUCT.md, Step 5: Record workflow defaults, Step 6: Wrap up or resume (+2 more)

### Community 61 - "Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)"
Cohesion: 0.20
Nodes (9): Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026), Documents, Events (12, all migrated), External links, Images, Inaccessible or missing source material, Interactive functionality on the old site, News (4 posts, all migrated, URLs unchanged) (+1 more)

### Community 62 - "make_logo.py"
Cohesion: 0.17
Nodes (6): lockup(), main(), shield(), text_path(), vos_lockup(), vos_text()

### Community 63 - "vercel.json"
Cohesion: 0.14
Nodes (13): includeFiles, buildCommand, cleanUrls, framework, functions, api/page.py, headers, installCommand (+5 more)

### Community 64 - "Common Cognitive Load Violations"
Cohesion: 0.22
Nodes (9): 1. The Wall of Options, 2. The Memory Bridge, 3. The Hidden Navigation, 4. The Jargon Barrier, 5. The Visual Noise Floor, 6. The Inconsistent Pattern, 7. The Multi-Task Demand, 8. The Context Switch (+1 more)

### Community 65 - "iOS platform"
Cohesion: 0.22
Nodes (9): Color & materials, Components & controls, iOS platform, Layout & structure, Motion, The iOS slop test, Touch targets, Typography (+1 more)

### Community 66 - "Operate mode depth (and Read notes)"
Cohesion: 0.22
Nodes (9): Color, Components, Layout, Motion, Operate mode depth (and Read notes), Product constraints, Product permissions, The product slop test (+1 more)

### Community 67 - "Shape"
Cohesion: 0.22
Nodes (8): Cadence, Confirm and stop, Phase 1: Discovery interview, Phase 2: Resolve the design direction, Phase 3: Write the brief, Round 1: purpose, people, and outcome, Round 2: material, behavior, and boundaries, Shape

### Community 68 - "generate.md"
Cohesion: 0.15
Nodes (11): Step 1: Parse the request, Step 2: Reuse the page, then start, Step 3: Generate, Step 4: Accept and close, append-arrays, append-string, Config drift, Consent prompt (use this phrasing) (+3 more)

### Community 69 - "adapt.md"
Cohesion: 0.08
Nodes (22): Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, Mobile Adaptation (Desktop → Mobile), Adaptation Strategies (+14 more)

### Community 70 - "Android platform"
Cohesion: 0.25
Nodes (8): Android platform, Color & theming, Components & motion, Layout & structure, The Android slop test, Touch targets, Typography, Verifying the build

### Community 71 - "Responsive Design"
Cohesion: 0.20
Nodes (10): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+2 more)

### Community 72 - "Persona-Based Design Testing"
Cohesion: 0.25
Nodes (8): 1. Impatient Power User: "Alex", 2. Confused First-Timer: "Jordan", 3. Accessibility-Dependent User: "Sam", 4. Deliberate Stress Tester: "Riley", 5. Distracted Mobile User: "Casey", Persona-Based Design Testing, Project-Specific Personas, Selecting Personas

### Community 73 - "Extract Flow"
Cohesion: 0.25
Nodes (7): Extract Flow, Step 1: Discover the Design System, Step 2: Identify Patterns, Step 3: Plan Extraction, Step 4: Extract & Enrich, Step 5: Migrate, Step 6: Document

### Community 74 - "image"
Cohesion: 0.25
Nodes (7): Commands, Documentation, Editorial workflow, Security notes, Shared code, vos.mojezdravka.cz, Where things are

### Community 76 - "Generate Report"
Cohesion: 0.29
Nodes (7): Audit Health Score, Detailed Findings by Severity, Executive Summary, Generate Report, Patterns & Systemic Issues, Platform Conformance Verdict, Positive Findings

### Community 77 - "Cognitive Load Assessment"
Cohesion: 0.29
Nodes (7): Cognitive Load Assessment, Cognitive Load Checklist, Extraneous Load: Bad Design, Germane Load: Learning Effort, Intrinsic Load: The Task Itself, The Working Memory Rule, Three Types of Cognitive Load

### Community 78 - "Impeccable Finish Reviewer"
Cohesion: 0.29
Nodes (6): Checks, in order, Disposition, Impeccable Finish Reviewer, Input Contract, Output Contract, Verdict Pass

### Community 79 - "Impeccable Manual Edit Applier"
Cohesion: 0.29
Nodes (6): Checks, Entry Atomicity, Impeccable Manual Edit Applier, Input Contract, Output Contract, Workflow

### Community 81 - "live-browser-ignores.js"
Cohesion: 0.52
Nodes (6): globToRegex(), matchesScope(), normalizeIgnoreRule(), normalizeIgnoreValue(), pageCandidates(), resolveDetectIgnores()

### Community 82 - "$impeccable hooks"
Cohesion: 0.33
Nodes (6): Constraints, Failure modes, Flow, $impeccable hooks, Routing, Triage findings

### Community 83 - "render"
Cohesion: 0.16
Nodes (13): handler, listing(), not_found(), render(), render_event(), build(), event_when(), plain() (+5 more)

### Community 84 - "Diagnostic Scan"
Cohesion: 0.33
Nodes (6): 1. Accessibility (VoiceOver / TalkBack), 2. Performance, 3. Appearance & Theming, 4. Platform Conformance (CRITICAL), 5. Adaptivity, Diagnostic Scan

### Community 85 - "Visualize: Direction Comps & Asset Production"
Cohesion: 0.33
Nodes (5): After approval: the comp becomes a spec, Generate three compositional options, One approval point, Plates and provenance, Visualize: Direction Comps & Asset Production

### Community 86 - "Analysis, architecture and roadmap"
Cohesion: 0.33
Nodes (5): Analysis, architecture and roadmap, Architecture, Reference repositories (read only, not modified), Roadmap (all done in this session), Tools

### Community 88 - "Impeccable Documenter"
Cohesion: 0.40
Nodes (4): Impeccable Documenter, Input Contract, Output Contract, Workflow

### Community 89 - "Heuristics Scoring Guide"
Cohesion: 0.50
Nodes (4): Heuristics Scoring Guide, Issue Severity (P0–P3), Reference Material, Score Summary

### Community 92 - "Region map"
Cohesion: 0.40
Nodes (4): Containment, Painted material, Region map, What varies independently

### Community 94 - "Brand compliance and the school logo"
Cohesion: 0.50
Nodes (3): Brand compliance and the school logo, Open approvals, School logo, banner and photographs

### Community 96 - "QA report (19 Oct 2026)"
Cohesion: 0.33
Nodes (5): Cross-device audit and publishing workflow (21 October 2026), Pre-presentation audit (19 Oct 2026, after the header change), QA report (19 Oct 2026), Shared Supabase database (21 October 2026), Unresolved

### Community 100 - "enableInlineEdit"
Cohesion: 0.22
Nodes (9): collectEditableTextRows(), visit(), own(), pickable(), stopFocusOutIntoChrome(), enableInlineEdit(), layoutFlowChildren(), onInlineInput() (+1 more)

### Community 107 - "Operate"
Cohesion: 0.50
Nodes (3): Comps, Directions, Operate

### Community 108 - "Persuade and Experience"
Cohesion: 0.50
Nodes (3): Comps, Directions, Persuade and Experience

## Knowledge Gaps
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Monorepo notes` connect `New visual work` to `m`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `i` (e.g. with `e()` and `i()`) actually correct?**
  _`i` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `live-browser.js` be split into smaller, more focused modules?**
  _Cohesion score 0.03137254901960784 - nodes in this community are weakly interconnected._
- **Why does `e()` connect `.listen` to `modern-screenshot.umd.js`, `Module`, `quill.js`, `o`, `_`, `i`, `m`, `.forEach`, `b`, `N`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Module()` (e.g. with `ac()` and `$b()`) actually correct?**
  _`Module()` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Should `modern-screenshot.umd.js` be split into smaller, more focused modules?**
  _Cohesion score 0.08897243107769423 - nodes in this community are weakly interconnected._
- **Why does `_` connect `_` to `.listen`, `x`, `a`, `h`, `w`, `r`, `n`, `de`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._