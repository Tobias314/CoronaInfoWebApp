<template>
  <body>
    <h3>
      Darf ich noch raus?
    </h3>
    {{infos}}
    <div v-if="infos_loaded">
    <div v-if="infos.is_lockdown"><b> In {{this.$parent.location}} gibt es eine Ausgangssperre! </b></div>
    <div v-if="!infos.is_lockdown"> In {{this.$parent.location}} gibt es keine Ausgangssperre. Trotzdem ist es ratsam zuhause zu bleiben!</div>
    <br/>
    <div>Aktuelle Regelung zu öffentlichen Versammlungen in {{this.$parent.location}}:
    {{infos.max_number_public}}</div>
    <br/>
    <div v-if="infos.club_sport_allowed"> Sport in Vereinen oder öffentlichen Sportanlagen ist erlaubt. </div>
    <div v-if="!infos.club_sport_allowed"> Sport in Vereinen oder öffentlichen Sportanlagen ist <b>nicht</b> erlaubt. </div>
    <br/>
    <div> Mehr Informationen findest du hier: <br/>
      <a v-for="link in infos.website" :key="link" class="nav__item nav__link" :href="'//' + link" target="_blank">{{link}} <br/></a></div>
    </div>
  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'legal_info',

  data:function(){
    return{
      infos_loaded: false,
      infos: {},
    }
  },

  mounted(){
    Api.get(`/lockdown_info/${this.$parent.location}`)
    .then(response => {
      this.infos = response.data;
      this.infos.website = response.data.website.split(";")
      this.infos_loaded = true;
    }, error => {
      console.error(error);
    });
  }
}
</script>

<style>

</style>
