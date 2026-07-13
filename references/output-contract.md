# Output Contract

Keep planning output concise and user-readable. Internal schemas must not leak into image-generation prompts.

## Consolidated Plan

Before generation, return:

1. **Product lock:** primary product, supporting elements, excluded products.
2. **Count:** automatic 6, 8, or 10 and a short commerce-coverage plus material-richness reason; explicit user-requested 4 is a compact showcase.
3. **Value tree:** one core value, 1-3 advantage pillars, and evidence for each.
4. **Five candidate selling points:** idea, source status, and proposed headline.
5. **Commerce coverage:** where product recognition, core value, advantage expression, proof, usage imagination, and purchase decision appear.
6. **Seven-style fit table:** show every style pack with product-specific fit rating and expected effect; mark recommended, safe alternative, and optional contrasting direction.
7. **Recommended sequence and page-layout table:** for every page show role, commerce job, image structure, text structure, image-text relationship, headline, visual idea, and layout type.
8. **Series lock:** palette, typography, logo position, background world, and copy direction.
9. **Decision items:** only unsupported objective claims or choices that materially change intent.
10. **One confirmation question.**

Automatic counts are 6, 8, or 10. Six is the minimum complete tier and eight is the default recommendation. Use four only when explicitly requested and label it as a compact showcase with compressed-content notes.

Do not ask the user to approve count, background, typography, layout, and each page separately.

The seven-style table is a transparent recommendation surface, not a seven-step questionnaire. Recommend one direction and allow one consolidated confirmation.

For every page also record:

- `headline_form`;
- whether it is the `series_peak_page`, and its type: `visual_peak|evidence_peak|information_peak`;
- what new information it adds beyond earlier pages.

For eight- and ten-image sets, the plan is incomplete without a category-appropriate series peak. The final page is incomplete when its new-information field only repeats prior colors, occasions, or selling points.

## Page Plan

After confirmation, every page plan must contain:

- page id and role;
- primary commerce job;
- image modules and text modules;
- image-text relationship: what the image demonstrates and what the text adds;
- memorable headline;
- one proof line;
- exact visible labels, if any;
- visual idea and product-concept relationship;
- source facts used;
- subject state, camera distance, and subject position;
- layout blueprint;
- background variation inside the shared brand world.

## Production Prompt

Every image prompt must preserve these fields:

1. Page objective.
2. Full visual scene and lighting.
3. Product restoration invariants.
4. Composition, camera, pose/state, support relationship, and crop.
5. Exact visible copy.
6. Layout blueprint and typography hierarchy.
7. Five to ten page-specific negative constraints.

Do not add workflow explanations, scoring fields, source-status schemas, approval logic, or QA labels to the image prompt.

## Generated Asset Record

For each output record:

- section id;
- file path;
- role;
- status: `approved` or `needs_revision`;
- concrete inspection note.

Deliver only approved assets. State count, section themes, paths, and unresolved objective facts. This skill produces image assets only, not websites or code previews.
