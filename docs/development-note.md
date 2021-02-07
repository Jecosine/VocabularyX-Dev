# 开发日志

## 构建环境

## 项目需求

- 主要需求
  - 要好康
  - 要好康！
  - 要好康！！！
- 自动生成练习
  - 选择题(基于单词相似度, 词根, 词形 | 单词的各种时态变形)
  - 填空题(基于在线例句, 可能存在多解问题?)
  - 单词听写
  - 错词记录 (分单词本)
- 词汇背诵方式支持
  - 在背诵模式中选择遮掩释义等
  - 或者根据释义默写对应单词
  - 单词本差集计算
  - ...
- 单词学习
  - 页面
    - 单词读音播放 (英/美)
    - 基本释义
    - 记忆法
    - 词根
    - 单词形式变化 (名词是否可数 动词各个时态 对应形容词副词)
  - 机制
    - ~~`ptt`计算~~
    - 单词本完成度模型
    - 学习计划生成/调整 (如设定每日计划, 短期计划等)
- 其他功能
  - 学习时长等统计信息
  - 可迁移用户设置, 拷贝用户文件后, 在其他端也可以同步使用
  - 主题切换, 添加背景图~~分散注意力~~
- 进阶功能
  - 可私有化部署 (部署到服务器上, 局域网内部共同学习, 多端同步, 或者可以部署为Github App)

## 技术栈

- 核心
  - Vue 2.x
  - Electron
- 前端框架
  - Element UI
  - FontAwesome
- 数据库操作
  - Sequelize
  - Sqlite3

## Installation

### Element UI

```bash
npm i element-ui -S
```

### Babel Import

```bash
npm install babel-plugin-component -D
```

route/index.js

```javascript
import { Button, Select } from 'element-ui'

Vue.use(Button)
Vue.use(Select)
```

### Multi-theme

Install sass

```bash
npm install --save-dev sass-loader
npm install --save-dev node-sass
```

webpack.base.conf.js


```js
test: /\.sass$/,
loaders: ['style', 'css', 'sass']
```

Install element ui theme tools

```bash
npm i element-theme -g
npm i element-theme-chalk -D
```