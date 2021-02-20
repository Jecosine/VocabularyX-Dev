<!--
 * @Date: 2021-02-20 18:27:52
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 18:36:09
-->
<template>
  <el-container id="reader-container">
    <el-main id="reader-main">
      <Word word="currentWord"/>
    </el-main>
    <el-aside id="reader-aside">
      
    </el-aside>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      currentWord: ''
    }
  },
  methods: {},
  mounted () {
    // todo render aside catalog
    // ...
    // test
  },
  created () {
    // todo get last record
    // ...
  }
}
</script>

<style scoped>
#reader-container {
  width: 100%;
  height: 100%;
}
#reader-main {
  background-color: aqua;
  padding: 0;
  margin: 0;

}
#reader-aside {
  background-color: beige;
}
</style>