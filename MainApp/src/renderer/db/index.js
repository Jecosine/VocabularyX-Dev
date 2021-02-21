/*
 * @Date: 2021-02-15 13:53:45
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 18:24:40
 */
const path = require('path')
const { Sequelize } = require('sequelize')
const { UserModel, NotebookModel, WordModel } = require('../models')
// create connection

const sequelize = new Sequelize(undefined, undefined, undefined, {
  host: 'localhost',
  dialect: 'sqlite',
  storage: (process.env.NODE_ENV === 'development') ? path.join(process.cwd(), './customData/test.db') : path.join(process.cwd(), './resources/customData/test.db')
})
console.log(`in db.js, dirname: ${__dirname}`)
// const User = sequelize.define('User', UserModel, {
//   tableName: 'user',
//   timestamps: false
// })
const Word = sequelize.define('Word', WordModel, {
  tableName: 'word',
  timestamps: false
})
const Notebook = sequelize.define('Notebook', NotebookModel, {
  tableName: 'notebook',
  timestamps: false
})
// const WordNotebook = sequelize.define('WordNotebook', {
//   id: {
//     type: DataTypes.TEXT,
//     primaryKey: true
//   },
//   word_id: {
//     type: DataTypes.TEXT,
//     references: {
//       model: Word,
//       key: 'id'
//     }
//   },
//   notebook_id: {
//     type: DataTypes.TEXT,
//     references: {
//       model: Notebook,
//       key: 'id'
//     }
//   }
// }, {
//   tableName: 'word_notebook',
//   timestamps: false
// })
Notebook.belongsToMany(Word, {
  through: 'word_notebook',
  timestamps: false,
  foreignKey: 'notebook_id'
})
Word.belongsToMany(Notebook, {
  through: 'word_notebook',
  timestamps: false,
  foreignKey: 'word_id'
})
// User.belongsToMany(Notebook, {
//   through: 'user_notebook',
//   timestamps: false,
//   foreignKey: 'user_id'
// })
// Notebook.belongsToMany(User, {
//   through: 'user_notebook',
//   timestamps: false,
//   foreignKey: 'notebook_id'
// })
// async function fc () {
//   const test1 = await Word.findOne({
//     where: {
//       spell: 'abandon'
//     },
//     include: Notebook
//   })
//   console.log(test1)
// }
// // fc()
export default sequelize
