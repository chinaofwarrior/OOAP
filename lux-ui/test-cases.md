# Lux 组件库测试用例

## 视觉一致性

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| VIS-01 | 全局色彩 | 打开包含所有组件的页面 | 主色一致，辅助色与边框色稳定 |
| VIS-02 | 阴影层级 | 对比卡片、Modal、Toast | 阴影层级从低到高递进明显 |
| VIS-03 | 字体层级 | 检查标题、副标题、正文 | 字号与行高符合层次规范 |

## 交互与状态

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| INT-01 | 按钮 | Hover 主按钮 | 背景加深并轻微上浮 |
| INT-02 | 按钮 | 点击并松开 | 按下回落，不产生跳动 |
| INT-03 | 输入框 | Focus 输入框 | 边框主色 + 柔光外圈 |
| INT-04 | 输入框 | 设置 data-invalid="true" | 红色边框与外圈 |
| INT-05 | Tabs | 点击不同 Tab | 对应面板展示，其他隐藏 |
| INT-06 | Dropdown | 点击触发器 | 菜单显示并 aria-expanded=true |
| INT-07 | Dropdown | 点击页面空白 | 菜单关闭并 aria-expanded=false |
| INT-08 | Modal | 点击打开按钮 | Modal 与遮罩显示 |
| INT-09 | Modal | 点击遮罩或关闭按钮 | Modal 关闭并 aria-hidden=true |
| INT-10 | Toast | 调用 showToast | Toast 进入并在指定时间移除 |

## 响应式布局

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| RES-01 | Grid | 宽度 1200px | .lux-grid-4 显示四列 |
| RES-02 | Grid | 宽度 960px | .lux-grid-4 显示两列 |
| RES-03 | Grid | 宽度 720px | .lux-grid-2 显示一列 |
| RES-04 | 容器 | 宽度 720px | .lux-container 内边距缩小 |

## 无障碍访问

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| A11Y-01 | 按钮 | 键盘 Tab 聚焦 | 出现清晰 focus-visible 外框 |
| A11Y-02 | Tabs | 使用方向键切换 | 选中状态随之更新 |
| A11Y-03 | Dropdown | 打开后按 Escape | 菜单关闭 |
| A11Y-04 | Modal | 打开后按 Escape | Modal 关闭 |
| A11Y-05 | Tooltip | 键盘聚焦 Tooltip | 提示文本显示 |
| A11Y-06 | Reduced Motion | 系统开启减少动效 | 动效时长降至最小 |

## 性能与稳定性

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| PERF-01 | 初始化 | 调用 LuxUI.init() | 绑定事件不阻塞页面加载 |
| PERF-02 | Toast | 连续触发 10 次 | 依次展示并按时间移除 |
| PERF-03 | Dropdown | 快速开关 10 次 | 无明显闪烁或状态错乱 |

## 兼容与降级

| 编号 | 组件 | 步骤 | 预期 |
| --- | --- | --- | --- |
| COMP-01 | 无 JS | 禁用脚本 | 组件仍可渲染为基础样式 |
| COMP-02 | 无动效 | prefers-reduced-motion | 动效被最小化 |
