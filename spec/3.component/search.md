# Spec: Search (搜索框)

[Metadata]
- **Component**: `d-search`
- **Figma Node**: 164:370
- **Template Source**: `spec/4.template/search-tem.html`
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths**.

## 2. Content Presentation (内容呈现)

### 2.1 Layout Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Width**: 296px (Default), can be 100%.
-   **Height**: 32px (MD).
-   **Padding**: 0 8px.
-   **Border Radius**: 6px.
-   **Gap**: 4px (Icon to Text).

### 2.2 Icon & Text
-   **Icon**: `../../../icon/miniDev-icon/action/search.svg` (Relative Path).
-   **Placeholder**: 14px Regular, Color `var(--devui-placeholder)`.
-   **Text**: 14px Regular, Color `var(--devui-text)`.
-   **Visual**:
    ```html
    <div class="devui-search">
        <img src="..." class="devui-search-icon">
        <input class="devui-search-input" placeholder="请输入搜索内容">
    </div>
    ```

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
        *(Note: User specific requirement for light blue outline using box-shadow)*.
-   **Disabled**:
    -   Bg: `var(--devui-disabled-bg, #F3F3F3)`.
    -   Border: 1px solid `var(--devui-disabled-line, #DFE1E6)`.
    -   Text: `var(--devui-disabled-text, #ADB0B8)`.
    -   Cursor: `not-allowed`.

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/`
- **引用规则**: 相对路径，根据 HTML 文件深度计算。

### 4.2 渲染方式
搜索图标为**单色线性图标**，必须使用 **CSS Mask**：
```css
.devui-search-icon {
  background-color: currentColor;
  -webkit-mask: url('相对路径/search.svg') no-repeat center/contain;
  mask: url('相对路径/search.svg') no-repeat center/contain;
}
```

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 |
|:---|:---|:---|:---|
| 搜索图标 | `search.svg` | 16×16 | mask |

### 4.4 Anti-Pattern
- ❌ 禁止使用 `<img>` 加载搜索图标
- ❌ 禁止在 `style=""` 内联写 mask-image 长路径

---

## 5. Dynamic Response (动态响应)
-   **Interactive**:
    -   Input background is transparent.
    -   Container handles the visual border and background.
    -   Clicking container focuses input.
