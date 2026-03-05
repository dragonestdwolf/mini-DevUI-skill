# Spec: MenuCard

[Metadata]
- **Component**: `d-menuCard`
- **Template Source**: `spec/4.template/menuCard-tem.html`

## 2. Content Presentation (内容呈现)
描述不同类型的数据应如何组装 HTML：

### 2.1 Icon with Label
-   Scenario: Used in Sidebar and Menu lists.
-   Structure:
    ```html
    <a class="devui-menuCard" href="javascript:void(0)">
        <span class="devui-menuCard-icon"></span>
        <span class="devui-menuCard-text">{{label}}</span>
    </a>
    ```
-   Note: Icon size 16px, Gap 8px. Fixed Component Width 240px, Height 36px.

## 3. Visual Spec (视觉规范)

### 3.1 Interaction States (交互状态)
-   **Default**: 背景透明 (Transparent)，文本与图标颜色为 #252B3A。
-   **Hover**: 当鼠标悬停时，背景色变为 `#FFFFFF` (var(--devui-base-bg))，同时添加阴影 `0 1px 6px 0 rgba(0, 0, 0, 0.08)` (var(--devui-shadow-length-base))。
-   **Active/Selected**: 激活/选中状态，与 Hover 状态视觉效果一致。需给顶级元素添加 class `active`。

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/` 或其他业务子目录
- **引用规则**: 通过注入 `{{iconClass}}` 类名，在 CSS 中声明 mask-image 路径。

### 4.2 渲染方式
菜单项图标为**单色线性图标**，必须使用 **CSS Mask** + `currentColor`：
```css
.devui-menuCard-icon.[iconClass] {
  width: 16px; height: 16px;
  background-color: currentColor;
  -webkit-mask: url('相对路径/[icon].svg') no-repeat center/contain;
  mask: url('相对路径/[icon].svg') no-repeat center/contain;
}
```

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| 各菜单项图标 | 由 `{{iconClass}}` 动态注入 | 16×16 | mask | 每项对应不同 SVG |

### 4.4 Anti-Pattern
- ❌ 禁止使用 `<img>` 加载菜单图标
- ❌ 禁止在 HTML 内联 `style` 中写 mask-image 路径
- ❌ 禁止使用 Emoji 或 Unicode 字符替代 SVG 图标

---

## 5. Dynamic Response (动态响应)
-   **Text Overflow**:
    -   Title: 文字内容超出容器宽度时，一行显示并末尾增加省略号（Ellipsis at 1 line）。

## 6. Template Injection (模版注入)
-   **{{active}}**: 如果为激活状态则注入 `active` 类名。
-   **{{iconClass}}**: 图标特定的遮罩（mask）类名，用来控制不同图标展示。
-   **{{label}}**: 菜单项显示的文本内容。
