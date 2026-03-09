# Spec: Table (表格交互规范)

[Metadata]
- **Component**: `d-table`
- **Template Source**: `spec/4.template/table-tem.html`
- **Figma Node**: 259:426
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths (e.g., `../../../icon/...`)**.

## 2. Content Presentation (内容呈现)
定义表格内部不同类型数据的 HTML 组装方式。

### 2.1 Header Cell (表头)
-   **Standard**: `<span>{{label}}</span>` (Bold, 12px)
-   **Sortable** (Default when no description):
    ```html
    <div class="devui-table-header-cell">
        <span>{{label}}</span>
        <span class="devui-table-sort-icon"></span>
        <!-- Icon: icon/miniDev-icon/action/sort-icon.svg -->
    </div>
    ```
-   **Filterable** (Default when no description):
    ```html
    <div class="devui-table-header-cell">
        <span>{{label}}</span>
        <span class="devui-table-filter-icon"></span>
        <!-- Icon: ../../../icon/miniDev-icon/action/filter.svg (Must rely on relative path from html location) -->
    </div>
    ```
-   **Sort & Filter**:
    ```html
    <div class="devui-table-header-cell">
        <span>{{label}}</span>
        <div class="devui-header-icons">
             <span class="devui-table-sort-icon"></span>
             <span class="devui-table-filter-icon"></span>
        </div>
    </div>
    ```
-   **Style**:
    -   Icon Size: 16x16px.
    -   Gap (Text to Icon): 8px.
    -   Gap (Icon to Icon): 4px.
    -   Icon Color: #191919.
