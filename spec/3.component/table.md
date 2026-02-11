# Spec: Table (表格交互规范)

[Metadata]
- **Component**: `d-table`
- **Template Source**: `spec/4.template/table-tem.html`
- **Figma Node**: 259:426

## 1. Content Presentation (内容呈现格式)
定义表格内部不同类型数据的 HTML 组装方式。

### 1.1 Header Cell (表头)
-   **Standard**: `<span>{{label}}</span>` (Bold, 12px)
-   **Sortable**:
    ```html
    <div class="devui-table-header-cell">
        <span>{{label}}</span>
        <span class="devui-table-sort-icon">
            <!-- Icon SVG -->
        </span>
    </div>
    ```
-   **Checkbox**: `<input type="checkbox" />` (Centered)

### 1.2 Body Cell Types (单元格类型)

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
    - **Icon**: `icon/miniDev-icon/操作图标/collapse.svg` (16x16px).
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
-   **Icon**: `icon/miniDev-icon/状态图标/成功.svg`.
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

## 2. Dynamic Response (动态响应策略)

### 2.1 Text Overflow (文本溢出)
-   **Strategy**: Ellipsis ( `text-overflow: ellipsis` )
-   **Constraint**: Container must have fixed width or `max-width`.
-   **Tooltip**: REQUIRED if text is truncated.
    -   *Spec*: On hover, show native `title` attribute or custom Tooltip component.

### 2.2 Empty State (空状态)
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

## 3. Visual Variants (视觉变体)

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

## 4. Space Strategy (空间策略)

-   **Checkbox Column**: Fixed Width **40px**.
-   **Action Column**: Hug Content (Min-width 100px).
-   **Data Columns**:
    -   Fluid: `flex: 1` or `width: auto` (distribute remaining space).
    -   Fixed: Explicit pixel width if specified (e.g., Date column 160px).
