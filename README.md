# Overwatch Counter

当前版本：**v3.8.1**

## v3.8.1 修复

修复英雄详情页顶部头像被拉成长条的问题。

原因是 v3.8.0 中详情头像使用：

```text
hero-portrait detail
```

而页面主体本身已经存在：

```text
.detail
```

样式，其中包含较大的 `min-height` 和 `padding`，导致图片同时继承了详情面板样式。

本版已经把头像尺寸类改成：

```text
profile
```

并明确锁定：

- 桌面：72 × 72
- 手机：56 × 56
- `aspect-ratio: 1 / 1`
- `object-fit: cover`
- 禁止 flex 拉伸
- 清除额外 padding / margin

因此英雄详情顶部头像现在会保持正常的圆角方形比例。

## 版本

```text
v3.8.0 → v3.8.1
```