-   **Checkbox**: `<span class="devui-checkbox-box"></span>` (Size: 16x16px, Border: 1px solid #ADB0B8, Radius: 2px)

### 2.2 Body Cell Types (单元格类型)

#### A. Simple Text (文本)
-   **HTML**: `<span>{{text}}</span>`
-   **Behavior**: Default alignment left. Vertical center.

#### B. Text with Subtext (双行文本)
-   **Scenario**: Name + Email, Order ID + Date.
-   **Snippet**:
    ```html
    <div class="devui-table-cell-text-group">
        <div class="devui-text-primary">{{primaryText}}</div>
        <div class="devui-text-secondary">{{secondaryText}}</div>
    </div>
    ```
-   **Style**: Primary (14px, #252b3a), Secondary (12px, #71757f).

#### C. Operation Column (操作列)
-   **Structure**: Flex Row, Gap 8px.
-   **Content**: 3 Icons (16x16px).
    -   `star.svg` (Follow).
    -   `add-test-case.svg` (Add/Box+Plus).
    -   `more-vertical.svg` (More Actions).
-   **Padding**: Left/Right 16px.
-   **Snippet**:
    ```html
    <div class="devui-cell-operation">
        <img src="..." class="devui-operation-icon">
        <img src="..." class="devui-operation-icon">
        <img src="..." class="devui-operation-icon">
    </div>
    ```

#### D. Tree Structure
  - Standard Height: 42px.
  - Composition:
    - **Icon**: `icon/miniDev-icon/action/collapse.svg` (16x16px).
      - Default: Points Right (Collapsed).
      - Click Interaction: Rotates 90deg Down (Expanded).
    - **Gap**: 8px.
    - **Text**: 14px Regular.
  - Padding: Left/Right 16px.

#### E. Priority Level
-   **Structure**: Icon (16px) + Gap (8px) + Text (14px Regular).
-   **Icons**:
    -   Low: `icon/flag_low.svg`
    -   Middle: `icon/flag_middle.svg`
    -   High: `icon/flag_hight.svg` (Note typography in file name)
-   **Snippet**:
    ```html
    <div class="devui-tree-cell" style="padding-left: {{level * 16}}px">
        <span class="devui-tree-icon"></span>
        <span class="devui-tree-content">{{content}}</span>
    </div>
    ```

#### G. Status with Name (StatusWithName)
-   **Structure**: Icon (16px) + Gap (8px) + Text (14px Regular).
-   **Icon**: `icon/miniDev-icon/action/success.svg`.
-   **Snippet**:
    ```html
    <div class="devui-status-with-name">
        <img src="..." class="devui-status-icon-img">
        <span class="devui-status-text">Status</span>
    </div>
    ```

#### H. Text with Label (textWithLabel)
-   **Structure**: Link/Text + Gap (8px) + Label.
-   **Label Style**: Outline (Stroke), Size MD (Height 24px).
-   **Snippet**:
    ```html
    <div class="devui-cell-pair">
        <span>Text</span>
        <span class="devui-tag-outline devui-tag-md devui-tag-primary">Label</span>
    </div>
    ```

#### I. Label with Text (LabelWithText)
-   **Structure**: Label + Gap (8px) + Link/Text.
-   **Label Style**: Light (Shallow Bg), Size MD (Height 24px).
-   **Snippet**:
    ```html
    <div class="devui-cell-pair">
        <span class="devui-tag-light devui-tag-md devui-tag-warning">Label</span>
        <span>Text</span>
    </div>
    ```
    <!-- Chevron Icon -->
        </span>
        <span>{{label}}</span>
    </div>
    ```

## 4. Icon Spec (图标规范)

### 4.1 图标来源
- **目录**: `icon/miniDev-icon/action/`
- **引用规则**: 相对路径 `../../../icon/miniDev-icon/action/...`（根据 HTML 文件深度调整层级）

### 4.2 渲染方式
所有表格内图标均为**单色线性图标**，必须使用 **CSS Mask** 渲染：
```css
.devui-icon-[name] {
  background-color: currentColor;
  -webkit-mask: url('相对路径') no-repeat center/contain;
  mask: url('相对路径') no-repeat center/contain;
}
```

### 4.3 图标映射表

| 用途 | 图标文件 | 尺寸 | 渲染方式 |
|:---|:---|:---|:---|
| 排序（升序） | `sort-asc.svg` | 16×16 | mask |
| 排序（降序） | `sort-desc.svg` | 16×16 | mask |
| 筛选漏斗 | `filter.svg` | 16×16 | mask |
| 下拉箭头 | `chevron-down.svg` | 16×16 | mask |
| 表头复选框 | 内联 CSS 方块（非 SVG） | 16×16 | border |
| 操作列-编辑 | `edit.svg` | 16×16 | mask |
| 操作列-删除 | `delete.svg` | 16×16 | mask |
| 操作列-更多 | `more-horizontal.svg` | 16×16 | mask |
| 搜索（筛选面板） | `search.svg` | 16×16 | mask |

### 4.4 Anti-Pattern
- ❌ 禁止使用 `<img>` 加载操作类图标（无法跟随文本色变化）
- ❌ 禁止在 HTML `style=""` 内联属性中写 `mask-image` 长路径
- ❌ 禁止猜测图标文件名，必须先确认文件存在

---

## 5. Dynamic Response (动态响应)

### 5.1 Text Overflow (文本溢出)
-   **Strategy**: Ellipsis ( `text-overflow: ellipsis` )
-   **Constraint**: Container must have fixed width or `max-width`.
-   **Tooltip**: REQUIRED if text is truncated.
    -   *Spec*: On hover, show native `title` attribute or custom Tooltip component.

### 5.2 Empty State (空状态)
-   **Trigger**: No data in `tbody`.
-   **Visual**:
    ```html
    <tr>
        <td colspan="{{columnCount}}">
            <div class="devui-table-empty">
                <img src="assets/no-data.png" />
                <span>No Data Available</span>
            </div>
        </td>
    </tr>
    ```
-   **Height**: Minimum 200px container.

## 3. Visual Spec (视觉规范)

### 3.1 Striped Rows (斑马纹)
-   **Class**: Add `.devui-table-striped` to `<table>`.
-   **Effect**: Even rows background `#fafafa`.

### 3.2 Hover State
-   **Trigger**: Mouse enter `<tr>`.
-   **Effect**: Background color `#f2f5fc` (DevUI List Item Hover).
-   **Scope**: Entire row highlights.

### 3.3 Selected/Active Row
-   **Trigger**: Checkbox checked or row selected.
-   **Effect**: Background color `#f2f5fc` (Same as hover) + Optional Left Border Highlight.

### 3.4 Space Strategy (空间策略)

-   **Checkbox Column**: Fixed Width **48px**.
-   **Action Column**: Hug Content (Min-width 100px).
-   **Data Columns**:
    -   Fluid: `flex: 1` or `width: auto` (distribute remaining space).
    -   Fixed: Explicit pixel width if specified (e.g., Date column 160px).
