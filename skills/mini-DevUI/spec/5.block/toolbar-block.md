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
    -   `height: 32px`
    -   `padding: 0 16px`
    -   `margin-bottom: 10px`
    -   `background-color`: `transparent` (放置在 content 底色 `#F3F3F3` 上)

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
        -   Style: Active item has Gray Bg `#F3F3F3` (跟随外部 content 深色背景) and Dark Icon.

## 2. Template Code (模版代码)

```html
<div class="devui-block-toolbar">
    
    <!-- LEFT AREA -->
    <div class="devui-block-left">
        <!-- Scope Filter -->
        <div class="devui-dropdown-trigger">
            <span>全部</span>
            <span class="devui-icon-arrow icon-select-arrow"></span> <!-- select-arrow.svg -->
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
            <span class="devui-btn-icon icon-add"></span> <!-- new.svg -->
            <span>新建</span>
        </button>

        <!-- Temp Filter -->
        <div class="devui-dropdown-trigger">
            <span>临时过滤</span>
            <span class="devui-icon-arrow icon-select-arrow"></span>
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
                 <span class="devui-icon-action icon-close-circle"></span>
                 <span class="devui-divider-vertical-sm"></span>
                 <span class="devui-icon-action icon-save"></span>
                 <span class="devui-icon-action icon-folder"></span>
            </div>
        </div>

        <!-- Text Buttons -->
        <button class="devui-btn devui-btn-text">
            <span class="devui-btn-icon icon-setting"></span>
            <span>表格设置</span>
        </button>
        
        <div class="devui-btn-icon icon-more" style="cursor: pointer;"></div>
        <button class="devui-btn devui-btn-text">
            <span>更多</span>
        </button>

        <!-- Divider -->
        <div class="devui-divider-vertical"></div>

        <!-- View Toggle (Wrapped/Solid) -->
        <div class="devui-tabs" data-type="wrapped">
            <div class="devui-tab-item active">
                <span class="devui-tab-icon icon-list"></span>
            </div>
            <div class="devui-tab-item">
                <span class="devui-tab-icon icon-kanban"></span>
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
    padding: 0 16px;
    height: 32px; /* Fixed robust height */
    margin-bottom: 10px; /* Space before table */
    background-color: transparent; /* Sits naturally on the page canvas */
    border-radius: 4px; /* Only if it has background, else optional */
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

/* Base Icon Rule for Buttons & Tabs */
.devui-btn-icon, .devui-tab-icon {
    width: 16px;
    height: 16px;
    display: inline-block;
    background-color: currentColor; /* Syncs color with parent text color via mask */
    -webkit-mask-repeat: no-repeat;
    -webkit-mask-position: center;
    -webkit-mask-size: contain;
}

/* Base Icon Rule for Sub-actions */
.devui-icon-action {
    width: 14px;
    height: 14px;
    cursor: pointer;
    opacity: 0.6;
    background-color: #252b3a;
    -webkit-mask-size: contain;
    -webkit-mask-position: center;
    -webkit-mask-repeat: no-repeat;
    transition: opacity 0.2s;
}
.devui-icon-action:hover {
    opacity: 1;
}

/* CSS Mask Image Definitions - ONLY use CSS classes, never inline styles */
.icon-add { -webkit-mask-image: url('../../icon/miniDev-icon/action/new.svg'); }
.icon-setting { -webkit-mask-image: url('../../icon/miniDev-icon/action/settings.svg'); }
.icon-more { -webkit-mask-image: url('../../icon/miniDev-icon/action/more-horizontal.svg'); }
.icon-list { -webkit-mask-image: url('../../icon/miniDev-icon/action/list-view.svg'); }
.icon-kanban { -webkit-mask-image: url('../../icon/miniDev-icon/action/board-view.svg'); }
.icon-close-circle { -webkit-mask-image: url('../../icon/miniDev-icon/action/close.svg'); }
.icon-save { -webkit-mask-image: url('../../icon/miniDev-icon/action/save.svg'); }
.icon-folder { -webkit-mask-image: url('../../icon/miniDev-icon/action/folder.svg'); }


/* Category Search Specifics */
.devui-category-search-container {
    flex: 1; /* Fill remaining width inside right block */
    background-color: #ffffff;
    border: 1px solid #adb0b8;
    border-radius: 6px; /* Elegant 6px border */
    height: 32px;
    padding: 0 8px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
}
.devui-category-search-container:focus-within {
    border-color: var(--devui-brand);
    box-shadow: 0 0 0 4px rgba(94, 124, 224, 0.08); /* Soft blue aura */
}

.devui-search-tag {
    display: inline-flex;
    align-items: center;
    height: 20px; /* Sophisticated slim height */
    padding: 0 8px;
    background-color: #f2f5fc; /* Subtle blue/purple tint */
    border-radius: 4px;
    font-size: 12px;
    color: #252b3a;
    white-space: nowrap;
    gap: 4px;
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

.devui-dropdown-trigger .devui-icon-arrow {
    width: 12px;
    height: 12px;
    background-color: currentColor;
    -webkit-mask: url('../../icon/select-arrow.svg') no-repeat center;
}

/* Vertical Divider */
.devui-divider-vertical {
    width: 1px;
    height: 16px;
    background-color: #DFE1E6;
}
.devui-divider-vertical-sm {
    width: 1px;
    height: 12px;
    background-color: #DFE1E6;
    margin: 0 2px;
}

/* View Toggle Specifics - Tabs */
.devui-tabs[data-type="pills"] .devui-tab-item {
    position: relative;
    padding: 8px 0;
    color: #575D6C;
}
.devui-tabs[data-type="pills"] .devui-tab-item.active {
    color: #252B3A;
    font-weight: 700;
}
.devui-tabs[data-type="pills"] .devui-tab-item.active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #252B3A; /* Solid black elegant line */
}

.devui-tabs[data-type="wrapped"] .devui-tab-item {
    width: 32px;
    height: 32px;
    padding: 0;
    border-radius: 4px; /* Icon buttons usually rounded square in toggles */
}
```
