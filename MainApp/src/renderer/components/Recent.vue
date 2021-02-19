<!--
 * @Date: 2021-02-10 15:06:46
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 02:12:13
-->
<template>
  <el-container>
    <el-header height="8rem">
      <!-- <div id="recent-header">
        VocabularyX
      </div> -->
      <div id="search-container">
        <div id="search-wrapper">        
          <el-input ref="search" v-model="searchText" size="large" id="main-search-bar" @keydown.esc.native="unfocus()">
            <template slot="append">
              <el-button icon="el-icon-search" id="search-button" type="primary"></el-button>
            </template>            
          </el-input>
        </div>
      </div>
    </el-header>
    <el-main id="main">
      <el-row class="main-row" :gutter="80">
        <el-col :xl="12" :lg="10" :md="8" :sm="24" :xs="24">
          <div id="shortcut-operation" class="main-col">
            <div class="col-title">Start</div>
            <div class="link-group">
              <div class="link-item" v-for="(item, i) in linkItems" :key="i">
                <a :href="item.link">{{item.name}}</a>
              </div>
            </div>
          </div>
        </el-col>
        <el-col :xl="12" :lg="14" :md="16" :sm="24" :xs="24">
          <div id="recent-notebook" class="main-col">
            <div class="col-title">Recent</div>
            <el-card
              shadow="hover"
              :body-style="{
                borderRadius: '0.2rem'
              }"
              v-for="(item, i) in recentNote"
              :key="i"
              class="recent-note-card"
            >
              <el-row>
                <el-col :xl="18" :lg="16" :md="14" :sm="24" :xs="24">
                  <div class="notebook-title">
                    {{ item.name }}
                  </div>
                  <div class="notebook-statistic">
                    <div>
                      Current:
                      <span class="highlight-word">{{
                        item.statistic.recent
                      }}</span>
                    </div>
                    <div>
                      Words:
                      <span class="highlight-word"
                        >{{ item.statistic.mastered }} /
                        {{ item.statistic.total }}</span
                      >
                    </div>
                  </div>
                </el-col>
                <el-col
                  :xl="6"
                  :lg="8"
                  :md="10"
                  v-if="screenWidth > 1300"
                  class="progress-circle-container"
                >
                  <div>
                    <el-progress
                      type="circle"
                      class="progress-circle"
                      :width="70"
                      color="#7190aa"
                      stroke-linecap="butt"
                      :stroke-width="14"
                      :show-text="false"
                      :percentage="
                        getPercentage(
                          item.statistic.mastered,
                          item.statistic.total
                        )
                      "
                    ></el-progress>
                  </div>
                </el-col>
              </el-row>
            </el-card>
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
      screenWidth: null,
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
      ],
      searchText: '',
      linkItems: [
        {
          name: 'Create A New Notebook',
          link: ''
        },
        {
          name: 'Create A New Plan',
          link: ''
        },
        {
          name: 'Start A Contest',
          link: ''
        },
        {
          name: 'Go to New Words Book',
          link: ''
        },
        {
          name: 'Go to Problem List',
          link: ''
        }
      ]
    }
  },
  methods: {
    unfocus () {
      if (this.$refs['search'].focused) {
        this.$refs['search'].blur()
      }
    },
    getPercentage (a, b) {
      return b === 0 ? 0 : (a / b).toFixed(2) * 100
    },
    progressFormat (a, b) {
      return `${a} / ${b}`
    }
  },
  created () {
    // get recent notebook data
    // ...
    this.showCommand = true
  },
  mounted () {
    const that = this
    window.onresize = () => {
      return (() => {
        window.screenWidth = document.body.clientWidth
        that.screenWidth = window.screenWidth
      })()
    }
  }
}
</script>

<style scoped>
@import '../theme/base.css';

* {
  user-select: none;
}
#search-container {
  position: relative;
  width: 100%;
  height: 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#search-wrapper {
  width: 60%;
  min-width: 20rem;
  height: 3rem;
  margin-top: 5rem;
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
#main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#recent-notebook {
  width: 100%;
  min-height: 4rem;
}
.main-row {
  box-sizing: content-box;
  padding-top: 4rem;
  position: relative;
  max-width: 80rem;
  margin: 0 auto;
  width: 100%;
  /* margin-top: 2rem; */
  min-height: 40rem;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
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
.recent-note-card:hover {
  background-color: var(--color-primary);
}
.recent-note-card:hover .notebook-title {
  color: #fff;
}

.progress-circle-container {
  text-align: center;
}
.progress-circle {
}
.col-title {
  font-size: 2rem;
  color: var(--color-primary-secondary);
  margin-bottom: 1rem;
}
.link-item {
  height: 3rem;
  line-height: 3rem;
  
  font-size: 1.2rem;
}
.link-item > a {
  text-decoration: none;
  color: var(--color-primary)!important;
}
#search-wrapper >>> .el-input-group__append,
#search-button {
  background-color: var(--color-primary-secondary);
  color: white;
  border-radius: 0;
  border-width: 0.2rem;
  border-color: var(--color-primary-secondary);
}
#main-search-bar {
  box-sizing: content-box;
}
</style>
