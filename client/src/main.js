// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import YmapPlugin from 'vue-yandex-maps'


const settings = {
  apiKey: 'e1a4bcd0-9721-40af-9d52-8d3948c7aab6',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1'
}
Vue.use(YmapPlugin, settings)


Vue.use(BootstrapVue)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})

