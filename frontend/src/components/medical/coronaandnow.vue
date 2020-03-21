<template>
  <body>
    <h3>
      Ich habe Corona, was sollte ich tun?
    </h3>
    <div> 
      <md-table v-model="websites" md-card>
      <md-table-toolbar>
        <h1 class="md-title">Websites</h1>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Dienst" >{{ item.name }}</md-table-cell>
        <md-table-cell md-label="Link" >{{ item.link }}</md-table-cell>
      </md-table-row>
    </md-table>
    </div>
  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'medical_info',

  data: function(){
    return {
      websites: [],
    }
  },

  mounted(){
    Api.get(`/weblinks/coronainfected`)
    .then(response => {
      this.websites = response.data.websites;
    }, error => {
      console.error(error);
    });
  },

}
</script>

<style>

</style>