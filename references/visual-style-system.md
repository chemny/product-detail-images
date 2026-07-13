# Visual Style System

Choose one visual style and one typography/layout effect before writing image prompts.

## Visual Styles

Magazine editorial:
- Use for fashion, bags, premium appliances, professional gear, high-ticket items.
- Signals: large serif titles, grid alignment, editorial whitespace, controlled contrast.

Watercolor art:
- Use for pet food, snacks, mother-and-baby, soft lifestyle products, handmade or organic products.
- Signals: soft wash edges, warm backgrounds, hand-painted accents, gentle typography.

Tech future:
- Use for electronics, tools, lighting, smart devices, vehicles, sports equipment.
- Signals: cool palette, geometric lines, data visualization, technical callouts, controlled glow.

Retro film:
- Use for coffee, fragrance, lifestyle accessories, nostalgic packaging, food and drink.
- Signals: warm grain, paper texture, Polaroid frames, muted color.

Nordic minimal:
- Use for home goods, apparel basics, skincare, stationery, premium simple products.
- Signals: large whitespace, geometry, neutral palette, restrained type.

Neon cyber:
- Use only when the product already supports a bold futuristic or gaming tone.
- Signals: dark background, neon outlines, glow, urban future mood.

Natural organic:
- Use for food, wellness, pet, outdoor, sustainable, plant-based products.
- Signals: earth colors, plant elements, handmade texture, natural light.

## Typography And Layout Effects

Magazine:
- Large serif title.
- Thin decorative lines.
- Strict grid alignment.

Modern:
- Glassmorphism cards.
- Semi-transparent backgrounds.
- Soft rounded corners.

Luxury:
- Embossed or metallic title effects.
- Controlled highlights.
- Elegant shadows.

Art:
- Handwritten labels.
- Brush strokes.
- Asymmetric composition.

Cyber:
- Heavy sans-serif type.
- Neon outlines.
- Light trails.

Minimal:
- Thin type.
- Large whitespace.
- Precise alignment.

## Selection Heuristics

Make the visual decision from four evidence layers:

1. Product category:
   - Technical/professional equipment -> tech future, magazine editorial, industrial premium.
   - Fashion/accessories -> magazine editorial, luxury, minimal.
   - Food/pet/mother-and-baby -> natural organic, watercolor, warm lifestyle.
   - Home/lifestyle -> Nordic minimal, warm editorial, natural organic.

2. Source-image visual language:
   - Continue source signals only when they belong to the product or approved brand system: product color, contrast relationship, product angle, graphic style, and information density.
   - Do not automatically continue the photographed environment, surface, room, landscape, lighting, or background palette. Route those decisions through `background-system.md`.
   - If source images already use a dark high-contrast studio style, do not switch to soft watercolor or cute illustration.
   - If source images use bright packaging and playful graphics, do not switch to heavy industrial darkness unless the user asks.

3. Brand identity:
   - Preserve brand colors, logo position logic, typography tone, and visual accents.
   - Use brand accent colors sparingly as system markers across all images.

4. Buyer and platform:
   - Professional buyers need trust, specs, clarity, and controlled premium design.
   - Lifestyle buyers need scene, aspiration, comfort, and emotional relevance.
   - Marketplace detail pages need scan-friendly text and clear product proof.

Keep one visual style and one typography effect across all sections. Keep logo placement consistent, usually top-left unless the brand system suggests another fixed placement.

## Style Rationale Output

Before generation, summarize:

- Selected style.
- Evidence from source images.
- Brand color and accent logic.
- Typography direction.
- Styles deliberately avoided and why.

## Bilingual Layout Formats

Format A, stacked:
- Chinese title larger on top.
- English title smaller below.
- Best default for Chinese ecommerce pages.

Format B, inline:
- Chinese / English on the same line.
- Best for bullet points, cards, and badges.

Format C, separated:
- Chinese and English placed in different corners or zones.
- Use for editorial layouts with strong negative space.

Default combination:
- Titles use Format A.
- Selling points use Format B.
- Decorative English microcopy may use Format C.
