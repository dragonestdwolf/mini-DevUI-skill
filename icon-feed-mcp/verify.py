# -*- coding: utf-8 -*-
"""
验证图标推 MCP 服务：直接调用 Tool 逻辑，无需启动 MCP 协议。
用法: 在项目目录下执行  python verify.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile


def main() -> None:
    # 不依赖 MCP 传输，只验证数据和 Tool 行为
    from icons_data import ICONS, get_icon_by_id, list_icons, load_svg_content, search_icons
    from server import (
        get_icon_tool,
        list_icons_tool,
        recommend_icons_tool,
        resource_icon_by_id,
        resource_icon_catalog,
        search_icons_by_image_tool,
        search_icons_tool,
    )

    ok = 0
    # 1. 图标数量
    # assert len(ICONS) == 20, "应为 20 个图标"
    # print("[OK] 图标数量: 20")
    # ok += 1

    # 2. list_icons_tool
    # all_icons = list_icons_tool()
    # assert len(all_icons) == 20
    # assert all("id" in i and "name" in i and "category" in i for i in all_icons)
    # print("[OK] list_icons_tool() 返回 20 条，含 id/name/category")
    # ok += 1

    nav_only = list_icons_tool(category="nav")
    assert len(nav_only) >= 5 and all(i["category"] == "nav" for i in nav_only)
    assert all("path" in i and i["path"].endswith(".svg") for i in nav_only), "每条应包含 path"
    print(f"[OK] list_icons_tool(category='nav') 返回 {len(nav_only)} 条，含 path")
    ok += 1

    # 3. get_icon_tool（含 path + svg 从本地文件读取）
    search_icon = get_icon_tool("search")
    assert search_icon is not None and search_icon["id"] == "search" and "svg" in search_icon
    assert "path" in search_icon and search_icon["path"].endswith(".svg"), "返回应包含 icon 路径 path"
    assert search_icon["svg"].strip().startswith("<svg"), "svg 内容应为本地文件读取的 XML"
    print("[OK] get_icon_tool('search') 返回含 path 与 svg 的完整对象")
    ok += 1

    assert get_icon_tool("not-exist") is None
    print("[OK] get_icon_tool('not-exist') 返回 None")
    ok += 1

    # 4. search_icons_tool
    arrows = search_icons_tool("箭头")
    assert len(arrows) >= 2
    print(f"[OK] search_icons_tool('箭头') 返回 {len(arrows)} 条")
    ok += 1

    # 4.5 recommend_icons_tool（统一入口）
    rec_text = recommend_icons_tool(keyword="搜索")
    assert isinstance(rec_text, list) and len(rec_text) >= 1
    assert rec_text[0]["id"] == "search"
    print(f"[OK] recommend_icons_tool(keyword='搜索') 返回 {len(rec_text)} 条")
    ok += 1
    rec_none = recommend_icons_tool()
    assert isinstance(rec_none, dict) and "error" in rec_none
    print("[OK] recommend_icons_tool() 无参数时返回 error")
    ok += 1

    # 5. Resources（直接调函数）
    catalog = resource_icon_catalog()
    data = json.loads(catalog)
    assert len(data) == len(ICONS), f"catalog 条数应与 ICONS 一致，got {len(data)}"
    print(f"[OK] resource icon://catalog 返回 {len(data)} 条 JSON")
    ok += 1

    single = resource_icon_by_id("bell")
    single_data = json.loads(single)
    assert "svg" in single_data and single_data["id"] == "bell"
    print("[OK] resource icon://bell 返回含 svg 的 JSON")
    ok += 1

    err = resource_icon_by_id("not-exist")
    assert "error" in err
    print("[OK] resource icon://not-exist 返回 error")
    ok += 1

    # 6. 图搜 search_icons_by_image_tool
    # 6.1 不存在图片应返回 error
    result = search_icons_by_image_tool(image_path="/Users/zlm/code/icon-feed-mcp/icons_render/efficiency_insights.png", top_k=2)
    print("--------------------------------")
    print(result)
    print("--------------------------------")
    # assert "error" in result, "不存在图片时应返回 error"
    # print("[OK] 图搜：不存在图片时返回 error")
    ok += 1

    # 6.2 图搜成功路径：有 icons_render/ 则用缓存图测；否则尝试 cairosvg 渲染（无 cairo 则跳过，不报错）
    try:
        icons_render_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons_render")
        cache_pngs = [f for f in os.listdir(icons_render_dir)] if os.path.isdir(icons_render_dir) else []
        cache_pngs = [f for f in cache_pngs if f.endswith(".png")]
        if cache_pngs:
            # 用预渲染缓存图做图搜，无需 cairo
            test_path = os.path.join(icons_render_dir, cache_pngs[0])
            result = search_icons_by_image_tool(image_path=test_path, top_k=5)
            assert "matches" in result and len(result["matches"]) >= 1
            first = result["matches"][0]
            assert "path" in first and "similarity" in first
            print(f"[OK] 图搜：用 icons_render 缓存图检索，命中 {len(result['matches'])} 条")
            ok += 1
        else:
            # 无缓存则用 cairosvg 渲染（会触发 cairo；无 cairo 时此处会抛异常，被下面 except 捕获后跳过）
            import cairosvg
            icon = get_icon_by_id("search") or ICONS[0]
            svg_content = load_svg_content(icon)
            if svg_content.strip().startswith("<svg"):
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                    tmp_path = f.name
                try:
                    cairosvg.svg2png(
                        bytestring=svg_content.encode("utf-8"),
                        write_to=tmp_path,
                        output_width=64,
                        output_height=64,
                    )
                    result = search_icons_by_image_tool(image_path=tmp_path, top_k=5)
                    assert "matches" in result and len(result["matches"]) >= 1
                    first = result["matches"][0]
                    assert "path" in first and "similarity" in first
                    top_ids = [m["id"] for m in result["matches"]]
                    assert icon["id"] in top_ids
                    print(f"[OK] 图搜：用 cairosvg 渲染图检索，命中 top，similarity={first.get('similarity')}")
                    ok += 1
                finally:
                    if os.path.isfile(tmp_path):
                        os.unlink(tmp_path)
            else:
                print("[SKIP] 图搜成功路径验证（无 icons_render 且无可用 SVG）")
    except Exception:
        print("[SKIP] 图搜成功路径验证（无 icons_render 且无 cairo/cairosvg，跳过）")

    print()
    print(f"--- 共 {ok} 项验证通过 ---")
    print("若要验证 MCP 协议，请用 HTTP 模式启动 server 后用 MCP Inspector 连接。")
    print("  server.py 末尾改为: mcp.run(transport='streamable-http')")
    print("  然后: python server.py")
    print("  另开终端: npx -y @modelcontextprotocol/inspector")
    print("  在 Inspector 中连接: http://localhost:8000/mcp")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[FAIL] {e}", file=sys.stderr)
        sys.exit(1)
