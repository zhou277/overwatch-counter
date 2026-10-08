# 地图底图

把地图底图放在这个目录，例如：

```text
assets/maps/国王大道.png
assets/maps/直布罗陀.png
```

然后在 `data.xlsx` 的 `maps` Sheet 中，把对应地图的 `image_path` 填成：

```text
assets/maps/国王大道.png
```

路线本身不要画进图片里，而是在 `map_routes` Sheet 维护 SVG 坐标。

## 坐标系统

路线坐标使用百分比坐标：

- 左上角：`0,0`
- 右上角：`100,0`
- 左下角：`0,100`
- 右下角：`100,100`

例如：

```text
8,78;25,65;44,58;68,42;90,25
```

表示路线依次经过 5 个点。
