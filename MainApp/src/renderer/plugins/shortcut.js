/*
 * @Date: 2021-02-14 11:24:15
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-14 11:30:25
 */
import keymaster from 'keymaster'
// import Vue from 'vue'

const bindKeyHandler = f => {
  return () => {
    f()
    return false
  }
}

export const shortcut = {
  bind: (seed, func) => keymaster(seed, bindKeyHandler(func)), ...keymaster
}
