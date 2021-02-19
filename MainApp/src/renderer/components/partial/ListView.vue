<!--
 * @Date: 2021-02-19 10:55:53
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-19 13:12:42
-->
<template>
  <div class="list-container">
    <div class="list-item-container" v-for="(item, i) in parsedData" :key="i">
      <div :class="['item-key', keyClass?keyClass:'']">{{item[0]}}</div>
      <div :class="['item-value', valueClass?valueClass:'']">{{item[1]}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'list-view',
  props: {
    listData: {
      type: Object,
      require: true
    },
    keyClass: {
      type: String,
      require: false
    },
    valueClass: {
      type: String,
      require: false
    }
  },
  data () {
    return {

    }
  },
  computed: {
    parsedData: function () {
      if (!(this.listData instanceof Object)) {
        return []
      }
      let keys = Object.keys(this.listData)
      let arr = []
      let that = this
      keys.forEach(element => {
        arr.push([element, that.listData[element]])
      })
      console.log(arr)
      return arr
    }
  },
  methods: {

  }
}
</script>

<style scoped>
@import '../../theme/base.css';
.list-container {
  box-sizing: content-box;
  min-width: 10rem;
  width: 100%;
  height: 100%;
}
.list-item-container {
  display: flex;
  flex-direction: row;
  align-content: center;
  box-sizing: content-box;
  padding: 0.15rem;
  height: 2rem;
  line-height: 2rem;
}
.item-key {
  color: var(--color-primary);
  font-weight: bold;
  font-size: 0.8rem;
  line-height: 2rem;
  width: 10rem;
  margin-left: 1rem;
}
.item-value {
  font-weight: regular;
  font-size: 0.8rem;
  line-height: 2rem;
  color: var(--color-text-secondary);
}
</style>