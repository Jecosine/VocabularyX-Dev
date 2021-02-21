<!--
 * @Date: 2021-02-03 07:02:08
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-21 13:08:22
-->
<template>
  <el-container id="main-container">
    <el-header id="navigation-container" height="2.25rem">
      <div class="navigation-wrapper">
        <titlebar :title="title" :height="'2.25rem'" />
      </div>
      <div id="command-container">
        <div id="command-wrapper" v-show="showCommand">
          <div id="command-box">
            <el-input
              id="command-input"
              ref="searchBarRef"
              style="fontFamily:'Fira Code'"
              v-model="command"
              @keydown.27.native="triggerCommand"
              @keydown.enter.native="executeCommand"
              @keydown.up.native="prevCommand"
              @keydown.down.native="nextCommand"
            ></el-input>
          </div>
        </div>
      </div>
    </el-header>
    <el-container>
      <el-aside width="4.25rem" id="side-container">
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'recent'
          }"
          @click="openMenu('recent')"
        >
          <font-awesome-icon :icon="['fas', 'home']"></font-awesome-icon>
        </div>
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'notebook'
          }"
          @click="openMenu('notebook')"
        >
          <font-awesome-icon :icon="['fas', 'atlas']"></font-awesome-icon>
        </div>
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'search'
          }"
          @click="openMenu('recent')"
        >
          <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
        </div>
        <div
          :class="{
            'menu-button': true,
            'menu-button-selected': currentMenu === 'word'
          }"
          @click="openMenu('word')"
        >
          <font-awesome-icon :icon="['fas', 'font']"></font-awesome-icon>
        </div>
      </el-aside>
      <el-container>
        <el-main id="content-main">
          <transition name="fade">
            <router-view />
          </transition>
        </el-main>
        <el-footer id="footer-container" height="2.125rem"></el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import { setTheme } from '../utils/index'
import CommandParseException from '../exceptions/CommandParseException'
import CommandExecuteException from '../exceptions/CommandExecuteException'

