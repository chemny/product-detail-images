---
name: product-detail-images
description: "Generate ecommerce product detail-page image sets from uploaded product images or product descriptions. Use when the user asks for ecommerce KV posters, marketplace detail images, visual selling-point analysis, section plans, production prompts, or generated product-detail image assets. This skill produces images only, not websites or code previews."
metadata:
  version: "1.5.0"
---

# Product Detail Images

Create a coherent ecommerce image set through three layers: planning, creative generation, and post-generation quality control. Keep internal workflow rules out of image-generation prompts.

## Layer 1: Planning

1. Lock the primary product.
   - Inventory every uploaded input before deciding how to use it. Assign one or more roles: `product_appearance`, `brand_asset`, `content_copy`, `style_reference`, or `spec_evidence`.
   - Treat long screenshots, existing detail pages, documents, and copy boards as information sources to extract, not merely as visual references.
   - Identify plausible sellable subjects in the source.
   - If the user has not identified the product and two or more candidates are plausible, ask one concise question and stop.
   - Record the primary product, supporting elements, and excluded products.

2. Analyze the source.
   - Read `references/product-analysis-schema.md` and `references/category-routing.md`.
   - Extract visible product identity, color, structure, surface, brand signals, audience cues, and usable information.
   - Route the sold product to one primary category family from the buyer's main decision risk. Load `references/structured-durable-adapter.md` for `structured_durable`, `references/packaged-consumable-adapter.md` for `packaged_consumable`, and `references/electronics-adapter.md` for `electronics_equipment`; otherwise use the common workflow unless another adapter exists.
   - Separate the sold product from supporting styling elements. Protect the sold product's recognizable identity; allow ordinary variation in supporting props unless it competes with the product, becomes physically implausible, or introduces a clearly recognizable third-party brand mark.
   - Classify source details as `clear`, `ambiguous`, or `supporting`. Preserve clear identity features, allow plausible interpretation of ambiguous details, and do not turn case-specific styling differences into global constraints.
   - Separate objective claims from creative expression. Exact material, data, certification, review, performance, size, and brand-history claims require visible or user-provided support. Mood, aesthetic language, color association, and visual metaphor may be created freely when they do not imply an objective fact.

3. Build a complete commerce story, then select the count.
   - Read `references/poster-sequence.md`.
   - First define the core value, 1-3 advantage pillars, visible or supplied proof, usage imagination, and purchase-decision support.
   - Automatically use only 6, 8, or 10 images. Six is the minimum complete detail-page set; eight is the default recommendation; ten is for richer products or longer decision paths.
   - Choose the smallest tier that can express the complete commerce story without overcrowding or hollow repetition. Material richness controls evidence depth and may justify expansion; image clarity never determines count.
   - A user-specified count overrides the automatic tier. If the user explicitly requests four images, treat it as a compact showcase rather than the default complete-detail-page format and explain which content must be compressed.
   - Resolve the requested platform, language, output directory, and per-image dimensions or aspect ratios before generation. Record them in a delivery manifest. Do not replace the 6/8/10 completeness logic with another skill's fixed main-image/detail-image count.

4. Build the recommendation.
   - Read `references/content-dimension-system.md`, `references/style-packs.md`, and `references/background-system.md`.
   - Propose exactly five candidate selling points, then organize them into one core value, 1-3 advantage pillars, and supporting evidence instead of treating all five equally.
   - Always show all seven style packs with concise product-specific fit ratings. Mark one recommended style, one safe alternative, and optionally one contrasting alternative. The full library must remain visible, but the user only needs to confirm one direction rather than answer seven separate questions.
   - Use the stable page skeleton for the selected count, then apply the loaded category adapter's evidence emphasis, visual carriers, and decision modules. Replace only modules that are unsupported or clearly low-value.
   - Default background mode to `replace`: the source is product evidence, not an automatic environment template.

5. Obtain one consolidated confirmation.
   - Read `references/output-contract.md`.
   - Present the primary product, count, recommended style, the visible seven-style fit table, five selling points, page sequence, page-layout table, headlines, background world, delivery manifest, and only the decisions that materially change commercial responsibility.
   - The page-layout table must state each page's commerce job, image structure, text structure, and image-text relationship so the user can review the complete detail-page design before generation.
   - Do not ask the user to choose routine design details separately.
   - Do not generate images before confirmation.

## Layer 2: Creative Generation

