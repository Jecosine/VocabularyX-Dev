/*
 * @Date: 2021-02-17 12:23:04
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-17 17:29:31
 */
export default class extends Error {
  constructor (message) {
    super(message)
    this.message = message
    this.name = 'CommandParseException'
    this.scope = 'Command'
  }
}
// export default CommandParseException
