<!--
 * @Date: 2021-02-03 07:02:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 09:44:06
-->
<template>
  <el-container id="main-container">
    <el-header id="navigation-container" height="2.25rem">
      <div class="navigation-wrapper">
        <titlebar :title="title" :height="'2.25rem'" />
      </div>
    </el-header>
    <el-main id="content-main"></el-main>
  </el-container>
</template>

<script>
export default {
  components: {
    titlebar: require('@/components/partial/Titlebar').default
  },
  data () {
    return {
      title: 'VocabularyX'
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
.navigation-wrapper {
  width: calc(100% - 2.25rem);
  padding: 0 1.125rem;
}
</style>