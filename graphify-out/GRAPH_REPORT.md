# Graph Report - skolapraha  (2026-11-02)

## Corpus Check
- 88 files · ~179,212 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .woff2 16, .toml 4, (none) 4)

## Summary
- 2412 nodes · 5340 edges · 118 communities (103 shown, 15 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 196 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1c778ba8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- live-browser.js
- modern-screenshot.umd.js
- Module
- quill.js
- el
- showToast
- setLiveState
- i
- initGlobalBar
- m
- o
- build.py
- news-editor.js
- renderDesignVisual
- initPageChat
- s
- connectSSE
- _
- Components
- live.md
- a
- New visual work
- captureElementToBlob
- adapt.md
- new-work.md
- createLiveBrowserDomHelpers
- c
- onboard.md
- import_vos.py
- SKILL.md
- The Toolkit
- createLiveBrowserSessionState
- .listen
- N
- w
- serve
- create
- initGlobalBar
- animate.md
- Handle `generate`
- n
- Generate Report
- optimize
- optimize.md
- Scan mode (approach C: auto-extract, then confirm descriptive language)
- Hardening Dimensions
- Product
- critique.md
- Simplify the Design
- x
- b
- clarify.md
- Nielsen's 10 Heuristics
- Generate Combined Critique Report
- document.md
- polish.md
- quieter.md
- adapt.native.md
- make_logo.py
- h
- Init flow
- Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)
- mountSvelteComponentVariant
- vercel.json
- Common Cognitive Load Violations
- iOS platform
- Operate mode depth (and Read notes)
- Shape
- page.py
- actOnAgentTarget
- Android platform
- colorize.md
- Persona-Based Design Testing
- Extract Flow
- image
- resolveLiveInjectionAnchor
- Generate Report
- Cognitive Load Assessment
- Impeccable Finish Reviewer
- Impeccable Manual Edit Applier
- live-browser-ignores.js
- o
- render_simple
- Diagnostic Scan
- Visualize: Direction Comps & Asset Production
- Analysis, architecture and roadmap
- ci.yml
- Impeccable Documenter
- Heuristics Scoring Guide
- $impeccable hooks
- de
- Region map
- Handler
- Brand compliance and the school logo
- CLAUDE.md
- QA report (19 Oct 2026)
- legacy-url-map.md
- Clean
- rt
- make_og.py
- d
- re
- u
- .mcp.json
- Operate
- .getClaims
- serve
- c
- Publishing (news, events, notices, galleries)
- interface
- k
- Z
- Persuade and Experience
- Read
- 3. Choose the right amount of invention

## God Nodes (most connected - your core abstractions)
1. `_` - 73 edges
2. `de` - 67 edges
3. `i` - 57 edges
4. `Module()` - 50 edges
5. `h()` - 48 edges
6. `n` - 46 edges
7. `s` - 42 edges
8. `o` - 39 edges
9. `m` - 38 edges
10. `a` - 37 edges

## Surprising Connections (you probably didn't know these)
- `Step 1: Parse the request` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/generate.md → build.py
- `3. Load the action's reference` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/live.md → build.py
- `Phase D: Squint test` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/live.md → build.py
- `After approval: the comp becomes a spec` --references--> `image()`  [INFERRED]
  .agents/skills/impeccable/reference/visualize.md → static/js/vendor/quill-2.0.3/quill.js
- `Schema (for reference)` --references--> `events()`  [INFERRED]
  docs/publishing.md → api/page.py

## Import Cycles
- None detected.

## Communities (118 total, 15 thin omitted)

### Community 0 - "live-browser.js"
Cohesion: 0.04
Nodes (96): addManualContextText(), applyGlobalBarLabelState(), applyLiveBarPreference(), applyPlaceholderSizingStyles(), bindEditBadgeProxy(), buildInsertPlaceholderSnapshotFromDom(), buildLocatorForLeaf(), buildPickedAnchorSnapshot() (+88 more)

### Community 1 - "modern-screenshot.umd.js"
Cohesion: 0.09
Nodes (53): ae(), be(), bt(), Ce(), Ct(), de(), dt(), _e() (+45 more)

### Community 2 - "Module"
Cohesion: 0.06
Nodes (34): Module(), a(), Aa(), bb(), c(), cc(), a(), d() (+26 more)

### Community 3 - "quill.js"
Cohesion: 0.05
Nodes (35): build(), buildItem(), buildLabel(), buildOptions(), buildPicker(), close(), constructor(), copy() (+27 more)

