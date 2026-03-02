# -*- coding: utf-8 -*-
"""
图标推 MCP 服务：基于 20 个图标的 MCP 服务。
提供 Tools：list_icons, get_icon, search_icons
提供 Resources：icon://catalog, icon://{id}
"""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from icon_search import search_icons_by_image
from icons_data import (
    ICONS,
    add_svg_dimensions_to_icons,
    get_icon_by_id,
    get_icon_path,
    list_icons,
    load_svg_content,
    search_icons,
)

mcp = FastMCP(
    "图标推",
    json_response=True,
)

# ---------- Tools ----------


@mcp.tool()
def list_icons_tool(category: str | None = None) -> list[dict[str, Any]]:
    """列出所有图标，可选按分类筛选。category 可选: nav, status, action, form, content。不传则返回全部 20 个。"""
    icons = add_svg_dimensions_to_icons(list_icons(category))
    return [
        {
            "id": i["id"],
            "name": i["name"],
            "name_en": i["name_en"],
            "category": i["category"],
            "tags": i["tags"],
            "path": get_icon_path(i),
            "size": i.get("size", []),
        }
        for i in icons
    ]


@mcp.tool()
def get_icon_tool(icon_id: str) -> dict[str, Any] | None:
    """根据 id 获取单个图标的完整信息（含 SVG）。icon_id 例如: search, bell, arrow-left, check。"""
    icon = get_icon_by_id(icon_id)
    if not icon:
        return None
    icon = add_svg_dimensions_to_icons([icon])[0]
    return {
        "id": icon["id"],
        "name": icon["name"],
        "name_en": icon["name_en"],
        "category": icon["category"],
        "tags": icon["tags"],
        "path": get_icon_path(icon),
        "size": icon.get("size", []),
        "svg": load_svg_content(icon),
    }


@mcp.tool()
def search_icons_tool(keyword: str) -> list[dict[str, Any]]:
    """按关键词搜索图标（匹配中文名、英文名、标签）。"""
    icons = add_svg_dimensions_to_icons(search_icons(keyword))
    return [
        {
            "id": i["id"],
            "name": i["name"],
            "name_en": i["name_en"],
            "category": i["category"],
            "tags": i["tags"],
            "path": get_icon_path(i),
            "size": i.get("size", []),
        }
        for i in icons
    ]


@mcp.tool()
def search_icons_by_image_tool(image_path: str, top_k: int = 5) -> dict[str, Any]:
    """图搜：根据图片在图标库中检索最相似的图标。输入为本地图片路径，返回最相似的 top_k 个，每条含 id、name、path、similarity、size（[宽, 高]）等。"""
    return search_icons_by_image(image_path=image_path, top_k=top_k)


@mcp.tool()
def recommend_icons_tool(
    keyword: str | None = None,
    image_path: str | None = None,
    top_k: int = 5,
) -> dict[str, Any] | list[dict[str, Any]]:
    """图标推荐：根据文本关键词或图片路径推荐最匹配的图标。传 keyword 则按关键词搜索；传 image_path 则按图片相似度搜索。必须传 keyword 或 image_path 之一；若都传则优先使用 image_path。"""
    if image_path and image_path.strip():
        return search_icons_by_image(image_path=image_path.strip(), top_k=top_k)
    if keyword and keyword.strip():
        icons = add_svg_dimensions_to_icons(search_icons(keyword.strip()))
        return [
            {
                "id": i["id"],
                "name": i["name"],
                "name_en": i["name_en"],
                "category": i["category"],
                "tags": i["tags"],
                "path": get_icon_path(i),
                "size": i.get("size", []),
            }
            for i in icons
        ]
    return {"error": "请提供 keyword（文本）或 image_path（图片路径）之一"}


# ---------- Resources ----------


@mcp.resource("icon://catalog")
def resource_icon_catalog() -> str:
    """获取图标目录（20 个图标的 id、名称、分类、标签，不含 SVG）。"""
    icons = add_svg_dimensions_to_icons(ICONS)
    catalog = [
        {
            "id": i["id"],
            "name": i["name"],
            "name_en": i["name_en"],
            "category": i["category"],
            "tags": i["tags"],
            "path": get_icon_path(i),
            "size": i.get("size", []),
        }
        for i in icons
    ]
    return json.dumps(catalog, ensure_ascii=False, indent=2)


@mcp.resource("icon://{icon_id}")
def resource_icon_by_id(icon_id: str) -> str:
    """根据 id 获取单个图标的完整信息（含 SVG）。"""
    icon = get_icon_by_id(icon_id)
    if not icon:
        return json.dumps({"error": f"未找到图标: {icon_id}"}, ensure_ascii=False)
    icon = add_svg_dimensions_to_icons([icon])[0]
    return json.dumps(
        {
            "id": icon["id"],
            "name": icon["name"],
            "name_en": icon["name_en"],
            "category": icon["category"],
            "tags": icon["tags"],
            "path": get_icon_path(icon),
            "size": icon.get("size", []),
            "svg": load_svg_content(icon),
        },
        ensure_ascii=False,
        indent=2,
    )


def main() -> None:
    """MCP 服务入口，供 pyproject.toml 的 icon-feed-mcp 命令调用。"""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
