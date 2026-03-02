# -*- coding: utf-8 -*-
"""
图搜：根据输入图片与图标库做感知哈希相似度匹配。
输入为图片路径（PNG/JPG 等），与图标库中每个图标的位图做相似度比较。
图标位图来源（二选一，优先 1）：
  1) 预渲染缓存 icons_render/{id}.png（无需 cairo）
  2) 运行时用 cairosvg 将 SVG 转为位图（需系统安装 cairo）
"""

from __future__ import annotations

import io
import os
from typing import Any

# 不在此处 import cairosvg，避免无 cairo 时 import 即报错；在 _load_icon_image 内按需导入并捕获异常

try:
    import imagehash
    from PIL import Image
except ImportError:
    imagehash = None  # type: ignore
    Image = None  # type: ignore

from icons_data import ICONS, add_svg_dimensions_to_icons, get_icon_path, load_svg_content

# 预渲染缓存目录（与 icons 同级），存放 {icon_id}.png，有则优先用，无需 cairo
_ICONS_RENDER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons_render")
_RENDER_SIZE = 64
_hash_cache: dict[str, Any] = {}


def _load_icon_image(icon: dict) -> "Image.Image | None":
    """
    获取图标的位图，用于算哈希。优先从 icons_render/{id}.png 读取；否则用 cairosvg 渲染 SVG。
    失败返回 None（如无缓存且 cairo 未安装）。
    """
    if not Image:
        return None
    icon_id = icon["id"]
    # 1) 预渲染 PNG 缓存（无需 cairo）
    cache_path = os.path.join(_ICONS_RENDER_DIR, icon_id + ".png")
    if os.path.isfile(cache_path):
        try:
            return Image.open(cache_path).convert("RGB")
        except Exception:
            pass
    # 2) 用 cairosvg 把 SVG 转成位图（需 cairo）；延迟导入，避免无 cairo 时 import 报错
    svg_content = load_svg_content(icon)
    if not (svg_content or "").strip().startswith("<svg"):
        return None
    try:
        import cairosvg
        png_bytes = cairosvg.svg2png(
            bytestring=svg_content.encode("utf-8"),
            output_width=_RENDER_SIZE,
            output_height=_RENDER_SIZE,
        )
        return Image.open(io.BytesIO(png_bytes)).convert("RGB")
    except Exception:
        return None


def _get_icon_hash(icon: dict) -> Any | None:
    """获取单个图标的感知哈希。先取位图（缓存或 cairosvg），再 phash。"""
    if not imagehash:
        return None
    icon_id = icon["id"]
    if icon_id in _hash_cache:
        return _hash_cache[icon_id]
    img = _load_icon_image(icon)
    if img is None:
        return None
    h = imagehash.phash(img)
    _hash_cache[icon_id] = h
    return h


def search_icons_by_image(
    image_path: str,
    top_k: int = 5,
) -> dict[str, Any]:
    """
    根据图片路径（PNG/JPG 等）在图标库中检索最相似的 top_k 个图标。
    返回格式：{ "error": str } 或 { "matches": [ { icon_meta, path, similarity }, ... ] }
    """
    if not imagehash or not Image:
        return {
            "error": "图搜依赖未安装。请执行: pip install Pillow imagehash",
        }
    path = os.path.abspath(os.path.expanduser(image_path))
    if not os.path.isfile(path):
        return {"error": f"图片文件不存在: {path}"}
    try:
        query_img = Image.open(path).convert("RGB")
    except Exception as e:
        return {"error": f"无法打开图片: {e}"}
    query_hash = imagehash.phash(query_img)
    scored: list[tuple[dict, float]] = []
    for icon in ICONS:
        h = _get_icon_hash(icon)
        if h is None:
            continue
        dist = query_hash - h
        similarity = 1.0 - (dist / 64.0)
        scored.append((icon, max(0.0, similarity)))
    if not scored:
        return {
            "error": "无法生成图标位图用于比对。请任选其一："
            " 1) 在有 cairo 的环境执行 pip install cairosvg 并安装 cairo（如 macOS: brew install cairo）；"
            " 2) 或运行 python render_icons_cache.py 生成 icons_render/ 后拷贝到本机（无需 cairo）。",
        }
    scored.sort(key=lambda x: -x[1])
    top = scored[: max(1, top_k)]
    icons_with_dims = add_svg_dimensions_to_icons([icon for icon, _ in top])
    matches = []
    for (icon, sim), enriched in zip(top, icons_with_dims):
        matches.append({
            "id": icon["id"],
            "name": icon["name"],
            "name_en": icon["name_en"],
            "category": icon["category"],
            "tags": icon["tags"],
            "path": get_icon_path(icon),
            "size": enriched.get("size", []),
            "similarity": round(sim, 4),
        })
    return {"matches": matches}
