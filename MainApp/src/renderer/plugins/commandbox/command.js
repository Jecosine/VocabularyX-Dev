/*
 * @Date: 2021-02-15 09:17:01
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-18 11:21:10
 */

import parser from './parser'
const mapper = {}
const cmdParser = parser
const command = {
  bind: (cmd, func) => {
    // todo
    console.log('In bind')
    mapper[cmd] = func
  },
  parse: (raw) => {
    return cmdParser.parse(raw)
  },
  execute: (raw) => {
    // todo
    console.log(`try parsing command ${raw}`)
    let commandData = command.parse(raw)
    console.log(`in commandjs ${commandData}`)
    let reg = /\/(\w+)/
    let principal = raw.match(reg)[1]
    let fn = mapper[principal]
    fn(commandData)
  },
  run: (task) => {
    task.func(task.opts)
  }
}

export default command
