# Product Analysis

Analyze enough to create a strong image set. Do not turn recognition into a long compliance exercise.

## Required Recognition

- Primary product, supporting elements, and excluded products.
- Product category and concrete product name.
- Visible color, silhouette, pattern, closure, structure, surface, and notable details.
- Visible brand name, logo style, packaging language, or collection cues.
- Source-image clarity and restoration limitations.
- Source environment: incidental, useful context, required evidence, or protected brand asset.
- Likely audience, price feeling, aesthetic direction, and use context as planning inferences.
- Independent source-material groups for evidence depth and the automatic 6/8/10 count tier.

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

1. Primary product lock.
2. Source-material richness and fixed count.
3. Visible product identity and restoration invariants.
4. Brand, palette, audience, and aesthetic direction.
5. Five candidate selling points.
6. One core value, 1-3 advantage pillars, and the evidence available for each.
7. Only objective facts that genuinely need a user decision.

Do not expose a large internal JSON schema unless another system explicitly requires structured data.

When structured validation is required, include a `commerce_story` object with `core_value`, 1-3 `advantage_pillars`, `proof`, `usage_imagination`, and `purchase_decision`. Automatic `fixed_image_count` must be 6, 8, or 10. A count of 4 is valid only for a user-requested `compact_showcase`.
