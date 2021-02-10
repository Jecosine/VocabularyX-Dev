<!--
 * @Date: 2021-02-06 21:16:20
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 10:26:58
-->
<template>
  <div id="title-container" :style="{'height': height, 'lineHeight': height}">
    <div class="title-text" :style="{'lineHeight': height}">
      <font-awesome-icon :icon="['fab', 'artstation']" class="title-icon"></font-awesome-icon>
      <div class="title-self">{{ title }}</div>      
    </div>
    <div class="title-button-group" :style="{'height': height}">
      <div id="button-minimize" class="window-button" :style="{'width': height, 'height': height}">
        <!-- <font-awesome-icon :icon="['far','window-minimize']"></font-awesome-icon> -->
        <i class="el-icon-minus"></i>

      </div>
      <div id="button-maximum" class="window-button" :style="{'width': height, 'height': height}">
        <!-- <font-awesome-icon :icon="['far','square']"></font-awesome-icon> -->
        <i class="el-icon-upload2"></i>

      </div>
      <div id="button-close" class="window-button" :style="{'width': height, 'height': height}">
        <!-- <font-awesome-icon :icon="['fas','times']"></font-awesome-icon> -->
        <i class="el-icon-close"></i>
      </div>
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
.title-button-group {
  position: absolute;
  display: flex;
  top: 0;
  right: -1.125rem;
}
.title-icon,
.title-self {
  display: inline-block;
  line-height: 100%;
  color: var(--color-primary);
}
.title-self {
  margin-left: 1rem;
}
.window-button {
  display: inline-block;
  position: relative;
  height: 100%;
  text-align: center;
  /* line-height: 100%; */
  color: var(--color-primary);
}
.window-button:hover {
  background-color: var(--color-primary-secondary);
}
#button-close {
  font-weight: 800;
  font-size: 18px;
}
</style>