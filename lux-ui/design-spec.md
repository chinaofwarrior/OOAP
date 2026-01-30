# Lux 组件体系设计说明

## 目标与设计原则

Lux 组件体系围绕精致视觉层次、优雅动效与高品质材质感展开，以轻量、可复用、可扩展为核心。设计目标如下：

- 视觉层次：以细腻对比与分层阴影建立信息优先级
- 动效体验：缓入缓出与微位移构建柔和反馈
- 色彩与材质：高对比主色配合柔光材质，保证清晰与质感
- 一致性：统一使用设计令牌驱动所有组件
- 可访问性：显式聚焦态与键盘可达性优先

## 组件库整体架构

1. Foundations（基础层）
   - 设计令牌：颜色、字体、尺寸、间距、圆角、阴影、动效
   - 全局排版与基础文本
2. Components（组件层）
   - 表单、导航、反馈、数据展示等常用组件
3. Patterns（模式层）
   - 组合型结构，例如卡片内信息区、对话框、表格
4. Behavior（交互层）
   - 基于数据属性的轻量 JS 行为，保证可替换与框架无关

## 设计令牌

- 颜色：高对比墨色文本 + 紫色主调 + 柔和辅助色
- 阴影：三层渐进阴影，建立层级深度
- 圆角：两级圆角与满圆角，保证柔和边缘
- 动效：短、常规、慢三段时长与统一缓动曲线

## 组件清单与视觉规范

### 按钮

类名：

- .lux-button
- .lux-button--ghost
- .lux-button--soft
- .lux-button--danger

视觉规范：

- 默认：主色填充 + 高亮阴影
- 悬停：更深主色 + 轻微上浮
- 按下：回落并收束阴影
- 禁用：降低透明度并移除阴影

### 输入控件

类名：

- .lux-input
- .lux-select
- .lux-textarea

视觉规范：

- 默认：细边框与浅色背景
- 悬停：边框轻微增强
- 聚焦：主色边框 + 柔光外圈
- 错误：红色边框 + 柔光外圈

### 切换与选择

类名：

- .lux-checkbox
- .lux-radio
- .lux-switch
- .lux-switch-input
- .lux-switch-knob

视觉规范：

- 选中：主色为强调
- 聚焦：标准聚焦环

### 标签与徽标

类名：

- .lux-badge
- .lux-chip

视觉规范：

- 徽标采用主色柔光填充
- 标签采用中性浅色背景

### 卡片与分隔

类名：

- .lux-card
- .lux-surface
- .lux-divider

视觉规范：

- 卡片使用材质渐变与层级阴影
- 分隔使用渐隐线增强空间秩序

### 表格与数据

类名：

- .lux-table

视觉规范：

- 表头使用弱墨色
- 行悬停以浅色背景强调

### 反馈组件

类名：

- .lux-progress
- .lux-progress-bar
- .lux-spinner
- .lux-skeleton
- .lux-toast
- .lux-toast-stack

视觉规范：

- 进度条使用渐变主色
- 骨架屏使用流动浅色
- Toast 使用高层阴影与边框提示

### 导航与信息组织

类名：

- .lux-tabs
- .lux-tablist
- .lux-tab
- .lux-tab-panel
- .lux-dropdown
- .lux-dropdown-menu
- .lux-dropdown-item

视觉规范：

- Tab 选中态凸显高光背景与阴影
- Dropdown 使用浮层阴影与浅色背景

### 弹层与提示

类名：

- .lux-modal
- .lux-modal-backdrop
- .lux-modal-content
- .lux-tooltip

视觉规范：

- Modal 使用柔光背景与层级阴影
- Tooltip 使用深色提示与轻微上浮

## 交互状态定义

### 通用状态

- default
- hover
- active
- focus-visible
- disabled
- selected
- invalid

### 组件状态映射

- 按钮：hover / active / disabled / focus-visible
- 输入框：hover / focus-visible / invalid / disabled
- Tabs：selected / focus-visible
- Dropdown：open / closed
- Modal：open / closed
- Toast：enter / exit

## 响应式布局规则

断点：

- 1024px：多列布局降级为两列
- 768px：两列布局降级为单列，容器内边距缩小

布局类：

- .lux-container
- .lux-stack
- .lux-inline
- .lux-grid / .lux-grid-2 / .lux-grid-3 / .lux-grid-4

## 无障碍访问支持

- 所有可交互组件支持 :focus-visible 聚焦环
- Tabs、Dropdown、Modal 由 JS 维护 aria-selected 与 aria-expanded
- Tooltip 允许 hover 与 focus 触发
- prefers-reduced-motion 关闭动效

## 代码结构与用法

文件结构：

- lux-ui/lux.css
- lux-ui/lux.js

引入方式：

```html
<link rel="stylesheet" href="/lux-ui/lux.css" />
<script src="/lux-ui/lux.js"></script>
```

初始化：

```html
<script>
  LuxUI.init();
</script>
```

### Tabs

```html
<div class="lux-tabs" data-lux-tabs>
  <div class="lux-tablist" role="tablist">
    <button class="lux-tab" data-lux-tab="overview" role="tab">Overview</button>
    <button class="lux-tab" data-lux-tab="details" role="tab">Details</button>
  </div>
  <div class="lux-tab-panel" data-lux-panel="overview" role="tabpanel">
    Overview content
  </div>
  <div class="lux-tab-panel" data-lux-panel="details" role="tabpanel" hidden>
    Details content
  </div>
</div>
```

### Dropdown

```html
<div class="lux-dropdown" data-lux-dropdown data-state="closed">
  <button class="lux-button lux-button--ghost" data-lux-dropdown-trigger aria-expanded="false">
    Actions
  </button>
  <div class="lux-dropdown-menu" data-lux-dropdown-menu hidden>
    <a class="lux-dropdown-item" href="#">Edit</a>
    <a class="lux-dropdown-item" href="#">Archive</a>
  </div>
</div>
```

### Modal

```html
<button class="lux-button" data-lux-open="lux-modal-1">Open modal</button>
<div class="lux-modal-backdrop" data-lux-backdrop="lux-modal-1" data-state="closed"></div>
<div class="lux-modal" data-lux-modal="lux-modal-1" data-state="closed" aria-hidden="true">
  <div class="lux-modal-content lux-stack">
    <div class="lux-title">Confirm action</div>
    <div class="lux-text">This action cannot be undone.</div>
    <div class="lux-inline">
      <button class="lux-button" data-lux-close>Confirm</button>
      <button class="lux-button lux-button--ghost" data-lux-close>Cancel</button>
    </div>
  </div>
</div>
```

### Toast

```html
<button class="lux-button" onclick="LuxUI.showToast({ title: 'Saved', description: 'Changes synced' })">
  Show toast
</button>
```

## 性能与一致性策略

- 使用 CSS 变量统一色彩与尺寸，降低维护成本
- 交互逻辑轻量，避免大规模 DOM 操作
- 动效遵循系统偏好，降低动效负担
- 组件以可组合类名为主，避免渲染耦合
