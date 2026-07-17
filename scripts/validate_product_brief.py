#!/usr/bin/env python3
"""Validate a product brief JSON for the product-detail-images skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "primary_product",
    "supporting_elements",
    "excluded_products",
    "material_richness",
    "image_quality",
    "source_environment",
    "category_route",
    "brand",
    "product",
    "selling_points",
    "visual_identity",
    "audience",
    "claims_and_parameters",
    "commerce_story",
    "needs_user_confirmation",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_product_brief.py <product_brief.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    if not isinstance(data.get("selling_points", []), list):
        errors.append("selling_points must be a list")
    elif len(data.get("selling_points", [])) != 5:
        errors.append("selling_points must include exactly 5 candidate items")
    else:
        allowed_statuses = {"visible", "user_provided", "proposed", "not_supported"}
        for index, item in enumerate(data["selling_points"], start=1):
            if not isinstance(item, dict):
                errors.append(f"selling_points[{index}] must be an object")
            elif item.get("source_status") not in allowed_statuses:
                errors.append(
                    f"selling_points[{index}].source_status must be visible, user_provided, proposed, or not_supported"
                )

    if not isinstance(data.get("supporting_elements", []), list):
        errors.append("supporting_elements must be a list")
    if not isinstance(data.get("excluded_products", []), list):
        errors.append("excluded_products must be a list")
    if not data.get("primary_product"):
        errors.append("primary_product is required")

    material_richness = data.get("material_richness", {})
    if not isinstance(material_richness, dict):
        errors.append("material_richness must be an object")
    else:
        if material_richness.get("level") not in {
            "level_1",
            "level_2",
            "level_3",
            "level_4",
        }:
            errors.append("material_richness.level must be level_1, level_2, level_3, or level_4")
        fixed_count = material_richness.get("fixed_image_count")
        if fixed_count == 4:
            if data.get("deliverable_scope") != "compact_showcase" or data.get("count_source") != "user_requested":
                errors.append(
                    "4 images are allowed only when deliverable_scope=compact_showcase and count_source=user_requested"
                )
        elif fixed_count not in {6, 8, 10}:
            errors.append("automatic fixed_image_count must be 6, 8, or 10")

    image_quality = data.get("image_quality", {})
    if not isinstance(image_quality, dict):
        errors.append("image_quality must be an object")
    elif image_quality.get("clarity") not in {"high", "medium", "low"}:
        errors.append("image_quality.clarity must be high, medium, or low")

    source_environment = data.get("source_environment", {})
    if not isinstance(source_environment, dict):
        errors.append("source_environment must be an object")
    else:
        allowed_roles = {
            "incidental",
            "contextual",
            "required",
            "brand_asset",
            "user_required",
        }
        if source_environment.get("evidence_role") not in allowed_roles:
            errors.append(
                "source_environment.evidence_role must be incidental, contextual, required, brand_asset, or user_required"
            )
        if not isinstance(source_environment.get("preservation_required"), bool):
            errors.append("source_environment.preservation_required must be a boolean")

    if not isinstance(data.get("needs_user_confirmation", []), list):
        errors.append("needs_user_confirmation must be a list")

    category_route = data.get("category_route", {})
    if not isinstance(category_route, dict):
        errors.append("category_route must be an object")
    else:
        allowed_families = {
            "human_worn",
            "structured_durable",
            "packaged_consumable",
            "electronics_equipment",
        }
        family = category_route.get("family")
        if family not in allowed_families:
            errors.append(
                "category_route.family must be human_worn, structured_durable, packaged_consumable, or electronics_equipment"
            )
        if not category_route.get("primary_adapter"):
            errors.append("category_route.primary_adapter is required")
        elif family == "structured_durable" and category_route.get("primary_adapter") != "structured-durable-adapter":
            errors.append(
                "structured_durable must use primary_adapter=structured-durable-adapter"
            )
        elif family == "packaged_consumable" and category_route.get("primary_adapter") != "packaged-consumable-adapter":
            errors.append(
                "packaged_consumable must use primary_adapter=packaged-consumable-adapter"
            )
        elif family == "electronics_equipment" and category_route.get("primary_adapter") != "electronics-adapter":
            errors.append(
                "electronics_equipment must use primary_adapter=electronics-adapter"
            )
        if family == "packaged_consumable" and category_route.get("consumable_profile") not in {
            "edible",
            "topical_care",
            "ordinary_packaged",
        }:
            errors.append(
                "packaged_consumable category_route.consumable_profile must be edible, topical_care, or ordinary_packaged"
            )
        if not category_route.get("buyer_decision_risk"):
            errors.append("category_route.buyer_decision_risk is required")

    commerce_story = data.get("commerce_story", {})
    if not isinstance(commerce_story, dict):
        errors.append("commerce_story must be an object")
    else:
        if not commerce_story.get("core_value"):
            errors.append("commerce_story.core_value is required")
        pillars = commerce_story.get("advantage_pillars")
        if not isinstance(pillars, list) or not 1 <= len(pillars) <= 3:
            errors.append("commerce_story.advantage_pillars must contain 1 to 3 items")
        for key in ("proof", "usage_imagination", "purchase_decision"):
            if not commerce_story.get(key):
                errors.append(f"commerce_story.{key} is required")

    product = data.get("product", {})
    if isinstance(product, dict):
        if not product.get("category"):
            errors.append("product.category is required")
        if not product.get("product_name"):
            errors.append("product.product_name is required")
    else:
        errors.append("product must be an object")

    if errors:
        print("Product brief validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Product brief validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
