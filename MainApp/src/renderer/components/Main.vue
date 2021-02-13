<!--
 * @Date: 2021-02-03 07:02:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-13 11:26:34
-->
<template>
  <el-container id="main-container">
    <el-header id="navigation-container" height="2.25rem">
      <div class="navigation-wrapper">
        <titlebar :title="title" :height="'2.25rem'" />
      </div>
      <div id="command-container" v-show="false">
        <div id="command-wrapper">
          <div id="command-box">
            <el-input id="command-input" style="fontFamily:'Fira Code'" v-model="command"></el-input>
          </div>
        </div>
      </div>
    </el-header>
    <el-container>
      <el-aside width="4.25rem" id="side-container">
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'recent'
          }"
          @click="openMenu('recent')"
        >
          <font-awesome-icon :icon="['fas', 'home']"></font-awesome-icon>
        </div>
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'notebook'
          }"
          @click="openMenu('notebook')"
        >
          <font-awesome-icon :icon="['fas', 'atlas']"></font-awesome-icon>
        </div>
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'search'
          }"
          @click="openMenu('search')"
        >
          <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
        </div>
      </el-aside>
      <el-container>
        <el-main id="content-main">
          <router-view />
        </el-main>
        <el-footer id="footer-container" height="1.125rem"></el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
export default {
  components: {
    titlebar: require('@/components/partial/Titlebar').default
  },
  data () {
    return {
      title: 'VocabularyX',
      currentMenu: 'recent',
      command: ''
    }
  },
  methods: {
    openMenu (name) {
      if (this.currentMenu !== name) {
        this.$router.push({ name: name })
        this.currentMenu = name
      }
    }
  }
}
</script>

<style scoped>
@import '../theme/base.css';

#main-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
}

#navigation-container {
  width: 100%;
  height: 2rem;
  padding: 0;
  background-color: #e7e7e7;
}
#side-container {
  /* height: calc(100vh - 2rem); */
  background-color: var(--color-primary);
  position:relative;
}
#command-container {
  position: absolute;
  left: 0;
  width: 100%;
  height: 3.2rem;
  background-color: transparent;
  display: flex;
  flex-direction: column;
  align-items: center;  
}
#command-wrapper {
  box-sizing: content-box;

  padding: 0.1rem 0.5rem;
  width: 33%;
  height: 3.2rem;
  background-color: #e7e7e7;
  box-shadow: 0 0.1rem 0.1rem 0.1rem rgba(0,0,0,0.16);
  line-height: 100%;
}
#command-box {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 100%;
}
#command-input.el-input__inner {
  font-family: 'Fira Code';
}
.navigation-wrapper {
  width: calc(100% - 2.25rem);
  padding: 0 1.125rem;  
}
#footer-container {
  background-color: #e7e7e7;
}
.menu-button {
  box-sizing: content-box;
  /* padding: 0 0.1rem; */
  width: 4.15rem;
  height: 4.25rem;
  text-align: center;
  border-width: 0 0 0 0.1rem;
  border-style: solid;
  border-color: transparent;
  line-height: 4.25rem;
  font-size: 2rem;
  color: var(--color-menu-unselected);
}
.menu-button-selected {
  box-sizing: content-box;
  border-color: #e7e7e7;
  color: var(--color-menu-selected);
  transition: none;
}
</style>
