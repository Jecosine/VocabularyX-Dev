<!--
 * @Date: 2021-02-15 09:21:07
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-21 13:11:50
-->
<template>
  <div id="word-main-container">
    <div class="wrapper">
      <div class="word-title">{{ word }}</div>
      <el-divider></el-divider>
      <div
        class="word-pron-container"
        v-if="wordData.phonetic && wordData.phonetic.length"
      >
        <div class="word-pron">
          <div class="pron-text">
            美&nbsp;&nbsp;&nbsp;&nbsp;[{{ wordData.phonetic[0] }}]
          </div>
          <div class="audio-source" @click="playAudio('us')">
            <font-awesome-icon :icon="['fas', 'volume-up']"></font-awesome-icon>
          </div>
        </div>
        <div class="word-pron" v-if="wordData.phonetic.length > 1">
          <div class="pron-text">
            英&nbsp;&nbsp;&nbsp;&nbsp;[{{
              wordData.phonetic.length > 1 ? wordData.phonetic[0] : ''
            }}]
          </div>
          <div class="audio-source" @click="playAudio('uk')">
            <!-- <el-button size="mini" round> -->
            <font-awesome-icon :icon="['fas', 'volume-up']"></font-awesome-icon>
            <!-- </el-button> -->
          </div>
        </div>
      </div>
      <div class="word-definition-container">
        <div class="word-section-title">
          释义
        </div>
        <ul class="word-section-content">
          <li
            class="word-definition-item"
            v-for="(item, i) in wordData.pos"
            :key="i"
          >
            <el-tag
              size="mini"
              class="word-definition-tag"
              :color="colorMap[item.type] || '#909399'"
              >{{ item.type }}.</el-tag
            >
            <div class="word-definition-text">{{ item.definition }}</div>
          </li>
        </ul>
      </div>
      <div class="word-forms-container">
        <div class="word-section-title">
          形态变换
        </div>
        <el-row :gutter="20" style="width: 100%;height: 2rem;">
          <el-col :span="12" v-for="(wf, j) in wordData['word_forms']" :key="j">
            <div class="wf-container">
              <el-tag size="mini" effect="light" class="wf-name">{{
                wf.name
              }}</el-tag>
              <div class="wf-content">{{ wf.value }}</div>
            </div>
          </el-col>
        </el-row>
      </div>
      <div class="word-definition-container">
        <div class="word-section-title">
          记忆法
        </div>
        <div class="word-definition-content word-mem-tip">
          <div class="word-icon">
            <font-awesome-icon :icon="['fas', 'lightbulb']"></font-awesome-icon>
          </div>
          {{ wordData.tip }}
        </div>
      </div>
      <div class="word-definition-container">
        <div class="word-section-title">
          中文词源
        </div>
        <div class="word-definition-content">
          {{ wordData.cn_source }}
        </div>
        <div class="ref">
          —— 来源 <a href="https://www.quword.com">quword.com</a>
        </div>
      </div>
      <div class="word-definition-container">
        <div class="word-section-title">
          英文词源
        </div>
        <div
          class="word-definition-content word-source"
          v-html="wordData.en_source"
        ></div>
        <div class="ref">
          —— 来源 <a href="https://www.quword.com">quword.com</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const colorMap = {
  noun: '#E6A23C',
  verb: '#F56C6C',
  adj: '#67C23A',
  adv: '#6344ab'
}
export default {
  name: 'word',
  props: {
    word: {
      type: String,
      required: false,
      default: 'abandon'
    }
  },
  watch: {
    $route (to, from) {
      if (to.path !== from.path) {
        this.fetchData(this.word)
      }
    }
  },
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
        word_forms: [
          {
            name: 'form1',
            value: 'form1 value'
          },
          {
            name: 'form2',
            value: 'form2 value'
          }
        ],
        tip: 'Tips here',
        cn_etym: 'cn source here',
        en_etym: `<section class="word__defination--2q7ZH"><p>late 14c., "to give up (something) absolutely, relinquish control, give over utterly;" also reflexively, "surrender (oneself), yield (oneself) utterly" (to religion, fornication, etc.), from Old French abandonner "surrender, release; give freely, permit," also reflexive, "devote (oneself)" (12c.).</p><p>The Old French word was formed from the adverbial phrase à bandon "at will, at discretion," from à "at, to" (from Latin ad; see <a href="/word/ad-?ref=etymonline_crossreference" class="crossreference notranslate">ad-</a>) + bandon "power, jurisdiction," from Latin bannum, "proclamation," which is from a Frankish or other Germanic word, from Proto-Germanic *bannan- "proclaim, summon, outlaw" (things all done by proclamation); see <a href="/word/ban?ref=etymonline_crossreference#etymonline_v_248" class="crossreference notranslate">ban</a> (v.).</p><blockquote><span class="foreign notranslate">Mettre sa forest à bandon</span> was a feudal law phrase in the 13th cent. = <span class="foreign notranslate">mettre sa forêt à permission</span>, i.e. to open it freely to any one for pasture or to cut wood in; hence the later sense of giving up one's rights for a time, letting go, leaving, abandoning. [Auguste Brachet, "An Etymological Dictionary of the French Language," transl. G.W. Kitchin, Oxford, 1878]</blockquote><p>Meaning "to leave, desert, forsake (someone or something) in need" is from late 15c. &nbsp;Related: <span class="foreign notranslate">Abandoned</span>; <span class="foreign notranslate">abandoning</span>.</p><p>Etymologically, the word carries a sense of "put (something) under someone else's control," and the earliest appearance of the word in English is as an adverb (mid-13c.) with the sense "under (one's) control," hence also "unrestricted."</p><blockquote>Again, as that which is placed at the absolute command of one party must by the same act be entirely given up by the original possessor, it was an easy step from the sense of conferring the command of a thing upon some particular person to that of renouncing all claim to authority over the subject matter, without particular reference to the party into whose hands it might come ; and thus in modern times the word has come to be used almost exclusively in the sense renunciation or desertion. [Hensleigh Wedgwood, "A Dictionary of English Etymology," 1859]</blockquote></section>`
      },
      word_forms: {},
      audio_sources: [],
      audioInstances: [null, null],
      audioPlayBlock: false
    }
  },
  methods: {
    playAudio (type) {
      if (this.audioPlayBlock) {
        return false
      }
      let that = this
      this.audioPlayBlock = true
      setTimeout(() => {
        that.audioPlayBlock = false
      }, 1500)
      if (type === 'uk') {
        if (this.audioInstances[1] instanceof Audio) {
          this.audioInstances[1].play()
        }
      } else {
        if (this.audioInstances[0] instanceof Audio) {
          this.audioInstances[0].play()
        }
      }
    },
    async fetchData (word) {
      this.wordData = await this.$db.models['Word'].findOne({
        where: {
          spell: this.word
        },
        attributes: [
          'id',
          'spell',
          'pos',
          'cn_etym',
          'en_etym',
          'audio_sources',
          'parsed',
          'raw',
          'word_forms'
        ]
      })
      if (this.wordData === null) {
        this.$notify({
          title: `[Word] Word ${this.word} is NOT in Database`,
          message: `Fetching definition from internet...`,
          position: 'bottom-right',
          type: 'warning'
        })
      }
      this.wordData = JSON.parse(JSON.stringify(this.wordData))
      let ukAudio = this.wordData['uk-speech']
        ? new Audio(this.wordData['uk-speech'])
        : null
      let usAudio = this.wordData['us-speech']
        ? new Audio(this.wordData['us-speech'])
        : null
      this.audioInstances = [usAudio, ukAudio]
      if (this.wordData.parsed === 0 && this.wordData.raw.length) {
        let rawData = JSON.parse(this.wordData.raw)
        rawData = rawData['basic']
        this.wordData.pos = [
          {
            type: 'none',
            definition: rawData['explains'][0]
          }
        ]
        this.wordData.audio_sources = [
          rawData['us-speech'],
          rawData['uk-speech']
        ]
        this.wordData.phonetic = [
          rawData['us-phonetic'],
          rawData['uk-phonetic']
        ]
      }

      // debug code
      this.wordData.word_forms = [
        {
          name: 'form1',
          value: 'form1 value'
        },
        {
          name: 'form2',
          value: 'form2 value'
        }
      ]
    }
  },
  mounted () {
    console.log('mounted')
  },
  async created () {
    console.log('word created')
    // request word data
    if (!this.word) {
      this.$notify({
        title: `[Word] Word props is NOT Provided`,
        message: `Fetching definition from internet...`,
        position: 'bottom-right',
        type: 'error',
        customClass: 'notify-container'
      })
    } else {
      // fetch data
      await this.fetchData(this.word)
    }
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
  color: var(--color-text-regular);
}
.audio-source {
  cursor: pointer;
  transition: color 0.1s;
}
.audio-source:hover {
  color: var(--color-text-primary);
}
.word-mem-tip {
  box-sizing: content-box;
  width: 100%;
  padding: 2rem 3rem;
  background-color: #fff7ec;
  border-radius: 0.2rem;
}
.word-definition-content {
  position: relative;
}
.word-icon {
  position: absolute;
  height: 100%;
  display: flex;
  color: #cf9b52;
  flex-direction: row;
  align-items: center;
  left: 1.2rem;
  top: 0;
  font-size: 1.2rem;
}
.ref {
  color: var(--color-text-secondary);
  font-style: italic;
  text-align: right;
  font-size: 0.9rem;
}
.word-source {
  box-sizing: content-box;
  font-family: 'Palatino Linotype' !important;
  width: 100%;
  font-size: 1.1rem;
  /* font-weight: bold; */
  color: var(--color-text-regular);
}

.word-source section,
.word-source p,
.word-source a {
  font-family: 'Palatino Linotype';
}
.word-word-forms-container {
  box-sizing: content-box;
  width: 100%;
  height: 3rem;
  padding: 0.5rem 1rem;
}
.wf-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
  line-height: 100%;
  font-size: 1rem;
}
.wf-name {
  font-weight: bold;
  margin-right: 1rem;
}
.wf-content {
  font-family: 'Palatino Linotype';
  font-weight: bold;
  color: var(--color-text-regular);
}
</style>
