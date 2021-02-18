/*
 * @Date: 2021-02-18 11:30:31
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-18 11:33:11
 */
export default class extends Error {
  constructor (message) {
    super(message)
    this.message = message
    this.name = 'CommandExecuteException'
    this.scope = 'Command'
  }
}
