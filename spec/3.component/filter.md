# Spec: Filter (筛选)

[Metadata]
- **Component**: `d-filter`
- **Figma Node**: 960:2744
- **Template Source**: `spec/4.template/filter-tem.html`

## 1. Content Presentation (内容呈现格式)

### 1.1 Trigger Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Content**: Text + Icon.
-   **Gap**: 4px.
-   **Cursor**: Pointer.

### 1.2 Elements
-   **Text**: 
    -   Font: 14px Regular.
    -   Color: `var(--devui-text, #252b3a)`.
-   **Icon**:
    -   Source: `select-arrow.svg` (Inline Data URI).
    -   Size: 14x14px.
    -   Color: `currentColor` (Inherits from text).
    -   Transition: Rotate 180deg when active.

## 2. Visual Variants (视觉变体)

### 2.1 States
-   **Normal**:
    -   Text Color: `var(--devui-text, #252b3a)`.
    -   Icon Color: `var(--devui-text, #252b3a)`.
-   **Hover**:
    -   Text Color: `var(--devui-primary, #5e7ce0)`.
    -   Icon Color: `var(--devui-primary, #5e7ce0)`.
-   **Active (Dropdown Open)**:
    -   Text Color: `var(--devui-primary, #5e7ce0)`.
    -   Icon Color: `var(--devui-primary, #5e7ce0)`.
    -   Icon Transform: `rotate(180deg)`.
-   **Disabled**:
    -   Text Color: `var(--devui-disabled-text, #adb0b8)`.
    -   Icon Color: `var(--devui-disabled-text, #adb0b8)`.
    -   Cursor: `not-allowed`.

## 3. Dynamic Response (动态响应)
-   **Click**: Toggles Active state (Rotates icon).
-   **Dropdown**: (Out of scope for this spec, usually absolute positioned panel).
