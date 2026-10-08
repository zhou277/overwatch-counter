# Overwatch Counter

当前版本：**v3.4.0**

## v3.4.0：自动下载并本地化实际俯视图

本版把实际地图图片处理改成自动流程：

```text
公开俯视图资源
→ prepare_map_assets.py 下载到临时内存
→ Pillow 加入来源署名条
→ 生成本地派生 PNG
→ 保存到 assets/maps/real/
→ build.py 生成网页
→ GitHub Actions 自动提交 PNG + index.html
```

这样网页最终加载的是仓库自己的本地图片，不再依赖图片热链。

## 已批量接入实际俯视图

当前使用 StatBanana / Coggle 明确给出使用条件的资源，共 **14 张当前项目地图**：

```text
国王大道
直布罗陀
66号公路
渣客镇
多拉多
里阿尔托
艾兴瓦尔德
努巴尼
好莱坞
伊利奥斯
漓江塔
尼泊尔
釜山
绿洲
```

这些图片不会原样保存。`prepare_map_assets.py` 会在底部加入来源署名，生成项目使用的派生文件。

来源：

```text
https://overwatch.statbanana.com/images
```

StatBanana 的公开说明要求：免费用途、不要原样重新分发，并保留 Logo 或注明来源。

## OW2 新地图

以下当前项目地图暂时继续使用 v3.3.1 的战术示意底图：

```text
皇家赛道
哈瓦那
中城
新皇后街
斗兽场
埃斯佩兰萨
苏拉瓦萨
新渣客城
阿特利斯
霓虹交汇点
```

原因不是技术问题，而是目前没有为这些地图统一找到和 StatBanana 一样、**使用条件清晰且适合直接纳入 GitHub 项目**的实际俯视图资源。

我没有用版权状态不明的搜索结果冒充可自由打包资源。

## GitHub 使用

上传完整项目后，Actions 会执行：

```text
pip install openpyxl pillow
python prepare_map_assets.py
python build.py
```

并提交：

```text
assets/maps/real/*.png
index.html
```

第一次 Action 成功后，你的仓库里会真正出现例如：

```text
assets/maps/real/kings-row.png
assets/maps/real/gibraltar.png
assets/maps/real/dorado.png
...
```

之后网页会直接读这些本地文件。

## 地图数据字段

`maps` Sheet 现在包括：

```text
image_path
image_credit
image_source
image_aspect
image_fallback
asset_status
asset_provider
```

`asset_status` 可以直接看到该地图目前是：

```text
自动下载实际俯视图
```

还是：

```text
保留战术示意图
```

## 版本规则

本次增加自动素材获取、派生处理、Actions 集成，属于功能级更新：

```text
v3.3.5 → v3.4.0
```
