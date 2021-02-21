<!--
 * @Date: 2021-02-20 18:27:52
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-21 16:54:42
-->
<template>
  <el-container id="reader-container">
    <el-main id="reader-main">
      <Word word="currentWord"/>
      <div id="unfold-button"></div>
      <div id="reader-aside" v-show="unfold">
        <font-awesome-icon :icon="['fas',unfold ? 'arrow-right' : 'arrow-right']"></font-awesome-icon>
      </div>
      <!-- catalog -->
      

    </el-main>
    
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      currentWord: '',
      unfold: true
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
#unfold-button {
  width: 0.5rem;
  height: 5rem;

}
#reader-aside {
  width: 10rem;
  height: 100%;
  background-color: beige;
}
</style>