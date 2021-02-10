<!--
 * @Date: 2021-02-03 07:02:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 13:12:44
-->
<template>
  <el-container id="main-container">
    <el-header id="navigation-container" height="2.25rem">
      <div class="navigation-wrapper">
        <titlebar :title="title" :height="'2.25rem'" />
      </div>
    </el-header>
    <el-container>
      <el-aside width="4.25rem" id="side-container">
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'home'
          }"
          @click="openMenu('home')"
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
      currentMenu: 'home'
    }
  },
  methods: {
    openMenu (name) {
      if (this.currentMenu !== name) {
        this.$router.push({ name: 'notebook' })
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
}
.navigation-wrapper {
  width: calc(100% - 2.25rem);
  padding: 0 1.125rem;
}
#footer-container {
  background-color: #e7e7e7;
}
.menu-button {
  box-sizing: border-box;
  /* padding: 0 0.1rem; */
  height: 4.25rem;
  text-align: center;
  line-height: 4.25rem;
  font-size: 2rem;
  color: var(--color-menu-unselected);
}
.menu-button-selected {
  box-sizing: border-box;
  border-width: 0 0 0 0.1rem;
  border-color: #e7e7e7;
  border-style: solid;
  color: var(--color-menu-selected);
}
</style>
