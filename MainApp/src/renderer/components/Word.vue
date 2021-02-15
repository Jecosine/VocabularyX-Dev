<!--
 * @Date: 2021-02-15 09:21:07
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-15 10:34:57
-->
<template>
  <div id="word-main-container">
    <div class="wrapper">
      <div class="word-title">{{wordData.spell}}</div>
      <el-divider></el-divider>
      <div class="word-pron-container" v-if="wordData.phonetic && wordData.phonetic.length">
        <div class="word-pron">
          <div class="pron-text">
            美&nbsp;&nbsp;&nbsp;&nbsp;[{{wordData.phonetic[0]}}]
          </div>
          <div class="audio-source">
              <font-awesome-icon :icon="['fas', 'volume-up']"></font-awesome-icon>
          </div>
        </div>
        <div class="word-pron" v-if="wordData.phonetic.length > 1">
          <div class="pron-text">
            英&nbsp;&nbsp;&nbsp;&nbsp;[{{ wordData.phonetic.length > 1 ? wordData.phonetic[0]: '' }}]
          </div>
          <div class="audio-source">
            <!-- <el-button size="mini" round> -->
              <font-awesome-icon :icon="['fas', 'volume-up']"></font-awesome-icon>
            <!-- </el-button> -->
          </div>
        </div>
      </div>
      <div class="word-definition-container">
        <div class="word-section-title">
          Definition
        </div>
        <ul class="word-section-content">
          <li class="word-definition-item" v-for="(item, i) in wordData.pos" :key="i">
            <el-tag size="mini" class="word-definition-tag" :color="colorMap[item.type] || '#909399'">{{item.type}}.</el-tag> 
            <div class="word-definition-text">{{item.definition}}</div>
          </li>
        </ul>
      </div>
      <div class="word-mem"></div>
      
    </div>
  </div>
</template>

<script>
const colorMap = {
  'noun': '#E6A23C',
  'verb': '#F56C6C',
  'adj': '#67C23A',
  'adv': '#6344ab'

}
export default {
  data () {
    return {
      colorMap: colorMap,
      wordData: {
        spell: 'abandon',
        phonetic: ['əˈbændən', 'əˈbændən'],
        pos: [
          {
            type: 'noun',
            definition: '放任，狂热'
          },
          {
            type: 'verb',
            definition: '遗弃；离开；放弃；终止；陷入'
          }
        ],
        mem_help: 'mem help here',
        cn_source: 'cn source here',
        en_source: 'en source here'
      }
    }
  },
  methods: {},
  mounted () {

  },
  created () {
    // request word data
  }
}
</script>

<style scoped>
@import '../theme/base.css';

#word-main-container {
  /* position: absolute; */
  display: flex;
  /* width: 100%; */
  flex-direction: column;
  align-items: center;
  /* background-color: antiquewhite; */
}

.wrapper {
  position: relative;
  box-sizing: content-box;
  padding: 2rem;
  width: 70%;
  max-width: 60rem;
  /* background-color: aliceblue; */
}

.word-title {
  font-family: 'Palatino Linotype';
  font-size: 3rem;
  font-weight: bolder;
  color: var(--color-text-primary);
  text-align: left;
}
.word-pron {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 2rem;
  line-height: 2rem;
  font-size: 1.1rem;
  /* font-weight: bold; */
  color: var(--color-text-secondary);
  font-family: 'Palatino Linotype', 'Noto Sans SC';
}
.pron-text {
  font-family: 'Palatino Linotype', 'Noto Sans SC';
  margin-right: 1rem;
}
.word-section-title {
  margin: 1.5rem 0 0.5rem 0;
  height: 2rem;
  line-height: 2rem;
  font-size: 1.4rem;
  color: var(--color-text-regular);
  font-weight: bold;
}
.word-definition-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 2rem;
}
.word-definition-tag {
  position: absolute;
  color: white;
  margin-right: 0.5rem;
}
.word-definition-text {
  padding-left: 4rem;
}
.audio-source {
  cursor: pointer;
  transition: color 0.1s;
}
.audio-source:hover {
  color: var(--color-text-primary);  
}
</style>