### Community 4 - "el"
Cohesion: 0.07
Nodes (54): actionLabel(), applyConfigureBarChrome(), bindConfigureCountPillTooltip(), bindConfigureInlineControlHover(), bindConfigureModifierPillHover(), buildConfigureActionControl(), buildConfigureCountControl(), buildConfigureRow() (+46 more)

### Community 5 - "showToast"
Cohesion: 0.07
Nodes (67): abandonForeignSession(), abandonSupersededGo(), abortSvelteComponentInjection(), cleanup(), cleanupAcceptedSession(), clearHandled(), clearMountErrorCard(), clearScrollY() (+59 more)

### Community 6 - "setLiveState"
Cohesion: 0.15
Nodes (43): applyEditing(), beginNewLiveConfiguration(), cancelEditing(), cancelEditingToPicking(), cancelInsertConfigure(), captureAndEmit(), clearAnnotations(), clearInsertPicking() (+35 more)

### Community 7 - "i"
Cohesion: 0.06
Nodes (5): getText(), handleDOM(), i, removeFormat(), U()

### Community 8 - "initGlobalBar"
Cohesion: 0.19
Nodes (23): clearStoredManualApplyState(), fetchPendingCount(), handleManualEditActivity(), hidePendingApplyDock(), manualApplyLoadingText(), manualApplyStateKey(), manualEditEventForCurrentPage(), numberOrNull() (+15 more)

### Community 9 - "m"
Cohesion: 0.10
Nodes (5): attachUI(), g(), getHTML(), m, query()

### Community 10 - "o"
Cohesion: 0.09
Nodes (20): a, applyDelta(), attach(), deleteText(), f, formatLine(), formatText(), getDelta() (+12 more)

### Community 11 - "build.py"
Cohesion: 0.07
Nodes (45): render_event(), breadcrumbs(), build(), crumbs_html(), _descendants(), enhance_body(), fix_img(), enhance_files() (+37 more)

### Community 12 - "news-editor.js"
Cohesion: 0.10
Nodes (47): addCategory(), afterSignIn(), askCode(), attachmentRow(), categories(), clearPhoto(), dateHint(), del() (+39 more)

### Community 13 - "renderDesignVisual"
Cohesion: 0.08
Nodes (39): buildCollapsible(), buildColorModels(), buildDesignHeader(), buildListHtml(), buildRadiiModels(), buildTypographyModels(), cssSafe(), designEmptyMessage() (+31 more)

### Community 14 - "initPageChat"
Cohesion: 0.08
Nodes (52): armPageChatForTyping(), attachSteerFocusDebug(), attachSteerFocusGuard(), buildSteerProcessingDots(), buildSteerQueueHint(), clearSteerAwaitTimer(), clearSteerFocusRecoverTimer(), collapsePageChat() (+44 more)

### Community 15 - "s"
Cohesion: 0.06
Nodes (3): h(), register(), s

### Community 16 - "connectSSE"
Cohesion: 0.07
Nodes (59): applyParamDefaults(), applyParamValue(), applyPlaceholderDimensions(), applySavedSessionMeta(), checkpointPayload(), clampVariantIndex(), closedClipPath(), commitAcceptedVariantToDom() (+51 more)

### Community 17 - "_"
Cohesion: 0.05
Nodes (19): _, ae, b, C(), ce, constructor(), E(), ee() (+11 more)

### Community 18 - "Components"
Cohesion: 0.07
Nodes (29): Buttons, Calendar block, Colors, Components, Content-status bar (preview only), Content-status (preview only), Design System: VOŠZ Suverénního řádu maltézských rytířů, Do: (+21 more)

### Community 19 - "live.md"
Cohesion: 0.07
Nodes (26): Step 1: Parse the request, Step 2: Reuse the page, then start, Step 3: Generate, Step 4: Accept and close, Cleanup, Exit, First-time setup, Handle `accept` (+18 more)

### Community 20 - "a"
Cohesion: 0.08
Nodes (4): a, d(), k, update()

### Community 21 - "New visual work"
Cohesion: 0.15
Nodes (13): Step 1: Run the pass, 1. Decide what is already true, 2. Ask what will change the work, 4. Commit the world, 5. Record the decision, 6. Build with full commitment, 7. Inspect and finish, Both paths (+5 more)

### Community 22 - "captureElementToBlob"
Cohesion: 0.08
Nodes (37): averageRgb01(), beginEditPin(), bufferToBase64(), buildAnnotationsForCapture(), buildPinElement(), cancelEditingPin(), captureChromeNodes(), captureElementFromRenderedAncestor() (+29 more)

