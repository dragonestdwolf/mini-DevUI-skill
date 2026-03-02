# 图标推 MCP 服务

基于本地 SVG 图标的 MCP（Model Context Protocol）服务，提供图标列表、按 id 获取、关键词搜索、**图搜（输入图片返回最相似图标）**、**图标推荐（文本或图片统一入口）** 等能力。

## 图标列表（20 个）

| id | 名称 | 分类 |
|----|------|------|
| search | 搜索 | nav |
| bell | 通知/铃铛 | nav |
| arrow-left | 左箭头 | nav |
| arrow-right | 右箭头 | nav |
| arrow-down | 下箭头 | nav |
| user | 用户 | nav |
| home | 首页 | nav |
| settings | 设置 | nav |
| check | 勾选/完成 | status |
| circle | 圆点/待处理 | status |
| more | 更多/三点 | action |
| filter | 筛选 | action |
| edit | 编辑 | action |
| trash | 删除 | action |
| download | 下载 | action |
| upload | 上传 | action |
| link | 链接 | action |
| calendar | 日历 | form |
| document | 文档 | content |
| chart | 图表 | content |

## 安装

```bash
cd icon-feed-mcp
pip install -r requirements.txt
# 或
pip install -e .   # 可安装包，支持 icon-feed-mcp 命令
# 或
uv pip install -r requirements.txt
```

## 运行

**stdio 模式（推荐给 Cursor / Claude Desktop）：**

```bash
python server.py
# 或
uv run server.py
```

**HTTP 模式（可选，便于浏览器或远程调用）：**

修改 `server.py` 最后一行为：

```python
mcp.run(transport="streamable-http")
```

然后运行：

```bash
python server.py
# 默认在 http://localhost:8000 提供 Streamable HTTP 端点
```

## 在 Cursor 中配置

1. 打开 Cursor 设置 → MCP → 添加服务器。
2. 选择「Command」或「stdio」方式，命令示例：

   ```bash
   /Users/zlm/code/icon-feed-mcp 下执行: python server.py
   ```

   或使用 uv：

   ```bash
   uv run server.py
   ```

   工作目录设为：`/Users/zlm/code/icon-feed-mcp`。

## MCP 能力

### Tools

- **list_icons_tool**  
  - 列出全部或按分类筛选的图标（返回 id、name、name_en、category、tags）。  
  - 参数：`category`（可选）：`nav` | `status` | `action` | `form` | `content`。

- **get_icon_tool**  
  - 根据 `icon_id` 获取单个图标完整信息（含 SVG）。  
  - 参数：`icon_id`：如 `search`、`bell`、`arrow-left`。

- **search_icons_tool**  
  - 按关键词搜索图标（匹配中文名、英文名、标签）。  
  - 参数：`keyword`。

- **recommend_icons_tool**（图标推荐，统一入口）  
  - 根据文本或图片推荐图标。传 `keyword` 则按关键词搜索；传 `image_path` 则按图片相似度搜索。  
  - 参数：`keyword`（可选）、`image_path`（可选）、`top_k`（可选，默认 5）。必须传 keyword 或 image_path 之一。

- **search_icons_by_image_tool**（图搜）  
  - 输入为**图片路径**（PNG/JPG 等），在图标库中检索最相似的图标。  
  - 参数：`image_path`（必填，本地图片路径）、`top_k`（可选，默认 5）。  
  - 返回：`{ "matches": [ { id, name, path, similarity }, ... ] }`；出错时 `{ "error": "说明" }`。  
  - 图搜依赖：Pillow、imagehash。图标位图二选一：**1）** 使用预渲染缓存 `icons_render/`（无需 cairo）：在有 cairo 的机器运行 `python render_icons_cache.py` 生成后拷贝到本机；**2）** 安装 cairosvg + 系统 cairo（如 macOS：`brew install cairo`），运行时自动把 SVG 转为位图。

### Resources

- **icon://catalog**  
  - 图标目录（20 个图标的元数据，不含 SVG）。

- **icon://{icon_id}**  
  - 单个图标完整信息（含 SVG），例如 `icon://search`、`icon://bell`。

## 如何验证

### 方式一：本地脚本（推荐，无需 MCP 客户端）

在项目目录下执行：

```bash
cd /Users/zlm/code/icon-feed-mcp
python verify.py
```

会检查：20 个图标、`list_icons_tool`、`get_icon_tool`、`search_icons_tool` 以及 `icon://catalog`、`icon://{id}` 的返回。全部通过会打印「共 9 项验证通过」。

### 方式二：MCP Inspector（验证完整 MCP 协议）

1. 在 `server.py` 末尾把 `mcp.run(transport="stdio")` 改为：
   ```python
   mcp.run(transport="streamable-http")
   ```
2. 启动服务：
   ```bash
   python server.py
   ```
   服务会在 `http://localhost:8000` 提供 Streamable HTTP。
3. 新开一个终端，启动 MCP Inspector：
   ```bash
   npx -y @modelcontextprotocol/inspector
   ```
4. 在浏览器打开的 Inspector 里，连接地址填：`http://localhost:8000/mcp`。
5. 在 Inspector 中可查看并调用 Tools（list_icons_tool、get_icon_tool、search_icons_tool）和 Resources（icon://catalog、icon://search 等），确认请求与返回是否符合预期。

### 方式三：在 Cursor 里实际用

在 Cursor 中配置好该 MCP 服务器后，在对话里让 AI 调用「图标推」的工具（例如「列出所有图标」或「搜索箭头图标」），看返回是否正常。

---

## 图搜无 cairo 时：预渲染缓存

若本机未安装 cairo（图搜会报 `no library called "cairo"`），可用预渲染 PNG 缓存，**无需 cairo**：

1. 在有 cairo 的环境（或先 `brew install cairo` 后）执行：  
   `python render_icons_cache.py`  
2. 会生成 `icons_render/` 目录（每个图标一个 `{id}.png`）。  
3. 将 `icons_render/` 拷贝到当前项目或提交到仓库；图搜会优先使用该目录，不再调用 cairosvg。

## 本地 SVG 图标

图标内容从 **本地文件** 读取，目录为项目下的 `icons/`（与 `icons_data.py` 同级的 `icons` 文件夹）。

- 每个图标在 `icons_data.py` 中有元数据（id、name、name_en、category、tags）和 `file` 文件名（如 `search.svg`）。
- 实际 SVG 内容来自 `icons/<file>`，例如 `icons/search.svg`。
- **替换成你的图标**：把对应的 `.svg` 文件放进 `icons/` 并保持文件名一致，或修改 `icons_data.py` 里该图标的 `file` 指向你的文件名。
- 修改 `icons_data.py` 可增删图标或改元数据；修改/新增 SVG 文件后无需改代码，重启服务即可生效。
