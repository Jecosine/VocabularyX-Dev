<!--
 * @Date: 2021-02-15 13:52:55
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 01:39:01
-->
<template>
  <el-container>
    <el-header id="notebook-detail-header-container">
      <div class="toolbar">
        current notebook: {{$route.params["name"]}}
      </div>
    </el-header>
    <el-main id="notebook-detail-main-container">
      <div id="detail-main-wrapper">
        <div class="notebook-title">Title</div>
        <el-divider></el-divider>
        <div class="status-container">
          <list-view :listData="listData" :keyClass="'test-key-class'"/>
        </div>
        <div class="statistic-container">
          <el-tabs>
            <el-tab-pane class="overview-container" label="Overview">
              <!-- overview components -->
              <overview :data="[]" />
            </el-tab-pane>
            <el-tab-pane class="recent-week" label="Weekly">
              <!-- recent data in a week (time and word count) -->
            </el-tab-pane>
            <el-tab-pane class="recent-month" label="Monthly">
              <!-- recent data in a month (time and word count) -->
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
      
    </el-main>
  </el-container>
</template>

<script>
import ListView from './partial/ListView'
import Overview from './partial/Overview'
export default {
  components: {
    'list-view': ListView,
    'overview': Overview
  },
  data () {
    return {
      currentTab: 'status',
      listData: {
        '创建日期': 'test-value',
        '最近使用': 'test-value1',
        '总词汇量': 'test-value2',
        '已掌握': 'test-value2'
      }
    }
  },
  methods: {

  },
  mounted () {

  },
  created () {
    console.log(this.$route.params.name)
  }

}
</script>

<style scoped>
@import '../theme/base.css';
#notebook-detail-main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#detail-main-wrapper {
  position: relative;
  box-sizing: content-box;
  padding: 2rem;
  width: 70%;
  max-width: 60rem;
}
#notebook-detail-header-container {
  width: 100%;
  height: 5rem;
}
.notebook-title {
  font-size: 3rem;
  font-family: 'Palatino Linotype';
  font-weight: bolder;
  color: var(--color-primary);
  text-align: left;
  height: 4rem;
  line-height: 4rem;
}
.statistic-container {
  width: 100%;
  min-height: 30rem;
  background-color: #f7f7f7;
  box-sizing: content-box;
  overflow-x: scroll;
  padding: 1rem;
  margin: 1rem 0;
}
.toolbar {
  width: 100%;
  height: 4rem;
}
.status-container >>> .test-key-class {
  font-size: 1.1rem;
  width: 7rem;
  font-family: 'Noto Sans SC';
}
.statistic-container >>> .test-value-class {
  font-size: 1rem;
}
.overview-container {
  overflow-x: scroll;
}
</style>