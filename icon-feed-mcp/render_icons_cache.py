# -*- coding: utf-8 -*-
"""
将 icons/ 下所有图标的 SVG 渲染为 icons_render/{id}.png，供图搜在不安装 cairo 的环境使用。
需在已安装 cairo 与 cairosvg 的机器上运行一次，生成后可将 icons_render/ 提交到仓库。
用法: 在项目根目录执行  python render_icons_cache.py
"""

from __future__ import annotations

import os
import sys

try:
    import cairosvg
except (ImportError, OSError) as e:
    if "cairo" in str(e).lower() or "libcairo" in str(e).lower():
        print("本机未检测到 cairo 库，无法渲染 SVG。请任选其一：", file=sys.stderr)
        print("  1) 安装 cairo 后重试：macOS 执行  brew install cairo  ；或 conda 执行  conda install -c conda-forge cairo", file=sys.stderr)
        print("  2) 在有 cairo 的机器上运行本脚本，将生成的 icons_render/ 目录拷贝到本机使用（图搜即可用，无需本机装 cairo）", file=sys.stderr)
    else:
        print(f"导入 cairosvg 失败: {e}", file=sys.stderr)
    sys.exit(1)

from icons_data import ICONS, load_svg_content

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "icons_render")
SIZE = 64


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    ok, fail = 0, 0
    for icon in ICONS:
        icon_id = icon["id"]
        svg = load_svg_content(icon)
        if not (svg or "").strip().startswith("<svg"):
            print(f"[SKIP] {icon_id}: 无有效 SVG")
            fail += 1
            continue
        out_path = os.path.join(OUT_DIR, icon_id + ".png")
        try:
            cairosvg.svg2png(
                bytestring=svg.encode("utf-8"),
                write_to=out_path,
                output_width=SIZE,
                output_height=SIZE,
            )
            print(f"[OK] {icon_id} -> {out_path}")
            ok += 1
        except Exception as e:
            print(f"[FAIL] {icon_id}: {e}", file=sys.stderr)
            fail += 1
    print(f"\n完成: 成功 {ok}，失败 {fail}。icons_render/ 可拷贝到无 cairo 环境使用。")


if __name__ == "__main__":
    main()
