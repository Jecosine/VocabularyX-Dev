<!--
 * @Date: 2021-02-11 11:20:04
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 15:51:57
-->
# 快捷呼出命令支持

## 前言

需要加上`/`作为命令的开始

## 视图类

### `route`

#### 描述

定位到特定的视图

#### 语法

```
/route -p <page-url> -o [options]
```

#### 样例 

跳转到笔记本页

```
/route -p notebook
```

跳转到特定笔记本

```
/route -p notebook/<notebook-name>
```
### 页面名称汇总

|Name|Description |
|-|-|
|`notebook`|笔记本
|`recent`|欢迎页
|`settings`|设置页
|`manual`|手册页
|`about`|关于软件

###

## `notebook`


单词本相关命令


## `setting`

### 视图设置

#### 设置主题

```bash
/set theme <theme-name>
```

