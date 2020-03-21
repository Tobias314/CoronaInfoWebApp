import Vue from "vue";
import Router from "vue-router";

import List from "./components/list.vue";
import LegalInfo from "./components/legalInfo.vue";
import MedicalInfo from "./components/medicalInfo.vue";
import GeneralInfo from "./components/generalInfo.vue";
import MentalHealthInfo from "./components/mentalhealth.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/legal",
      component: LegalInfo
    },
    {
      path: "/medical",
      component: MedicalInfo
    },
    {
      path: "/virus",
      component: GeneralInfo
    },
    {
      path: "/mentalhealth",
      component: MentalHealthInfo
    },
    {
      path: "*",
      component: List
    }
  ]
});

router.beforeEach(function (to, from, next) { 
  window.scrollTo(0, 0);
  next();
});

export default router;