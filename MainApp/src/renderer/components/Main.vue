<!--
 * @Date: 2021-02-03 07:02:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-06 23:53:06
-->
<template>
  <el-container id="main-container">
    <el-header id="navigation-container" height="4rem">
      <titlebar :title="title" :height="'2rem'" />
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
  background-color: #114514;
}

</style>