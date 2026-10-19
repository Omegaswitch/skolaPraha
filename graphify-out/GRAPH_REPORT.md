# Graph Report - skolaPraha  (2026-10-19)

## Corpus Check
- 80 files · ~250,238 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 29 file(s) not represented in the graph (top: .woff2 16, .toml 4, (none) 3)

## Summary
- 1939 nodes · 4814 edges · 105 communities (92 shown, 13 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 132 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8bb177ee`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- live-browser.js
- modern-screenshot.umd.js
- .remove
- quill.js
- el
- o
- setLiveState
- i
- initGlobalBar
- m
- length
- build.py
- news-editor.js
- renderDesignVisual
- initPageChat
- .forEach
- resumeSession
- enhance_body
- Components
- live.md
- mountSvelteComponentVariant
- startVariantObserver
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
- New visual work
- news.js
- serve
- jt
- re
- animate.md
- Handle `generate`
- initGlobalBar
- Generate Report
- u
- optimize.md
- Scan mode (approach C: auto-extract, then confirm descriptive language)
- Hardening Dimensions
- Product
- critique.md
- Simplify the Design
- .reduce
- clarify.md
- Nielsen's 10 Heuristics
- Generate Combined Critique Report
- document.md
- polish.md
- quieter.md
- c
- adapt.md
- make_logo.py
- Init flow
- Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)
- .getLength
- vercel.json
- Common Cognitive Load Violations
- iOS platform
- Operate mode depth (and Read notes)
- Shape
- Clean
- adapt.native.md
- Android platform
- colorize.md
- Persona-Based Design Testing
- Extract Flow
- image
- Read
- Generate Report
- Cognitive Load Assessment
- Impeccable Finish Reviewer
- Impeccable Manual Edit Applier
- live-browser-ignores.js
- syncPageChatFocus
- scheduleAcceptCleanup
- Diagnostic Scan
- Visualize: Direction Comps & Asset Production
- Analysis, architecture and roadmap
- R
- Impeccable Documenter
- Heuristics Scoring Guide
- showToast
- Persuade and Experience
- Region map
- captureElementToBlob
- Brand compliance and the school logo
- CLAUDE.md
- QA report (19 Oct 2026)
- legacy-url-map.md
- syncEditBadgeHitProxies
- enableInlineEdit
- read_doc
- _index

## God Nodes (most connected - your core abstractions)
1. `i` - 63 edges
2. `m` - 51 edges
3. `length()` - 51 edges
4. `o` - 47 edges
5. `s` - 44 edges
6. `h()` - 35 edges
7. `connectSSE()` - 34 edges
8. `setLiveState()` - 33 edges
9. `resumeSession()` - 33 edges
10. `showToast()` - 31 edges

## Surprising Connections (you probably didn't know these)
- `Safe Areas: Handle the Notch` --references--> `env()`  [INFERRED]
  .agents/skills/impeccable/reference/adapt.md → api/news.js
- `Step 1: Parse the request` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/generate.md → build.py
- `3. Load the action's reference` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/live.md → build.py
- `Phase D: Squint test` --references--> `layout()`  [INFERRED]
  .agents/skills/impeccable/reference/live.md → build.py
- `Painted material` --references--> `image()`  [INFERRED]
  .agents/skills/impeccable/reference/region-map.md → static/js/vendor/quill-2.0.3/quill.js

## Import Cycles
- None detected.

## Communities (105 total, 13 thin omitted)

### Community 0 - "live-browser.js"
Cohesion: 0.04
Nodes (101): addManualContextText(), applyLiveBarPreference(), applyPlaceholderDimensions(), applyPlaceholderSizingStyles(), buildPlaceholderResizeHandles(), buildSvelteExpressionTextMap(), buildSveltePropValuesFromLiveElement(), buildSveltePropValuesV2() (+93 more)

### Community 1 - "modern-screenshot.umd.js"
Cohesion: 0.09
Nodes (55): ae(), be(), bt(), Ce(), s(), Ct(), de(), dt() (+47 more)

### Community 2 - ".remove"
Cohesion: 0.20
Nodes (10): buildItem(), buildLabel(), buildOptions(), buildPicker(), close(), escape(), l(), listenDOM() (+2 more)

### Community 3 - "quill.js"
Cohesion: 0.08
Nodes (38): attach(), build(), constructor(), deleteAt(), detach(), Dt(), emit(), enforceAllowedChildren() (+30 more)

### Community 4 - "el"
Cohesion: 0.08
Nodes (51): actionLabel(), applyConfigureBarChrome(), bindConfigureCountPillTooltip(), bindConfigureInlineControlHover(), bindConfigureModifierPillHover(), buildConfigureActionControl(), buildConfigureCountControl(), buildConfigureRow() (+43 more)

### Community 5 - "o"
Cohesion: 0.13
Nodes (10): create(), descendants(), insertContents(), nt(), o, optimize(), p(), v() (+2 more)

### Community 6 - "setLiveState"
Cohesion: 0.11
Nodes (51): applyEditing(), beginNewLiveConfiguration(), buildInsertPlaceholderSnapshotFromDom(), buildLocatorForLeaf(), buildPickedAnchorSnapshot(), cancelEditing(), cancelEditingToPicking(), cancelInsertConfigure() (+43 more)

### Community 8 - "initGlobalBar"
Cohesion: 0.12
Nodes (40): actOnAgentTarget(), agentTargetBusyReason(), agentTargetOverlayGone(), agentTargetTaken(), claimAgentTarget(), claimAndActOnAgentTarget(), clearStoredManualApplyState(), declineAgentTargetBusy() (+32 more)

### Community 9 - "m"
Cohesion: 0.10
Nodes (8): attachUI(), d(), g(), getHTML(), handler(), length(), m, query()

### Community 10 - "length"
Cohesion: 0.11
Nodes (15): applyDelta(), deleteText(), E(), formatText(), getFormat(), h(), hasNext(), insertEmbed() (+7 more)

### Community 11 - "build.py"
Cohesion: 0.15
Nodes (27): breadcrumbs(), build(), crumbs_html(), _descendants(), enhance_files(), event_slug(), event_when(), events_list() (+19 more)

### Community 12 - "news-editor.js"
Cohesion: 0.12
Nodes (35): Constraints, Failure modes, Flow, $impeccable hooks, Routing, Triage findings, addCategory(), attachmentRow() (+27 more)

### Community 13 - "renderDesignVisual"
Cohesion: 0.08
Nodes (39): buildCollapsible(), buildColorModels(), buildDesignHeader(), buildListHtml(), buildRadiiModels(), buildTypographyModels(), cssSafe(), designEmptyMessage() (+31 more)

### Community 14 - "initPageChat"
Cohesion: 0.10
Nodes (42): applyGlobalBarLabelState(), armPageChatForTyping(), buildSteerProcessingDots(), buildSteerQueueHint(), clearSteerAwaitTimer(), collapsePageChat(), configureVoiceContext(), expandPageChat() (+34 more)

### Community 15 - ".forEach"
Cohesion: 0.07
Nodes (12): A(), clean(), copy(), f, formatLine(), i(), image(), k (+4 more)

### Community 16 - "resumeSession"
Cohesion: 0.11
Nodes (26): applySavedSessionMeta(), checkpointPayload(), clampVariantIndex(), clearHandled(), compileShader(), enterRecoveryWaitingForAnchor(), findActiveSessionSummary(), findAdoptableServerSession() (+18 more)

### Community 17 - "enhance_body"
Cohesion: 0.33
Nodes (3): enhance_body(), fix_img(), image_size()

### Community 18 - "Components"
Cohesion: 0.07
Nodes (29): Buttons, Calendar block, Colors, Components, Content-status bar (preview only), Content-status (preview only), Design System: VOŠZ Suverénního řádu maltézských rytířů, Do: (+21 more)

### Community 19 - "live.md"
Cohesion: 0.07
Nodes (26): Step 1: Parse the request, Step 2: Reuse the page, then start, Step 3: Generate, Step 4: Accept and close, Cleanup, Exit, First-time setup, Handle `accept` (+18 more)

### Community 20 - "mountSvelteComponentVariant"
Cohesion: 0.15
Nodes (19): applyOriginalAttrsToSvelteAnchor(), commitAcceptedSvelteComponentToDom(), componentModuleCandidates(), cyclingCounterText(), cyclingShownVariant(), describeMountFailure(), detectDevServerBase(), findInsertAnchorInDom() (+11 more)

### Community 21 - "startVariantObserver"
Cohesion: 0.11
Nodes (35): applyParamDefaults(), applyParamValue(), closedClipPath(), commitAcceptedVariantToDom(), ensureInsertPlaceholder(), finalizeInsertSession(), findVariantsWrapper(), getMountedSvelteComponentAnchor() (+27 more)

### Community 22 - "b"
Cohesion: 0.17
Nodes (6): b(), descendant(), Et(), find(), handleDOM(), show()

### Community 23 - "N"
Cohesion: 0.09
Nodes (12): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+4 more)

