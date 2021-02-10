/*
 * @Date: 2020-11-11 09:58:43
 * @LastEditors: Jecosine
 * @LastEditTime: 2020-11-11 11:07:09
 */
'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
    NODE_ENV: '"development"'
})
