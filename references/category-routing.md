# Category Routing

Route the product before building the commerce story. Category routing changes emphasis and quality-control priorities; it does not replace the common 6/8/10 narrative, seven-style library, fact boundary, or delivery contract.

## Category Families

Choose one primary family from the sold product and the buyer's main decision risk:

1. `human_worn`: apparel and other products whose value depends mainly on fit, silhouette, body relationship, styling, or wearing context.
2. `structured_durable`: bags, home goods, furniture, organizers, tools, simple appliances, and other products whose choice depends on form, construction, capacity, assembly, or use relationship.
3. `packaged_consumable`: food, beverage, beauty, skincare, pet, mother-and-baby, wellness, and other products whose choice depends on packaging, ingredients, sensory expectation, origin, usage, or trust information.
4. `electronics_equipment`: consumer electronics, smart devices, gaming hardware, lighting, digital accessories, professional equipment, and complex kits whose choice depends on function, interaction, compatibility, interfaces, components, or specifications.

Use one primary family. A secondary family may contribute one or two modules when the product is genuinely hybrid, such as a wearable smart device or a premium packaged electronic accessory. Do not blend full adapters.

## Routing Behavior

- Route automatically from the product, evidence, and purchase decision. Do not ask the user to select a category when the answer is clear.
- Ask only when two plausible sold products would load materially different rules, or when the requested positioning contradicts the visible product.
- Record `category_family`, `primary_adapter`, and any `secondary_module` in the plan.
- Load a category adapter only when it exists. Otherwise use the common workflow and state that category-specific validation is not yet proven.
- Never use category routing to invent facts, increase image count arbitrarily, introduce CTA, or turn one product into a fixed per-SKU template.

## Adapter Authority

A category adapter may specialize:

- source inventory and evidence fields;
- sold-product identity anchors;
- value-tree emphasis and buyer concerns;
- page-module selection and visual carriers;
- prompt vocabulary and likely material failures;
- category-specific QA severity.

It may not override:

- the primary-product lock;
- automatic 6/8/10 completeness tiers;
- the approved visible-copy list;
- objective-claim evidence requirements;
- the no-CTA rule for detail-page sections;
- supporting-element tolerance;
- the one-automatic-regeneration limit.

## Implemented Adapter

- `structured_durable` -> `structured-durable-adapter.md`
- `packaged_consumable` -> `packaged-consumable-adapter.md`
- `electronics_equipment` -> `electronics-adapter.md`

`human_worn` currently uses the common workflow. Its category examples in style or layout references describe reasonable directions, not proof of a separate production-level adapter.
