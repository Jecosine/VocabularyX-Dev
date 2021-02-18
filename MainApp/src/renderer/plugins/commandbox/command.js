/*
 * @Date: 2021-02-15 09:17:01
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-18 12:30:11
 */

import exceptions from '../../exceptions'
import parser from './parser'
const mapper = {}
const cmdParser = parser
const command = {
  bind: (cmd, func, config) => {
    // todo
    console.log('In bind')
    mapper[cmd] = {
      function: func,
      configuration: config
    }
  },
  parse: (raw) => {
    return cmdParser.parse(raw, mapper)
  },
  execute: (raw) => {
    // todo
    console.log(`try parsing command ${raw}`)
    let commandData
    try {
      commandData = command.parse(raw)
    } catch (e) {
      return {
        status: -1,
        msg: e
      }
    }
    console.log(`in commandjs ${commandData}`)
    let principal = commandData.name
    let fn = mapper[principal].function
    try {
      fn(commandData)
    } catch (e) {
      return {
        status: -2,
        msg: e
      }
    }
  },
  run: (task) => {
    task.func(task.opts)
  }
}

export default command
