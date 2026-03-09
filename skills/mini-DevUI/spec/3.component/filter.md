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

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/`
- **引用规则**: 相对路径，根据 HTML 文件深度计算。

### 4.2 渲染方式
Filter 内图标为**单色线性图标**，必须使用 **CSS Mask**：
```css
.devui-filter-icon {
  background-color: currentColor;
  -webkit-mask: url('相对路径/chevron-down.svg') no-repeat center/contain;
  mask: url('相对路径/chevron-down.svg') no-repeat center/contain;
}
```

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| 下拉箭头 | `chevron-down.svg` | 16×16 | mask | Active 态旋转 180° |

### 4.4 Anti-Pattern
- ❌ 禁止使用 `<img>` 加载 chevron 图标
- ❌ 禁止图标颜色与文本脱钩（必须用 `currentColor`）

---

## 5. Dynamic Response (动态响应)
-   **Click**: Toggles Active state (Rotates icon).
-   **Dropdown**: (Out of scope for this spec, usually absolute positioned panel).
