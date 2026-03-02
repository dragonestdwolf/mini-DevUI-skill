---
name: icon-feed-mcp
description: 提供基于本地 SVG 的图标 MCP 服务使用说明；支持图搜（输入为图片，返回最相似图标）。在需要列出/获取/搜索图标、按图片搜图标、或需要图标本地路径与 SVG 内容时使用。
---

# 图标推 MCP 服务

基于本地 SVG 文件的 MCP 服务，暴露图标目录、按 id 获取、关键词搜索；所有返回均包含图标本地文件路径 `path`。

## 何时使用

- 用户或对话中提及「图标推」、icon-feed-mcp、图标列表、按 id 取图标、搜索图标、**图搜**。
- 需要图标的**本地路径**（`path`）或 **SVG 内容**时。
- **图搜**：输入为**图片**（本地路径），需要在图标库中检索最相似的图标时，使用 **search_icons_by_image_tool**。
- **图标推荐**：用户输入为文本或图片时，使用 **recommend_icons_tool** 统一入口，自动选择文本搜索或图搜。
- 在 Cursor 中已配置该 MCP 且需调用其 Tools/Resources 时。

## 服务位置与启动

- 项目路径：`icon-feed-mcp/`（与本 SKILL 同目录或上级的 `icon-feed-mcp`）。
- 启动（stdio，供 Cursor/Claude Desktop）：
  ```bash
  cd icon-feed-mcp && python server.py
  ```
- 工作目录须为 `icon-feed-mcp`，依赖：`pip install -r requirements.txt`（`mcp[cli]`）。

## MCP 能力概览

| 类型   | 名称                       | 说明 |
|--------|----------------------------|------|
| Tool   | **recommend_icons_tool**   | **图标推荐**：统一入口，传 keyword 或 image_path 之一；自动选择文本搜索或图搜。 |
| Tool   | list_icons_tool            | 列出图标，可选按 category 筛选；每条含 `path`。 |
| Tool   | get_icon_tool              | 按 icon_id 取单个图标；含 `path`、`svg`。 |
| Tool   | search_icons_tool          | 按 keyword 搜索；每条含 `path`。 |
| Tool   | **search_icons_by_image_tool** | **图搜**：输入为图片路径，返回最相似的 top_k 个图标（含 `path`、`similarity`）。 |
| Resource | icon://catalog           | 图标目录 JSON；每条含 `path`。 |
| Resource | icon://{icon_id}         | 单个图标 JSON；含 `path`、`svg`。 |

**约定**：所有返回的图标条目均包含 **path**（该图标 SVG 的绝对路径），便于调用方读文件或展示。

## 返回结构

**列表/目录中的每条图标：**

```json
{
  "id": "search",
  "name": "搜索",
  "name_en": "Search",
  "category": "action",
  "tags": ["搜索", "查找", "search"],
  "path": "/absolute/path/to/icon-feed-mcp/icons/搜索.svg"
}
```

**单个图标（get_icon_tool / icon://{id}）额外含：**

```json
"svg": "<svg viewBox=\"...\">...</svg>"
```

## Tools 参数

- **list_icons_tool**
  - `category`（可选）：`nav` | `status` | `action` | `form` | `content` | `brand` | `navigation` 等；不传则返回全部。
- **get_icon_tool**
  - `icon_id`（必填）：如 `search`、`bell`、`filter`、`home`。
- **search_icons_tool**
  - `keyword`（必填）：匹配中文名、英文名、tags。
- **recommend_icons_tool**（图标推荐，统一入口）
  - `keyword`（可选）：文本关键词，匹配中文名、英文名、tags。
  - `image_path`（可选）：本地图片路径，按相似度检索。
  - `top_k`（可选，默认 5）：图搜时返回前几个结果。
  - 必须传 keyword 或 image_path 之一；若都传则优先 image_path。文本搜索返回 list；图搜返回 `{ "matches": [...] }`；出错返回 `{ "error": "..." }`。
- **search_icons_by_image_tool**（图搜）
  - `image_path`（必填）：本地图片的绝对或相对路径（如截图、裁剪出的图标图）。
  - `top_k`（可选，默认 5）：返回最相似的前几个图标。
  - 返回：`{ "matches": [ { id, name, name_en, category, tags, path, similarity }, ... ] }`；出错时 `{ "error": "说明" }`。无 cairo 时可用预渲染缓存：在有 cairo 环境运行 `python render_icons_cache.py` 生成 `icons_render/` 后拷贝到本机即可。

## 图标数据与路径

