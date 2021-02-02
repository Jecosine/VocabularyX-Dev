# Vite + Vue3 + Electron

记一次 Vite + Vue3 + Electron 的构建经历

本文假定你已经安装好了 node 环境, 如果还没准备好或者不知道是什么请先去网上别的资料补课

## 使用 Vite 创建新 App


## 安装 Electron 到项目目录

## 调整项目结构

```
Project
├─node_modules    依赖包目录
├─script          工具脚本(编译,启动,签名等)
├─public          Vite 项目自带目录
├─src
│  ├─main         Electron 目录
│  ├─render       Vue3 目录
│  └─common       两个进程的公共源码资源
├─index.html      Vue3 入口
├─package.json    项目配置文件
├─...
```
