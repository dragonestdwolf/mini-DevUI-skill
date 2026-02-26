# Block: Table Header Operation Area (表格头部操作区)

[Metadata]
- **Block Name**: Table Header Operation Area
- **Category**: Block / Pattern
- **DevUI Components**: `d-tabs`, `d-button`, `d-category-search`, `d-dropdown`
- **Version**: v1.0
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths (e.g., `../../../icon/...`)**.

## 1. Layout Structure (布局结构)

整个操作区为一个 Flex 容器，采用 `justify-content: space-between` 将内容分为左右两部分。

-   **Container**:
    -   `display: flex`
    -   `align-items: center`
    -   `width: 100%`
    -   `height: 48px`
    -   `padding: 0 16px`
    -   `background-color`: `var(--devui-base-bg, #FFFFFF)`

### 1.1 Left Area (左侧区域)
内容：Global Filter + Navigation Tabs.

-   **Structure**: Flex Row, `flex-shrink: 0`, `gap: 16px`.

### 1.2 Right Area (右侧区域)
内容：Actions + Search + View Toggles.

-   **Structure**: Flex Row, `flex: 1`, `align-items: center`, `gap: 12px`, `min-width: 0`.
-   **Responsive Rule**:
    -   All elements except "Category Search" adapt width to content.
    -   "Category Search" fills remaining width (`flex: 1`).
-   **Elements**:
    1.  **Vertical Divider**: `height: 16px`, `border-left: 1px solid #DFE1E6`.
    2.  **Main Action (新建)**:
        -   Type: `d-button` (`variant="primary"`).
        -   Content: Icon `new.svg` + "新建".
    3.  **Temporary Filter (临时过滤)**:
        -   Type: Text Dropdown.
        -   Content: "临时过滤" + `select-arrow.svg`.
        -   Style: `white-space: nowrap`, `flex-shrink: 0`.
    4.  **Category Search**:
        -   Type: `d-category-search`.
        -   Width: ~320px (Flexible).
        -   Content: Tags ("类型: Story...", "状态: ...") + Input.
    5.  **Settings (表格设置)**:
        -   Type: `d-button` (`variant="text"`).
        -   Content: Icon `settings.svg` + "表格设置".
    6.  **More Actions**:
        -   Type: `d-button` (`variant="text"`).
        -   Content: Icon `more-horizontal.svg` + "更多".
    7.  **Vertical Divider**: Same as above.
    8.  **View Toggle**:
        -   Type: `d-tabs` (`type="wrapped"` / Solid Gray Block).
        -   Items: List Icon (Active), Kanban/Grid Icon (`board-view.svg`).
        -   Style: Active item has Gray Bg `#F5F5F5` and Dark Icon.

## 2. Template Code (模版代码)

```html
<div class="devui-block-toolbar">
    
    <!-- LEFT AREA -->
    <div class="devui-block-left">
        <!-- Scope Filter -->
        <div class="devui-dropdown-trigger">
            <span>全部</span>
            <span class="devui-icon-arrow"></span> <!-- select-arrow.svg -->
        </div>

        <!-- Navigation Tabs (Pills/Underline) -->
        <div class="devui-tabs" data-type="pills">
            <div class="devui-tab-item active">Backlog</div>
            <div class="devui-tab-item">缺陷</div>
        </div>
    </div>

    <!-- RIGHT AREA -->
    <div class="devui-block-right">
        
        <!-- Divider -->
        <div class="devui-divider-vertical"></div>

        <!-- Main Button -->
        <button class="devui-btn devui-btn-primary">
            <span class="devui-icon-add"></span> <!-- new.svg -->
            <span>新建</span>
        </button>

        <!-- Temp Filter -->
        <div class="devui-dropdown-trigger">
            <span>临时过滤</span>
            <span class="devui-icon-arrow"></span>
        </div>

        <!-- Category Search -->
        <div class="devui-category-search-container">
            <span class="devui-search-icon"></span>
            <!-- Tags -->
            <div class="devui-search-tag">
                <span>类型: Story | Task | Bug</span>
                <span class="devui-icon-close"></span>
            </div>
            <div class="devui-search-tag">
                <span>状态: 新建 | 进行中 | 已解决...</span>
                <span class="devui-icon-close"></span>
            </div>
            <input type="text" class="devui-search-input" placeholder="点击此处输入关键词...">
            <!-- Right Actions inside Search -->
            <div class="devui-search-actions">
                 <span class="devui-icon-close-circle"></span>
                 <span class="devui-divider-vertical-sm"></span>
                 <span class="devui-icon-save"></span>
                 <span class="devui-icon-folder"></span>
            </div>
        </div>

        <!-- Text Buttons -->
        <button class="devui-btn devui-btn-text">
            <span class="devui-icon-setting"></span>
            <span>表格设置</span>
        </button>
        
        <div class="devui-icon-more"></div>
        <button class="devui-btn devui-btn-text">
            <span>更多</span>
        </button>

        <!-- Divider -->
        <div class="devui-divider-vertical"></div>

        <!-- View Toggle (Wrapped/Solid) -->
        <div class="devui-tabs" data-type="wrapped">
            <div class="devui-tab-item active">
                <span class="devui-icon-list"></span>
            </div>
            <div class="devui-tab-item">
                <span class="devui-icon-kanban"></span>
            </div>
        </div>

    </div>
</div>
```

## 3. CSS Reference (样式参考)

```css
.devui-block-toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    /* padding: 8px 16px; removed padding to match strict 32px height vertical centering */
    padding: 0 16px;
    height: 32px;
    background-color: transparent;
}


.devui-block-left {
    display: flex;
    align-items: center;
    gap: 16px; 
    flex-shrink: 0;
}

.devui-block-right {
    display: flex;
    align-items: center;
    gap: 16px;
    flex: 1; /* Take remaining space */
    min-width: 0; /* Prevent overflow */
}

.devui-category-search-container {
    flex: 1; /* Fill remaining width inside right block */
    width: auto;
    /* ... other styles ... */
}

.devui-dropdown-trigger {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 14px;
    color: #252B3A;
    cursor: pointer;
    white-space: nowrap; /* Fix width issue */
    flex-shrink: 0;
}


/* Vertical Divider */
.devui-divider-vertical {
    width: 1px;
    height: 16px;
    background-color: #DFE1E6;
}

/* View Toggle Specifics */
.devui-tabs[data-type="wrapped"] .devui-tab-item {
    width: 32px;
    height: 32px;
    padding: 0;
    border-radius: 4px; /* Icon buttons usually rounded square in toggles */
}
```