### Community 24 - "new-work.md"
Cohesion: 0.08
Nodes (23): Recommended Actions, Craft (deprecated alias), Opting out of the boot check, Step 2: Act by severity, Step 3: Deprecated fields are binding, Step 4: Do not overclaim on truth drift, What this owns, and what it does not, Apply (+15 more)

### Community 25 - "createLiveBrowserDomHelpers"
Cohesion: 0.13
Nodes (19): createLiveBrowserDomHelpers(), activeElementDeep(), cloneWithoutChrome(), copyTextViaSelection(), cssId(), liveUiRoot(), makeFrozenAnchor(), own() (+11 more)

### Community 27 - "onboard.md"
Cohesion: 0.09
Nodes (22): Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption, Guided Tours & Walkthroughs (+14 more)

### Community 28 - "import_vos.py"
Cohesion: 0.14
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
Cohesion: 0.14
Nodes (9): formula(), getBounds(), hide(), link(), qt(), rangeToNative(), St(), T() (+1 more)

### Community 33 - "New visual work"
Cohesion: 0.12
Nodes (17): Step 1: Run the pass, 1. Decide what is already true, 2. Ask what will change the work, 3. Choose the right amount of invention, 4. Commit the world, 5. Record the decision, 6. Build with full commitment, 7. Inspect and finish (+9 more)

