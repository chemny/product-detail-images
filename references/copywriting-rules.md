# Copywriting And Production Prompt Rules

## Series Copy Strategy

Choose one category-appropriate series-level commercial mood before writing page copy. Examples include editorial confidence for apparel, organized ease for bags, ingredient-led warmth for food, precise capability for electronics, calm utility for home goods, or professional performance for tools.

Give each page a distinct language job:

- Hero: position the product and set the tone.
- Lifestyle: create use or wearing desire.
- Concept: deliver the strongest memory point.
- Detail: name and explain one visible advantage.
- Moodboard: elevate color, collection, or aesthetic meaning.
- Specification: support a decision with confirmed information.
- Guide: reduce hesitation with useful instructions.

## Page Copy

Use two primary layers:

1. **Headline:** normally 4-12 Chinese characters; memorable, commercial, and specific to the page idea.
2. **Proof line:** one concrete sentence that explains the visible, supplied, experiential, or clearly conceptual basis.

Add up to three scan labels only when they improve understanding. English supports atmosphere and hierarchy; it does not need to translate every Chinese line mechanically.

Avoid using the same sentence structure across the set. Do not make every headline a neutral feature label or a repeated `短句，短句` construction.

For sets of six or more, use at least three headline forms:

- short naming: `A字宽摆`;
- structural progression: from handle to interior, ingredient to taste, interface to workflow, or form to use;
- question or choice: ask which color, size, flavor, mode, kit, or scenario fits;
- direct benefit: name one visible or supported advantage plainly;
- emotional positioning: define the product's desired lifestyle or brand mood;
- contrast or transformation: show before/after use, compact/expanded, ordinary/special, or setup/result when supported.

Do not reuse the examples mechanically. Record the headline form in the page plan and revise the later page when two adjacent pages use the same form.

Creative aesthetic language may be bold. Exact composition, data, certification, review, performance, medical, safety, comparison, size, and brand-history claims require support.

## Layout Copy Rules

- Keep the main headline to no more than two lines.
- Keep one proof line concise enough to read on mobile.
- Use Chinese as the primary sales language unless the user requests otherwise.
- Use English as a smaller title, caption, label, or separated editorial element.
- Do not generate internal field labels such as `标题`, `副标题`, `卖点一`, `示例`, or `待补充`.
- Do not place CTA or button-like copy in detail-page sections.
- Every final detail-page image needs useful commerce copy; no text-free final page.

## Full Production Prompt Structure

Do not condense away any of these sections before calling image generation.

### 1. Page objective

State the purchase or emotional job and the single memorable visual idea.

### 2. Visual scene

Describe the actual environment, materials, foreground and background elements, palette, lighting direction, depth, atmosphere, and how the product interacts with conceptual elements. Describe how the desired effect is formed rather than merely requesting `premium`, `editorial`, or `luxury`.

### 3. Product restoration

State the source invariants: silhouette, color, pattern, closure, logo, visible text, proportions, surface, and relevant structure. The uploaded image is the product reference, not an automatic background reference.

### 4. Composition and camera

State subject position and approximate scale, framing type, camera distance, pose or state, support relationships, text-safe region, allowed crop, and required visible edges. Use measurements only when they clarify the design.

### 5. Exact visible copy

List the final Chinese headline, English support line when used, proof line, and up to three labels. Do not send placeholders.

### 6. Layout blueprint

State logo zone, subject zone, text zone, headline width and line count, alignment axis, Chinese-English relative size, font categories, color contrast, spacing, and low-texture area behind text.

### 7. Page-specific negative constraints

Use only constraints relevant to likely failures on the page. Examples: wrong SKU color or garment structure for apparel; wrong handle, closure, or compartment for bags; invented ingredient or package text for food; wrong ports, controls, or specifications for electronics; incorrect scale, assembly, or room contact for home goods. Add anatomy, crop, text, CTA, or background constraints only when relevant.

Do not paste workflow rules, evidence schemas, scoring logic, risk essays, or generic 20-30-item negative lists into the image prompt.

## Prompt Quality Check

Before generation, confirm that the prompt makes these questions answerable:

- What is the one visual idea?
- What exactly appears in the frame?
- How does the product relate to the scene or concept?
- Where are the subject and text?
- What exact words appear?
- What product details cannot change?
- Which few failures are most likely on this page?