6. Lock one series concept.
   - Define one commercial mood, palette, lighting character, typography family, grid, logo position, and background world for the set.
   - Allow different spaces by page role while keeping them recognizably part of one brand world.

7. Write the series copy.
   - Read `references/copywriting-rules.md`.
   - Give every page a distinct language job: positioning, desire, memory, explanation, proof, inspiration, or decision support.
   - Use a memorable headline plus one concrete proof line. Avoid repeating the same sentence pattern across the set.
   - Assign each page a deliberate copy density: `low`, `medium`, or `high`. Base it on the page's commerce job and the richness of supplied content; do not flatten useful source information into slogans or fill weak evidence with decorative paragraphs.
   - For sets of six or more, use at least three headline forms across the series, such as short naming, contrast, question, structural phrase, emotional phrase, or direct benefit. Do not repeat a `four-character phrase + comma + four-character phrase` formula mechanically.

8. Build each page as a layout blueprint.
   - Read `references/layout-archetypes.md` and `references/typography-system.md`.
   - For every page specify the subject region and scale, camera distance, subject state, text region, title width and line count, alignment, Chinese-English size relationship, logo position, background texture zone, and allowed crop.
   - Add a lightweight direction note: `scene_mode` (`literal`, `reinterpret`, or `conceptual`), 2-3 recognizable `scene_cues` when copy names a concrete setting, plus the model's action, expression, gaze, and camera angle. Concrete scene copy needs concrete visual evidence; conceptual copy may use abstract space.
   - Before prompting, compare adjacent pages. If they repeat the same setting, action, expression/gaze, distance, and angle, change at least two of those dimensions. Treat this as pre-generation planning, not a reason to police harmless differences after generation.
   - Use horizontal text on at least 80% of pages by default. Do not mix text directions casually.
   - In every eight- or ten-image set, designate one `series_peak_page` based on category and buyer needs: `visual_peak`, `evidence_peak`, or `information_peak`. Lifestyle and image-led products may need a memorable concept; technical and high-consideration products may need stronger proof, comparison, structure, or data instead. The peak must add commerce meaning, not spectacle alone.
   - Require the final decision page to add new purchase information or resolve a buyer concern. It must not merely repeat earlier color, scene, or slogan content.

9. Write full production prompts.
   - Do not compress away design instructions before generation.
   - Every prompt must retain: page objective, visual scene, product identity anchors, composition and camera, exact visible copy, layout blueprint, and only the page-specific negative constraints needed for likely material failures. Do not target a fixed negative-prompt count.
   - Carry the approved scene cues, model action, expression, gaze, and camera direction into the prompt. Do not use a generic wall, curtain, or studio as a substitute for an explicitly named city, cafe, home, office, outdoor, travel, or other concrete scene.
   - Keep internal scores, evidence fields, risk explanations, count logic, approval workflow, and QA status labels out of the image prompt.
   - Favor positive visual direction over prohibitions. Use negative constraints only for likely failures on that page.
   - Use exact or absolute preservation language only for clear, purchase-relevant identity features. Describe ambiguous source details positively and allow a plausible interpretation. Do not inherit a previous product's belt, hardware, accessory, logo, or styling failure as a constraint for a new product.
   - Carry only the relevant category-adapter anchors and likely material failures into each prompt. Do not paste a full adapter or generic category checklist into every image request.

10. Generate images.
   - Use uploaded images as product references.
   - Generate the hero first for apparel, human models, multiple products, weak sources, or complex compositions; inspect it before continuing.
   - Generate later pages in batches of no more than two.
   - Every final detail-page image must contain useful commerce copy. Do not deliver text-free pages.
   - Treat the approved visible copy as a closed list. Do not invite the image model to invent extra material, comfort, performance, efficacy, or user-experience statements. Additional descriptive text is allowed only when it was explicitly included in the approved page copy.
   - Do not use CTA or button-like elements in detail-page sections. CTA is allowed only for an explicitly separate header, campaign, or landing hero.

## Layer 3: Post-Generation Quality Control

