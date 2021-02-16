<!--
 * @Date: 2021-02-06 20:56:48
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 10:37:38
-->
<template>
  <el-container>
    <el-header id="notebook-header-container">
      <div class="notebook-toolbar-container">
        <div class="toolbar-wrapper">
          <el-button-group>
            <el-button type="primary" size="mini"
              ><font-awesome-icon :icon="['fas', 'list']"></font-awesome-icon
            ></el-button>
            <el-button type="primary" size="mini"
              ><font-awesome-icon
                :icon="['fas', 'th-large']"
              ></font-awesome-icon
            ></el-button>
          </el-button-group>
        </div>
      </div>
    </el-header>
    <el-main>
      <div id="notebook-list-container">
        <div
          class="notebook-item-container"
          v-for="(item, i) in notebookData"
          :key="i"
        ></div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      notebookData: []
    }
  },
  mounted () {},
  async created () {
    // get notebook data
    window.routerApp = this
    this.notebookData = await this.$db.models.Notebook.findAll({
      attributes: ['*']
    })
    this.$nextTick(() => {
      console.log(this.notebookData)
    })
  }
}
</script>

<style scoped>
@import '../theme/base.css';
#notebook-header-container {
  padding: 0;
}
.notebook-toolbar-container {
  width: 100%;
  height: 2.4rem;
  background-color: aliceblue;
  line-height: 2rem;
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
</style>
