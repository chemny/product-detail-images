# Structured Durable Adapter

Load this adapter when `category_family` is `structured_durable`. It covers bags, organizers, home goods, furniture, tools, simple appliances, outdoor equipment, and other durable products whose purchase depends mainly on form, construction, capacity, assembly, or use relationship.

## 1. Source Inventory

Inspect and assign every available source:

- appearance: front, back, sides, top, bottom, folded, expanded, open, closed, assembled, installed, worn, or carried states;
- structure: openings, closures, hinges, handles, straps, chains, pockets, compartments, seams, joints, fasteners, edges, feet, supports, or contact surfaces;
- interior and capacity: internal views, dividers, usable space, example contents, dimensions, volume, load, or weight evidence;
- use relationship: supplied hand, body, room, furniture, vehicle, workbench, installation, storage, carrying, or operation references;
- component evidence: included parts, accessories, replacement pieces, tools, packaging, assembly steps, or combination relationships;
- specification evidence: dimensions, weight, material, load, durability, resistance, compatibility, care, warranty, certification, or test results;
- brand assets and style references, kept separate from product evidence.

Do not infer a hidden pocket, interior divider, capacity, load, material, opening mechanism, included accessory, assembly structure, or product dimension from category convention alone.

## 2. Identity Anchors

Classify only clearly visible or supplied purchase-relevant features as strict anchors:

- overall silhouette, width-height-depth relationship, and dominant proportions;
- opening, closure, flap, zipper, buckle, latch, hinge, lock, or folding relationship;
- handle, strap, chain, support, leg, mount, or connector shape and attachment position;
- visible pocket, compartment, panel, frame, seam, joint, edge, base, or surface pattern;
- approved logo, model mark, distinctive hardware, and SKU color;
- assembled, expanded, installed, worn, or carried state when it changes what is being sold.

Allow ordinary variation in models, clothing, hands, rooms, desks, plants, vehicles, styling props, and other supporting elements. A supporting object becomes critical only when it is presented as included, structurally connected, load-bearing, scale evidence, or part of the product's function.

## 3. Product Preservation Mode

Choose one mode per page and record it in the page plan:

- `preserve_or_composite`: default when the source product is clear and the page needs only a new background, typography, annotation, detail crop, or surrounding scene. Retain the product pixels or structure as closely as the tool allows.
- `reference_reconstruction`: use only when a new open/closed state, angle, body relationship, room relationship, operation, installation, assembly, or carrying state is necessary and cannot be built from the source.
- `conceptual_support`: generate light, motion, organization, protection, capacity, or material metaphors around a preserved or reconstructed product without presenting them as measured proof.

Do not reconstruct an entire durable product merely to change the background. When reconstruction is necessary, compare against the authoritative source rather than an earlier generated page. An accepted hero may lock style, but it never replaces the source as product truth.

## 4. Value And Evidence Chain

Build each advantage through:

`buyer need -> visible or supplied structure -> use or proof relationship -> customer meaning -> page message`

Avoid stopping at generic words such as `premium`, `large`, `strong`, `organized`, `comfortable`, `durable`, or `protective`. Show which visible structure, supplied measurement, use state, or confirmed result makes the advantage believable.

Exact dimensions, capacity, load, weight, material, resistance, durability, comfort, fit, compatibility, care, warranty, certification, test, or included contents require supplied evidence.

## 5. Complete Structured-Durable Narrative

Use the common count tiers. For an eight-image default set, prefer:

1. **Positioning:** product recognition, core value, and 2-3 short supported advantages.
2. **Use or ownership scene:** carrying, placing, organizing, operating, installing, combining, or belonging in the buyer's environment.
3. **Core structure or function:** the strongest structural reason to choose the product.
4. **Exterior detail evidence:** closure, hardware, surface, seam, frame, joint, support, or construction relationship.
5. **Opening, operation, assembly, or state change:** only when supplied or visibly supportable.
6. **Interior, capacity, scale, body, or room relationship:** only with adequate evidence; otherwise replace with another visible use or structure page.
7. **Material, component, combination, care, or trust information:** confirmed information or visible proof.
8. **Specification, package, selection, fit, compatibility, or final purchase decision:** new information, not a slogan recap or survey.

