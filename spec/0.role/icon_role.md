# Role: Icon Usage (图标使用规范)

[Metadata]
- **Role Name**: Icon Role
- **Root Directory**: `icon/miniDev-icon/`
- **Primary Source**: `icon/miniDev-icon/action/` (Operation Icons)
- **File Type**: SVG
- **Version**: v1.1

## Core Rule: Source of Truth
**所有 HTML 生成中的图标资源，必须严格从 `icon/miniDev-icon/` 及其子目录中选取。**

- **Primary Location**: Most functional icons (Search, Close, Delete, Settings etc.) are located in `icon/miniDev-icon/action/`.
- **Naming Note**: Filenames are in English/Kebab-case.
    - Search -> `icon/miniDev-icon/action/search.svg`
    - Close -> `icon/miniDev-icon/action/close.svg`
    - Settings -> `icon/miniDev-icon/action/settings.svg`
    - Check -> `icon/miniDev-icon/action/selected.svg`
- **Action**: 若不确定文件名，需先使用 `find` 或 `list_dir` 确认文件存在，禁止猜测路径。

## Critical Rule: SVG Rendering Strategy (图标渲染策略) 🔴 MUST FOLLOW
**必须区分不同场景的图标，采用不同的渲染方式：**

2.  **Linear/Action Icons (单色/线性/功能操作类图标)**：
    - 例如：搜索、关闭、排序箭头、分页箭头、子菜单操作项等。
    - **必须使用** 专属的 CSS Class（如 `.devui-icon-search`），在类内部声明 `-webkit-mask-image`，并搭配 `background-color: currentColor`（或指定的色值）。
    - 🔴 **绝对禁止** **将超长的 `mask` 路径直接写在 HTML 的 `style="..."` 内联属性中**，以保证代码可读性。
    - 原因：此类图标需要跟随文本颜色变化，或者响应 Hover/Active 状态变色。
    - CSS 示例：
      ```css
      .devui-icon-action {
        width: 16px;
        height: 16px;
        background-color: currentColor; /* 或 var(--devui-primary) */
        -webkit-mask: url('../../../icon/miniDev-icon/action/search.svg') no-repeat center/contain;
        mask: url('../../../icon/miniDev-icon/action/search.svg') no-repeat center/contain;
      }
      ```

2.  **Colorful/Brand Icons (自带原生色彩的图标/品牌类/大型栏目图标)**：
    - 例如：项目 Avatar (`D-48x48.svg`)、侧边栏一级菜单的应用图标（如仪表盘、工作项等如果本身具备复杂色彩）。
    - **必须使用** `background-image` 或 `<img>` 标签。
    - **绝对不要** 设置 `background-color` 作为掩盖层，这会导致图标变成纯黑方块。
    - CSS 示例：
      ```css
      .devui-icon-brand {
        width: 32px;
        height: 32px;
        background-image: url('../../../icon/miniDev-icon/project-initial/D-48x48.svg');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        /* 禁止在此处写入 background-color 掩盖原生颜色的属性 */
      }
      ```

## Critical Rule: Relative Path Resolution (相对路径解析)
**HTML 文件通常位于深层目录 (e.g., `HistoryRender/component/table/v17.html`)，必须计算相对路径以正确访问根目录的 Icon 资源。**

**绝对禁止** 直接使用 `icon/...` 或 `/icon/...` (除非确信在服务器根目录下运行)。
**必须使用** `../` 回退到根目录。

### Calculation Logic
1.  **Identify HTML Depth**: 计算当前 HTML 文件相对于项目根目录的深度。
    - `HistoryRender/component/table/v17.html` -> Depth = 3
2.  **Calculate Prefix**: Depth * `../`
    - Depth 3 -> `../../../`
3.  **Construct Path**: `[Prefix]Icon/miniDev-icon/...`

### Examples
- **Wrong**: `src="icon/miniDev-icon/action/search.svg"` (Browser looks in `HistoryRender/component/table/icon/...` -> 404)
- **Correct**: `src="../../../Icon/miniDev-icon/action/search.svg"` (Browser resolves to Project Root/Icon/... -> 200)


## Core Rule: Dimension Control (尺寸严格定义)
**图标尺寸必须严格遵循用户需求或组件设计规范。**

1.  **User Defined**: 若用户在 Prompt 中指定尺寸 (e.g. "use 20px icons")，**必须**显式设置 CSS 宽高为 `20px`。
2.  **Component Skill**: 若用于特定组件，遵循组件文档 (e.g. Button sm=12px, md=16px)。
3.  **Strict Enforcement**: 
    - ❌ 禁止使用 `width: auto`。
    - ✅ 必须使用 `width: [size]px; height: [size]px;`。

## Usage Pattern (使用模式)

### 1. Img Tag (General Use)
```html
<!-- Example: Search Icon (Size: Strict 16px) -->
<!-- 注意：路径需根据实际文件结构调整 -->
<img src="icon/miniDev-icon/action/搜索.svg" class="devui-icon-search" alt="search" />

<style>
.devui-icon-search {
  width: 16px; /* User strict requirement */
  height: 16px;
  display: block;
}
</style>
```

### 2. Multi-Color Elements
```css
/* CORRECT: Preserves native SVG colors for brand/large UI icons */
.devui-project-avatar {
  width: 32px;
  height: 32px;
  background-image: url('../../../icon/miniDev-icon/project-initial/D-48x48.svg');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}
```

### 3. Action / Monochromatic Elements
```css
/* CORRECT: Uses mask to allow CSS color controlling */
.devui-input-icon {
  width: 16px;
  height: 16px;
  background-color: currentColor;
  -webkit-mask: url('../../../icon/miniDev-icon/action/search.svg') no-repeat center/contain;
  mask: url('../../../icon/miniDev-icon/action/search.svg') no-repeat center/contain;
}
```

## Audit Checklist (生成前自检)
1.  **Path Valid**: 路径是否真实存在？(e.g. 是 `搜索.svg` 还是 `search.svg`?)
2.  **Size Strict**: `width/height` 是否已显式写入 CSS？
3.  **Source Compliance**: 是否使用了 `icon/miniDev-icon` 下的资源？
