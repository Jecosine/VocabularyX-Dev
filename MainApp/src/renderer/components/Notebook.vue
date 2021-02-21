<!--
 * @Date: 2021-02-06 20:56:48
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 20:31:00
-->
<template>
  <el-container>
    <el-header id="notebook-header-container" height="2.4rem">
      <div class="notebook-toolbar-container">
        <div class="toolbar-wrapper">
          <el-button-group>
            <el-button
              @click="triggerListView"
              :type="isListView ? 'primary' : 'plain'"
              size="mini"
              ><font-awesome-icon :icon="['fas', 'list']"></font-awesome-icon
            ></el-button>
            <el-button
              @click="triggerGridView"
              :type="!isListView ? 'primary' : 'plain'"
              size="mini"
              ><font-awesome-icon
                :icon="['fas', 'th-large']"
              ></font-awesome-icon
            ></el-button>
          </el-button-group>
        </div>
      </div>
    </el-header>
    <el-main id="notebook-main-container">
      <div id="main-wrapper">
        <div
        id="notebook-list-container"
        :class="{
          'notebook-list-container-list': isListView,
          'notebook-list-container-grid': !isListView,
          'notebook-list-container': true
        }"
      >
        <div
          :class="{
            'notebook-item-container-list': isListView,
            'notebook-item-container-grid': !isListView,
            'notebook-item-container': true
          }"
          v-for="(item, i) in notebookData"
          :key="i"
        >
          <el-row :gutter="20">
              <el-col :span="14">
                <div class="notebook-item-title">
                  <font-awesome-icon :icon="['fas', 'book']"></font-awesome-icon> 
                  <div class="text-container">{{ item.name }}</div>
                </div>
              </el-col>
              <el-col :span="10">
                <div class="notebook-item-content">            
                  <el-progress
                    type="circle"
                    class="progress-circle"
                    :width="50"
                    color="#7190aa"
                    stroke-linecap="butt"
                    :stroke-width="10"
                    :show-text="false"
                    :percentage="
                      getPercentage(100, 140)
                    "
                  ></el-progress>
                </div>
              </el-col>
            </el-row>
        </div>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      notebookData: [],
      isListView: true // load from database
    }
  },
  methods: {
    getPercentage (a, b) {
      return b === 0 ? 0 : (a / b).toFixed(2) * 100
    },
    progressFormat (a, b) {
      return `${a} / ${b}`
    },
    triggerListView () {
      this.isListView = true
    },
    triggerGridView () {
      this.isListView = false
    }
  },
  mounted () {},
  async created () {
    // get notebook data
    window.routerApp = this
    this.notebookData = await this.$db.models.Notebook.findAll({attributes: ['id', 'name']})
    this.$nextTick(() => {
      console.log(this.notebookData)
      this.notebookData = JSON.parse(JSON.stringify(this.notebookData))
    })
  }
}
</script>

<style scoped>
@import '../theme/base.css';
#notebook-header-container {
  padding: 0;
  height: 2.4rem;
}
#notebook-main-container {
  height: calc(100vh - 2.4rem - 2.25rem - 2.125rem);
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.notebook-toolbar-container {
  width: 100%;
  height: 2.4rem;
  background-color: aliceblue;
  line-height: 2rem;
}

/* container  */
.notebook-list-container {
  display: flex;
  align-items: center;
}
.notebook-list-container-list {
  flex-direction: column;
}
.notebook-list-container-grid {
  flex-direction: row;
  flex-wrap: wrap;
}
/* item */
.notebook-item-container {
  margin: 1rem;
  min-width: 2rem;
  height: 12rem;
  border-radius: 0.1rem;
  /* box-shadow: 0 0 0.1rem 0.1rem rgba(0, 0, 0, 0.1); */
}
.notebook-item-container-list  >>> .el-col {
  height: 100%;
}
.notebook-item-container-list  >>> .el-row {
  width: 100%;
  height: 100%;
}
.notebook-item-container-list {
  display: flex;
  flex-direction: row;
  align-items: center;
  box-sizing: border-box;
  background-color: aliceblue;
  width: 100%;
  height: 5rem;
  padding: 1rem;
  margin: 0.2rem;
}
.notebook-item-container-grid {
  background-color: aliceblue;
  width: 9rem;
}
.notebook-item-content {
  height: 5rem;
}
.notebook-item-title {
  height: 3rem;
  line-height: 3rem;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.notebook-item-title .text-container {
  margin-left: 1rem;
  color: var(--color-primary);
}
.toolbar-wrapper {
  float: right;
  width: 10rem;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  line-height: 100%;
  /* background-color: aqua; */
}
#main-wrapper {
  box-sizing: content-box;
  width: 70%;
  max-width: 60rem;
  padding: 2rem;
}
</style>
