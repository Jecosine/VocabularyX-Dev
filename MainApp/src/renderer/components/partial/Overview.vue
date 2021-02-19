<!--
 * @Date: 2021-02-19 16:18:13
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-20 01:36:56
-->
<template>
  <div class="svg-container" ref="container">
    <div id="tip" ref="tip">
      
    </div>
    <svg xmlns="http://www.w3.org/2000/svg" class="svg-item" ref="svgItem">
      <g transform="translate(0, 0)">        
        <g :transform="`translate(${i * 14}, 0)`" v-for="i of timeScale==='year' ? 53 : 7" :key="i">
          <rect width="10" height="10" x="0" rx="2" ry="2" class="overview-block" :y="`${j * 14}`" v-for="j of timeScale==='year' ? 7 : 6" :key="j" :fill="`rgba(31, 71, 103, ${Math.random()})`" :data-x="i" :data-y="j" @mouseenter="blockHover" @mouseleave="hideTip"><div><strong>pos</strong> {{i}}, {{j}}</div></rect>
        </g>
      </g>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    timeScale: {
      type: String,
      require: false,
      default: 'year',
      validator: (value) => {
        return ['month', 'year'].indexOf(value) !== -1
      }
    },
    colorRank: {
      type: Array,
      require: false,
      validator: (value) => {
        return value.length === 2 && value[0].length === value[1].length && value[0].length >= 2
      }
    },
    statisticData: {
      type: Object,
      require: true,
      default: () => ({'testDate': {duration: 3.6, mastered: 154}})
    },
    offset: {
      type: Number,
      require: false
    }
  },
  data () {
    return {
      pointerDate: 'testDate',
      currentDate: '',
      total: 0,
      firstDate: null
    }
  },
  methods: {
    blockHover (e) {
      // console.log(e)
      // this.$refs['tip'].style.display = 'block'
      // this.$refs['tip'].style.left = `${e.offsetX}px`
      // this.$refs['tip'].style.top = `${Math.floor(e.offsetY / 16)}rem`
      console.log(this.toDate(parseInt(e.target.dataset['x']), parseInt(e.target.dataset['y'])))
      this.$refs['tip'].innerHTML = `<div class="date-container">${this.currentDate}</div>
      <div class="statisitic-item">
        <div class="statistic-title">Duration</div>
        <div class="statistic-value">${this.statisticData[this.pointerDate].duration}</div>
      </div>
      <div class="statisitic-item">
        <div class="statistic-title">Mastered</div>
        <div class="statistic-value">${this.statisticData[this.pointerDate].mastered}</div>
      </div>`
    },
    hideTip (e) {
      // this.$refs['tip'].style.display = 'none'
    },
    toDate (i, j) {
      let currentDate = new Date(Date.parse(this.firstDate))
      currentDate.setDate(currentDate.getDate() + i * 7 + j)
      this.currentDate = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`
      return `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`
    }
  },
  computed: {
  },
  mounted () {
    let that = this
    window.svgItem = this.$refs['svgItem']
    window.container = this.$refs['container']
    let now = new Date()
    this.total = 52 * 7 + (now.getDay() ? now.getDay() : 7)
    this.firstDate = new Date()
    this.firstDate.setDate(now.getDate() - this.total + 1)
    this.$nextTick(() => {
      // let vx = this.$refs['svgItem'].getBBox().width
      // let vy = this.$refs['svgItem'].getBBox().height
      // let ratio = vy / vx
      // vx = this.$refs['container'].offsetWidth
      // vy = Math.ceil(vx * ratio)
      that.$refs['svgItem'].setAttribute('viewBox', `0,0,768,124`)
      // that.$refs['svgItem'].setAttribute('width', `${vx}`)
      // that.$refs['svgItem'].setAttribute('height', `${vy}`)
    })
  },
  created () {

  }
}
</script>

<style scoped>
@import '../../theme/base.css';
.overview-block {
  /* color: var(--color-primary);
  background-color: var(--color-primary);
  fill: var(--color-primary); */
}
.svg-item {
  position: absolute;
  left: 0;
  top: 4rem;
  /* width: 100%; */
}
.svg-container {
  /* width: 100%; */
  position: relative;
  min-height: 14rem;
}
#tip {
  display: block;
  box-sizing: content-box;
  padding: 0.4rem;
  margin: 0.5rem 1rem;
  pointer-events: none;
  position: absolute;
  /* width: 5rem; */
  min-height: 1rem;
  background-color: rgba(0,0,0,0.1);
  border-radius: 0.2rem;
  color: white;
  font-size: 0.6rem;
  z-index: 9999;
}
#tip >>> .date-container {
  color: var(--color-primary);
}
#tip >>> .statisitic-item {
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  font-size: 0.9rem;
  min-width: 7rem;
}
#tip >>> .statistic-title {
  color: var(--color-primary);
  font-weight: bold;
  margin-right: 1rem;
}
#tip >>> .statistic-value {
  font-size: 0.8rem;
  color: var(--color-text-regular);
  font-weight: regular;
}
</style>