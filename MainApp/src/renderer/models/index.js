/*
 * @Date: 2021-02-15 14:19:19
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-15 15:46:22
 */
const {DataTypes} = require('sequelize')

const WordModel = {
  id: DataTypes.TEXT,
  spell: DataTypes.TEXT,
  phonetic: DataTypes.TEXT,
  tip: DataTypes.TEXT,
  cn_source: DataTypes.TEXT,
  en_source: DataTypes.TEXT,
  notebookId: DataTypes.TEXT
}

const NotebookModel = {
  id: DataTypes.TEXT,
  name: DataTypes.TEXT,
  author: DataTypes.TEXT
}
const UserModel = {
  id: DataTypes.TEXT,
  total: DataTypes.INTEGER,
  name: DataTypes.TEXT
}

export default {WordModel, NotebookModel, UserModel}
