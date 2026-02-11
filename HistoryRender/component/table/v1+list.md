# Design Review Report: HistoryRender/component/table/v1.html
**Figma Node**: 497:2419 (Table DataTable)
**Status**: ⚠️ Warnings Found

## 🔴 Critical Issues (Layout, Spacing, Alignment)
- [ ] **Body Row Padding**: 
    -   Expected: Height `42px` with Line-Height `22px` implies vertical padding of **10px**.
    -   Found: `padding: 11px 16px` (Results in 11+11+22 = 44px required height, causing potential overflow or misalignment within the fixed 42px container).
- [ ] **Header Background**: 
    -   Expected: Figma code output shows `bg-[var(--背景颜色/devui-base-bg,white)]` for header cells.
    -   Found: `background-color: var(--devui-global-bg, #f5f5f5)`. 
    -   *Note*: Confirm if Gray header is a specific design intent deviation or a Figma interpretation error. `get_design_context` explicitly lists white background for header items.

## 🟡 Visual Discrepancies (Colors, Fonts, Radius)
- [ ] **Container Shadow**: 
    -   Expected: `0px 4px 12px 0px rgba(0,0,0,0.16)`.
    -   Found: `0 2px 8px rgba(0, 0, 0, 0.1)`.

## 🟢 Verified Matches
- [x] **Row Height**: Strictly `42px` for both Header and Body.
- [x] **Checkbox Column Width**: `48px`.
- [x] **Typography Size**: Header `12px/20px`, Body `14px/22px`.
- [x] **Typography Weight**: Header `Bold (700)`, Body `Regular (400)`.
- [x] **Colors**: Text `#252b3a`, Border `#dfe1e6`.

## 🛠 Fix Recommendations
1.  **Adjust Body Padding**: Change `tbody td` padding to `10px 16px` to fit the 22px text within 42px height.
2.  **Update Shadow**: Copy exact Figma shadow values.
3.  **Fix Font**: Import and use `Noto Sans SC`.
4.  **Clarify Header Bg**: If Gray Header is standard for DevUI, update Figma or acknowledge deviation. If White is intended, fix CSS to `#ffffff`.
