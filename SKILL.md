---
name: product-detail-images
description: "Generate ecommerce product detail-page image sets from uploaded product images or product descriptions. Use when the user asks for ecommerce KV posters, marketplace detail images, visual selling-point analysis, section plans, production prompts, or generated product-detail image assets. This skill produces images only, not websites or code previews."
metadata:
  version: "1.0.0"
---

# Product Detail Images

Create a coherent ecommerce image set through three layers: planning, creative generation, and post-generation quality control. Keep internal workflow rules out of image-generation prompts.

## Layer 1: Planning

1. Lock the primary product.
   - Identify plausible sellable subjects in the source.
   - If the user has not identified the product and two or more candidates are plausible, ask one concise question and stop.
   - Record the primary product, supporting elements, and excluded products.

2. Analyze the source.
   - Read `references/product-analysis-schema.md`.
   - Extract visible product identity, color, structure, surface, brand signals, audience cues, and usable information.
   - Separate objective claims from creative expression. Exact material, data, certification, review, performance, size, and brand-history claims require visible or user-provided support. Mood, aesthetic language, color association, and visual metaphor may be created freely when they do not imply an objective fact.

3. Build a complete commerce story, then select the count.
   - Read `references/poster-sequence.md`.
   - First define the core value, 1-3 advantage pillars, visible or supplied proof, usage imagination, and purchase-decision support.
   - Automatically use only 6, 8, or 10 images. Six is the minimum complete detail-page set; eight is the default recommendation; ten is for richer products or longer decision paths.
   - Choose the smallest tier that can express the complete commerce story without overcrowding or hollow repetition. Material richness controls evidence depth and may justify expansion; image clarity never determines count.
   - A user-specified count overrides the automatic tier. If the user explicitly requests four images, treat it as a compact showcase rather than the default complete-detail-page format and explain which content must be compressed.

4. Build the recommendation.
   - Read `references/content-dimension-system.md`, `references/style-packs.md`, and `references/background-system.md`.
   - Propose exactly five candidate selling points, then organize them into one core value, 1-3 advantage pillars, and supporting evidence instead of treating all five equally.
   - Always show all seven style packs with concise product-specific fit ratings. Mark one recommended style, one safe alternative, and optionally one contrasting alternative. The full library must remain visible, but the user only needs to confirm one direction rather than answer seven separate questions.
   - Use the stable page skeleton for the selected count. Replace only modules that are unsupported or clearly low-value.
   - Default background mode to `replace`: the source is product evidence, not an automatic environment template.

5. Obtain one consolidated confirmation.
   - Read `references/output-contract.md`.
   - Present the primary product, count, recommended style, the visible seven-style fit table, five selling points, page sequence, page-layout table, headlines, background world, and only the decisions that materially change commercial responsibility.
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
   - For sets of six or more, use at least three headline forms across the series, such as short naming, contrast, question, structural phrase, emotional phrase, or direct benefit. Do not repeat a `four-character phrase + comma + four-character phrase` formula mechanically.

8. Build each page as a layout blueprint.
   - Read `references/layout-archetypes.md` and `references/typography-system.md`.
   - For every page specify the subject region and scale, camera distance, subject state, text region, title width and line count, alignment, Chinese-English size relationship, logo position, background texture zone, and allowed crop.
   - Use horizontal text on at least 80% of pages by default. Do not mix text directions casually.
   - In every eight- or ten-image set, designate one `series_peak_page` based on category and buyer needs: `visual_peak`, `evidence_peak`, or `information_peak`. Lifestyle and image-led products may need a memorable concept; technical and high-consideration products may need stronger proof, comparison, structure, or data instead. The peak must add commerce meaning, not spectacle alone.
   - Require the final decision page to add new purchase information or resolve a buyer concern. It must not merely repeat earlier color, scene, or slogan content.

9. Write full production prompts.
   - Do not compress away design instructions before generation.
   - Every prompt must retain: page objective, visual scene, product restoration, composition and camera, exact visible copy, layout blueprint, and only the page-specific negative constraints needed for likely failures. Do not target a fixed negative-prompt count.
   - Keep internal scores, evidence fields, risk explanations, count logic, approval workflow, and QA status labels out of the image prompt.
   - Favor positive visual direction over prohibitions. Use negative constraints only for likely failures on that page.

10. Generate images.
   - Use uploaded images as product references.
   - Generate the hero first for apparel, human models, multiple products, weak sources, or complex compositions; inspect it before continuing.
   - Generate later pages in batches of no more than two.
   - Every final detail-page image must contain useful commerce copy. Do not deliver text-free pages.
   - Do not use CTA or button-like elements in detail-page sections. CTA is allowed only for an explicitly separate header, campaign, or landing hero.

## Layer 3: Post-Generation Quality Control

11. Inspect after generation.
   - Read `references/generation-qa.md`.
   - First check delivery basics: product identity, anatomy, crop, physical relationships, readable text, objective claims, and CTA absence.
   - Then check creative quality: visual impact, page-level idea, product-concept interaction, layout completion, new information, and set rhythm.
   - A technically valid but visually generic image still fails creative QA.

12. Revise only the failed dimension.
   - Identify the concrete failure and revise the corresponding prompt instruction.
   - Do not preload every possible failure into every prompt.
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
3. Product identity and details that must remain invariant.
4. Subject position, scale, camera, pose/state, support, and allowed crop.
5. Exact visible Chinese and optional English copy.
6. Layout blueprint: text zone, hierarchy, alignment, relative sizes, logo, and low-texture area.
7. Five to ten page-specific negative constraints.

Do not send workflow explanations, scoring rubrics, user-decision logic, evidence-status schemas, or generic safety essays to the image model.

## Resource Guide

- `references/product-analysis-schema.md`: product recognition and evidence extraction.
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

Deliver only approved image assets. State the image count, section themes, file paths, and unresolved objective facts. Do not offer a website or code-based page as part of this skill.
