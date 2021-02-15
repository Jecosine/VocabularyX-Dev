/*
 * @Date: 2021-02-15 14:19:19
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 02:17:13
 */
const {DataTypes} = require('sequelize')

const WordModel = {
  id: {
    type: DataTypes.TEXT,
    primaryKey: true
  },
  spell: DataTypes.TEXT,
  phonetic: DataTypes.TEXT,
  tip: DataTypes.TEXT,
  cn_source: DataTypes.TEXT,
  en_source: DataTypes.TEXT,
  notebookId: DataTypes.TEXT
}

const NotebookModel = {
  id: {
    type: DataTypes.TEXT,
    primaryKey: true
  },
  name: DataTypes.TEXT,
  author: DataTypes.TEXT
}
const UserModel = {
  id: {
    type: DataTypes.TEXT,
    primaryKey: true
  },
  total: DataTypes.INTEGER,
  name: DataTypes.TEXT
}

export default {WordModel, NotebookModel, UserModel}
