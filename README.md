# Overwatch Counter

当前版本：**v3.6.1**

## v3.6.1 更新

克制查询布局调整：

之前：

```text
坦克 | 输出 | 辅助
```

三列并排。

现在改为三个横向区域：

```text
坦克克制  ─────────────────────
          Top1   Top2   Top3

输出克制  ─────────────────────
          Top1   Top2   Top3

辅助克制  ─────────────────────
          Top1   Top2   Top3
```

桌面端每个位置占满详情区域宽度，Top 3 在该横条内横向排列。

手机端仍然自动改成单列，避免文字过窄。

## v3.6.0 更新

地图功能重新简化：**取消地图图片、俯视图和进攻路线，只保留阵容建议。**

地图详情现在只显示：

- 地图名称
- 地图模式 / 风格
- 坦克推荐
- 输出推荐
- 辅助推荐
- 参考阵容
- 阵容思路

## 为什么取消地图路线功能

实际俯视图存在图片体积大、GitHub 上传和网页加载成本高、不同地图素材许可不统一，以及路线坐标需要持续校准等问题。

因此从 v3.6.0 开始，地图页重新聚焦在最实用的信息：

```text
这张地图适合什么英雄
+
推荐什么阵容
+
为什么推荐这套阵容
```

## Excel

`maps` Sheet 重新精简为 A:O：

```text
order
name
mode
style
tank1
tank2
tank3
dps1
dps2
dps3
support1
support2
support3
composition
reason
```

之前的图片和路线相关字段不再使用。

`map_routes` 和 `route_help` Sheet 仅留下停用说明，避免旧文件兼容时产生误解。

## 项目清理

本版删除：

```text
assets/maps/
map_assets.json
prepare_map_assets.py
```

GitHub Actions 也移除了地图图片下载和 Pillow 依赖。

之后的自动构建重新恢复为：

```text
data.xlsx
→ build.py
→ index.html
```

## 版本规则

这次移除一整套地图图片 / 路线功能并重新简化地图页面，属于功能级调整：

```text
v3.5.0 → v3.6.0
```
