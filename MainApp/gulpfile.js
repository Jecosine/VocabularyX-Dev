/*
 * @Date: 2021-02-16 11:47:44
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 12:46:12
 */
const path = require('path')
const gulp = require('gulp')
const cleanCSS = require('gulp-clean-css')
const cssWrap = require('gulp-css-wrap')

gulp.task('css-wrap', () => {
  return gulp.src(path.resolve('./src/renderer/theme/index.css')).pipe(cssWrap({
    selector: '.theme-ff8623'
  })).pipe(cleanCSS()).pipe(gulp.dest('./src/renderer/theme/ff8623'))
})
