import Vue from 'vue'
import App from './App.vue'
import router from "./routes.js";

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

Vue.use(VueMaterial)

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('body');
