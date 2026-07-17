# Generated Image Quality Assurance

Inspect after generation. Do not preload this entire checklist into every image prompt.

Assign one status:

- `approved`: delivery basics and creative quality pass.
- `needs_revision`: a critical, purchase-relevant failure remains.

## Issue Severity

Classify before revising:

- **Critical — regenerate:** the sold product becomes a different product or SKU; its main color, major silhouette, dominant pattern, key structure, or required text materially changes; anatomy or product-body interaction is broken; an objective claim is fabricated; a CTA appears where prohibited.
- **Review — usually accept or repair locally:** a minor sold-product detail drifts but remains within a plausible interpretation of the source; the visual idea is weaker than planned without becoming misleading; or the model adds harmless descriptive text outside the approved copy list. Judge it in the context of the full set before revising.
- **Acceptable variation — pass:** ordinary changes to supporting shoes, bags, jewelry, metal hardware, hair, props, lighting, pose, or source-ambiguous construction that do not misrepresent or compete with the sold product.

Ask one question before regeneration: `Would this difference materially change what a buyer believes they are purchasing?` If no, do not regenerate.

## Gate 1: Delivery Basics

Check:

- primary product remains dominant and recognizable;
- the sold product's clear identity anchors do not materially drift;
- anatomy, pose, garment-body interaction, hands, limbs, and face are plausible;
- planned crop is respected and important product/body edges remain visible;
- supporting accessories are physically plausible and visually subordinate; ordinary metal or decorative changes are not failures;
- subject scale, contact shadow, perspective, and support surface feel grounded;
- required copy is readable and no internal labels or unwanted text appear;
- generated text matches the approved closed copy list; any extra comfort, fit, material, performance, efficacy, comparison, popularity, or user-experience statement is treated as unsupported unless supplied or visibly evidenced;
- objective claims match supplied or visible information;
- no CTA or button-like element appears on a detail-page section.

Only a critical failure requires automatic revision. Log review-level differences and judge the complete set before deciding whether they justify the cost and drift risk of another generation.

## Gate 1B: Delivery Manifest

Before handoff, verify mechanically:

- every approved asset exists in the declared output directory;
- delivered count, numerical order, role, and section theme match the approved manifest;
- filenames use stable numerical prefixes and do not silently overwrite another approved asset;
- actual pixel width, height, and aspect ratio have been inspected and recorded;
- any resize, crop, or padding preserves the product and approved composition without stretching;
- source files remain untouched unless the user explicitly requested an edit to them.

A missing file, wrong count, or materially wrong delivery size blocks delivery but does not require regenerating a visually correct image when export correction can solve it.

## Gate 2: Creative Quality

Check:

- the page communicates one clear idea at first glance;
- the image has a deliberate focal point and commercial visual impact;
- the product meaningfully interacts with the scene or concept rather than sitting in a generic background;
- concrete scene copy is supported by recognizable environmental cues; conceptual pages do not pretend to depict a literal place;
- typography feels integrated into the composition, not pasted onto a leftover empty area;
- the headline is memorable and the proof line adds meaning;
- the page adds new purchase, use, aesthetic, or decision value;
- information density fits the archetype;
- the result looks like a finished ecommerce design, not a generic beauty shot.

A technically valid but visually generic image is a review-level issue unless it leaves the page without a clear commerce job or useful product meaning.

## Gate 3: Commerce Completeness

Check the full set:

- product recognition is immediate;
- one core value is memorable after viewing the set;
- 1-3 advantage pillars are clearly expressed;
- important advantages have visible or supplied proof;
- at least one page creates usage, wearing, pairing, or ownership imagination;
- at least one page supports purchase choice or resolves a likely buyer concern;
- image and text contribute different but complementary information;
- no page exists only because it is beautiful;
- the selected count carries the story without overcrowding or filler.
- an eight- or ten-image set contains a genuine category-appropriate visual, evidence, or information peak tied to the strongest advantage;
- the final page adds new decision information rather than summarizing earlier pages only.

If any mandatory role is absent, the set is incomplete even when every individual page looks good.

## Gate 4: Set Quality

After all individual pages pass, check:

- palette, lighting character, typography, margins, logo logic, and material language form one brand world;
- page spaces and compositions still vary meaningfully;
- complete sets contain at least three camera distances, three subject states, and four visual carriers;
- no two pages share pose/state, camera distance, and subject position together;
- adjacent model pages vary meaningfully in at least two of setting, action, expression/gaze, distance, or angle when the storyboard calls for variation;
- adjacent pages do not repeat the same layout rhythm or information density;
- copy sentence patterns do not repeat mechanically;
- copy density varies intentionally by page role, and substantive supplied information has not been flattened into generic slogans;
- sets of six or more use at least three headline forms, and adjacent pages do not repeat the same form without a strong reason;
- covering the text still leaves clearly distinct images;
- the sequence has rhythm: attraction, imagination, proof, and decision support rather than repeated hero imagery.

## Revision Rule

Name the concrete critical failure, then revise only the relevant prompt dimension:

- generic visual → strengthen the product-concept relationship and scene construction;
- pasted-on typography → redesign the text zone, hierarchy, and low-texture area;
- weak copy → rewrite the page idea and headline, not only the adjective;
- repeated page → change visual carrier, subject state, distance, position, or blueprint;
- scene-copy mismatch → add the missing recognizable scene cues or rewrite the copy as conceptual;
- critical sold-product drift → reinforce only the affected clear identity anchors;
- crop/anatomy failure → clarify framing, required edges, and pose;
- garbled text → shorten the copy, enlarge hierarchy, or repair typography after visual approval;
- unapproved extra text → remove or replace the text locally when possible; regenerate only when the unsupported statement materially changes the product promise and cannot be separated from the image;
- objective-claim failure → remove or replace the unsupported fact.

Automatically regenerate a page at most once. Text-only failures on an otherwise approved visual should be repaired locally before considering full regeneration. Do not revise for ordinary supporting-accessory changes, source ambiguity, or cosmetic differences that do not change the sold-product promise. If a second critical failure remains, report it and let the user decide whether another generation is worthwhile.

Deliver approved assets and briefly note any accepted ambiguity that materially affects interpretation. Do not turn minor visual variation into a warning list.
