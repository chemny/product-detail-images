# Packaged Consumable Adapter

Use this adapter for food, beverages, coffee, beauty, skincare, pet, mother-and-baby, wellness, and ordinary packaged goods. It specializes the common workflow; it does not create a template for each product.

## Route The Subprofile

Record one `consumable_profile`:

- `edible`: food, beverage, coffee, and other products evaluated through flavor, texture, serving state, ingredients, nutrition, and trust.
- `topical_care`: beauty, skincare, and personal-care products evaluated through texture, application, ingredients, routine, efficacy, and trust.
- `ordinary_packaged`: other packaged goods evaluated mainly through form, opening, use, quantity, package relationship, and trust information.

## Source Inventory

Inventory every visible or supplied source before planning:

- front, back, side, top, and bottom package faces;
- brand, product name, SKU, flavor, scent, color, or variant;
- net content, count, size, and pack configuration;
- ingredient, nutrition, usage, care, warning, origin, certification, and efficacy information;
- outer package, inner package, individual units, included items, and their relationship;
- product-state evidence such as whole, broken, poured, served, dispensed, swatched, opened, or in use;
- separate brand, copy, specification, and style-reference assets.

Do not infer a hidden label, ingredient, nutrition value, allergen, efficacy, shelf life, origin, certification, warning, or package content from category convention.

## Identity Anchors

Protect the purchase-relevant identity of the sold product:

- package geometry, dominant color system, and principal graphics;
- visible brand and product name;
- SKU, flavor, scent, color, or other variant marker;
- net content, count, and pack configuration when supplied or legible;
- the product's recognizable form, color, and primary depiction;
- the relationship between the outer package, inner package, and individual units.

Allow supporting dishes, utensils, surfaces, ingredients used only as decoration, hands, props, and environments to vary when they do not change the product promise or imply unsupported contents.

## Label Text Hierarchy

Treat package text according to purchase impact:

1. `critical_identity`: brand, product name, SKU or variant, net content, count, and pack configuration. Preserve exactly when visible or supplied.
2. `decision_claim`: ingredients, nutrition, usage, warnings, certifications, origin, and efficacy. Show only when legible or user supplied.
3. `decorative_fine_print`: unreadable small print and ornamental label detail. Preserve its visual role without reconstructing or inventing copy; keep it non-prominent.

Use deterministic local typography or compositing for dense exact labels and specification panels when available. If only text is wrong on an otherwise approved page, repair the text locally before considering full regeneration.

## Product Preservation Mode

Choose the lowest-risk carrier that still proves the page's point:

- `preserve_or_composite` is the default for packaging, logos, variants, and specification-bearing views.
- `reference_reconstruction` may show an edible product broken, poured, plated, or served, or a topical product dispensed, swatched, or applied, when the visible source supports its form and color.
- `conceptual_support` may express mood, aroma, softness, refreshment, ritual, or sensory association, but must not imply a measured result or factual ingredient.

Do not make the image model redraw exact package text merely to vary the camera angle. Change the supporting world, crop, scale, or product-state relationship while preserving or compositing the package when identity accuracy matters.

## Sensory Expression And Objective Claims

Creative sensory language may describe a visible or clearly aesthetic impression, such as crisp-looking layers, silky visual texture, warm baked color, refreshing mood, or a quiet daily ritual. It must remain clearly expressive rather than measured.

The following require visible or user-provided evidence: exact ingredients, allergens, nutrition, calorie or sugar claims, health or medical benefit, tested efficacy, duration, safety result, origin, process, organic status, freshness guarantee, certification, comparative performance, and quantified sensory claims.

If information is missing, state the gap once and let the user choose whether to supply it, replace the module with supported content, or use a clearly conceptual expression. Do not invent a substitute fact.

## Quantity And Pack Visualization

- Communicate exact count, weight, volume, and pack configuration through approved deterministic text.
- Do not require the image model to draw every unit merely to prove an exact count.
- Representative units plus an exact supplied specification are acceptable when the visual is clearly illustrative.
- When outer package and individual units are both shown, keep their size, quantity relationship, and opening logic plausible.

## Commerce Story Emphasis

Start with the six-image default. When additional supported packaging, sensory, routine, variant, or trust dimensions justify an eight-image expanded set, use this category narrative:

1. product recognition and positioning;
2. consumption, use, or routine imagination;
3. core sensory or practical value;
4. product state, texture, form, or interaction evidence;
5. ingredient, material, process, or efficacy evidence only when supported;
6. outer package, individual unit, contents, or combination relationship;
7. trust information, usage guidance, warning, or decision reassurance;
8. SKU, variant, net content, count, and package-decision summary.

For the six-image default, merge adjacent packaging, sensory, routine, and decision modules without losing mandatory coverage. Expand to ten only when supplied information still supports deeper proof, comparison, routine, variant, or specification content after a strong eight-page plan. Never add hollow pages to reach a count.

### Evidence Carriers By Subprofile

- `edible`: whole and broken states, crumb or cross-section, pour or serving state, scale with tableware, individual packaging, and supported ingredient or process evidence.
- `topical_care`: package preservation, product texture, dispensing or swatch, application relationship, routine order, and supported ingredient or efficacy evidence.
- `ordinary_packaged`: package opening, product form, use relationship, inner and outer packaging, contents, quantity, and supplied trust or instruction information.

Decorative raw ingredients may support atmosphere only when they do not suggest the product contains them. A factual ingredient module requires evidence.

## Prompt Emphasis

Carry only the anchors needed for the page:

- exact package or product identity anchors;
- preservation mode;
- product state and physical relationship;
- exact approved visible copy and its label tier;
- evidence-supported sensory, ingredient, usage, or trust content;
- likely page-specific failures, such as wrong variant, wrong quantity, implausible pack relationship, or invented claim.

Avoid generic piles of ingredients, laboratory graphics, certification seals, health icons, or benefit badges unless they are supported and serve the page's commerce job.

## Category QA

Treat these as critical when visible or supplied and purchase relevant:

- wrong brand, product name, SKU, flavor, scent, color, or variant;
- materially wrong package geometry, dominant color, product form, or pack configuration;
- wrong net content, count, size, or outer-to-inner-package relationship;
- fabricated ingredient, allergen, nutrition, origin, process, health, medical, efficacy, safety, certification, warning, or included item;
- package text or imagery that materially changes what the buyer believes the product is or contains.

Treat decorative fine-print drift, minor supporting-prop variation, and harmless serving or styling differences as reviewable or acceptable when they do not change product identity or promise. Apply the common one-automatic-regeneration limit, and prefer local repair for isolated text errors.
