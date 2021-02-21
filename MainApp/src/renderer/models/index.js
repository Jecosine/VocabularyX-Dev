/*
 * @Date: 2021-02-15 14:19:19
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 20:55:46
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
  cn_etym: DataTypes.TEXT,
  en_etym: DataTypes.TEXT,
  word_forms: DataTypes.TEXT,
  audio_sources: DataTypes.TEXT,
  raw: DataTypes.TEXT,
  parsed: DataTypes.INTEGER,
  notebookId: DataTypes.TEXT
}

const NotebookModel = {
  id: {
    type: DataTypes.TEXT,
    primaryKey: true
  },
  name: {
    type: DataTypes.TEXT
  },
  // author: {
  //   type: DataTypes.TEXT
  // },
  count: {
    type: DataTypes.INTEGER
  }
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
