# Product Analysis

Analyze enough to create a strong image set. Do not turn recognition into a long compliance exercise.

## Input Inventory And Routing

Inspect every uploaded input and assign one or more practical roles:

- `product_appearance`: identifies the sold product's visible form, color, structure, pattern, or packaging;
- `brand_asset`: logo, wordmark, brand colors, packaging system, or approved identity element;
- `content_copy`: existing headlines, product story, selling-point text, detail-page content, or long screenshots to extract;
- `style_reference`: composition, typography, photography, lighting, palette, or art-direction reference;
- `spec_evidence`: visible specifications, labels, measurements, ingredients, parameters, certifications, or other factual support.

Do not assume that every image is a product reference. A long screenshot or existing detail page may contribute information architecture and copy depth even when its visual style is not reused.

When sources conflict, prefer: the user's current explicit instruction, then clear supplied specification or packaging evidence, then the clearest current product image, then older marketing material, then inference. Ask only when the conflict changes the sold product, an objective claim, or the intended commercial direction. Otherwise choose conservatively and record the assumption in the plan.

## Required Recognition

- Primary sold product, supporting styling elements, and excluded products.
- Category family, primary adapter, and any justified secondary module from `category-routing.md`.
- Product category and concrete product name.
- Visible color, silhouette, pattern, closure, structure, surface, and notable details.
- Visible brand name, logo style, packaging language, or collection cues.
- Source-image clarity and restoration limitations.
- Source environment: incidental, useful context, required evidence, or protected brand asset.
- Likely audience, price feeling, aesthetic direction, and use context as planning inferences.
- Independent source-material groups for evidence depth and the automatic 6/8/10 count tier.

## Adaptive Fidelity

Classify visible details before prompting:

- `clear_identity`: purchase-relevant features that are clearly visible and define the sold product, such as category, main color, major silhouette, dominant pattern, key closure, or major structure;
- `ambiguous_detail`: details that the source does not resolve reliably, such as whether a narrow waist treatment is a seam, elastic channel, facing, or separate band;
- `supporting_element`: shoes, bags, jewelry, props, scenery, and other elements that are not being sold.

Preserve `clear_identity`. Allow a plausible visual interpretation of `ambiguous_detail` unless the user confirms it. Let `supporting_element` vary ordinarily unless it competes with the sold product, becomes physically implausible, or adds a clearly recognizable third-party brand mark.

Do not create a per-product template or persistent case rule. Keep this classification as a lightweight analysis for the current request only.

## Exactly Five Candidate Selling Points

For each candidate state:

- the idea;
- source status: `visible`, `user_provided`, `proposed`, or `not_supported`;
- short evidence or reasoning;
- suggested commercial headline.

Do not force all five into the final sequence.

## Information Boundary

Treat these as objective facts requiring visible or user-provided support:

- exact material or composition;
- dimensions, weight, capacity, power, percentages, duration, and measured performance;
- certification, award, genuine review, sales result, comparison result, warranty, safety, medical, or efficacy claim;
- exact care, storage, ingredient, nutrition, or compliance instruction.

Allow these as creative planning language when they do not imply measured facts:

- mood and lifestyle;
- color association;
- aesthetic positioning;
- sensory or poetic metaphor;
- conceptual scene and collection inspiration.

Rule of thumb: facts must be supported; mood may be created.

## Concise Recognition Output

Return:

1. Input inventory and assigned roles.
2. Primary product lock.
3. Category family, loaded adapter, and buyer decision risk.
4. Source-material richness and fixed count.
5. Visible sold-product identity anchors, ambiguity notes, and supporting-element freedom.
6. Brand, palette, audience, and aesthetic direction.
7. Five candidate selling points.
8. One core value, 1-3 advantage pillars, and the evidence available for each.
9. Only objective facts that genuinely need a user decision.

Do not expose a large internal JSON schema unless another system explicitly requires structured data.

When structured validation is required, include a `category_route` object with `family`, `primary_adapter`, `buyer_decision_risk`, and optional `secondary_module`. For `packaged_consumable`, also include `consumable_profile` as `edible`, `topical_care`, or `ordinary_packaged`. Also include a `commerce_story` object with `core_value`, 1-3 `advantage_pillars`, `proof`, `usage_imagination`, and `purchase_decision`. Automatic `fixed_image_count` must be 6, 8, or 10. A count of 4 is valid only for a user-requested `compact_showcase`.