Compress the same roles into six images for simple products. Expand structure proof, state changes, components, installation, comparison, scale, or decision support to ten images for complex products.

## 6. Scale And Human Relationship

- Treat an exact body, hand, room, furniture, or object relationship as scale evidence only when the source or supplied dimensions support it.
- When scale is unknown, use the scene to express styling or use context without making size, fit, capacity, reach, comfort, or load claims.
- In reconstructed wearing or carrying scenes, preserve the product's width-height ratio, side depth, handle or strap attachment, closure, hardware position, and visible pattern before judging model styling.
- A minor scale variation is review-level when the product remains the same SKU and no size claim is made. Regenerate only when the relationship would materially change what the buyer believes fits, carries, holds, reaches, or occupies space.

## 7. Structure Evidence Rule

A structure or function page must add visible evidence beyond the hero. Use at least one:

- a faithful detail crop;
- open versus closed, folded versus expanded, assembled versus separated, or before/during/after state;
- a real hand, body, surface, room, mount, component, or combination relationship;
- interior/exterior comparison supported by source material;
- a dimension, capacity, load, compatibility, or package relationship supported by supplied facts;
- annotations that terminate on the actual physical feature being explained.

Mentally hide the text and callouts: the image should still reveal more about the structure or use than the hero page. If it does not, redesign the evidence carrier before generation.

## 8. Visual Direction

Choose style from product identity and buyer expectations rather than applying one durable-goods look:

- premium bags and accessories often fit `Magazine Editorial` or `Nordic Minimal`;
- home, storage, and simple furniture often fit `Nordic Minimal`, `Natural Organic`, or restrained editorial systems;
- tools, appliances, and performance equipment may fit `Tech Future` or rational minimal systems;
- outdoor products may fit `Natural Organic`, technical outdoor, or restrained performance direction.

Keep one primary visual center. Avoid decorative rooms, models, HUD graphics, or luxury props that dominate the sold product or substitute atmosphere for evidence.

## 9. Prompt Additions

For relevant pages include only:

- selected `product_preservation_mode` and authoritative product source;
- strict silhouette, proportion, opening, closure, attachment, pocket, component, and hardware anchors;
- supported state, scale, capacity, body, room, assembly, or use relationship;
- which supporting elements may vary;
- the page-specific difference most likely to mislead a buyer.

Do not paste the full adapter into every prompt.

## 10. Structured-Durable QA

Treat these as critical only when visible or supplied and purchase-relevant:

- wrong SKU silhouette or materially wrong width-height-depth relationship;
- wrong closure, opening, handle, strap, chain, hinge, joint, pocket, support, attachment, or assembly relationship;
- logo, distinctive hardware, surface pattern, included component, or SKU color materially changes;
- fabricated interior, compartment, capacity, dimension, load, material, resistance, comfort, compatibility, care, package, certification, or durability claim;
- impossible body, hand, room, support, mounting, carrying, or load-bearing relationship;
- a structure annotation points to the wrong physical feature and changes buyer understanding.

Usually accept or review:

- ordinary variation in model, clothing, hair, room, desk, plant, background, generic styling prop, reflection, or lighting;
- minor scale or pose differences that do not change the product identity or imply a factual fit/capacity claim;
- source-ambiguous surface or construction details that remain plausible and subordinate.

Before regeneration ask: `Would this difference change what the buyer believes the product is, opens, closes, carries, holds, includes, supports, fits, or connects to?` If no, do not regenerate.

## 11. Missing-Information Behavior

When interior, capacity, dimension, material, load, assembly, use, compatibility, or package evidence is absent:

- state what can be expressed from visible evidence;
- state which decision claim is unsupported;
- offer the user a concise choice: supply evidence, replace the module with visible exterior/use information, or proceed with a clearly conceptual page;
- do not fabricate a generic interior, capacity demonstration, material story, or specification table.