### Community 34 - "news.js"
Cohesion: 0.08
Nodes (37): ALLOWED, CATEGORIES, commit(), crypto, editable(), env(), esc(), excerptOf() (+29 more)

### Community 35 - "serve"
Cohesion: 0.14
Nodes (15): Act on the receipt, Assemble and review, Plan and asset review, Plan, capture, serve, Core Rule, Decision Comps, Impeccable Asset Producer, Input Contract (+7 more)

### Community 36 - "jt"
Cohesion: 0.20
Nodes (15): appendChild(), Bt(), Ct(), Ft(), Gt(), e(), jt(), kt() (+7 more)

### Community 37 - "re"
Cohesion: 0.18
Nodes (5): lockup(), main(), Page, redirect_rules(), resolves()

### Community 38 - "animate.md"
Cohesion: 0.12
Nodes (14): Accessibility and control, Choose material by meaning, Find the job, Implement to the runtime, Set the motion thesis, Timing and easing, Verify, Visitor mode (+6 more)

### Community 39 - "Handle `generate`"
Cohesion: 0.12
Nodes (16): 1. Read the screenshot (if present), 2. Wrap the element, 3. Load the action's reference, 4. Plan three variants: identity first, then mode, then axes, 5. Apply the freeform prompt (if present), 6. Deliver variants, 7. Parameters (composition-sized, 0-4 per variant), 8. Signal done (+8 more)

### Community 40 - "initGlobalBar"
Cohesion: 0.10
Nodes (35): agentHasWorkInFlight(), agentStatusText(), barPaletteForTheme(), brandMarkSvg(), buildParamsPanel(), designPanelCss(), detectPageTheme(), ensureAgentPollTooltip() (+27 more)

### Community 41 - "Generate Report"
Cohesion: 0.13
Nodes (14): 1. Accessibility (A11y), 2. Performance, 3. Theming, 4. Responsive Design, 5. Implementation Integrity (CRITICAL), Audit Health Score, Detailed Findings by Severity, Diagnostic Scan (+6 more)

### Community 42 - "u"
Cohesion: 0.14
Nodes (7): Monorepo notes, add(), attribute(), getDelta(), u, value(), values()

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

### Community 49 - ".reduce"
Cohesion: 0.15
Nodes (3): q(), X, z()

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

### Community 57 - "c"
Cohesion: 0.15
Nodes (6): c, clone(), insertAt(), keys(), split(), splitAfter()

### Community 58 - "adapt.md"
Cohesion: 0.12
Nodes (15): Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, Mobile Adaptation (Desktop → Mobile), Navigation Adaptation (+7 more)

### Community 59 - "make_logo.py"
Cohesion: 0.16
Nodes (6): lockup(), main(), shield(), text_path(), vos_lockup(), vos_text()

### Community 60 - "Init flow"
Cohesion: 0.20
Nodes (10): Completion gate, Init flow, Step 1: Load current state, Step 2: Explore the project, Step 3: Interview for product truth, Step 4: Write PRODUCT.md, Step 5: Record workflow defaults, Step 6: Wrap up or resume (+2 more)

