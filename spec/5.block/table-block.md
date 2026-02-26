# Block: Table Block (表格区块)

[Metadata]
- **Block Name**: Table Block
- **Category**: Block / Composite
- **Composition**: `Table Header Block` + `Table` + `Pagination`
- **Version**: v1.0
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths (e.g., `../../../icon/...`)**.

## 1. Layout Structure (布局结构)

整个区块为垂直排列的 Flex 容器。

-   **Container (`.devui-table-block`)**:
    -   `display: flex`
    -   `flex-direction: column`
    -   `width: 100%`
    -   `background-color`: `transparent`

### 1.1 Header Area
-   **Source**: `spec/5.block/toolbar-block.md`
-   **Class**: `.devui-block-toolbar`
-   **Placement**: Top

### 1.2 Table Area
-   **Source**: `spec/3.component/table.md`
-   **Class**: `.devui-table-container`
-   **Placement**: Middle (below Header)
-   **Style**: `margin-top: 10px`
-   **Style**: `flex: 1` (optional, depends on page layout, but usually table takes height)

### 1.3 Pagination Area
-   **Source**: `spec/3.component/pagination.md`
-   **Class**: `.devui-pagination`
-   **Placement**: Bottom (below Table)
-   **Padding**: `16px 0` (Top/Bottom padding)
-   **Alignment**: Right aligned (based on design image typically, or specified in pagination spec as center/right). *Note: Pagination spec says Items Alignment: Total(Left), List(Center/Right). Let's use `justify-content: flex-end` or space-between if total is present.*

## 2. Template Code (模版代码)

```html
<div class="devui-table-block">
    <!-- 1. Header Block -->
    <div class="devui-block-toolbar">
        <!-- ... content from toolbar-block ... -->
    </div>

    <!-- 2. Table Container -->
    <div class="devui-table-container">
        <!-- ... content from table component ... -->
    </div>

    <!-- 3. Pagination -->
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
```

## 3. CSS Reference (样式参考)

```css
.devui-table-block {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
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