- 元数据与文件名在 `icons_data.py` 的 `ICONS` 中定义，每项有 `id`、`name`、`name_en`、`category`、`tags`、`file`（如 `搜索.svg`）。
- SVG 文件位于项目下的 **icons/** 目录；`path` 为 `icons/` + `file` 的绝对路径。
- 增删改图标：改 `icons_data.py` 的 `ICONS`，并在 `icons/` 中放置对应 `.svg` 文件；替换图标只需替换同名文件，无需改代码。

## 验证

在项目目录执行：

```bash
python verify.py
```

通过即表示 Tools/Resources 及 `path` 返回正常。

## 简要对照

| 需求           | 使用方式                    |
|----------------|-----------------------------|
| **图标推荐（文本或图片）** | recommend_icons_tool(keyword=...) 或 recommend_icons_tool(image_path=...) |
| 列出全部图标   | list_icons_tool() 或 icon://catalog |
| 按分类列图标   | list_icons_tool(category="nav")     |
| 按 id 取图标   | get_icon_tool(icon_id) 或 icon://{icon_id} |
| 按关键词搜索   | search_icons_tool(keyword)          |
| **按图片搜图标（图搜）** | search_icons_by_image_tool(image_path, top_k=5) |
| 需要图标路径   | 任意 Tool/Resource 返回中的 `path` 字段 |

---

# 图标推荐（UI 页面 → 匹配 SVG → 更新 DSL）

在「根据 UI 页面 + 目标检测结果，为页面中的每个图标推荐最相似的本地 SVG，并写回 DSL」时使用本流程。

## 输入

- **UI 页面图**：整页截图（与检测时使用的同一张图），例如 `20260224-163420.png`。
- **目标检测 DSL**：JSON 文件，例如 `data/image_dsl/20260224-163420.json`。结构为：
  - `data.ui_detection_res`：数组，每项为 `{ "cls": "类别", "bbox": [x1, y1, x2, y2] }`。
  - `bbox` 为像素坐标，顺序一般为 **左上 x、左上 y、右下 x、右下 y**（具体以项目约定为准）。

## 流程概述

1. **从 DSL 中读取 icon 的 bbox**  
   遍历 `data.ui_detection_res`，筛选 `cls === "icon"` 的项，取出每项的 `bbox`。

2. **按 bbox 从页面图中截取 icon 区域**  
   使用 bbox `[x1, y1, x2, y2]` 在 UI 页面图上裁剪对应矩形区域，得到每个图标的截图（小图）。

3. **在图标库中找最相似 SVG**  
   图标库目录：本项目的 **icons/**（即 icon_svg 候选集，可与 icon-feed-mcp 的 `icons/` 或项目内 `icon_svg/` 一致）。  
   对每个裁剪出的小图，与图标库中的每个 SVG 做**相似度匹配**（例如：将 SVG 渲染成与裁剪图同尺寸的位图后做像素/特征对比，或使用感知哈希、特征向量等），选出相似度最高的一个 SVG，得到其**本地路径**（即 `path`）。

4. **更新输入的 DSL**  
   对每个 `cls === "icon"` 的检测项，在对应对象上增加或覆盖字段 **`svg_path`**，值为上一步得到的最相似图标的 SVG 文件路径（绝对路径或相对路径，与项目约定一致）。写回原 DSL 文件或另存为新文件。

## DSL 更新约定

- **写入字段**：`svg_path`，表示推荐图标的 SVG 路径。
- **写入位置**：仅对 `data.ui_detection_res` 中 `cls === "icon"` 的项写入；其他类别不修改。
- **示例**（更新后的一条 icon 项）：
  ```json
  {
    "cls": "icon",
    "bbox": [85.82, 7.56, 156.09, 73.64],
    "svg_path": "/path/to/icon-feed-mcp/icons/首页.svg"
  }
  ```

## 与 MCP 的配合

- 获取图标库列表与路径：使用 **list_icons_tool()** 或 **icon://catalog**，得到所有候选图标的 `path`，用于相似度匹配与写回 `svg_path`。
- **图标推荐**：对单个裁剪出的 icon 小图，可直接用 **recommend_icons_tool(image_path=小图路径)** 得到最相似 SVG；对语义描述可用 **recommend_icons_tool(keyword=描述)**。
- 若需按语义辅助筛选：可先用 **search_icons_tool(keyword)** 或 **recommend_icons_tool(keyword=...)** 缩小候选集，再在候选集上做图像相似度匹配。
- 写回 DSL 时，`svg_path` 可直接使用 MCP 返回的 `path`（绝对路径），或按需转为相对路径。
