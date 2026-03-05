# Spec: Header (顶部导航)

[Metadata]
- **Component**: `d-header`
- **Template Source**: `spec/4.template/header-tem.html`
- **Benchmark Source**: `HistoryRender/component/header/benchmark.html` (Figma Node 3090:13855)

## 2. Content Presentation (内容呈现)
描述不同类型的数据应如何组装 HTML：

### 2.1 Left Section (左侧应用信息与主导航)
- **Container**: `height: 32px`, `align-items: center`
-   Structure:
    ```html
    <div class="devui-header-left">
        <div class="devui-header-menu-btn">
            <span class="devui-icon-menu"></span>
        </div>
        <div class="devui-header-logo">
            <img class="devui-logo-img" src="{{logoSrc}}" alt="logo" />
            <!-- Text is optional depending on Logo SVG -->
            <!-- <span class="devui-logo-text">{{logoText}}</span> -->
        </div>
        <div class="devui-header-divider"></div>
        <div class="devui-header-console">控制台</div>
        <div class="devui-header-location">
            <span class="devui-icon-location"></span>
            <span class="devui-header-location-text">华北-北京四</span>
            <span class="devui-icon-arrow-down"></span>
        </div>
        <div class="devui-header-nav">
            <!-- Navigation Items Slot -->
            {{navItems}}
        </div>
    </div>
    ```

### 2.2 Navigation Item (导航项)
-   **Scenario**: Used for main navigation links like "首页", "工作台", "效能洞察", "服务", "华为开源镜像站".
-   **Layout**: Flex container, `height: 32px`, `gap: 4px; padding: 4px 8px; border-radius: 2px;`
-   **Icon logic**: Nav items MUST use `<img>` tags (`size: 24x24`) pointing to `icon/miniDev-icon/top-nav/` (e.g., `首页-1.svg`). DO NOT use CSS `-webkit-mask` icon classes from the sidebar for top navigation, as top navigation icons are multi-colored.
-   **Text logic**: Text expects `size: 14px, line-height: 22px`.
-   **Variations**:
    -   **Standard Item**:
    ```html
    <div class="devui-header-nav-item">
        <div class="devui-header-nav-content">
            <img class="devui-header-nav-icon" src="{{iconSrc}}" />
            <span class="devui-header-nav-text">{{text}}</span>
        </div>
    </div>
    ```
    -   **Item with Dropdown**:
    ```html
    <div class="devui-header-nav-item">
        <div class="devui-header-nav-content">
            <img class="devui-header-nav-icon" src="{{iconSrc}}" />
            <span class="devui-header-nav-text">{{text}}</span>
        </div>
        <span class="devui-icon-arrow-down" style="margin-left: 4px;"></span>
    </div>
    ```

### 2.3 Right Section (右侧全局操作与个人中心)
-   **Structure**: Flex with `gap: 12px; padding: 4px 11px 4px 20px;`
-   Structure:
    ```html
    <div class="devui-header-right">
        <div class="devui-header-actions">
            <!-- Action buttons contain an inner 16x16 icon mask -->
            <div class="devui-header-action-btn">
                <span class="devui-action-icon devui-icon-notification"></span>
            </div>
            <div class="devui-header-action-btn">
                <span class="devui-action-icon devui-icon-codehub"></span>
            </div>
            <div class="devui-header-lang">EN</div>
        </div>
        <div class="devui-header-avatar">{{userInitials}}</div>
    </div>
    ```

### 2.4 Avatar (头像)
-   Structure: 
    ```html
    <div class="devui-header-avatar">HZ</div>
    ```
-   Style: Circular shape, `size: 28px`, `var(--devui-brand)` background, white bold text (`size: 12px`, `weight: 500`).

## 5. Dynamic Response (动态响应)
-   **Text Overflow**:
    -   Navigation Items: Prevent wrapping (`white-space: nowrap`).
    -   Console and Location blocks: Prevent wrapping.
-   **Responsive Layout**:
    -   Header container acts as absolute width parent: `flex`, `justify-content: space-between`, `padding: 0 8px`, `height: 48px`.

## 7. Anti-Patterns (负面示例)
禁止在生成代码时出现以下模式：

1.  **❌ 禁止顶部导航图标单色化**
    ```html
    <!-- Bad: 使用 Sidebar 的单色 SVG mask 类名用于 Header 主导航 -->
    <span class="devui-icon-mask ic-dashboard" style="background-color:currentColor;"></span>
    
    <!-- Good: 使用 img 标签引入 multi-color 彩色 SVG 素材 -->
    <img class="devui-header-nav-icon" src="../../../../icon/miniDev-icon/top-nav/首页-1.svg" />
    ```

## 6. Template Injection (模版注入)
-   **{{logoSrc}}**: 标志图片路径
-   **{{logoText}}**: 品牌名称(可选)
-   **{{navItems}}**: 根据 "Navigation Item" 规则拼接的 HTML 字符串
-   **{{userInitials}}**: 用户名缩写，如 "HZ"