### Community 23 - "adapt.md"
Cohesion: 0.08
Nodes (25): Assess Adaptation Challenge, Breakpoints: Content-Driven, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Detect Input Method, Not Just Screen Size, Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Patterns (+17 more)

### Community 24 - "new-work.md"
Cohesion: 0.09
Nodes (21): Recommended Actions, Craft (deprecated alias), Monorepo notes, Opting out of the boot check, Step 2: Act by severity, Step 3: Deprecated fields are binding, Step 4: Do not overclaim on truth drift, What this owns, and what it does not (+13 more)

### Community 25 - "createLiveBrowserDomHelpers"
Cohesion: 0.16
Nodes (15): createLiveBrowserDomHelpers(), activeElementDeep(), cloneWithoutChrome(), copyTextViaSelection(), cssId(), liveUiRoot(), makeFrozenAnchor(), raiseHitModal() (+7 more)

### Community 26 - "c"
Cohesion: 0.12
Nodes (3): c, j, normalizeNative()

### Community 27 - "onboard.md"
Cohesion: 0.09
Nodes (22): Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption, Guided Tours & Walkthroughs (+14 more)

### Community 28 - "import_vos.py"
Cohesion: 0.17
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
Cohesion: 0.09
Nodes (25): vt(), Bt(), Ct(), Et(), F(), Ft(), Gt(), hide() (+17 more)

### Community 33 - "N"
Cohesion: 0.11
Nodes (5): E(), N, q(), R(), w()

### Community 34 - "w"
Cohesion: 0.11
Nodes (11): f, g, i, l, p, S, T(), u (+3 more)

### Community 35 - "serve"
Cohesion: 0.22
Nodes (7): Core Rule, Decision Comps, Impeccable Asset Producer, Input Contract, Output Contract, Review handoff, The job

### Community 36 - "create"
Cohesion: 0.21
Nodes (5): create(), descendant(), descendants(), et, nt()

### Community 37 - "initGlobalBar"
Cohesion: 0.08
Nodes (41): agentHasWorkInFlight(), agentStatusText(), barPaletteForTheme(), brandMarkSvg(), buildParamsPanel(), designPanelCss(), detectPageTheme(), own() (+33 more)

### Community 38 - "animate.md"
Cohesion: 0.12
Nodes (14): Accessibility and control, Choose material by meaning, Find the job, Implement to the runtime, Set the motion thesis, Timing and easing, Verify, Visitor mode (+6 more)

### Community 39 - "Handle `generate`"
Cohesion: 0.12
Nodes (16): 1. Read the screenshot (if present), 2. Wrap the element, 3. Load the action's reference, 4. Plan three variants: identity first, then mode, then axes, 5. Apply the freeform prompt (if present), 6. Deliver variants, 7. Parameters (composition-sized, 0-4 per variant), 8. Signal done (+8 more)

### Community 41 - "Generate Report"
Cohesion: 0.13
Nodes (14): 1. Accessibility (A11y), 2. Performance, 3. Theming, 4. Responsive Design, 5. Implementation Integrity (CRITICAL), Audit Health Score, Detailed Findings by Severity, Diagnostic Scan (+6 more)

### Community 42 - "optimize"
Cohesion: 0.13
Nodes (17): appendChild(), clone(), deleteAt(), enforceAllowedChildren(), format(), formatAt(), insertAt(), isolate() (+9 more)

### Community 43 - "optimize.md"
Cohesion: 0.14
Nodes (13): Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), Interaction to Next Paint (INP < 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance, Network Optimization (+5 more)

### Community 44 - "Scan mode (approach C: auto-extract, then confirm descriptive language)"
Cohesion: 0.15
Nodes (13): Component translation rules, Narrative mapping, Scan mode (approach C: auto-extract, then confirm descriptive language), Schema, Step 1: Find the design assets, Step 2: Auto-extract what can be auto-extracted, Step 2b: Stage the frontmatter, Step 3: Ask the user for qualitative language (+5 more)

### Community 45 - "Hardening Dimensions"
Cohesion: 0.17
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

### Community 50 - "b"
Cohesion: 0.17
Nodes (6): A(), b(), find(), getFormat(), n(), O()

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

### Community 57 - "adapt.native.md"
Cohesion: 0.25
Nodes (7): Adaptation Strategies, Assess Adaptation Challenge, Implement & Verify, Orientation & foldables, Phone → Tablet (iPad / large screens), Platform → platform (iOS ↔ Android), Web → native (porting a website or web app)

### Community 58 - "make_logo.py"
Cohesion: 0.17
Nodes (6): lockup(), main(), shield(), text_path(), vos_lockup(), vos_text()

### Community 59 - "h"
Cohesion: 0.14
Nodes (5): h(), m, se, Y(), z()

### Community 60 - "Init flow"
Cohesion: 0.20
Nodes (10): Completion gate, Init flow, Step 1: Load current state, Step 2: Explore the project, Step 3: Interview for product truth, Step 4: Write PRODUCT.md, Step 5: Record workflow defaults, Step 6: Wrap up or resume (+2 more)

### Community 61 - "Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)"
Cohesion: 0.20
Nodes (9): Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026), Documents, Events (12, all migrated), External links, Images, Inaccessible or missing source material, Interactive functionality on the old site, News (4 posts, all migrated, URLs unchanged) (+1 more)

