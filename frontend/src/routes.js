import Vue from "vue";
import Router from "vue-router";

import CoronaUnsureInfo from "./components/medical/doihavecorona.vue";
import CoronaHavingInfo from "./components/medical/coronaandnow.vue";
import MentalHealthInfo from "./components/medical/mentalhealth.vue";
import stayHome from "./components/legal/stayhomeinfo.vue"
import financialSupoort from "./components/legal/financialSupport.vue";
import VirusInfo from "./components/virus/virusInfo.vue";
import Research from "./components/virus/research.vue";
import Distribution from "./components/virus/distribution.vue";
import List from "./components/list.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/doihavecorona",
      component: CoronaUnsureInfo
    },
    {
      path: "/coronaandnow",
      component: CoronaHavingInfo
    },
    {
      path: "/mentalhealth",
      component: MentalHealthInfo
    },
    {
      path: "/stayhome",
      component: stayHome
    },
    {
      path: "/finances",
      component: financialSupoort
    },
    {
      path: "/virus",
      component: VirusInfo
    },
    {
      path: "/research",
      component: Research
    },
    {
      path: "/distribution",
      component: Distribution
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