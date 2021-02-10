<!--
 * @Date: 2021-02-06 21:16:20
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 09:38:53
-->
<template>
  <div id="title-container" :style="{'height': height, 'lineHeight': height}">
    <div class="title-text" :style="{'lineHeight': height}">
      <font-awesome-icon :icon="['fab', 'artstation']" class="title-icon"></font-awesome-icon>
      <div class="title-self">{{ title }}</div>      
    </div>
    <div class="title-button-group">
      <div id="button-minimize">
        <font-awesome-icon :icon="['fas','user']"></font-awesome-icon>
      </div>
      <div id="button-maximum"></div>
      <div id="button-close"></div>
    </div>
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
  background-color: #e7e7e7;
}
.title-text {
  display: inline-block;
  height: 100%;
  font-size: 14px;
  color: var(--color-text-primary);
}
.title-icon,
.title-self {
  display: inline-block;
  line-height: 100%;
  color: var(--color-primary);
}
</style>