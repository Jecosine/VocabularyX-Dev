/*
 * @Date: 2021-02-15 09:17:01
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-15 13:43:34
 */

import {parser} from 'parser'

export const cmd = {
  bind: (command, func) => {
    // todo
    console.log('test1')
  },
  parse: (raw) => {
    return parser.parse(raw)
  },
  execute: (context, raw) => {
    // todo
    console.log(`try parsing command ${raw}`)
    this.run(context, this.parse(raw))
  },
  run: (context, func) => {
    func(context)
  }
}
