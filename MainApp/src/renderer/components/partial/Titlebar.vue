<!--
 * @Date: 2021-02-06 21:16:20
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-06 21:44:06
-->
<template>
  <div id="title-container" :style="{'height': height, 'lineHeight': height}">
    <div class="title-text" :style="{'lineHeight': height}">{{ title }}</div>
    <div class="title-text">- 0 x</div>
  </div>
</template>

<script>
export default {
  name: 'title-bar',
  props: [
    'title',
    'height'
  ]
}
</script>

<style scoped>
@import '../../theme/base.css';

#title-container {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: space-between;
  background-color: aqua;
}
.title-text {
  display: inline-block;
  height: 100%;
  font-size: 14px;
  color: var(--color-text-primary);
}
</style>