export default {
  components: {
    titlebar: require('@/components/partial/Titlebar').default
  },
  data () {
    return {
      title: 'VocabularyX',
      currentMenu: 'recent',
      command: '',
      showCommand: false,
      cmdHistory: [],
      cmdCursor: -1
    }
  },
  methods: {
    closeCommand () {
      if (this.showCommand) {
        this.showCommand = false
      }
    },
    prevCommand () {
      // first time
      if (this.cmdCursor < 0) {
        this.cmdHistory.push(this.command)
        this.cmdCursor = this.cmdHistory.length - 1
      }
      if (this.cmdCursor) {
        --this.cmdCursor
        this.command = this.cmdHistory[this.cmdCursor]
      }
    },
    nextCommand () {
      if (this.cmdCursor >= 0 && this.cmdCursor < this.cmdHistory.length - 1) {
        ++this.cmdCursor
        this.command = this.cmdHistory[this.cmdCursor]
      }
      // reach bottom
      if (this.cmdCursor === this.cmdHistory.length - 1) {
        this.cmdHistory.pop(-1)
        this.cmdCursor = -1
      }
    },
    triggerCommand () {
      this.showCommand = !this.showCommand
      if (this.showCommand) {
        this.$nextTick(function () {
          this.command = ''
          this.$refs.searchBarRef.focus()
          this.cmdCursor = -1
          if (this.cmdHistory[this.cmdHistory.length - 1] === '') {
            this.cmdHistory.pop(-1)
          }
        })
      }
    },
    executeCommand () {
      if (this.command.trim() !== '') {
        if (this.cmdHistory[this.cmdHistory.length - 1] === '') {
          this.cmdHistory.pop(-1)
        }
        this.cmdHistory.push(this.command)
      }
      if (this.cmdHistory > 10) {
        this.cmdHistory.shift()
      }
      let res = this.$command.execute(this.command)
      if (res && res['status'] < 0) {
        let title
        if (res['msg'] && res['msg'] instanceof Error) {
          title = `[${res['msg'].scope}] ${res['msg'].name}`
          this.$notify({
            title: title,
            message: res['msg'].message,
            position: 'bottom-right',
            type: 'error',
            customClass: 'notify-container'
          })
        }
      }
      this.triggerCommand()
    },
    popup (type, title, msg) {
      this.$notify({
        title: title,
        message: msg,
        position: 'bottom-right',
        type: type,
        customClass: 'notify-container'
      })
    },
    openMenu (name) {
      if (this.currentMenu !== name) {
        this.$router.push({ name: name })
        this.currentMenu = name
      }
    },
    testFunction (options) {
      console.log('It works!')
      console.log(options)
    },
    routerCommand (options) {
      // record current path
      let current = this.$route

      // check options
      if (!options['opts'] && options['opts']['path'] === undefined) {
        throw new CommandExecuteException(`'path' param not defined`)
      }
      if (current.path !== options['opts']['path']) {
        this.$router.push(options['opts']['path'])
      }
    },
    openNotebook (options) {},
    async openWord (options) {
      if (!options['opts']['word']) {
        this.popup(
          'error',
          `[Word] Word is NOT Provided`,
          `Word parameter is not provided in command`
        )
      }
      let wordText = options['opts']['word']
      if (this.word === wordText) {
        this.popup(
          'warning',
          `[Word] Already Opened`,
          `You are already at word ${wordText}`
        )
      }
      // todo check whether in database
      let check = await this.$db.models.Word.findOne({
        where: {
          spell: wordText
        },
        attributes: ['id']
      })
      console.log(check)
      if (check === null) {
        this.popup(
          'warning',
          `[Word] Word Not Found`,
          `Word ${wordText} is not in database`
        )
      } else {
        this.$router.push(`/word/${wordText}`)
      }
    }
  },
  mounted () {
    // const that = this
    // bind
    this.$shortcut.filter = function (event) {
      return true
    }
    this.$shortcut.setScope('input')
    this.$shortcut.bind('ctrl+shift+p', this.triggerCommand)
    this.$shortcut.bind('esc', this.triggerCommand)
    // set default theme
    setTheme(document.body, 'theme-default')
    let that = this

    this.$router.beforeEach((to, from, next) => {
      if (to.matched.length !== 0) {
        next()
      } else {
        that.$notify({
          title: '[Command] Route Command Error',
          message: `No such route: ${to.path}`,
          type: 'error',
          customClass: 'notify-container',
          position: 'bottom-right'
        })
      }
    })
    this.$command.bind('test', this.testFunction, {
      name: 'test',
      opts: {
        param1: {
          name: 'param1',
          type: 'string',
          short: '-p1',
          long: '--param1',
          require: false
        },
        param2: {
          name: 'param2',
          type: 'boolean',
          short: '-p2',
          long: '--param2',
          require: true
        }
      }
    })
    this.$command.bind('route', this.routerCommand, {
      name: 'route',
      opts: {
        path: {
          name: 'path',
          type: 'string',
          short: '-p',
          long: '--path',
          require: true
        }
      }
    })
    this.$command.bind('open', this.openNotebook, {
      name: 'open',
      opts: {
        name: {
          name: 'name',
          type: 'string',
          short: '-n',
          long: '--name',
          require: true
        }
      }
    })
    this.$command.bind('word', this.openWord, {
      name: 'word',
      opts: {
        word: {
          name: 'word',
          type: 'string',
          short: '-w',
          long: '--word',
          require: true
        }
      }
    })
  },
  created () {
    window.routeApp = this
  }
}
</script>

<style scoped>
@import '../theme/base.css';

#main-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
}

#navigation-container {
  width: 100%;
  height: 2rem;
  padding: 0;
  background-color: #e7e7e7;
  -webkit-app-region: drag;
}
#side-container {
  /* height: calc(100vh - 2rem); */
  background-color: var(--color-primary);
  position: relative;
}
#content-main {
  padding: 0;
  height: calc(100vh - 4.375rem);
}
#command-container {
  position: absolute;
  left: 0;
  width: 100%;
  height: 3.2rem;
  background-color: transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#command-wrapper {
  box-sizing: content-box;

  padding: 0.1rem 0.5rem;
  width: 33%;
  height: 3.2rem;
  background-color: #e7e7e7;
  box-shadow: 0 0.1rem 0.1rem 0.1rem rgba(0, 0, 0, 0.16);
  line-height: 100%;
  z-index: 9999;
}
#command-box {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 100%;
}
#command-input.el-input__inner {
  font-family: 'Fira Code';
}
.navigation-wrapper {
  width: calc(100% - 2.25rem);
  padding: 0 1.125rem;
}
#footer-container {
  background-color: #e7e7e7;
}
.menu-button {
  box-sizing: content-box;
  /* padding: 0 0.1rem; */
  width: 4.15rem;
  height: 4.25rem;
  text-align: center;
  border-width: 0 0 0 0.1rem;
  border-style: solid;
  border-color: transparent;
  line-height: 4.25rem;
  font-size: 2rem;
  color: var(--color-menu-unselected);
}
.menu-button-selected {
  box-sizing: content-box;
  border-color: #e7e7e7;
  color: var(--color-menu-selected);
  transition: none;
}
</style>
