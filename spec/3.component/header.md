# Spec: Header (顶部导航)

[Metadata]
- **Component**: `d-header`
- **Template Source**: `spec/4.template/header-tem.html`

## 1. Content Presentation (内容呈现格式)
描述不同类型的数据应如何组装 HTML：

### 1.1 Left Section (左侧应用信息与主导航)
-   Structure:
    ```html
    <div class="devui-header-left">
        <span class="devui-header-icon devui-icon-menu"></span>
        <div class="devui-header-logo">
            <img class="devui-logo-img" src="{{logoSrc}}" alt="logo" />
            <span class="devui-logo-text">{{logoText}}</span>
        </div>
        <div class="devui-header-divider"></div>
        <div class="devui-header-nav">
            <!-- Navigation Items -->
            {{navItems}}
        </div>
    </div>
    ```

### 1.2 Navigation Item (导航项)
-   Scenario: Used for main navigation links like "控制台", "首页", "工作台".
-   Variations:
    -   **Text Only**: `<a>控制台</a>`
    -   **With Left Icon & Right Dropdown Arrow**: 
    ```html
    <div class="devui-header-nav-item">
        <span class="devui-header-nav-icon">{{icon}}</span>
        <span class="devui-header-nav-text">{{text}}</span>
        <span class="devui-header-nav-arrow devui-icon-arrow-down"></span>
    </div>
    ```

### 1.3 Right Section (右侧全局操作与个人中心)
-   Structure:
    ```html
    <div class="devui-header-right">
        <!-- Action Icons -->
        <span class="devui-header-action-icon devui-icon-notification"></span>
        <span class="devui-header-action-icon devui-icon-task"></span>
        <!-- Language Switcher -->
        <span class="devui-header-lang">EN</span>
        <!-- User Avatar -->
        <div class="devui-header-avatar">{{userInitials}}</div>
    </div>
    ```

### 1.4 Avatar (头像)
-   Structure: 
    ```html
    <div class="devui-header-avatar">HZ</div>
    ```
-   Style: Circular shape, `var(--devui-brand)` or primary color background, white bold text.

## 2. Dynamic Response (动态响应)
-   **Text Overflow**:
    -   Navigation Items: Prevent wrapping (`white-space: nowrap`).
    -   Logo Text: Prevent wrapping.
-   **Responsive Layout**:
    -   Header container should be `flex` with `justify-content: space-between`.
    -   Left and Right sections should maintain layout, while the middle navigation area might need overflow handling (e.g., hiding or moving items to a "More" dropdown) if the screen is too narrow.

## 3. Template injection (模版注入)
-   **{{logoSrc}}**: 标志图片路径 (默认使用 `../../../icon/devcloud-logo-header.svg`)
-   **{{logoText}}**: "华为云"等品牌名称
-   **{{navItems}}**: 根据 "Navigation Item" 规则拼接的 HTML 字符串
-   **{{userInitials}}**: 用户名缩写，如 "HZ"