11. Inspect after generation.
   - Read `references/generation-qa.md`.
   - First check delivery basics: sold-product identity, anatomy, crop, physical relationships, readable text, objective claims, and CTA absence.
   - Then check creative quality: visual impact, page-level idea, product-concept interaction, layout completion, new information, and set rhythm.
   - Classify issues as critical, material-but-reviewable, or acceptable variation. Only critical issues trigger automatic regeneration.
   - Judge supporting props lightly. Ordinary changes in shoes, metal hardware, bags, jewelry, hair, or styling are acceptable unless they misrepresent the sold product, dominate it, become physically implausible, or show a clearly recognizable third-party brand mark.
   - Apply the loaded category adapter's purchase-relevant QA after the common checks. A category detail is critical only when it is visible or supplied and changes what the buyer believes the product is, includes, connects to, supports, or can do.
   - Verify the delivery manifest: requested count and order, stable numbered filenames, file existence, actual pixel dimensions and aspect ratios, and output location. Do not report an asset as delivered until the file and dimensions have been checked.

12. Revise only the failed dimension.
   - Identify the concrete failure and revise the corresponding prompt instruction.
   - Do not preload every possible failure into every prompt.
   - Automatically regenerate a page at most once, and only for a critical failure. Review the set as a whole before spending another generation on a non-critical difference.
   - For a text-only failure on an otherwise approved image, prefer local text repair or typography replacement when available. Regenerate the full image only when the text cannot be separated and the error materially changes the product promise.
   - If generation is refused or requires a material change to framing, claims, or page module, explain the result and let the user decide.

## Information Boundary

Allow creative expression without confirmation when it is clearly aesthetic or emotional, such as French mood, dusty rose, quiet luxury, silk-like visual poetry, urban ease, or natural breathing.

Require evidence or a user decision for objective claims such as exact composition, cooling percentage, waterproof rating, dimensions, certification, award, genuine review, sales rank, medical benefit, safety result, or comparative test.

Rule of thumb: creative mood may be proposed; objective facts must not be fabricated.

## Commerce Completeness And Stable Skeletons

Use `references/poster-sequence.md` as the source of truth:

- Every complete set must cover product recognition, core value, advantage expression, proof, usage imagination, and purchase decision.
- 6 images: minimum complete detail page.
- 8 images: default complete sales narrative.
- 10 images: rich commercial narrative with deeper proof and decision support.
- 4 images: user-requested compact showcase only; never an automatic complete-detail-page tier.

Replace unsupported modules at the same narrative level instead of changing the count or inventing facts.

## Prompt Payload

Send only these seven fields to image generation:

1. Page objective and memorable visual idea.
2. Scene, background, lighting, and product-concept relationship.
3. Sold-product identity anchors: clear features to preserve, ambiguous details that allow plausible interpretation, and supporting elements that may vary.
4. Subject position, scale, camera, pose/state, support, and allowed crop.
5. Exact visible Chinese and optional English copy.
6. Layout blueprint: text zone, hierarchy, alignment, relative sizes, logo, and low-texture area.
7. Only page-specific negative constraints needed for likely material failures; omit them when unnecessary.

Do not send workflow explanations, scoring rubrics, user-decision logic, evidence-status schemas, or generic safety essays to the image model.

## Resource Guide

- `references/product-analysis-schema.md`: product recognition and evidence extraction.
- `references/category-routing.md`: automatic category-family routing and adapter authority.
- `references/structured-durable-adapter.md`: structure, scale, capacity, use relationships, prompts, and QA for durable goods.
- `references/packaged-consumable-adapter.md`: packaging identity, sensory evidence, label hierarchy, quantity, claims, prompts, and QA for consumables and packaged goods.
- `references/electronics-adapter.md`: electronics-specific evidence, story, visual carriers, prompts, and QA.
- `references/poster-sequence.md`: deterministic counts and stable page skeletons.
- `references/content-dimension-system.md`: selling points and optional replacement modules.
- `references/style-packs.md`: seven visual directions.
- `references/visual-style-system.md`: series-level visual identity.
- `references/background-system.md`: replace, reinterpret, or preserve source environment.
- `references/layout-archetypes.md`: executable layout blueprints.
- `references/typography-system.md`: text direction and hierarchy.
- `references/copywriting-rules.md`: series copy and full prompt structure.
- `references/conditional-commerce-modules.md`: reviews, specs, endorsement, claims, close-ups, and CTA.
- `references/output-contract.md`: concise planning and delivery format.
- `references/generation-qa.md`: delivery and creative quality gates.
- `scripts/validate_product_brief.py`: optional structured-brief validation.

## Final Delivery

Deliver only approved image assets. State the image count, section themes, numbered file paths, actual dimensions, and unresolved objective facts. Do not offer a website or code-based page as part of this skill.
