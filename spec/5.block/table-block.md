# Block: Table Block (表格区块)

[Metadata]
- **Block Name**: Table Block
- **Category**: Block / Composite
- **Composition**: `Table Header Block` + `Table` + `Pagination`
- **Version**: v1.0
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths (e.g., `../../../icon/...`)**.

## 1. Layout Structure (布局结构)

外围大容器以流式伸缩结构向下延伸，但通过容器划分避免不需要的白底面积。

-   **Content Container (`.devui-content`)**:
    -   上下 `padding: 12px` 左右`padding: 20px`以紧凑排布周围。
    -   底色跟随最外层内容底色 `#F3F3F3`。

-   **Wrapper (`.devui-table-block`)**:
    -   `display: flex`
    -   `flex-direction: column`
    -   `width: 100%`
    -   `min-height: 0`

### 1.1 Header Area / Toolbar
-   **Source**: `spec/5.block/toolbar-block.md`
-   **Class**: `.devui-block-toolbar`
-   **Style**: 直接放置于背景上 (`background-color: transparent`)，独立占据上方区域。规定为紧凑型定高 `32px` 以及下外边距 `margin-bottom: 10px` 提供间距。

### 1.2 Table & Pagination Container
要求高度紧凑：不使用拉伸填充整页高度导致在数据较少时出现巨大的白底下半部分。
-   **Class**: `.devui-table-content-wrap`
-   **Style**: 白色实体背景 `var(--devui-base-bg, #FFFFFF)`，有 `border-radius: 4px` 和浅阴影 `box-shadow: 0 1px 3px 0 rgba(0,0,0,0.04)`。
-   **Structure**: 这是一个内部 flex 列容器，内部分别囊括 `Table Container` (`.devui-table-container`) 与左对齐或右对齐的底层 `Pagination` 区块。这样白底框子就只会被撑到真实表格与底部分页的实际总高度。

## 2. Template Code (模版代码)

```html
<div class="devui-table-block">
    <!-- 1. Header Block -->
    <div class="devui-block-toolbar">
        <!-- ... content from toolbar-block ... -->
    </div>

    <!-- 2. Table & Pagination Wrap (White background container) -->
    <div class="devui-table-content-wrap">
        
        <!-- 2.1 Table Container -->
        <div class="devui-table-container">
            <!-- ... content from table component ... -->
        </div>

        <!-- 2.2 Pagination -->
        <div class="devui-pagination">
            <!-- Total -->
            <span class="devui-pagination-total">总条数: 8</span>
            
            <!-- Spacer -->
            <div style="flex: 1"></div>

            <!-- Size Changer -->
            <div class="devui-select-sm">
                <span>15 条/页</span>
                <span class="devui-icon-arrow"></span>
            </div>

            <!-- Warning: Icon paths must be relative ../../../icon/... -->
            <button class="devui-pagination-item disabled">
                <img src="../../../icon/miniDev-icon/action/arrow-left.svg" class="devui-icon-s">
            </button>
            
            <button class="devui-pagination-item active">1</button>
            
            <button class="devui-pagination-item disabled">
                <img src="../../../icon/miniDev-icon/action/arrow-left.svg" class="devui-icon-s" style="transform: rotate(180deg);">
            </button>

            <!-- Jump -->
            <div class="devui-pagination-jump">
                <span>跳至</span>
                <input type="text" value="1">
                <span>页</span>
            </div>
        </div>
        
    </div>
</div>
```

## 3. CSS Reference (样式参考)

```css
.devui-table-block {
    display: flex;
    flex-direction: column;
    width: 100%;
    min-height: 0;
}

.devui-table-content-wrap {
    background-color: var(--devui-base-bg, #FFFFFF);
    border-radius: 4px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
}

.devui-pagination {
    display: flex;
    align-items: center;
    padding: 16px 0;
    gap: 8px;
    font-size: 12px;
    color: #252B3A;
}

.devui-pagination-item {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid transparent; 
    border-radius: 4px;
    background: transparent;
    cursor: pointer;
    font-size: 12px;
    color: #252B3A;
    transition: all 0.2s;
}

.devui-pagination-item:hover:not(.disabled) {
    background-color: #F2F5FC;
    color: #5E7CE0;
}

.devui-pagination-item.active {
    background-color: #F2F5FC;
    color: #5E7CE0;
    font-weight: 700;
}

.devui-pagination-item.disabled {
    cursor: not-allowed;
    opacity: 0.5;
}

.devui-pagination-jump input {
    width: 48px;
    height: 28px;
    border: 1px solid #D7D8DA;
    border-radius: 4px;
    text-align: center;
    margin: 0 4px;
}
```
