# Component: Sidebar Navigation (侧边导航)

[Metadata]
- **Component Name**: Sidebar Navigation
- **Category**: Component / Navigation
- **Version**: v1.0
- **Icon Strategy**: Ref `spec/0.role/icon_role.md`. **MUST use relative paths (e.g., `../../../icon/...`)**.
- **Related Files**: `Sidebar-tem.html`

## 1. Overview (概述)
Attributes: Fixed width, Vertical layout, Collapsible (optional logic).

## 2. Layout & Style (布局与样式)

-   **Container**:
    -   `width`: `240px` (Fixed)
    -   `height`: `100%` (Matches sidebar container)
    -   `background-color`: `#FFFFFF`
    -   `border-right`: `1px solid #DFE1E6`
    -   `display`: `flex`
    -   `flex-direction`: `column`
    -   `padding`: `8px 0`

-   **Project Header**:
    -   `height`: `48px`
    -   `padding`: `0 16px`
    -   `display`: `flex`
    -   `align-items`: `center`
    -   `justify-content`: `space-between`
    -   `cursor`: `pointer`
    -   `font-weight`: `700`
    -   `color`: `#252B3A`
    -   **Icon**: Project Avatar (32x32 or 24x24).

-   **Menu List**:
    -   `flex`: `1`
    -   `overflow-y`: `auto`
    -   `padding`: `4px`
    -   `display`: `flex`
    -   `flex-direction`: `column`
    -   `gap`: `4px`

-   **Menu Item**:
    -   `height`: `44px`
    -   `padding`: `0 8px`
    -   `display`: `flex`
    -   `align-items`: `center`
    -   `gap`: `12px`
    -   `cursor`: `pointer`
    -   `color`: `#252B3A`
    -   `font-size`: `14px`
    -   `position`: `relative`
    -   `transition`: `background-color 0.2s`
    -   `border-radius`: `4px`
-   **Menu List**:
    -   `overflow-x`: `hidden` (Prevent scroll from negative margins)

-   **Menu Group (`.devui-menu-group`)**:
    -   Wrapper for Parent Item + Sub Menu List.
    -   **Expanded State (`.is-expanded`)**:
        -   `margin`: `-2px -4px` (Visual Overflow)
        -   `padding-bottom`: `2px` (Optional adjustment)
        -   `background-color`: `#FBFBFC`
        -   `border`: `1px solid #DFE1E6`
        -   `border-radius`: `4px`
        -   `position`: `relative`
        -   `z-index`: `1`

-   **Items inside Expanded Group**:
    -   **Parent Item**: `padding`: `0 12px` (Compensate for -4px margin)
    -   **Sub Menu Item**: `padding`: `0 12px` (Compensate for -4px margin, plus indentation if applicable)

-   **Sub Menu List**:
    -   `overflow`: `hidden`
    -   `transition`: `all 0.3s ease-in-out`
    -   **Collapsed**: `max-height: 0`, `opacity: 0`.
    -   **Expanded**: `max-height: 500px` (or fitting value), `opacity: 1`.

-   **Sub Menu Item**:
    -   `height`: `40px`
    -   `padding-left`: `44px` (Align icon with Parent Text. Parent Text starts at 8px Padding + 20px Icon + 12px Gap = 40px? Need to check exact math.)
    -   **Active State**:
        -   `background-color`: `#EBF1FF`
        -   `color`: `#5E7CE0`
        -   `font-weight`: `700`
        -   `box-shadow`: `inset 3px 0 0 0 #5E7CE0` (Left Blue Bar)

## 3. States (状态)

### 3.1 Default
-   `background-color`: `transparent`
-   `color`: `#252B3A`

### 3.2 Hover
-   `background-color`: `#F2F5FC`

### 3.3 Active (选中)
-   `background-color`: `#EBF1FF` (Light Blue background)
-   `color`: `#252B3A`
-   `font-weight`: `700`
-   **Visual Indicator**: Blue vertical bar (`width: 3px`) on the left.
    -   `position`: `absolute`, `left`: `0`
    -   `top`: `0`, `bottom`: `0`
    -   `background-color`: `#5E7CE0` (DevUI Primary Blue)

## 4. Icons (图标)
-   **Source**: `icon/miniDev-icon/侧边导航图标/`
-   **Items**:
    -   `仪表盘.svg`
    -   `代码管理.svg`
    -   `制品仓库.svg`
    -   `测试管理.svg`
    -   `软件设计.svg`
    -   `项目协作.svg`
    -   `知识库.svg`
    -   `持续交付.svg`

## 5. Interaction (交互)
-   **Hover Effect**: Background changes immediately.
-   **Click**: Sets active state.
-   **Collapse**: Bottom icon triggers collapse mode (Width reduces to ~64px, text hides).

## 6. Template Structure
Ref: `spec/4.template/sidebar-tem.html`
