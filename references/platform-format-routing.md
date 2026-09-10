# Platform Format Routing

Select the canvas from the publishing surface, not from the platform name alone. A platform may use different formats for product-gallery images, detail sections, social cards, ads, and video covers.

## Resolution Order

Use this precedence:

1. User-specified per-image dimensions or ratio.
2. User-specified asset class, such as product main image, product detail module, social card, ad, or video cover.
3. Current official specification for the named platform surface.
4. Defaults in this file.

If upload compliance matters and the platform specification may have changed, verify the current official rule before generation. State when a value is a skill default rather than an official platform requirement.

## Stable Defaults

| Publishing surface | Default ratio | Default pixels | Notes |
|---|---:|---:|---|
| Generic ecommerce product-gallery image | 3:4 | 750x1000 | Safe default for apparel and lifestyle products when the platform is unknown. |
| Generic modular ecommerce detail image | 3:4 | 750x1000 | Prefer reusable modules over an assumed 9:16 canvas. |
| Xiaohongshu product image | 3:4 | 750x1000 | Official product-image formats include 1:1 and 3:4; use 1:1 only when requested or compositionally justified. |
| Douyin ecommerce 3:4 main image | 3:4 | 750x1000 | Use for the current 3:4 main-image publishing surface. |
| Short-video cover or immersive vertical ad | 9:16 | platform_default | Use only when the user explicitly requests this asset type. |
| Single long detail image | flexible | platform_default | Resolve current width, height, file-size, and slicing limits before generation. |

## Dual-Expression Canvas Lock

For the generic ecommerce default, always express the same canvas in both forms:

- ratio: `3:4 portrait`;
- target pixels: `750x1000 px`.

Put both forms in every production prompt. Use this exact default sentence at the beginning of field 1 and repeat it in field 6:

`Canvas lock: 3:4 portrait; target 750x1000 px.`

The ratio and pixels are not alternatives. They are redundant cues for generators that may recognize one form more reliably than the other.

User choice has priority. If the user supplies only a ratio, resolve compatible output pixels before generation. If the user supplies only pixels, derive and record the ratio. If the user supplies both and they conflict, obtain one corrected canvas decision before generation.

## Verified Platform Notes

Verified on 2026-07-18:

- Xiaohongshu Open Platform lists product images at 800x800 or 750x1000, with ratios 1:1 or 3:4. It lists product-detail images separately with a width of 750-1242 px, height no greater than 1546 px, and file size no greater than 2 MB per image. Source: https://school.xiaohongshu.com/en/open/product/create-spl-item.html
- Douyin Ecommerce Learning Center announced the unified `3:4 main image` publishing entry for new products, with rollout from 2026-04-01. Source: https://school.jinritemai.com/doudian/wap/article/aJgwEivJcR7G

These notes are a dated evidence snapshot, not a promise that every category, campaign placement, or future publishing surface uses the same rule.

## Planning Rules

- Ask for the target publishing surface only when choosing incorrectly would force regeneration or failed upload. Otherwise use the conservative default and label it clearly.
- Do not equate `detail image` with `9:16`.
- Do not equate a platform's short-video cover with its ecommerce product image.
- For a multi-platform apparel set without further direction, use 3:4 at 750x1000.
- Natural-language ratio and pixel instructions do not guarantee that a built-in generation tool will return the requested canvas. Inspect each raw output mechanically before continuing.
- When exact pixels are unsupported by the generation tool, preserve the approved 3:4 composition and export to 750x1000 using uniform scaling plus crop, pad, or background extension. Never stretch the product, text, model, or layout.
- A raw ratio mismatch triggers one page-level regeneration before normalization. Do not wait until the end of a set to discover mixed raw ratios.
