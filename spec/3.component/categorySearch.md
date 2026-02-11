# Spec: CategorySearch (分类搜索)

[Metadata]
- **Component**: `d-category-search`
- **Figma Node**: 147:312
- **Template Source**: `spec/4.template/categorySearch-tem.html`

## 1. Content Presentation (内容呈现格式)

### 1.1 Layout Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Width**: 852px (Expanded/Demonstrated), typically 100% of parent.
-   **Height**: 32px.
-   **Padding**: 0 8px.
-   **Border Radius**: 6px.
-   **Gap**: 8px.

### 1.2 Internal Elements
1.  **Search Icon**: Leftmost, `16x16px`.
2.  **Tags Group**: 
    -   Flex item.
    -   Contains selected filters (e.g., "Category: Active").
3.  **Input**: 
    -   Flex 1 (takes remaining space).
    -   Border: None.
    -   Placeholder: "Click to filter..." (or specific to context).
4.  **Right Actions**:
    -   **Clear Icon**: `close.svg`.
    -   **Divider**: Vertical line.
    -   **Save Icon**: `save.svg`.
    -   **Directory Icon**: `folder.svg`.

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
-   **Disabled**:
    -   Bg: `var(--devui-disabled-bg, #F3F3F3)`.
    -   Border: 1px solid `var(--devui-disabled-line, #DFE1E6)`.
    -   Cursor: `not-allowed`.

### 2.2 Tags
-   **Tag Style**:
    -   Height: `20px`.
    -   Bg: `var(--devui-list-item-hover-bg, #F2F5FC)`.
    -   Radius: `4px`.
    -   Text: 12px Regular, `var(--devui-text, #252b3a)`.
    -   Padding: `0 8px`.
    -   Gap: `4px` (Text to Close Icon).
    -   **Close Icon**: `12x12px`, 0.6 opacity -> 1.0 hover.

### 2.3 Dropdown Panel
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

## 3. Dynamic Response
-   **Input Behavior**: 
    -   Clicking anywhere in container focuses input.
    -   Focus activates Dropdown.
-   **Tag Interaction**:
    -   Clicking 'x' removes tag.
-   **Right Actions**:
    -   Always visible or visible on hover/content presence (Logic dependent, Figma shows them present).

