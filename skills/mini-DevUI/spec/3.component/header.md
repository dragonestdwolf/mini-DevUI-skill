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

## 4. Icon Spec (图标规范)

### 4.1 图标来源
Header 组件**同时使用两个图标目录**，渲染方式截然不同：

| 区域 | 图标目录 | 渲染方式 |
|:---|:---|:---|
| 顶部导航项图标 | `icon/miniDev-icon/top-nav/` | `<img>` 标签（多色） |
| 右侧操作图标 | `icon/miniDev-icon/action/` | CSS Mask（单色） |

### 4.2 渲染方式详解

**导航项图标（多色，`<img>`）**：
```html
<img class="devui-header-nav-icon" src="相对路径/top-nav/首页-1.svg" />
```
- 尺寸：24×24px
- 严禁使用 CSS Mask（会丢失多色信息）

**右侧操作图标（单色，CSS Mask）**：
```css
.devui-icon-[name] {
  width: 16px; height: 16px;
  background-color: currentColor;
  -webkit-mask: url('相对路径/action/[name].svg') no-repeat center/contain;
  mask: url('相对路径/action/[name].svg') no-repeat center/contain;
}
```

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 | 备注 |
|:---|:---|:---|:---|:---|
| 首页导航 | `top-nav/首页-1.svg` | 24×24 | `<img>` | 多色原生 |
| 工作台导航 | `top-nav/工作台-1.svg` | 24×24 | `<img>` | 多色原生 |
| 项目导航 | `top-nav/项目-1.svg` | 24×24 | `<img>` | 多色原生 |
| 看板导航 | `top-nav/看板-1.svg` | 24×24 | `<img>` | 多色原生 |
| 服务导航 | `top-nav/服务-1.svg` | 24×24 | `<img>` | 多色原生 |
| 搜索操作 | `action/search.svg` | 16×16 | mask | 右侧操作区 |
| 帮助操作 | `action/help.svg` | 16×16 | mask | 右侧操作区 |
| 更多操作 | `action/more-horizontal.svg` | 16×16 | mask | 右侧操作区 |

### 4.4 Anti-Pattern (🔴 高频出错项)
- ❌ **严禁** 对顶部导航图标使用 CSS Mask（top-nav 是多色图标，mask 后变成纯色方块）
- ❌ **严禁** 对右侧操作图标使用 `<img>`（无法跟随主题色变化）
- ❌ 禁止混淆 `top-nav/` 和 `sidebar/` 目录（两者是不同的图标集）
- ❌ 禁止使用中文路径前缀时遗漏 `-1` 后缀（如 `首页.svg` ≠ `首页-1.svg`）

---

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
