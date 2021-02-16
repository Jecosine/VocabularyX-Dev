/*
 * @Date: 2021-02-16 12:53:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 13:00:19
 */
const state = {
  theme: 'default'
}

const mutations = {
  SET_THEME (state, theme) {
    state.theme = theme
  }
}

const actions = {
  setTheme ({ commit }, theme) {
    console.log(`Set current theme to ${theme}`)
    commit('SET_THEME', theme)
  }
}

export default {
  state,
  mutations,
  actions
}
