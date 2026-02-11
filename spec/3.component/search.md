# Spec: Search (搜索框)

[Metadata]
- **Component**: `d-search`
- **Figma Node**: 164:370
- **Template Source**: `spec/4.template/search-tem.html`

## 1. Content Presentation (内容呈现格式)

### 1.1 Layout Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Width**: 296px (Default), can be 100%.
-   **Height**: 32px (MD).
-   **Padding**: 0 8px.
-   **Border Radius**: 6px.
-   **Gap**: 4px (Icon to Text).

### 1.2 Icon & Text
-   **Icon**: `icon/miniDev-icon/action/search.svg` (16x16px).
-   **Placeholder**: 14px Regular, Color `var(--devui-placeholder)`.
-   **Text**: 14px Regular, Color `var(--devui-text)`.
-   **Visual**:
    ```html
    <div class="devui-search">
        <img src="..." class="devui-search-icon">
        <input class="devui-search-input" placeholder="请输入搜索内容">
    </div>
    ```

## 2. Visual Variants (视觉变体)

### 2.1 States
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

## 3. Dynamic Response (动态响应)
-   **Interactive**:
    -   Input background is transparent.
    -   Container handles the visual border and background.
    -   Clicking container focuses input.