### Community 62 - "mountSvelteComponentVariant"
Cohesion: 0.14
Nodes (23): acceptedDomAlreadyClean(), applyOriginalAttrsToSvelteAnchor(), clearHandledWrapperReloadStamp(), commitAcceptedSvelteComponentToDom(), componentModuleCandidates(), deferredRecoverySuperseded(), describeMountFailure(), detectDevServerBase() (+15 more)

### Community 63 - "vercel.json"
Cohesion: 0.13
Nodes (14): excludeFiles, includeFiles, buildCommand, cleanUrls, framework, functions, api/page.py, headers (+6 more)

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

### Community 68 - "page.py"
Cohesion: 0.12
Nodes (18): as_event(), as_news(), cached(), dynamic_pages(), events(), file_info(), full_posts(), human_size() (+10 more)

### Community 69 - "actOnAgentTarget"
Cohesion: 0.26
Nodes (18): actOnAgentTarget(), agentTargetBusyReason(), agentTargetOverlayGone(), agentTargetTaken(), claimAgentTarget(), claimAndActOnAgentTarget(), declineAgentTargetBusy(), declineAgentTargetUnresolvable() (+10 more)

### Community 70 - "Android platform"
Cohesion: 0.25
Nodes (8): Android platform, Color & theming, Components & motion, Layout & structure, The Android slop test, Touch targets, Typography, Verifying the build

### Community 71 - "colorize.md"
Cohesion: 0.25
Nodes (7): Apply at system scale, Audit before choosing, Choose a strategy, Contrast and perception, Live-mode signature params, Verify, Visitor mode

### Community 72 - "Persona-Based Design Testing"
Cohesion: 0.25
Nodes (8): 1. Impatient Power User: "Alex", 2. Confused First-Timer: "Jordan", 3. Accessibility-Dependent User: "Sam", 4. Deliberate Stress Tester: "Riley", 5. Distracted Mobile User: "Casey", Persona-Based Design Testing, Project-Specific Personas, Selecting Personas

### Community 73 - "Extract Flow"
Cohesion: 0.25
Nodes (7): Extract Flow, Step 1: Discover the Design System, Step 2: Identify Patterns, Step 3: Plan Extraction, Step 4: Extract & Enrich, Step 5: Migrate, Step 6: Document

### Community 74 - "image"
Cohesion: 0.29
Nodes (6): Commands, Documentation, Editorial workflow, Security notes, Shared code, vos.mojezdravka.cz

### Community 75 - "resolveLiveInjectionAnchor"
Cohesion: 0.16
Nodes (19): buildSvelteExpressionTextMap(), buildSveltePropValuesFromLiveElement(), buildSveltePropValuesV2(), cloneWithoutElements(), collectTextNodes(), collectVisibleTexts(), cssEscapeIdent(), elementMatchesOriginalMarkup() (+11 more)

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

### Community 82 - "o"
Cohesion: 0.33
Nodes (3): _getAccessToken(), o, s()

### Community 83 - "render_simple"
Cohesion: 0.33
Nodes (3): handler, not_found(), render_simple()

### Community 84 - "Diagnostic Scan"
Cohesion: 0.33
Nodes (6): 1. Accessibility (VoiceOver / TalkBack), 2. Performance, 3. Appearance & Theming, 4. Platform Conformance (CRITICAL), 5. Adaptivity, Diagnostic Scan

### Community 85 - "Visualize: Direction Comps & Asset Production"
Cohesion: 0.33
Nodes (5): After approval: the comp becomes a spec, Generate three compositional options, One approval point, Plates and provenance, Visualize: Direction Comps & Asset Production

