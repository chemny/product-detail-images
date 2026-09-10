# Electronics And Equipment Adapter

Load this adapter when `category_family` is `electronics_equipment`. It covers consumer electronics, smart devices, gaming hardware, lighting, digital accessories, professional equipment, and complex electronic kits without creating a template for each product type.

## 1. Electronics Input Inventory

Inspect and assign every available source:

- product appearance: front, back, sides, top, bottom, folded/open states, colorways, finish, scale references;
- interface evidence: ports, buttons, switches, indicators, sensors, camera openings, vents, screens, controls, connectors;
- interaction evidence: supplied UI screenshots, app screens, workflows, hand relationships, mounting, charging, pairing, or installation;
- specification evidence: model, dimensions, weight, power, battery, charging, protocols, compatibility, rating, performance, warranty, certification;
- component evidence: included accessories, cables, adapters, cases, mounts, replaceable parts, package contents;
- brand assets: approved logo, product name, typography, UI language, packaging, color system;
- style references: lighting, composition, technical graphics, campaign direction, or competitor presentation that must not be mistaken for product evidence.

Do not infer a hidden interface, internal component, supplied accessory, UI screen, specification, or compatibility relationship from category convention alone.

## 2. Electronics Identity Anchors

Classify only clearly visible or supplied product-defining features as strict anchors:

- overall industrial-design geometry and proportions;
- SKU color and finish;
- visible screen, bezel, lens, sensor, grille, vent, hinge, handle, or control layout;
- visible or supplied port type, count, and location;
- model name, approved logo, and required device text;
- included components and their connection relationship;
- open, closed, installed, worn, docked, or assembled state when it changes what is being sold.

Allow reasonable variation in reflections, generic desks, hands, cables used only as scene props, non-sold furniture, and other supporting elements. A support prop becomes critical only when it is presented as included, compatible, or functionally connected.

## 3. Value And Evidence Chain

Build each advantage through:

`buyer problem -> supplied or visible feature -> mechanism or use evidence -> customer meaning -> page message`

Do not stop at decorative words such as `powerful`, `smart`, `professional`, `fast`, or `stable`. Explain what visible feature, supplied parameter, interaction, or comparison makes the benefit believable.

Exact battery life, power, speed, charging time, protocol, waterproof rating, refresh rate, resolution, accuracy, latency, durability, compatibility, benchmark, certification, or warranty requires supplied evidence. If absent, explain the missing information in the plan and let the user supply it, replace the module, or use visible product information.

## 4. Complete Electronics Narrative

Use the common count tiers. Start with the six-image default. When additional supported electronics dimensions justify an eight-image expanded set, prefer:

1. **Positioning:** product recognition, core outcome, and 2-3 short supported advantage labels.
2. **Buyer problem or use scene:** show the concrete work, entertainment, mobility, installation, or ownership context.
3. **Core capability overview:** connect the strongest 1-3 functions to one clear visual system.
4. **Feature or mechanism:** explain one decisive function through visible structure, supplied interaction, or supported technical concept.
5. **Interaction or workflow:** controls, UI, setup, pairing, handling, switching, installation, or use sequence.
6. **Structure, interface, or components:** ports, controls, external construction, included components, or assembly relationship.
7. **Specification, compatibility, or model choice:** confirmed parameters and decision guidance in a disciplined information layout.
8. **Package, usage, fit, support, or final decision:** new purchase information, not a slogan recap or buyer survey.

For the six-image default, merge related function, interaction, and proof modules without losing mandatory decision coverage. Expand to ten images only when further supported function proof, comparison, component systems, or decision support remain after a strong eight-page plan.

## 5. Electronics Visual Carriers

Choose carriers from the page's proof requirement:

- controlled product hero with scale and geometry visible;
- real use or installation relationship;
- external structure close-up;
- port and control map;
- supplied UI or interaction sequence;
- component or package-content system;
- dimension, compatibility, or specification file;
- supported comparison or state change;
- conceptual signal, energy, airflow, sound, light, or data visualization when clearly presented as explanation rather than measured proof.

Use an exploded view, transparent shell, internal cutaway, circuit path, thermal map, signal path, or mechanism diagram only when supplied evidence supports it. Otherwise show external structure or a clearly conceptual metaphor without presenting invented internals as fact.

## 6. Product Preservation Mode

Choose how the product enters the generated page before writing the prompt:

- `preserve_or_composite`: prefer when the source product is clear and the page does not require a new product angle or state. Keep the original product pixels, silhouette, controls, interfaces, display, logo, and structural relationships; rebuild the background, typography, annotations, shadows, and supporting scene around it.
- `reference_reconstruction`: use only when the page genuinely needs a new angle, hand interaction, open/closed state, installation relationship, or camera distance that the source cannot supply. Lock the visible industrial-design anchors and accept only differences that do not change the SKU or function.
- `conceptual_support`: use generated light, signal, motion, sound, energy, airflow, or data graphics around a preserved or reconstructed product. Never let the concept replace factual product structure.

Default to `preserve_or_composite` for clear industrial-product sources. Do not reconstruct the entire product merely to change the background or create more visual polish. Record the selected mode in every electronics page plan.

When `reference_reconstruction` is necessary, compare the result against the authoritative product source rather than only against an earlier generated page. Treat the accepted hero as a style reference, not as the new source of product truth.

## 7. Style And Layout Direction

- Recommend `Tech Future` for precise capability-led products.
- Use `Nordic Minimal` as the safe alternative for simple premium electronics, home devices, and accessories.
- Use `Neon Cyber` only when gaming, youth, nightlife, or bold futuristic positioning is genuinely supported.
- Prefer horizontal grid systems, strong alignment, consistent annotation logic, and clear information hierarchy.
- A technical page must still have one visual center. Do not fill the canvas with arbitrary HUD decoration, fake charts, random numbers, or meaningless glowing lines.
- When multiple exact values or compatibility labels must be perfect, generate the product visual first and use a deterministic typography or local text-compositing pass when available instead of relying on the image model to render dense technical text.

## 8. Electronics Prompt Additions

For relevant pages, add only the supported fields needed for the page:

- exact product state and viewing angle;
- strict visible geometry anchors;
- supported port, control, screen, component, and connection relationships;
- exact approved specification or compatibility copy;
- whether a diagram is factual, supplied, or explicitly conceptual;
- which support props may vary;
- the page-specific failure most likely to mislead a buyer.
- the selected `product_preservation_mode` and which source remains authoritative for product geometry.

Do not paste the full adapter into every prompt.

## 9. Functional Evidence Rule

A function or structure page must add visible evidence beyond the hero. It cannot be the same product angle with new copy and decorative callouts.

Use at least one evidence change:

- empty versus occupied state;
- open versus closed state;
- before, during, or after an operation;
- a new close-up that reveals the relevant structure;
- a real hand, cable, mount, component, or device relationship;
- a supported interface, workflow, compatibility, or package relationship;
- an external structure map whose annotations terminate on the actual physical feature.

Callout endpoints must land on the structure being explained, not on a support prop placed inside it. Mentally hide the text and callouts: the image should still reveal more about the function than the hero page. If it does not, redesign the evidence carrier before generation.

## 10. Electronics QA

Treat these as critical only when visible or supplied and purchase-relevant:

- wrong product or SKU geometry;
- wrong color, model name, logo, screen, control, port type, count, or location;
- impossible cable, mount, charging, assembly, or hand-product relationship;
- included component added, removed, or replaced;
- fabricated UI, internal mechanism, specification, compatibility, certification, comparison, or performance claim;
- a conceptual diagram presented as measured or literal proof.
- a function-page callout that identifies the wrong physical feature and would mislead the buyer about operation or structure.

Usually accept or review:

- minor reflection, highlight, background, generic desk, or non-sold prop variation;
- harmless changes to generic support cables that are not shown as included or connected;
- small styling differences that do not alter geometry, operation, compatibility, or the product promise.

Before regeneration ask: `Would this difference change what the buyer believes the device is, includes, connects to, supports, or can do?` If no, do not regenerate.

Also verify that a reconstructed product was necessary for the approved page. When a clear source could have been preserved, product drift caused by unnecessary reconstruction is a planning failure; switch the page to `preserve_or_composite` before spending another reconstruction attempt.

## 11. Missing-Information Behavior

When technical information is absent:

- state what can be expressed from visible evidence;
- state which parameter, UI, compatibility, or component claim is unsupported;
- offer the user a concise choice: supply evidence, replace the module with visible structure/use information, or proceed with a clearly conceptual page;
- do not automatically downgrade the entire series or fabricate a generic specification dashboard.