### Community 61 - "Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)"
Cohesion: 0.20
Nodes (9): Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026), Documents, Events (12, all migrated), External links, Images, Inaccessible or missing source material, Interactive functionality on the old site, News (4 posts, all migrated, URLs unchanged) (+1 more)

### Community 63 - "vercel.json"
Cohesion: 0.20
Nodes (9): buildCommand, cleanUrls, framework, headers, installCommand, outputDirectory, redirects, $schema (+1 more)

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

### Community 69 - "adapt.native.md"
Cohesion: 0.25
Nodes (7): Adaptation Strategies, Assess Adaptation Challenge, Implement & Verify, Orientation & foldables, Phone → Tablet (iPad / large screens), Platform → platform (iOS ↔ Android), Web → native (porting a website or web app)

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
Cohesion: 0.33
Nodes (5): Commands, Documentation, Editorial workflow, vos.mojezdravka.cz, Where things are

### Community 75 - "Read"
Cohesion: 0.50
Nodes (3): Comps, Directions, Read

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

### Community 82 - "syncPageChatFocus"
Cohesion: 0.29
Nodes (14): attachSteerFocusDebug(), attachSteerFocusGuard(), clearSteerFocusRecoverTimer(), focusConfigureInput(), focusSteerChat(), notePagePointerDown(), pageHasHostTextSelection(), scheduleSteerFocusRecover() (+6 more)

### Community 83 - "scheduleAcceptCleanup"
Cohesion: 0.31
Nodes (11): acceptedDomAlreadyClean(), clearHandledWrapperReloadStamp(), deferredRecoverySuperseded(), ensureAcceptedDomClean(), findAcceptedRuntimeWrappers(), handledWrapperReloadKey(), reloadAfterMissingAcceptedDom(), restoreAcceptedDomFromSnapshot() (+3 more)

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

### Community 90 - "showToast"
Cohesion: 0.09
Nodes (52): abandonForeignSession(), abandonSupersededGo(), abortSvelteComponentInjection(), cleanup(), clearMountErrorCard(), clearScrollY(), clearSession(), completeParameterGenerationIfReady() (+44 more)

### Community 91 - "Persuade and Experience"
Cohesion: 0.50
Nodes (3): Comps, Directions, Persuade and Experience

### Community 92 - "Region map"
Cohesion: 0.40
Nodes (4): Containment, Painted material, Region map, What varies independently

### Community 93 - "captureElementToBlob"
Cohesion: 0.08
Nodes (36): averageRgb01(), beginEditPin(), bufferToBase64(), buildAnnotationsForCapture(), buildPinElement(), cancelEditingPin(), captureChromeNodes(), captureElementFromRenderedAncestor() (+28 more)

### Community 94 - "Brand compliance and the school logo"
Cohesion: 0.50
Nodes (3): Brand compliance and the school logo, Open approvals, School logo, banner and photographs

### Community 96 - "QA report (19 Oct 2026)"
Cohesion: 0.50
Nodes (3): Pre-presentation audit (19 Oct 2026, after the header change), QA report (19 Oct 2026), Unresolved

### Community 100 - "syncEditBadgeHitProxies"
Cohesion: 0.27
Nodes (10): bindEditBadgeProxy(), editBadgeProxyTargets(), initEditBadge(), initEditBadgeHitProxies(), positionEditBadge(), proxyMouseEvent(), setImportantStyle(), styleEditBadgeProxy() (+2 more)

### Community 101 - "enableInlineEdit"
Cohesion: 0.40
Nodes (5): collectEditableTextRows(), visit(), enableInlineEdit(), onInlineInput(), wrapMixedContentTextNodes()

### Community 102 - "read_doc"
Cohesion: 0.50
Nodes (4): _fix(), load_news(), load_pages(), read_doc()

## Knowledge Gaps
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Monorepo notes` connect `u` to `new-work.md`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `i` (e.g. with `e()` and `i()`) actually correct?**
  _`i` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `live-browser.js` be split into smaller, more focused modules?**
  _Cohesion score 0.03773584905660377 - nodes in this community are weakly interconnected._
- **Why does `image()` connect `.forEach` to `New visual work`, `.remove`, `serve`, `quill.js`, `image`, `Visualize: Direction Comps & Asset Production`, `Region map`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Should `modern-screenshot.umd.js` be split into smaller, more focused modules?**
  _Cohesion score 0.08897243107769423 - nodes in this community are weakly interconnected._
- **Why does `Act on the receipt` connect `serve` to `.forEach`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Should `quill.js` be split into smaller, more focused modules?**
  _Cohesion score 0.08446455505279035 - nodes in this community are weakly interconnected._