### Community 86 - "Analysis, architecture and roadmap"
Cohesion: 0.33
Nodes (5): Analysis, architecture and roadmap, Architecture, Reference repositories (read only, not modified), Roadmap (all done in this session), Tools

### Community 87 - "ci.yml"
Cohesion: 0.13
Nodes (14): runs-on, steps, jobs, build, name, on, pull_request, push (+6 more)

### Community 88 - "Impeccable Documenter"
Cohesion: 0.40
Nodes (4): Impeccable Documenter, Input Contract, Output Contract, Workflow

### Community 89 - "Heuristics Scoring Guide"
Cohesion: 0.50
Nodes (4): Heuristics Scoring Guide, Issue Severity (P0–P3), Reference Material, Score Summary

### Community 90 - "$impeccable hooks"
Cohesion: 0.33
Nodes (6): Constraints, Failure modes, Flow, $impeccable hooks, Routing, Triage findings

### Community 92 - "Region map"
Cohesion: 0.25
Nodes (7): Containment, Painted material, Region map, What varies independently, Schema (for reference), Where things are, image()

### Community 94 - "Brand compliance and the school logo"
Cohesion: 0.50
Nodes (3): Brand compliance and the school logo, Open approvals, School logo, banner and photographs

### Community 96 - "QA report (19 Oct 2026)"
Cohesion: 0.33
Nodes (5): Cross-device audit and publishing workflow (21 October 2026), Pre-presentation audit (19 Oct 2026, after the header change), QA report (19 Oct 2026), Shared Supabase database (21 October 2026), Unresolved

### Community 103 - "d"
Cohesion: 0.25
Nodes (4): d(), handler(), Q, z()

### Community 104 - "re"
Cohesion: 0.13
Nodes (5): photos_of(), main(), Page, redirect_rules(), resolves()

### Community 105 - "u"
Cohesion: 0.10
Nodes (7): add(), detach(), G, remove(), u, value(), X

### Community 107 - "Operate"
Cohesion: 0.50
Nodes (3): Comps, Directions, Operate

### Community 108 - ".getClaims"
Cohesion: 0.24
Nodes (3): j, J(), R()

### Community 109 - "serve"
Cohesion: 0.36
Nodes (8): Act on the receipt, Assemble and review, Plan and asset review, Plan, capture, serve, serve(), do_GET(), end_headers(), guess_type()

### Community 110 - "c"
Cohesion: 0.43
Nodes (4): c, i(), n(), r()

### Community 111 - "Publishing (news, events, notices, galleries)"
Cohesion: 0.33
Nodes (5): Accounts, sign-in, roles, Publishing (news, events, notices, galleries), Running it locally, Security, What can be published

### Community 112 - "interface"
Cohesion: 0.40
Nodes (4): interface, default_prompt, display_name, short_description

### Community 115 - "Persuade and Experience"
Cohesion: 0.50
Nodes (3): Comps, Directions, Persuade and Experience

### Community 116 - "Read"
Cohesion: 0.50
Nodes (3): Comps, Directions, Read

### Community 117 - "3. Choose the right amount of invention"
Cohesion: 0.50
Nodes (4): 3. Choose the right amount of invention, Create a whole surface inside an established world, Create or replace the visual world, Extend an existing surface

## Knowledge Gaps
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `image()` connect `Region map` to `New visual work`, `quill.js`, `Visualize: Direction Comps & Asset Production`, `serve`?**
  _High betweenness centrality (0.240) - this node is a cross-community bridge._
- **Are the 12 inferred relationships involving `Module()` (e.g. with `ac()` and `$b()`) actually correct?**
  _`Module()` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Should `live-browser.js` be split into smaller, more focused modules?**
  _Cohesion score 0.0364977674238012 - nodes in this community are weakly interconnected._
- **Why does `_` connect `_` to `.listen`, `w`, `n`, `h`, `.getClaims`, `c`, `x`, `o`, `a`, `de`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Should `modern-screenshot.umd.js` be split into smaller, more focused modules?**
  _Cohesion score 0.08709273182957393 - nodes in this community are weakly interconnected._
- **Why does `e()` connect `.listen` to `modern-screenshot.umd.js`, `Module`, `create`, `o`, `s`, `_`, `b`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Should `Module` be split into smaller, more focused modules?**
  _Cohesion score 0.06060606060606061 - nodes in this community are weakly interconnected._