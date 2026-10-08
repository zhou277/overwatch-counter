# Overwatch Counter

当前版本：**v3.3.1**

## v3.3.1 更新

- 根据网上公开地图攻略、官方地图改动说明和常见高地/侧路打法，为当前 **24 张地图**补充路线
- 每张地图默认提供：
  - 主攻路线
  - 绕后 / 侧路
  - 高台 / 优势角路线
- 共新增 **72 条路线**
- 为 24 张地图分别生成本项目自制的 SVG 战术示意底图
- `map_routes` 新增 `source` 和 `basis`，记录参考网址与整理原则
- 路线图是战术学习示意图，不冒充官方像素级平面图

这些 SVG 不直接复制第三方地图图片，因此 GitHub Pages 不依赖外部图片链接，也方便以后继续从 Excel 调整路线。

## v3.3.0 更新

新增 **地图进攻路线可视化**。

采用：

```text
地图底图
+
SVG 路线层
```

而不是把路线直接画死在图片里。

### 支持的路线类型

- `main`：主攻路线
- `flank`：绕后路线
- `highground`：高台路线

网页会自动生成路线图例，并允许点击图例开关不同路线。

## 项目结构

```text
overwatch-counter/
├── .github/
├── assets/
│   └── maps/
│       └── 地图底图...
├── data.xlsx
├── template.html
├── build.py
├── index.html
└── README.md
```

## 如何添加地图底图

例如把图片放到：

```text
assets/maps/国王大道.png
```

然后在 `data.xlsx`：

```text
maps Sheet
→ 国王大道
→ image_path
→ assets/maps/国王大道.png
```

## map_routes Sheet

新增 Sheet：

```text
map_routes
```

字段：

| 字段 | 说明 |
|---|---|
| map | 地图名称，必须与 maps.name 一致 |
| route_type | main / flank / highground |
| label | 路线名称 |
| color | SVG 路线颜色 |
| points | 路线坐标 |
| line_width | 线宽 |
| dashed | 是否虚线 |
| note | 路线说明 |

### points 坐标

采用 0–100 的百分比坐标。

```text
0,0       = 左上
100,0     = 右上
0,100     = 左下
100,100   = 右下
```

例如：

```text
8,78;25,65;44,58;68,42;90,25
```

网页会把这些点自动连成带箭头的 SVG 路线。

## 为什么这样设计

地图图片和路线数据分开：

```text
底图变化
→ 只换 PNG/JPG

路线变化
→ 只改 Excel

网页结构
→ 不需要改
```

后续可以很方便地继续加入：

- 防守路线
- 高台控制点
- 狙击位
- 血包位置
- 开团点
- 危险区域

## GitHub Actions

修改并上传以下任一内容：

```text
data.xlsx
template.html
build.py
assets/maps/**
```

GitHub Actions 都会参与更新流程。

普通路线调整仍然建议：

```text
修改 data.xlsx
→ 上传 GitHub
→ Actions 自动生成 index.html
```

## 版本规则

- X：架构更新
- Y：功能更新
- Z：数据、样式、文案或 Bug 修复

本次新增地图 SVG 路线功能：

```text
v3.3.0 → v3.3.1
```
