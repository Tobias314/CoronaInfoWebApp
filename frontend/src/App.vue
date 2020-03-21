<template>
  <body>
    <header>
      <div class="md-layout md-gutter">
        <div class="md-layout-item">
      <h2 @click="gotoStart()">
        Corona-Informationen
      </h2>
        </div>
      <div class="md-layout-item">
      <md-field>
        <label for="location">Location</label>
        <md-select v-model="location" md-dense>
          <md-optgroup v-for="thing in districts" v-bind:key="thing.name" v-bind:label="thing.name">
            <md-option 
              v-for="item in thing.districts" v-bind:key="item" v-bind:value="item"> 
                {{item}} 
            </md-option>
          </md-optgroup>
        </md-select>
      </md-field>
      </div>
      </div>
    </header>
     <main>
      <transition name="component-fade" mode="out-in">
        <router-view />
      </transition>
    </main>
  </body>
</template>

<script>
import Api from "./components/api.js";

export default {
  name: 'App',

  data: function(){
    return{
      test: "testhallo",
      location: "",
      districts: [{name: "Baden-Württemberg", districts: []}, 
                  {name: "Bayern", districts: []}, 
                  {name: "Berlin", districts: []}, 
                  {name: "Brandenburg", districts: []}, 
                  {name: "Bremen", districts: []}, 
                  {name: "Hamburg", districts: []}, 
                  {name: "Hessen", districts: []}, 
                  {name: "Mecklenburg-Vorpommern", districts: []}, 
                  {name: "Niedersachsen", districts: []}, 
                  {name: "Nordrhein-Westfalen", districts: []}, 
                  {name: "Rheinland-Pfalz", districts: []}, 
                  {name: "Saarland", districts: []}, 
                  {name: "Sachsen", districts: []}, 
                  {name: "Sachsen-Anhalt", districts: []}, 
                  {name: "Schleswig-Holstein", districts: []}, 
                  {name: "Thüringen", districts: []},
      ] 
    }
  },

  methods: {
    gotoStart: function(){
      this.$router.push("/")
    },
  },

  mounted(){
    Api.get(`/district_infos/get_districts`)
    .then(response => {
      let district_states = response.data.district_states;
      let district_names = response.data.district_names;
      let dict = {"Baden-Württemberg": [],
                  "Bayern": [], 
                  "Berlin": [], 
                  "Brandenburg": [], 
                  "Bremen": [], 
                  "Hamburg": [], 
                  "Hessen": [], 
                  "Mecklenburg-Vorpommern": [], 
                  "Niedersachsen": [], 
                  "Nordrhein-Westfalen": [], 
                  "Rheinland-Pfalz": [], 
                  "Saarland": [], 
                  "Sachsen": [], 
                  "Sachsen-Anhalt": [], 
                  "Schleswig-Holstein": [], 
                  "Thüringen": [],};
      for (let i = 0; i < district_states.length; i++){
        (dict[district_states[i]]).push(district_names[i]);
      }
      for (let i = 0; i < this.districts.length; i++){
        this.districts[i].districts = [...new Set(dict[this.districts[i].name])].sort();
      }
    }, error => {
      console.error(error);
    });
  },
}
</script>

<style>

</style>
