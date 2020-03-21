<template>
  <body>
    <h3>
      Wo bekomme ich Hilfe bei psychischen Problemen?
    </h3>
    <div> 
      <md-table v-model="phone_numbers" md-card>
      <md-table-toolbar>
        <h1 class="md-title">Telefonnummern</h1>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Dienst" >{{ item.name }}</md-table-cell>
        <md-table-cell md-label="Nummer" >{{ item.number }}</md-table-cell>
      </md-table-row>
    </md-table>
    </div>
  </body>
</template>

<script>
import Api from "./api.js";

export default {
  name: 'medical_info',

  data: function(){
    return {
      phone_numbers: [],
    }
  },

  mounted(){
    Api.get(`/phone_number/mentalhealth`)
    .then(response => {
      this.phone_numbers = response.data.phone_numbers;
    }, error => {
      console.error(error);
    });
  },


  


}
</script>

<style>

</style>