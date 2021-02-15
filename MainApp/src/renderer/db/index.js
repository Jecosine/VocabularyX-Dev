/*
 * @Date: 2021-02-15 13:53:45
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-15 15:47:49
 */
const path = require('path')
const { Sequelize, DataTypes } = require('sequelize')
const { UserModel, NotebookModel, WordModel } = require('../models')
// create connection

const sequelize = new Sequelize(undefined, undefined, undefined, {
  host: 'localhost',
  dialect: 'sqlite',
  storage: path.join(__dirname, './test.db')
})
console.log(`in db.js, dirname: ${__dirname}`)
const User = sequelize.define('User', UserModel, {
  tableName: 'user'
})
const Word = sequelize.define('Word', WordModel, {
  tableName: 'word'
})
const Notebook = sequelize.define('Notebook', NotebookModel, {
  tableName: 'notebook'
})
const WordNotebook = sequelize.define('WordNotebook', {
  id: DataTypes.TEXT,
  wordId: {
    type: DataTypes.TEXT,
    references: {
      model: 'Word',
      key: 'id'
    }
  },
  notebookId: {
    type: DataTypes.TEXT,
    references: {
      model: 'Notebook',
      key: 'id'
    }
  }
})
Notebook.belongsToMany(Word, {
  through: WordNotebook
})
Word.belongsToMany(Notebook, {
  through: WordNotebook
})

async function fc () {
  const test1 = await Word.findOne({
    where: {
      spell: 'abandon'
    },
    include: Notebook
  })
  console.log(test1)
}
fc()
export default { sequelize, User, Word, Notebook }
