# Spec: CategorySearch (分类搜索)

[Metadata]
- **Component**: `d-category-search`
- **Figma Node**: 147:312
- **Template Source**: `spec/4.template/categorySearch-tem.html`
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths**.

## 2. Content Presentation (内容呈现)

### 2.1 Layout Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Width**: 852px (Expanded/Demonstrated), typically 100% of parent.
-   **Height**: 32px.
-   **Padding**: 0 8px.
-   **Border Radius**: 6px.
-   **Gap**: 8px.

### 2.2 Internal Elements
1.  **Search Icon**: Leftmost, `16x16px`.
2.  **Tags Group**: 
    -   Flex item.
    -   Contains selected filters (e.g., "Category: Active").
3.  **Input**: 
    -   Flex 1 (takes remaining space).
    -   Border: None.
    -   Placeholder: "Click to filter..." (or specific to context).
4.  **Right Actions**:
    -   **Clear Icon**: `close.svg` (Relative Path: `../../../icon/miniDev-icon/action/close.svg`).
    -   **Divider**: Vertical line.
    -   **Save Icon**: `save.svg` (Relative Path: `../../../icon/miniDev-icon/action/save.svg`).
    -   **Directory Icon**: `folder.svg` (Relative Path: `../../../icon/miniDev-icon/action/folder.svg`).

## 3. Visual Spec (视觉规范)

### 3.1 States
-   **Normal**: 
    -   Border: 1px solid `var(--devui-form-control-line, #ADB0B8)`.
    -   Bg: `var(--devui-base-bg, #FFFFFF)`.
-   **Hover**:
    -   Border: 1px solid `var(--devui-form-control-line-hover, #5E7CE0)`.
-   **Active / Focus**:
    -   Border: 1px solid `var(--devui-form-control-line-active, #5E7CE0)`.
    -   Shadow: `0 0 0 4px var(--devui-form-control-line-rippling, rgba(94, 124, 224, 0.08))`. 
-   **Disabled**:
    -   Bg: `var(--devui-disabled-bg, #F3F3F3)`.
    -   Border: 1px solid `var(--devui-disabled-line, #DFE1E6)`.
    -   Cursor: `not-allowed`.

### 3.2 Tags
-   **Tag Style**:
    -   Height: `20px`.
    -   Bg: `var(--devui-list-item-hover-bg, #F2F5FC)`.
    -   Radius: `4px`.
    -   Text: 12px Regular, `var(--devui-text, #252b3a)`.
    -   Padding: `0 8px`.
    -   Gap: `4px` (Text to Close Icon).
    -   **Close Icon**: `12x12px`, 0.6 opacity -> 1.0 hover.

### 3.3 Dropdown Panel
-   **Trigger**: Focus on Input.
-   **Position**: Absolute, Top 100% + 4px, Left 0.
-   **Style**:
    -   Bg: `#FFFFFF`.
    -   Shadow: `0 4px 12px rgba(0,0,0,0.16)`.
    -   Radius: `6px`.
    -   Padding: `4px`.
-   **Items**:
    -   Height: `36px`.
    -   Padding: `0 8px`.
    -   Hover Bg: `var(--devui-list-item-hover-bg, #F2F5FC)`.

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/`
- **引用规则**: 相对路径，根据 HTML 文件深度计算。

### 4.2 渲染方式
所有图标均为**单色线性图标**，必须使用 **CSS Mask** + `currentColor`。

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| 搜索图标（左侧） | `search.svg` | 16×16 | mask | 固定在输入框左侧 |
| Tag 关闭按钮 | `close.svg` | 12×12 | mask | opacity 0.6→1.0 hover |
| 保存按钮 | `save.svg` | 16×16 | mask | 右侧操作区 |
| 目录按钮 | `folder.svg` | 16×16 | mask | 右侧操作区 |

### 4.4 Anti-Pattern
- ❌ 禁止使用 `<img>` 加载操作图标
- ❌ 禁止 Tag 关闭图标使用文本 "×" 替代 SVG 图标
- ❌ 禁止图标路径使用中文文件名

---

## 5. Dynamic Response (动态响应)
-   **Input Behavior**: 
    -   Clicking anywhere in container focuses input.
    -   Focus activates Dropdown.
-   **Tag Interaction**:
    -   Clicking 'x' removes tag.
-   **Right Actions**:
    -   Always visible or visible on hover/content presence (Logic dependent, Figma shows them present).

