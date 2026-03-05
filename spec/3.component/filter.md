# Spec: Filter (筛选)

[Metadata]
- **Component**: `d-filter`
- **Figma Node**: 960:2744
- **Template Source**: `spec/4.template/filter-tem.html`
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths**.

## 2. Content Presentation (内容呈现)

### 2.1 Trigger Structure
-   **Container**: Flexbox, `align-items: center`.
-   **Content**: Text + Icon.
-   **Gap**: 4px.
-   **Cursor**: Pointer.

### 2.2 Elements
-   **Text**: 
    -   Font: 14px Regular.
    -   Color: `var(--devui-text, #252b3a)`.
-   **Icon**:
    -   Source: `select-arrow.svg` (Inline Data URI).
    -   Size: 14x14px.
    -   Color: `currentColor` (Inherits from text).
    -   Transition: Rotate 180deg when active.

## 3. Visual Spec (视觉规范)

### 3.1 States
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

## 5. Dynamic Response (动态响应)
-   **Click**: Toggles Active state (Rotates icon).
-   **Dropdown**: (Out of scope for this spec, usually absolute positioned panel).
