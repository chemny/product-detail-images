# Output Contract

Keep planning output concise and user-readable. Internal schemas must not leak into image-generation prompts.

## Consolidated Plan

Before generation, return:

1. **Product lock:** primary product, supporting elements, excluded products.
2. **Category route:** category family, loaded adapter, buyer decision risk, and any justified secondary module.
3. **Count:** automatic 6, 8, or 10 and a short commerce-coverage plus material-richness reason; explicit user-requested 4 is a compact showcase.
4. **Value tree:** one core value, 1-3 advantage pillars, and evidence for each.
5. **Five candidate selling points:** idea, source status, and proposed headline.
6. **Commerce coverage:** where product recognition, core value, advantage expression, proof, usage imagination, and purchase decision appear.
7. **Seven-style fit table:** show every style pack with product-specific fit rating and expected effect; mark recommended, safe alternative, and optional contrasting direction.
8. **Recommended sequence and page-layout table:** for every page show role, commerce job, image structure, text structure, image-text relationship, headline, visual idea, and layout type.
9. **Series lock:** palette, typography, logo position, background world, and copy direction.
10. **Decision items:** only unsupported objective claims or choices that materially change intent.
11. **Delivery manifest:** requested platform, language, destination, and one row per image with order, role, commerce job, target dimensions or aspect ratio, and planned filename.
12. **One confirmation question.**

Automatic counts are 6, 8, or 10. Six is the minimum complete tier and eight is the default recommendation. Use four only when explicitly requested and label it as a compact showcase with compressed-content notes.

Do not ask the user to approve count, background, typography, layout, and each page separately.

The seven-style table is a transparent recommendation surface, not a seven-step questionnaire. Recommend one direction and allow one consolidated confirmation.

For every page also record:

- `headline_form`;
- whether it is the `series_peak_page`, and its type: `visual_peak|evidence_peak|information_peak`;
- what new information it adds beyond earlier pages.

For eight- and ten-image sets, the plan is incomplete without a category-appropriate series peak. The final page is incomplete when its new-information field only repeats prior colors, occasions, or selling points.

## Delivery Manifest

Create the manifest before generation and keep it aligned with the approved page sequence. Each row contains:

- page id and numerical order;
- asset type: `main`, `detail`, or `gallery` when the platform distinguishes them;
- commerce job and section theme;
- target width, height, and aspect ratio, or an explicit `platform_default` when exact pixels were not supplied;
- language;
- input roles used as evidence or reference;
- stable numbered filename and output directory.

Dimension precedence is: user-specified per-image size, user-specified class size, supplied platform specification, then the skill's existing aspect-ratio default. Do not silently invent a current platform requirement.

If generation does not return the requested pixels, resize, crop, or pad only when it preserves the approved composition and never stretch the product. Record the actual final dimensions after export.

## Page Plan

After confirmation, every page plan must contain:

- page id and role;
- primary commerce job;
- image modules and text modules;
- image-text relationship: what the image demonstrates and what the text adds;
- memorable headline;
- one proof line;
- copy density: `low`, `medium`, or `high`;
- exact visible labels, if any;
- visual idea and product-concept relationship;
- source facts used;
- category-adapter mode when applicable, including `product_preservation_mode` for electronics and structured durables, and `consumable_profile` plus preservation mode for packaged consumables;
- scene mode and 2-3 recognizable scene cues when the copy names a concrete setting;
- model action, expression, gaze, camera distance, and camera angle;
- the intended visual difference from the previous and next page;
- subject state, camera distance, and subject position;
- layout blueprint;
- background variation inside the shared brand world.

## Production Prompt

Every image prompt must preserve these fields:

1. Page objective.
2. Full visual scene and lighting.
3. Sold-product identity anchors, ambiguity allowance, and supporting-element freedom.
4. Composition, camera, pose/state, support relationship, and crop.
5. Exact visible copy.
6. Layout blueprint and typography hierarchy.
7. Only the page-specific negative constraints needed to prevent likely material failures; omit them when none are necessary.

Do not add workflow explanations, scoring fields, source-status schemas, approval logic, or QA labels to the image prompt.

## Generated Asset Record

For each output record:

- section id;
- file path;
- role;
- planned and actual dimensions;
- status: `approved` or `needs_revision`;
- concrete inspection note and issue severity when revision is needed.

Deliver only approved assets. State count, section themes, numbered paths, actual dimensions, and unresolved objective facts. This skill produces image assets only, not websites or code previews.
