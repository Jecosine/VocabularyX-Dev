# 开发日志

## 构建环境

## 项目需求

- 要好康
- 要好康！
- 要好康！！！

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