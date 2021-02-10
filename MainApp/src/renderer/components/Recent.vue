<!--
 * @Date: 2021-02-10 15:06:46
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 17:11:01
-->
<template>
  <el-container>
    <el-header>
      <div id="recent-header">
        Recent
      </div>
    </el-header>
    <el-main>
      <el-row class="main-row" :gutter="20">
        <el-col :span="6">
          <div id="recent-notebook" class="main-col">
            <el-card 
              shadow="hover" 
              :body-style="{
                'borderRadius': '0.2rem'
              }"
              v-for="(item, i) in recentNote"
              :key="i"
              class="recent-note-card"
              >
              <el-row>
                <el-col :span="18">
                  <div class="notebook-title">
                    {{item.name}}
                  </div>
                  <div class="notebook-statistic">
                    <div>
                      Current: <span class="highlight-word">{{ item.statistic.recent }}</span>
                    </div>
                    <div>
                      Words: <span class="highlight-word">{{ item.statistic.mastered }} / {{ item.statistic.total }}</span>
                    </div>
                  </div>
                </el-col> 
                <el-col :span="6" class="progress-circle-container">
                  <div>
                    <el-progress 
                      type="circle" 
                      class="progress-circle" 
                      :width="60"
                      color="#1F4767"
                      stroke-linecap="butt"
                      :show-text="false"
                      :percentage="getPercentage(item.statistic.mastered, item.statistic.total)"></el-progress>
                  </div>
                </el-col>
              </el-row>              
            </el-card>
          </div>
        </el-col>
        <el-col :span="12">
          <div id="shortcut-operation" class="main-col">
            Test2
          </div>
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
            recent: 'abandon',
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
    getPercentage (a, b) {
      return (b === 0) ? 0 : (a / b).toFixed(2) * 100
    },
    progressFormat (a, b) {
      return `${a} / ${b}`
    }
  },
  created () {
    // get recent notebook data
    // ...
  }
}
</script>

<style scoped>
@import '../theme/base.css';

* {
  user-select: none;
}

#recent-header {
  height: 4rem;
  font-size: 3rem;
  font-weight: bolder;
  color: var(--color-text-regular);
}
.recent-note-card {
  background-color: var(--color-primary-secondary);

}
#recent-notebook {
  width: 100%;
  min-height: 4rem;
}
.main-row {
  position: relative;
  width: 100%;
  margin-top: 2rem;
}
.main-col {
  border-radius: 0.2rem;
}
.notebook-title {
  font-weight: bolder;
  color: #e7e7e7;
  font-size: 1.2em;
}
.notebook-statistic {
  width: 100%;
  color: #d1d1d1;
}
.highlight-word {
  font-weight: bolder;
  color: #e7e7e7;
}
.recent-note-card {
  position: relative;
  margin-bottom: 1rem;
  cursor: pointer;
}
.progress-circle-container {
}
.progress-circle {

}
</style>
