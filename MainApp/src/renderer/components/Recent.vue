<!--
 * @Date: 2021-02-10 15:06:46
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 15:26:45
-->
<template>
  <el-container>
    <el-header>
      <div id="recent-header">
        Recent
      </div>
    </el-header>
    <el-main>
      <el-row :gutter="20">
        <el-col :span="12" id="recent-notebook">

        </el-col>
        <el-col :span="12" id="shortcut-operation">
    
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      recentNote: [
        {
          name: 'Test Notebook 1',
          id: 'sadadafe',
          statistic: {
            recent: 3,
            total: 114,
            mastered: 20
          }
        },
        {
          name: 'Test Notebook 4',
          id: 'sadadaff',
          statistic: {
            recent: 3,
            total: 114,
            mastered: 20
          }
        },
        {
          name: 'Test Notebook 3',
          id: 'sadadafa',
          statistic: {
            recent: 3,
            total: 114,
            mastered: 20
          }
        }
      ]
    }
  },
  methods: {

  },
  created () {
    // get recent notebook data
    // ...

  }
}
</script>

<style scoped>
@import '../theme/base.css';

#recent-header {
  font-size: 3rem;
  font-weight: bolder;
  color: var(--color-text-regular);
}

#recent-notebook {
  width: 100%;
  min-height: 4rem;
  background-color: var(--color-primary-secondary);
}

</style>